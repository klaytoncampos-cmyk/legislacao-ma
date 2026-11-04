---
name: legislacao-tributaria-ma
description: >-
  Especialista em legislação tributária do Maranhão (ICMS). Use SEMPRE que a pergunta envolver ICMS no Maranhão,
  RICMS-MA (Decreto 19.714/2003), Código Tributário Estadual (Lei 7.799/2002), anexos do RICMS-MA, substituição
  tributária, antecipação, isenção, redução de base de cálculo, crédito presumido, diferimento, alíquotas, MVA,
  pauta fiscal ou valores de referência do ICMS (Tabela de Valores de Referência da SEFAZ-MA: cimento, materiais de
  construção, madeira, cervejas, refrigerantes, energéticos, águas, sorvetes), NCM/CEST, segmentos (autopeças,
  combustíveis, bebidas, medicamentos etc.), ou convênios, protocolos e ajustes SINIEF do CONFAZ citados pela
  legislação maranhense. Contém o texto integral e atualizado dessas normas, com histórico de redações. Consulte
  primeiro a base local (texto oficial) e use a web para complementar: normas fora da base, alterações recentes,
  jurisprudência e interpretação.
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

Os documentos (5.501 nesta edição: 143 da SEFAZ-MA, 1.828 normas complementares, 3.519 do CONFAZ) ficam agrupados em poucos arquivos `dados/*.md`, cada um começando por uma linha
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

## Valores de referência (pauta do ICMS)

`valores/<produto>.md` (ex.: `valores/cimento.md`) reúne a **Tabela de Valores de Referência** montada a partir das portarias da
SEFAZ-MA que incluem, alteram ou excluem itens da tabela. Comece por `python3 scripts/buscar.py --ler valores/cimento.md --linhas 1-80`.
- **Valores vigentes**: valor da portaria mais recente que tratou do item (código da tabela da SEFAZ ou, sem código, a descrição).
- **Situação incerta**: último valor conhecido, mas o item sumiu de uma relação completa posterior ou o **código dele foi dado a outro
  produto** (⚠, ex.: 53306 = Bravo na Portaria 141/2026, Mizu na 158/2026 e Zebu na 178/2026). Não apresente como vigente: diga o
  último valor, o motivo e recomende confirmar na SEFAZ.
- **Superados**: código trocado para o mesmo produto; informe até quando valeu.
- **Histórico por item**: todas as portarias que trataram do item, com a variação de valor e a origem da data (pub./efeitos/assin.).
- **Data passada (auditoria)**: "vigente", "incerto" e "superado" se referem à data de geração do arquivo. Para o valor numa
  data D, use o **histórico por item**: vale a última linha com vigência ≤ D (a coluna "vigência" já considera "entra em vigor a
  partir de"). Onde o projeto de geração estiver disponível, `python3 -I ~/legislacao-ma/scripts/tabela_valores.py produto
  bebidas --data AAAA-MM-DD --saida PASTA` gera a tabela inteira como estava em D (status calculados só com as portarias até D).
- **Vigência futura**: portaria já publicada que só vale depois (ex.: Portaria 402/2026, vigor em 01/11/2026) aparece como
  "→ R$ X a partir de DATA" ao lado do valor atual e na seção "Valores com vigência futura". Compare com a data de hoje e com a
  data do fato gerador: **se a data já foi alcançada, o valor futuro é o que vale**. O cabeçalho de cada arquivo diz quando ele foi gerado.
- Portarias marcadas **"DOE, fora do portal; texto de agregador"** saíram no Diário Oficial mas não estão no portal de legislação da
  SEFAZ; foram transcritas de site agregador. Diga isso ao citar o valor.
- **O portal da SEFAZ nem sempre publica todas as portarias de pauta.** Quando o valor for para lançamento ou a pergunta for sobre
  alteração recente, pesquise na web portarias posteriores à mais recente da base para o produto (ex.: "Portaria GABIN valores de
  referência cimento 2026").
- **Cite sempre a portaria** (número, data, link) e recomende conferir no texto oficial antes de lançamento: a leitura das tabelas é
  automática, e portarias com a tabela só em imagem (sobretudo 2003–2013) não foram lidas.
- **Bebidas** (`valores/bebidas-cerveja.md`, `-refrigerante`, `-energetico`, `-agua`, `-vinho`, `-destilado`, `-outras`): a tabela é
  dividida em seções de embalagem e volume ("Cerveja - Lata | 350 ml"), que entram entre parênteses na descrição; o mesmo código
  designa produtos diferentes em seções diferentes, então identifique o item por **descrição + embalagem + volume**, não só pelo
  código. Busque por marca e volume (ex.: `buscar.py "Heineken" --doc valores/bebidas-cerveja`). Esses arquivos existem **só na
  edição completa (Claude Code)**; no chat, diga que a pauta de bebidas não está nesta edição e pesquise na web.
- **Sorvetes e picolés** (`valores/sorvetes.md`): cada portaria é a tabela de um fornecedor (Nestlé/Garoto, Tigelí/Classicy, Ster
  Bom, Flamboyant Gelato, Maioca, Akaska, sorveterias regionais), quase sempre **sem código**: o item é identificado pela descrição
  (marca, sabor, peso ou volume), e a relação completa de um fornecedor só vale para os itens dele. Busque por marca e tamanho
  (ex.: `buscar.py "Ster Bom" --doc valores/sorvetes`). Item sem código sem atualização há mais de 3 anos fica "incerto". Arquivo
  **só na edição completa (Claude Code)**; no chat, diga que a pauta de sorvetes não está nesta edição e pesquise na web.
- **Materiais de construção** (`valores/construcao-materiais.md`: lajotas, telhas, tijolos, blocos, areia, barro, pedras e britas,
  gesso, mármores e granitos, o Grupo 03 da tabela menos o cimento) e **madeira** (`valores/construcao-madeira.md`: em tora,
  serrada, beneficiada e para cerca, por espécie): itens por código, com a seção ("Subgrupo 08 Pedra") entre parênteses quando
  a descrição não diz. Brita, pó de brita e pedras têm valores distintos para "consumidor final inscrito/construção civil" e
  "varejo", em tonelada e em m³; confira unidade e destino. Portaria sem código que altera item codificado (ex.: 115/2025, telha
  colonial e tijolo 6 furos) aparece com o código anterior marcado "(ant.)". O consolidado do Grupo 03 publicado pela SEFAZ pode
  estar defasado em relação às portarias: vale a portaria mais recente. Bloco de cimento e gipsita para cimento também estão em
  `cimento.md`. A pauta **não tem ferro de construção** (vergalhão, arame); "ferro" e "aço" na pauta são sucata. Arquivos **só na
  edição completa (Claude Code)**.
- Produtos ainda sem arquivo em `valores/`: diga que a pauta desse produto ainda não foi consolidada na base e pesquise na web.

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
    valores/<produto>.md        Tabela de Valores de Referência por produto (vigentes + histórico)
    catalogo/normas.md          catálogo de todas as normas complementares (data, ementa, remete a, situação)
    catalogo/confaz.md          catálogo de todas as normas do CONFAZ (ementa, situação, onde é citada)
    normas/<tipo>/*.md          portarias, resoluções, decretos e instruções normativas que remetem ao RICMS/anexos/CTE
    confaz/convenio/*.md        convênios ICMS (citados, suas alteradoras e os do ano corrente)
    confaz/protocolo/*.md       protocolos ICMS (citados, seus alteradores e os do ano corrente)
    confaz/ajuste/*.md          ajustes SINIEF (citados e seus alteradores)
```
