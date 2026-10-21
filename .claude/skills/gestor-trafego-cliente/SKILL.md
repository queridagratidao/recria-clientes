---
name: gestor-trafego-cliente
description: Planeja e acompanha campanhas de trafego pago (Meta e Google) de um cliente da Recria: objetivo, estrutura, orcamento, segmentacao, plano de teste de criativos, regras de pausa e escala e leitura semanal de CPL e CPA contra o break-even do cliente. Use ao subir, revisar ou diagnosticar campanhas.
---

# Gestor de trafego por cliente

## Passo 0
Identifique o cliente. Leia `[pasta]/conteudo/contexto.md`, `[pasta]/diagnostico-estrategico.md` (secoes de break-even, orcamento e plano de acao), a pasta `[pasta]/trafego-pago/` e, se houver, os arquivos de diagnostico de campanhas e automacao. Faca a prova de leitura: objetivo de negocio, verba, ticket, break-even, capacidade de atendimento.

## Plano de campanha
1. **Objetivo e funil**: venda direta, mensagem no WhatsApp, lead (formulario) ou engajamento para qualificacao; coerente com a verba. Verba curta pede um unico objetivo.
2. **Capacidade**: nao gere mais lead do que o cliente atende (Refugio: 1 vaga fixa por semana).
3. **Segmentacao**: geografia real do cliente, idade, interesses; evitar sobreposicao entre conjuntos.
4. **Estrutura**: 1 campanha, poucos conjuntos, 3 a 5 criativos por conjunto.
5. **Plano de teste**: uma variavel por vez (gancho, formato, oferta, CTA). Criativos vem do calendario e do banco de ganchos.
6. **Mensuracao**: UTMs, pixel, eventos (lead, conversa iniciada, compra) e registro do que cada palavra-chave do Youze trouxe.
7. **Metas**: CPL e CPA alvo derivados do break-even do diagnostico (ex.: quantas vendas pagam o investimento fixo).

## Regras de operacao (heuristicas; ajustar ao cliente)
- Nao mudar o orcamento mais de ~20% por vez; nao editar anuncio em fase de aprendizado sem necessidade.
- Pausar um criativo so com dado suficiente (por exemplo, gasto de 2 a 3 vezes o CPA alvo sem conversao) e registrar o motivo.
- Escalar so o que repete resultado por alguns dias.
- Verba pequena rende melhor com orcamento constante todos os dias do que ligando e desligando.
- Nunca prometer resultado ao cliente; trabalhar com faixas e hipoteses.

## Rotina semanal
Ler os numeros (gasto, alcance, CPL, conversas, vendas), comparar com a meta, listar decisoes (manter, pausar, testar), registrar em `[pasta]/trafego-pago/relatorio-semanal-AAAA-SNN.md` e levar aprendizados para `[pasta]/conteudo/decisoes.md`.

## Entrega
`[pasta]/trafego-pago/plano-AAAA-MM.md` (plano, metas, testes) e os relatorios semanais. Criativos e briefing visual seguem com `design-trafego-cliente`; copies com `copywriter-cliente`; checagem de promessas com `revisor-claims-cliente`.
