---
name: legislacao-tributaria-ma
description: Especialista em legislação tributária do Maranhão (ICMS). Use SEMPRE que a pergunta envolver ICMS no Maranhão, RICMS-MA (Decreto 19.714/2003), Código Tributário Estadual (Lei 7.799/2002), anexos do RICMS-MA, substituição tributária, antecipação, isenção, redução de base de cálculo, crédito presumido, diferimento, alíquotas, MVA, NCM/CEST, segmentos (autopeças, combustíveis, bebidas, medicamentos etc.), ou convênios, protocolos e ajustes SINIEF do CONFAZ citados pela legislação maranhense. Contém o texto integral e atualizado dessas normas, com histórico de redações. Consulte primeiro a base local (texto oficial) e use a web para complementar: normas fora da base, alterações recentes, jurisprudência e interpretação.
---

# Legislação tributária do Maranhão (ICMS)

Esta skill traz o **texto integral** das normas, extraído das fontes oficiais:

- **SEFAZ-MA**: CTE (Lei 7.799/2002), RICMS (Decreto 19.714/2003; o RICMS/1995 só como histórico) e os anexos do RICMS (em torno de 140).
- **Normas complementares da SEFAZ-MA**: portarias, resoluções administrativas, decretos e instruções normativas cujo texto remete
  ao RICMS, a um anexo ou ao CTE (ex.: Portaria nº 410/2025 – GABIN, que regulamenta o credenciamento do Anexo 4.24). Ficam fora
  as administrativas (repasses, códigos de receita, licitações…) e as tabelas de valores de referência.
- **CONFAZ**: os convênios ICMS, protocolos ICMS e ajustes SINIEF **citados** nesses documentos; as normas que **alteram, aderem,
  denunciam ou revogam** essas normas (citadas no cabeçalho e nas notas de alteração delas, ex.: o Prot. ICMS 50/16, que alterou o 41/08);
  e todas as do ano corrente. O texto das normas citadas já vem **consolidado** pelo CONFAZ, com as alterações incorporadas e as notas
  "Nova redação dada… pelo Prot. X"; a norma alteradora serve para conferir o texto original da alteração e suas regras de vigência.

Os documentos (5.476 nesta edição: 143 da SEFAZ-MA, 1.824 normas complementares, 3.509 do CONFAZ) ficam agrupados em poucos arquivos `dados/*.md`, cada um começando por uma linha
`<<<DOC caminho>>>`. Use sempre `scripts/buscar.py`, que separa os documentos e busca/lê cada um pelo seu caminho. `INDICE.md` (na raiz da skill) lista todos os documentos, com descrição,
situação (vigente/parcial/revogado), data de atualização na fonte e caminho.

## Como consultar (sempre nesta ordem)

Rode os comandos a partir da pasta da skill (onde está este `SKILL.md`). No Windows, se `python3` não existir
(ou abrir a Microsoft Store), use `py` ou `python` no lugar.

1. **Localize os documentos.** Leia `INDICE.md` (ou busque nele: `python3 scripts/buscar.py "autope" --doc INDICE`) para achar os anexos e convênios do assunto. Por exemplo, para autopeças: Anexo 4.41, RICMS (substituição tributária), Convênio ICMS 142/18 (Anexo II) e Protocolos ICMS 41/08 e 97/10. O Anexo 4.29 entra só como histórico, porque tem alerta ⚠ (veja o passo 6).
2. **Busque o texto:**
   ```bash
   python3 scripts/buscar.py "termo" --vigente            # só texto em vigor
   python3 scripts/buscar.py "8708.29" --doc anexo-4       # filtra por documento
   python3 scripts/buscar.py --artigo 291 --doc ricms      # localiza o caput de um artigo
   python3 scripts/buscar.py "Conv. ICMS 142/18" --onde    # onde a norma é citada
   ```
   A busca ignora acentos e maiúsculas. Sem `--regex`, o termo é literal e procurado no **texto corrido**: uma frase é
   encontrada mesmo que atravesse a quebra de linha do PDF (o resultado marca com » todas as linhas do trecho). Com `--regex`
   e `--artigo` a busca é linha a linha.
   **Dicas:** a legislação raramente usa o nome popular do segmento. Busque também os termos técnicos
   (ex.: autopeças → "peças, partes, componentes", "autopropulsados"), o **NCM** (com e sem pontos, ex.: `8708`, `8708.29`),
   o **CEST** (ex.: `01.075.00`) e o número da norma (`142/18`). Faça várias buscas curtas em vez de uma longa.
   **Segmentos sujeitos à ST** costumam seguir esta cadeia: anexo 4.x do RICMS-MA → RICMS (arts. 527 e seguintes) →
   anexo correspondente do Convênio ICMS 142/18 (lista de CEST/NCM) → protocolos ou convênios específicos.
