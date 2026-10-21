---
name: agencia-recria
description: Orquestra a agencia Recria de ponta a ponta. Dado um cliente e o que a Amanda quer (onboarding, diagnostico, marca, calendario, rotina de gravacao, copy, revisao, planner, criativos, anuncios, comercial, automacao, resultados, relatorio, proposta), indica a skill certa e a ordem, ou executa o ciclo mensal completo de um cliente. Use quando a Amanda nao souber por onde comecar ou disser "agencia, mes completo".
---

# Agencia Recria: orquestrador

## Como a Amanda chama
- "Agencia, qual o proximo passo da Camila?"
- "Agencia, mes completo da Strategia, novembro."
- "Agencia, so a rotina de gravacao da Paty."

## O que fazer
1. Pergunte (se faltar) o cliente e o mes.
2. Leia `AGENCIA.md` e a pasta do cliente (o que ja existe: questionario, diagnostico, marca, contexto, calendarios, copies, criativos, resultados).
3. Diga em que etapa o cliente esta e qual o proximo passo, com a skill e uma frase de como invocar.
4. Se faltar `[cliente]/conteudo/contexto.md`, crie a partir do diagnostico e peca confirmacao da Amanda antes de seguir.

## Ciclo mensal completo ("mes completo")
Execute em ordem, parando para aprovacao da Amanda ao final de cada bloco:
1. Contexto e prova de leitura.
2. `pesquisador-ganchos` (se o banco estiver desatualizado ou houver referencias novas).
3. `analista-resultados` do mes anterior (se houver Insights).
4. `estrategista-conteudo-cliente`: calendario do mes.
5. `claquete-rotina-gravacao`: cronograma de gravacao na agenda do cliente.
6. `copywriter-cliente` (externo): roteiros, legendas, carrosseis.
7. `revisor-claims-cliente`.
8. `planner-clicavel`: versao interna e do cliente.
9. `design-social-media-cliente` e, se houver anuncio, `gestor-trafego-cliente`, `design-trafego-cliente` e `automacao-youze-cliente`.
10. No fim do mes: `relatorio-mensal-cliente`.

## Regras
- Nao produza conteudo por conta propria: encaminhe para a skill da etapa.
- Nada vai ao cliente sem aprovacao da Amanda.
- Se uma skill necessaria nao existir neste repositorio (as marcadas "externa" em `AGENCIA.md`), diga qual e onde estao os insumos.
- Se houver conflito entre arquivos ou skills, mostre e pergunte.
