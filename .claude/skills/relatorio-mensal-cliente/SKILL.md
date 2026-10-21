---
name: relatorio-mensal-cliente
description: Gera o relatorio mensal para o cliente da Recria em linguagem simples e visual: o que foi publicado, resultados, aprendizados e proximo mes, com honestidade sobre limites. Use depois do analista-resultados, no fim de cada mes.
---

# Relatorio mensal para o cliente

## Passo 0
Identifique o cliente. Leia `[pasta]/conteudo/contexto.md`, `[pasta]/conteudo/resultados/AAAA-MM.md` (saida do `analista-resultados`), `[pasta]/conteudo/calendario-AAAA-MM.md` e `[pasta]/trafego-pago/` do mes. Se o resultado do mes ainda nao foi analisado, rode `analista-resultados` antes.

## Estrutura (maximo de 2 paginas)
1. **Resumo em 5 linhas**: o que foi feito e o principal resultado.
2. **O que publicamos**: quantidade por formato, com 3 destaques.
3. **Resultados**: alcance, novos seguidores, conversas, leads, vendas; comparar com o mes anterior; separar organico de anuncio.
4. **O que aprendemos**: 3 aprendizados e o que vamos repetir ou parar.
5. **Proximo mes**: temas, formatos e o que precisamos do cliente (gravacoes, depoimentos, aprovacoes).

## Regras
- Linguagem do cliente, sem jargao. Numeros arredondados e comparacoes simples.
- Seja honesto: mostre o que nao funcionou e o que e hipotese. Nao use dados fabricados nem generalize.
- Nao exponha fraquezas internas do cliente (as secoes de fraquezas dos diagnosticos sao so da agencia).
- Respeite as regras de tom do cliente (Eleva sem travessao, Strategia em 1a pessoa do plural).
- Se houver pendencia do cliente (gravacoes atrasadas), diga como isso afetou o resultado, sem culpar.

Salve em `[pasta]/conteudo/relatorio-cliente-AAAA-MM.md`. Se a Amanda pedir versao visual, gere HTML na mesma pasta com a identidade do cliente.