3. **Leia o dispositivo inteiro.** A linha encontrada não basta. Cada resultado mostra `documento:linha`; leia o trecho em volta
   e o artigo completo (caput, parágrafos, incisos, alíneas, notas de alteração) e os artigos vizinhos de que ele dependa:
   ```bash
   python3 scripts/buscar.py --ler sefaz/anexo-4.41.md --linhas 20-120
   python3 scripts/buscar.py --ler confaz/protocolo/protocolo-041-2008.md --linhas 1-80   # cabeçalho: alterações, adesões, denúncias
   python3 scripts/buscar.py --listar convenio-142                                        # nomes de documentos
   ```
4. **Procure as normas complementares do anexo.** Portarias costumam **regulamentar** o anexo (credenciamento, requisitos,
   procedimentos, prazos) e não aparecem no PDF do anexo. Veja a seção *Normas complementares da SEFAZ-MA por anexo* do `INDICE.md`,
   o catálogo `catalogo/normas.md` (data, ementa, situação de todas) ou busque: `python3 scripts/buscar.py "Anexo 4.24" --doc normas/`.
   **Situação das normas complementares** (no cabeçalho de cada arquivo e nas etiquetas da busca):
   - **REVOGADA** / *PARCIALMENTE REVOGADA*: revogação expressa em outra norma da base ("Fica revogada a Portaria nº 372/2017") ou
     anotação no **cabeçalho** do próprio PDF ("Revogada pela RA nº 09/24"). O cabeçalho do arquivo transcreve o trecho e aponta a
     revogadora: **confira esse trecho antes de afirmar a revogação**. Revogações de um artigo isolado em geral só aparecem como
     texto tachado `~~` dentro da norma.
   - *alteradora (incorporada)*: decreto/resolução que só altera o RICMS/anexo; a mudança deve estar no texto consolidado.
   - **alteradora RECENTE**: posterior à última atualização do PDF do anexo na fonte. A mudança **pode ainda não estar** no anexo
     consolidado; leia a própria norma.
   - *alteradora com dispositivos próprios*: altera o RICMS/anexo, mas também concede, convalida, remite ou prorroga algo. Leia a norma inteira.
   - *histórica*: alterava o RICMS/1995 (anterior a 10.07.2003); só serve como histórico.
   - sem etiqueta: nenhuma revogação identificada. **Não é garantia de vigência**, porque a detecção é automática e conservadora.
5. **Siga as remissões.** Se o texto maranhense remete a um convênio ("Conv. ICMS 142/18", "Protocolo ICMS 41/08"), leia
   `confaz/<tipo>/<tipo>-NNN-AAAA.md` (ex.: `confaz/convenio/convenio-142-2018.md`, `confaz/protocolo/protocolo-041-2008.md`).
   Se `--listar` não encontrar, diga que a norma não está na base. **Edição do chat (claude.ai):** por limite de tamanho, ela
   omite parte das normas (veja o aviso no topo do `INDICE.md`: alteradoras do CONFAZ de 2º nível e decretos mais antigos).
   O texto das normas citadas já vem consolidado, então isso raramente impede a resposta; quando impedir, diga que a norma está só
   na edição completa (Claude Code) e, se possível, consulte a fonte oficial na web.
6. **Confira a vigência** antes de afirmar qualquer coisa (veja as convenções abaixo). Cada resultado da busca traz entre
   colchetes a situação do documento, quando não é vigente: `[REVOGADO]`, `[parcial]`, `[DENUNCIADO …]`, `[MA SAIU …]` ou um
   alerta `[⚠ Prot. ICMS 36/04: DENUNCIADO]`. O alerta ⚠ quer dizer que o anexo maranhense se apoia numa norma do CONFAZ revogada
   ou denunciada, ou da qual o MA saiu (ex.: o Anexo 4.29 se baseia no Prot. ICMS 36/04, denunciado pelo Prot. ICMS 41/08 a partir de 01.06.08 e
   pelo MA via Prot. ICMS 97/10 a partir de 01.09.10). **Nunca apresente um anexo com ⚠ como regra aplicável sem explicar isso.**
   Por padrão o RICMS/1995 (histórico) fica fora da busca; use `--historico` só para pesquisa histórica. Olhe também as colunas *situação* e *alertas* do `INDICE.md`:
   anexos inteiros podem estar revogados mesmo sem aviso na descrição (ex.: o Anexo 45 foi revogado pela RA 27/2020).
   Um anexo pode estar com o texto "limpo" (sem tachado) e mesmo assim depender de um protocolo ou convênio já revogado ou denunciado.
   Abra a norma do CONFAZ e leia o cabeçalho ("Revogado pelo…", "Denunciado…", "Alterado pelo…").

## Convenções da base (importante)

- `~~texto~~` é **redação revogada ou anterior**. Na SEFAZ-MA, é o texto que aparece **tachado no PDF oficial**; no CONFAZ, são as redações anteriores. **Nunca apresente esse texto como vigente.** Use-o só para histórico ("até DD/MM/AAAA a redação era…").
- No CONFAZ, as linhas que começam com `>` são notas oficiais de alteração ("Nova redação dada… pelo Conv. ICMS X, efeitos a partir de…", "Redação anterior…"). Elas dizem **desde quando** vale cada redação.
- Na SEFAZ-MA, notas como `(NR Dec. 20.425/04)`, `(AC – RA 26/22)`, `(Revogado …)` indicam a norma que deu a redação (NR = nova redação; AC = acrescido).
- `<!-- p. N -->` marca a página do PDF original. Use para citar ("Anexo 1.4, art. 4º, p. 20 do PDF").
- `> **[PÁGINA N ESCANEADA…]**` indica conteúdo só em imagem (geralmente tabelas). Avise que o trecho não pôde ser lido e indique a página do PDF.
- A detecção de tachado é automática. Em **tabelas**, as bordas podem gerar falso tachado. Se uma linha de tabela inteira aparecer tachada sem nota de revogação por perto, trate como "a confirmar no PDF".

