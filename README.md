# Legislação tributária do Maranhão — skill para o Claude Code

Texto integral e atualizado do CTE (Lei 7.799/2002), do RICMS-MA (Decreto 19.714/2003) e seus anexos, das normas
complementares da SEFAZ-MA e dos convênios, protocolos e ajustes SINIEF do CONFAZ citados por elas. A base é
atualizada toda semana a partir das fontes oficiais, e cada atualização chega sozinha a quem instalou o plugin.

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

Para testar, pergunte por exemplo: *"Qual a MVA de autopeças no Maranhão?"*.

## Atualizar na mão

No terminal:

```
claude plugin update legislacao-tributaria-ma@legislacao-ma
```

Ou dentro do Claude Code: `/plugin` → **Installed** → `legislacao-tributaria-ma` → **Update now**, e depois `/reload-plugins`.

O registro do que mudou em cada atualização fica em `ATUALIZACOES.md`, dentro da pasta da skill.
