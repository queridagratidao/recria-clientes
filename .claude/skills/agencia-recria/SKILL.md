---
name: agencia-recria
description: Orquestra a agencia Recria de ponta a ponta. Dado um cliente e o que a Amanda quer (onboarding, diagnostico, calendario, copy, revisao, planner, criativos, anuncios, gravacao, resultados), indica a skill certa, a ordem e o que ja existe na pasta do cliente. Use quando a Amanda nao souber por onde comecar ou pedir o proximo passo de um cliente.
---

# Agencia Recria: orquestrador

## O que fazer
1. Pergunte qual cliente e qual o objetivo do momento.
2. Leia `AGENCIA.md` (fluxo e status das skills) e a pasta do cliente (`ls`): o que ja existe (questionario, diagnostico, marca, contexto, calendarios, copies, criativos, resultados).
3. Diga em que etapa o cliente esta, qual e o proximo passo e qual skill chamar, com uma frase de como invocar. Exemplo: "Falta o calendario de novembro. Use `estrategista-conteudo-cliente` para a Camila, novembro."
4. Se a etapa depende de uma skill que nao esta neste repositorio (questionario, diagnostico, copy, design), diga que ela roda fora daqui e aponte onde estao os insumos.
5. Se faltar `[cliente]/conteudo/contexto.md`, crie a partir do diagnostico antes de qualquer producao e peca a confirmacao da Amanda.

## Ordem tipica de um cliente novo
questionario-cliente, estrategista-cliente, branding-cliente, pesquisador-ganchos, estrategista-conteudo-cliente, copywriter-cliente, revisor-claims-cliente, planner-clicavel, design-social-media-cliente e design-trafego-cliente, analista-resultados (ciclo mensal).

## Regras
- Nao produza conteudo por conta propria: encaminhe para a skill da etapa.
- Nada vai ao cliente sem aprovacao da Amanda.
- Se houver conflito entre skills ou arquivos, mostre o conflito e pergunte.