## Como responder

- **Fundamente com citação precisa:** documento, artigo/§/inciso/alínea (ou cláusula/item/CEST, no CONFAZ), página do PDF e o link `fonte:` do cabeçalho do arquivo.
- **Separe o que diz o texto do que é interpretação.** Transcreva o trecho essencial entre aspas quando a resposta depender da redação exata.
- **Vigência:** diga qual redação está em vigor e desde quando. Se houve mudança recente, mostre a redação anterior.
- **Norma maranhense e CONFAZ:** um convênio *autorizativo* só vale no MA se foi internalizado. Confirme no RICMS/anexo maranhense. Nas operações internas, prevalece a regra do anexo maranhense. Se só achar o convênio e não a internalização, diga isso.
- **Protocolos (ST interestadual):** confira se o **MA é signatário**. Veja o preâmbulo ("Os Estados de …, Maranhão, …") e as notas do cabeçalho
  ("Adesão do MA pelo Prot. …", "Denunciado pelo MA…", "Exclusão do MA…"). Leia também as notas `>` das cláusulas, porque o CONFAZ altera
  protocolos com frequência (ex.: o Prot. ICMS 41/08, de autopeças, foi alterado pelo Prot. ICMS 93/26, com efeitos a partir de 01.10.26).
- **Mudanças recentes:** `ATUALIZACOES.md` (na raiz da skill) registra, por data, o que mudou em cada atualização semanal (documentos da SEFAZ
  alterados, normas novas do CONFAZ e normas alteradas por elas). Consulte-o quando a pergunta for "o que mudou" ou envolver fatos recentes.
- **Data da base:** informe a data `atualizado_na_fonte` do documento usado.

## Base local e internet

A base local é a **fonte primária do texto normativo**: oficial, integral, com histórico e com as revogações marcadas. A web **complementa**; não substitui.

- **Use a web (se disponível) para o que a base não cobre:** normas fora da base (LC 87/96, LC 214/2025 e reforma tributária, decretos e
  resoluções administrativas avulsos, Simples Nacional, convênios não citados pela legislação maranhense); alterações publicadas depois da
  última atualização da base (veja a data em `ATUALIZACOES.md`); interpretação (soluções de consulta, jurisprudência do TARF/STJ/STF,
  orientações da SEFAZ); e contexto prático.
- **Prefira fontes oficiais:** confaz.fazenda.gov.br, planalto.gov.br, sefaz.ma.gov.br / portal-sgc.sefaz.ma.gov.br, Diário Oficial do
  Estado. Sites de terceiros (consultorias, blogs) servem para orientação, nunca como fonte do texto legal.
- **Não troque o texto da base por um resumo da web.** Se a base tem o dispositivo, cite-o da base.
- **Identifique a origem** de cada informação na resposta ("base local: Anexo 4.41, art. 1º" ou "web: planalto.gov.br/…, acessado em …").
- **Divergência:** se a web indicar algo mais recente que contradiz a base (ex.: decreto novo), **não escolha em silêncio**. Mostre as
  duas versões com as datas, diga qual parece vigente e por quê, e sugira atualizar a base.
- Sem acesso à web: responda com a base, diga o que ficou de fora e recomende conferir no portal: https://portal-sgc.sefaz.ma.gov.br/portal/legislacao
- Não invente número de artigo, alíquota, MVA ou prazo. Se não encontrar, diga que não encontrou e o que foi pesquisado.

## Estrutura

```
INDICE.md                       documentos da SEFAZ (situação e alertas), normas complementares por anexo, resumo do CONFAZ
ATUALIZACOES.md                 registro das atualizações semanais
scripts/buscar.py               busca (--vigente, --doc, --artigo), leitura (--ler/--linhas) e listagem (--listar)
dados/*.md                      os documentos agrupados (lidos pelo buscar.py):
    sefaz/*.md                  CTE, RICMS e anexos (um arquivo por documento)
    catalogo/normas.md          catálogo de todas as normas complementares (data, ementa, remete a, situação)
    catalogo/confaz.md          catálogo de todas as normas do CONFAZ (ementa, situação, onde é citada)
    normas/<tipo>/*.md          portarias, resoluções, decretos e instruções normativas que remetem ao RICMS/anexos/CTE
    confaz/convenio/*.md        convênios ICMS (citados, suas alteradoras e os do ano corrente)
    confaz/protocolo/*.md       protocolos ICMS (citados, seus alteradores e os do ano corrente)
    confaz/ajuste/*.md          ajustes SINIEF (citados e seus alteradores)
```
