---
name: planner-clicavel
description: Transforma o calendario mensal de um cliente em um planner HTML interativo (semana em 7 colunas, cartoes que expandem com roteiro, copy, legenda, CTA, material e dia de gravacao), em versao interna e versao para o cliente, com opcao de PDF por links internos. Use depois que o calendario estiver pronto.
---

# Planner clicavel

## Passo 0
Identifique o cliente e leia `[pasta]/conteudo/contexto.md`, a identidade visual (`DESIGN.md`, `identidade-visual.md` ou `manual-de-marca.md`) e `[pasta]/conteudo/calendario-AAAA-MM.md`. Se nao houver calendario, use a skill `estrategista-conteudo-cliente` primeiro.

## O que gerar
Dois arquivos HTML, sem dependencias externas (um arquivo cada), em `[pasta]/conteudo/`:
- `planner-AAAA-MM-cliente.html`: sem notas internas, pensado para o cliente aprovar.
- `planner-AAAA-MM-interno.html`: com notas de estrategia, molde, hipotese de teste e pendencias.

## Estrutura
- Topo: nome do cliente, mes, legenda de cores por tipo de conteudo, filtro por tipo (reel, carrossel, estatico, WhatsApp) e por quem produz.
- Visao da semana: 7 colunas (seg a dom), navegacao por semana. Cada cartao mostra icone do tipo, horario, gancho (texto da capa) e etiqueta `GRAVAR` (cliente grava) ou `AMANDA CRIA` (carrossel/estatico).
- Dias sugeridos de gravacao destacados.
- Cada cartao e clicavel e expande para baixo (`<details>`): ID, formato, roteiro (topicos falados) ou texto de cada slide, legenda, CTA, material necessario, dia sugerido para gravar e o bloco "Status: aprovar / ajustar" (o cliente responde pelo ID, ex.: CAM-2611-03).
- Visual com a paleta e o tom da identidade do cliente; legivel no celular.

## PDF
Um PDF nao tem cartao que expande. Para PDF: gerar a versao com indice na primeira pagina e links internos (clicar no dia leva a pagina do conteudo), e orientar a imprimir o HTML como PDF pelo navegador usando CSS de impressao (`@media print`) que abre todos os cartoes.

## Regras
- Use apenas o conteudo do calendario aprovado/rascunho; nao invente copy nova.
- Respeite as restricoes do cliente (por exemplo, Eleva sem travessao).
- A aprovacao nao e gravada no arquivo; o fluxo e por ID no WhatsApp ou comentario.
