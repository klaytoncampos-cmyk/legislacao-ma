"""Busca e leitura na base de legislação (SEFAZ-MA + CONFAZ).

A base pode estar em uma pasta `base/` (projeto) ou agrupada em pacotes `dados/*.md` (skill empacotada,
cada documento precedido de uma linha `<<<DOC caminho>>>`); o script detecta sozinho e trata cada
documento separadamente, com os mesmos nomes e números de linha.

BUSCAR
    python3 scripts/buscar.py "autopeças"
    python3 scripts/buscar.py "8708" --doc anexo-4 --vigente
    python3 scripts/buscar.py --artigo 291 --doc ricms
    python3 scripts/buscar.py "Conv. ICMS 142/18" --onde      # só lista onde aparece

LER (use depois de buscar, para ler o dispositivo inteiro)
    python3 scripts/buscar.py --ler sefaz/anexo-4.41.md --linhas 30-120
    python3 scripts/buscar.py --ler confaz/protocolo/protocolo-041-2008.md --linhas 1-60
    python3 scripts/buscar.py --ler INDICE.md --linhas 1-200

LISTAR
    python3 scripts/buscar.py --listar protocolo-04          # documentos cujo caminho contém o texto

Opções de busca:
    --doc TEXTO     filtra documentos cujo caminho contém TEXTO (ex.: ricms, cte, anexo-4.29, convenio-142)
    --vigente       ignora linhas totalmente tachadas (~~...~~) e notas de redação anterior/original
    --regex         trata o termo como expressão regular (padrão: literal, sem diferenciar acentos/maiúsculas)
    --artigo N      localiza o caput "Art. N" (aceita Nº/N°/No/N-A)
    -C N            linhas de contexto (padrão 2)
    --max N         máximo de resultados (padrão 40)
    --onde          mostra só a contagem por documento
"""
import argparse, bisect, re, sys, pathlib, unicodedata

# no Windows a saída redirecionada usa cp1252 e quebraria em "⚠" e outros caracteres
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")

RAIZ = pathlib.Path(__file__).resolve().parent.parent
PASTA = RAIZ / "base"
DADOS = RAIZ / "dados"
MARCA = re.compile(r"^<<<DOC (.+?)>>>$", re.M)


class Base:
    """Acesso uniforme aos documentos, em pasta ou em pacotes dados/*.md."""

    def __init__(self):
        self.docs = None
        if PASTA.is_dir():
            self.nomes = sorted(str(p.relative_to(PASTA)) for p in PASTA.rglob("*.md"))
        elif DADOS.is_dir() and any(DADOS.glob("*.md")):
            self.docs = {}
            for pac in sorted(DADOS.glob("*.md")):
                txt = pac.read_text(encoding="utf-8")
                partes = MARCA.split(txt)  # ["", nome1, texto1, nome2, texto2, ...]
                for i in range(1, len(partes) - 1, 2):
                    self.docs[partes[i]] = partes[i + 1].lstrip("\n")
            for extra in ("INDICE.md", "ATUALIZACOES.md"):  # ficam na raiz da skill, fora dos pacotes
                if extra not in self.docs and (RAIZ / extra).exists():
                    self.docs[extra] = (RAIZ / extra).read_text(encoding="utf-8")
            self.nomes = sorted(self.docs)
        else:
            sys.exit(f"Base não encontrada (procurei {PASTA} e {DADOS}/*.md).")

    def texto(self, nome):
        if self.docs is not None:
            return self.docs[nome]
        return (PASTA / nome).read_text(encoding="utf-8")

    def resolve(self, nome):
        nome = nome.strip().lstrip("./").removeprefix("base/")
        if nome in self.nomes:
            return nome
        cand = [n for n in self.nomes if n.endswith("/" + nome) or n.endswith(nome)]
        if len(cand) == 1:
            return cand[0]
        sys.exit(f"Documento '{nome}' não encontrado." + (f" Candidatos: {', '.join(cand[:10])}" if cand else
                                                          " Use --listar para ver os nomes."))


def etiquetas(base):
    """Mapa caminho -> etiqueta de situação, lida das tabelas do INDICE.md e dos catálogos (catalogo/*.md)."""
    tags = {}
    fontes = [n for n in base.nomes if n == "INDICE.md" or n.startswith("catalogo/")]
    for fonte in fontes:
        cols = []
        for ln in base.texto(fonte).splitlines():
            if ln.startswith("| arquivo |"):
                cols = [c.strip() for c in ln.strip("|").split("|")]
                continue
            if not re.match(r"\| (sefaz|confaz|normas)/", ln):
                continue
            cel = [c.strip() for c in ln.strip("|").split("|")]
            row = dict(zip(cols, cel))
            partes = []
            sit = row.get("situação", "").replace("*", "")
            if sit and not sit.startswith("vigente"):
                partes.append(sit.split(":")[0].strip())
            if row.get("alertas"):
                partes.append(row["alertas"])
            if partes and cel[0] not in tags:
                tags[cel[0]] = " | ".join(partes)
    return tags


def prioridade(nome, tags):
    """Ordem dos resultados: CTE, RICMS 2003, anexos vigentes, normas complementares vigentes, CONFAZ vigente,
    alteradoras, revogados/históricos, índice e catálogos."""
    t = tags.get(nome, "")
    ruim = any(x in t for x in ("HISTÓRICO", "histórica", "DENUNCIADO", "MA SAIU")) or re.search(r"(?<!PARCIALMENTE )REVOGAD", t)
    if nome in ("INDICE.md", "ATUALIZACOES.md") or nome.startswith("catalogo/"):
        return (9, nome)
    if ruim:
        return (8, nome)
    if "alteradora (incorporada)" in t:
        return (6, nome)
    if nome.startswith("sefaz/cte"):
        return (0, nome)
    if nome.startswith("sefaz/ricms-decreto"):
        return (1, nome)
    if nome.startswith("sefaz/"):
        return (2, nome)
    if nome.startswith("normas/"):
        return (3, nome)
    return (4, nome)


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def padrao(termo, regex):
    if regex:
        return re.compile(termo, re.I)
    return re.compile(re.escape(sem_acento(termo)))


