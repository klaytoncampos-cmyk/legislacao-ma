# Legislação tributária do Maranhão: skill para o Claude Code

Texto integral e atualizado do CTE (Lei 7.799/2002), do RICMS-MA (Decreto 19.714/2003) e seus anexos, das normas
complementares da SEFAZ-MA e dos convênios, protocolos e ajustes SINIEF do CONFAZ citados por elas, além da **pauta
fiscal (Tabela de Valores de Referência do ICMS)** de cimento, materiais de construção, madeira, bebidas e sorvetes, com o histórico de cada item. A base é atualizada
toda semana a partir das fontes oficiais, e cada atualização chega sozinha a quem instalou o plugin.

## O que tem na base

- **Legislação**: CTE, RICMS-MA e todos os anexos, com as redações revogadas marcadas (tachado no PDF oficial) para
  consulta histórica; portarias, resoluções, decretos e instruções normativas da SEFAZ-MA que alteram ou disciplinam o
  RICMS e seus anexos; convênios, protocolos e ajustes SINIEF do CONFAZ citados pela legislação maranhense, com as
  redações anteriores.
- **Pauta fiscal / valores de referência**: a Tabela de Valores de Referência montada a partir das portarias da SEFAZ-MA
  que incluem, alteram ou excluem itens.
  - **Cimento**: valores vigentes e histórico desde 2011, conferidos contra os PDFs.
  - **Bebidas**: cervejas e chopes, refrigerantes, energéticos e isotônicos, águas, bebidas mistas, vinhos e destilados.
    Os itens são identificados por código **e** embalagem/volume, porque a SEFAZ usa o mesmo código para produtos
    diferentes em seções diferentes da tabela (ex.: 45027 é Heineken long neck 330 ml e Itaipava lata 473 ml).
  - **Materiais de construção** (Grupo 03: lajotas, telhas, tijolos, blocos, areia, barro, pedras e britas, gesso, mármores e
    granitos) e **madeira** (em tora, serrada, beneficiada e para cerca, por espécie), com histórico desde 2010.
  - **Sorvetes e picolés**: tabelas de cada fornecedor (Nestlé/Garoto, Tigelí, Ster Bom, Flamboyant, Maioca, sorveterias
    regionais), quase sempre sem código; o item é identificado pela descrição (marca, sabor, tamanho).
  - Para cada item: **valor vigente**, **histórico** (todas as portarias, com a variação), **valor com vigência futura**
    quando a portaria já foi publicada mas ainda não vale ("→ R$ X a partir de DATA"), e o link para o PDF da portaria.
  - Para **auditoria de período passado**, use o histórico do item: vale a última linha com vigência até a data do fato
    gerador. A vigência já considera "entra em vigor a partir de".

## Cuidados com a pauta

- A leitura das tabelas em PDF é automática. Foi conferida por amostragem e contra um extrator independente em todas as
  portarias de bebidas, mas **confira na portaria (link) antes de usar em lançamento**.
- "Situação incerta" e "superado" (item que deixou de aparecer nas republicações da tabela) são **dedução**: as
  portarias de pauta raramente excluem itens de forma expressa. Revogação de portaria de pauta não é tratada.
- **Vinhos**: a última portaria é de 2022 e a tabela nunca foi republicada inteira, então "vigente" significa só
  "último valor publicado". **Destilados**: quase não há itens na pauta; não use.
- Nem toda portaria de pauta é publicada no portal de legislação da SEFAZ. As conhecidas que saíram só no Diário
  Oficial entram marcadas como "DOE, fora do portal". Para valor recente, a skill também pesquisa na web.

## Instalação (Windows, Mac ou Linux)

1. **Python 3.** No Windows, o jeito mais simples é instalar o **Python 3** pela Microsoft Store, que já cria o comando `python3`.
   Se preferir o instalador do python.org, marque "Add python.exe to PATH".
2. **Claude Code** instalado e funcionando. No Windows ele precisa do Git for Windows.
3. No Claude Code, rode uma vez:

   ```
   /plugin marketplace add klaytoncampos-cmyk/legislacao-ma
   /plugin install legislacao-tributaria-ma@legislacao-ma
   ```

4. **Ligue a atualização automática:** digite `/plugin`, abra **Marketplaces**, escolha `legislacao-ma` e ative
   **Enable auto-update**. A partir daí, alguns minutos depois de você começar a usar o Claude Code ele confere se há
   versão nova da base e baixa sozinho. A versão nova vale na próxima vez que abrir o Claude Code (ou na hora, com `/reload-plugins`).
5. Feche e abra o Claude Code.

Para testar, pergunte por exemplo:

- *"Qual a MVA de autopeças no Maranhão?"*
- *"O que diz o Anexo 4.24 do RICMS sobre medicamentos?"*
- *"Qual o valor de referência da Heineken lata 350 ml? E quanto era em março de 2024?"*
- *"Histórico da pauta do cimento CP II Nassau 50 kg."*

## Atualizar na mão

No terminal:

```
claude plugin update legislacao-tributaria-ma@legislacao-ma
```

Ou dentro do Claude Code: `/plugin` → **Installed** → `legislacao-tributaria-ma` → **Update now**, e depois `/reload-plugins`.

O registro do que mudou em cada atualização fica em `ATUALIZACOES.md`, dentro da pasta da skill.

## Aviso

Ferramenta de apoio à consulta. Não é publicação oficial da SEFAZ-MA nem do CONFAZ e não substitui a leitura do texto
oficial: cada documento traz o link da fonte.

## Licença

Código e organização da base sob a [licença MIT](LICENSE). Os textos das normas (leis, decretos, portarias, convênios) são atos oficiais, sem direito autoral (Lei 9.610/1998, art. 8º, IV).
