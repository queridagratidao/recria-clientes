---
name: planner-clicavel
description: Gera o material de aprovacao do cliente em duas formas. (1) Modo Calendario: planner HTML interativo com semana em 7 colunas e cartoes que expandem. (2) Modo Feed: simulacao em HTML de como o perfil vai ficar no Instagram (grade do feed, carrossel que passa para o lado, reel que toca, stories, anuncios com botao que leva ao destino), com o material pronto e, onde ainda nao ha arte, uma simulacao com texto e sugestao de design, para o cliente aprovar vendo como vai ficar. Versao interna e versao cliente. Use depois que o calendario estiver pronto.
---

# Planner clicavel (calendario e feed simulado)

## Passo 0
Identifique o cliente e leia `[pasta]/conteudo/contexto.md`, a identidade visual (`DESIGN.md`, `identidade-visual.md` ou `manual-de-marca.md`) e `[pasta]/conteudo/calendario-AAAA-MM.md`. Veja o que ja existe de material final em `[pasta]/social-media/` (imagens, carrosseis, videos). Se nao houver calendario, use a skill `estrategista-conteudo-cliente` primeiro.

## Escolha o modo
- **Modo Calendario**: visao de planejamento (quando, o que, quem produz). Bom para a agenda de gravacao e a conversa de estrategia.
- **Modo Feed**: simulacao visual para aprovar. Padrao a partir de agora para aprovacao de materiais. Gere os dois quando a Amanda nao especificar.

## Modo Calendario
Dois arquivos HTML, sem dependencias externas, em `[pasta]/conteudo/`: `planner-AAAA-MM-cliente.html` (sem notas internas) e `planner-AAAA-MM-interno.html` (com molde, hipotese de teste e pendencias).
- Topo: cliente, mes, legenda de cores por tipo, filtro por tipo e por quem produz.
- Semana em 7 colunas, navegacao por semana. Cartao com icone do tipo, horario, gancho, etiqueta `GRAVAR` ou `AMANDA CRIA`.
- Cartao clicavel que expande (`<details>`): ID, formato, roteiro ou texto dos slides, legenda, CTA, material, dia sugerido de gravacao, bloco "aprovar / ajustar" por ID.
- Dias sugeridos de gravacao destacados; paleta e tom do cliente.

## Modo Feed (simulacao de aprovacao)
Um arquivo HTML unico por mes e por versao, em `[pasta]/conteudo/feed-AAAA-MM-cliente.html` (e `-interno.html`), pensado para celular, abrindo bem tambem no computador (moldura de celular no desktop).

### Telas
1. **Perfil e grade do feed**: foto, nome, bio e destaques do cliente; grade de 3 colunas com os posts do mes na ordem de publicacao (mais novo no topo), cada miniatura com a data prevista. Abas Feed, Reels e Stories.
2. **Post de imagem ou estatico**: abre em tamanho de feed, com legenda e CTA.
3. **Carrossel**: passa para o lado (setas e deslizar), indicador de slides, texto de cada slide.
4. **Reel ou video**: toca se o arquivo estiver na pasta; se nao houver video, mostra a simulacao (quadro 9:16 com gancho da capa, roteiro e tempo).
5. **Stories**: sequencia em 9:16 com barra de progresso e avanco por toque; stickers como espaco reservado (enquete, link, caixinha).
6. **Anuncios (dark post)**: tela separada, marcada "anuncio", com o botao do anuncio (ex.: Saiba mais) e o posicionamento.

### Botao do anuncio e links (CTA)
O botao (Saiba mais, Fale conosco, Enviar mensagem) e um link real e **configuravel por item**: site, LP ou `https://wa.me/55DDDNUMERO?text=...` (WhatsApp com mensagem pronta). Abre em nova aba, para o cliente testar o destino. Cada botao mostra um aviso curto "destino de teste" e fica registrado no bloco de dados do arquivo. Para stickers de link nos stories vale a mesma regra. Se o destino ainda nao existir, o botao mostra "destino a definir" e nao leva a lugar nenhum.

### Material pronto x simulacao
Cada item tem uma etiqueta clara:
- **PRONTO**: usa a arte final (imagem, slides, video) de `[pasta]/social-media/`.
- **SIMULACAO**: ainda nao existe a arte. Mostra o texto de cada slide ou tela, a sugestao de design (cores da marca, tipografia, composicao, foto ou ilustracao desejada) e um quadro com a paleta do cliente. O cliente aprova o texto e a ideia visual antes de criarmos.

### Aprovacao
- Cada item mostra o **ID** (ex.: CAM-2611-03).
- Botoes: **Aprovar** e **Pedir ajuste** (campo de texto). Sem servidor: o botao monta a mensagem pronta ("Aprovo CAM-2611-03" ou "Ajuste em CAM-2611-03: ...") e abre o WhatsApp da agencia (`wa.me`, numero configuravel no topo do arquivo) ou copia o texto.
- A aprovacao nao e gravada no arquivo; fica na conversa. A Amanda registra o status no calendario.

### Regras de construcao
- Arquivo unico com CSS e JS embutidos; imagens e videos referenciados por caminho relativo ou embutidos quando pequenos. Sem dependencias externas.
- Nao use o logotipo nem a marca do Instagram. Use icones genericos e deixe visivel o aviso **"Simulacao para aprovacao, nao e a publicacao real"**.
- Paleta, tipografia e tom do cliente (contexto + identidade). Placeholders usam as cores da marca, nunca cinza generico.
- Respeite as regras do cliente (Eleva sem travessao; Strategia em 1a pessoa do plural; sem prova social inventada; Pathy sem oferta de procedimento).
- Dados do planner (lista de itens com id, tipo, data, legenda, slides, caminho do video, destino do botao, status) em um bloco JSON no inicio do arquivo, para facilitar atualizacoes.
- Versao **cliente**: sem molde, hipotese de teste nem notas internas. Versao **interna**: com essas notas e filtros.

## PDF
Um PDF nao passa o carrossel para o lado nem toca video. Para PDF: gerar a versao com indice, uma pagina por conteudo (capa, cada slide, legenda e CTA) e links internos, ou orientar a imprimir o HTML pelo navegador com CSS de impressao (`@media print`) que abre todos os cartoes. Para o cliente, o HTML e preferivel ao PDF.

## Como compartilhar
O HTML pode ser enviado como arquivo ou publicado. Se for publicado como pagina (artefato), isso cria um link: a Amanda decide se publica, porque o conteudo e do cliente. Publicar so a versao **cliente**.

## Regras gerais
- Use apenas o conteudo do calendario (aprovado ou rascunho); nao invente copy nova.
- Rode `revisor-claims-cliente` antes de enviar ao cliente.
- A aprovacao final e da Amanda.