def ler(base, nome, linhas):
    nome = base.resolve(nome)
    ls = base.texto(nome).splitlines()
    ini, fim = 1, min(len(ls), 200)
    if linhas:
        a, _, b = linhas.partition("-")
        ini, fim = max(1, int(a)), min(len(ls), int(b) if b else int(a) + 199)
    print(f"=== {nome} (linhas {ini}-{fim} de {len(ls)})")
    for i in range(ini - 1, fim):
        print(f"{i + 1:6d}  {ls[i]}")
    if fim < len(ls):
        print(f"... continua: --ler {nome} --linhas {fim + 1}-{min(len(ls), fim + 200)}")


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("termo", nargs="?")
    ap.add_argument("--doc", default="")
    ap.add_argument("--vigente", action="store_true")
    ap.add_argument("--regex", action="store_true")
    ap.add_argument("--artigo")
    ap.add_argument("-C", type=int, default=2)
    ap.add_argument("--max", type=int, default=40)
    ap.add_argument("--onde", action="store_true")
    ap.add_argument("--ler")
    ap.add_argument("--linhas")
    ap.add_argument("--listar", nargs="?", const="")
    ap.add_argument("--historico", action="store_true", help="inclui o RICMS/1995 (histórico) na busca")
    a = ap.parse_args()
    base = Base()
    tags = etiquetas(base)

    if a.ler:
        return ler(base, a.ler, a.linhas)
    if a.listar is not None:
        for n in base.nomes:
            if a.listar.lower() in n.lower():
                print(n)
        return

    if a.artigo:
        n = re.escape(a.artigo.upper().replace("º", "").replace("°", ""))
        sufixo = "" if re.search(r"-[A-Z]$", a.artigo.upper()) else r"(?!\s*[-–]\s*[A-Z]\b)"
        pat = re.compile(rf"^\s*(?:~~)?\s*Art\.?\s*{n}(?:\s*[º°o])?(?![\d]){sufixo}[\s.\-–]", re.I)
        a.regex = True
    elif a.termo:
        pat = padrao(a.termo, a.regex)
        palavras = sem_acento(a.termo).split()
        pat_corrido = re.compile(r"\s+".join(re.escape(w) for w in palavras)) if palavras else pat
    else:
        ap.print_help()
        return

    total, por_doc = 0, {}
    incluir_hist = a.historico or "1995" in a.doc
    for nome in sorted(base.nomes, key=lambda n: prioridade(n, tags)):
        if a.doc.lower() not in nome.lower():
            continue
        if "ricms-1995" in nome and not incluir_hist:
            continue
        linhas = base.texto(nome).splitlines()
        pagina, paginas = None, []
        for ln in linhas:
            m = re.match(r"<!-- p\. (\d+) -->", ln)
            if m:
                pagina = m.group(1)
            paginas.append(pagina)
        def omitida(ln):
            return a.vigente and (ln.strip().startswith("~~") and ln.strip().endswith("~~") and "~~" not in ln.strip()[2:-2]
                                  or re.match(r"\s*> Reda[çc][ãa]o (anterior|original)", ln))

        # com --vigente, os trechos tachados (~~…~~) são apagados antes de casar, inclusive em linhas mistas
        casar = [re.sub(r"~~.*?~~", " ", ln) if a.vigente else ln for ln in linhas]
        if a.regex:  # regex e --artigo: linha a linha
            achados = [(i, i) for i, ln in enumerate(casar) if not omitida(linhas[i]) and pat.search(ln)]
        else:  # literal: no texto corrido (a frase pode atravessar quebras de linha)
            norm = [sem_acento(ln) for ln in casar]
            inicios, pos = [], 0
            for t in norm:
                inicios.append(pos)
                pos += len(t) + 1
            corrido = " ".join(norm)
            achados, vistos = [], set()
            for m in pat_corrido.finditer(corrido):
                i = bisect.bisect_right(inicios, m.start()) - 1
                j = bisect.bisect_right(inicios, max(m.start(), m.end() - 1)) - 1
                if i in vistos or omitida(linhas[i]):
                    continue
                vistos.add(i)
                achados.append((i, j))
        for i, j in achados:
            por_doc[nome] = por_doc.get(nome, 0) + 1
            total += 1
            if a.onde or total > a.max:
                continue
            ini, fim = max(0, i - a.C), min(len(linhas), j + a.C + 1)
            pg = f" p.{paginas[i]}" if paginas[i] else ""
            tg = f"  [{tags[nome]}]" if nome in tags else ""
            print(f"\n=== {nome}:{i + 1}{pg}{tg}")
            for k in range(ini, fim):
                if linhas[k].startswith("<!-- p."):
                    continue
                print(("» " if i <= k <= j else "  ") + linhas[k])
    print(f"\n--- {total} ocorrência(s) em {len(por_doc)} documento(s)"
          + (f" (mostrando {a.max})" if total > a.max and not a.onde else ""))
    if a.onde or len(por_doc) > 1:
        for d, c in sorted(por_doc.items(), key=lambda x: -x[1])[:30]:
            print(f"  {c:5d}  {d}" + (f"  [{tags[d]}]" if d in tags else ""))
    if not incluir_hist and (not a.doc or "ricms" in a.doc.lower()):
        print("(RICMS/1995, histórico, fora da busca; use --historico para incluí-lo)")


if __name__ == "__main__":
    main()
