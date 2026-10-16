# Funil de upsell e downsell dos e-books (páginas só com copy)

## Fluxo
Compra do e-book → **página de upsell** → (se recusar) **página de downsell** → **página de obrigado** (a de sempre, com WhatsApp, comunidade e sugestões).
Quem aceita uma oferta vai para o checkout da Hotmart daquele produto.

## Dois grupos (11 e-books, só 2 funis)
| Grupo | E-books (slug do `?p=`) | Upsell | Downsell |
|---|---|---|---|
| Conteúdo | calendario-de-conteudos, calendario-com-ia, post, reels, miv | **Recria Ads, R$ 97** (`/oferta-recria-ads/`) | **Manual de Narrativas, R$ 47** (`/oferta-manual/`) |
| Negócio | negocio-local, esteira-de-produtos, 100-ideias-low-ticket, medium-ticket, high-ticket, estrutura-de-negocio | **Diagnóstico Recria, R$ 67** (`/oferta-diagnostico/`) | **Curso Express, R$ 15** (`/oferta-express/`) |

O Diagnóstico como upsell **ainda precisa da sua confirmação** (depende da sua agenda).

## O que configurar na Hotmart (página de agradecimento de cada e-book)
Hoje cada e-book aponta para `https://www.agenciarecria.com.br/obrigado-ebook/?p=<slug>`.
Para ligar o funil, trocar para:
- Grupo conteúdo: `https://www.agenciarecria.com.br/oferta-recria-ads/?p=<slug>`
- Grupo negócio: `https://www.agenciarecria.com.br/oferta-diagnostico/?p=<slug>`
(as páginas passam o `p` adiante sozinhas até a página de obrigado)

## Pixel
- O evento **Purchase** do e-book dispara na **primeira página** (a de upsell), com o valor de lista, e a página de obrigado **não repete** (mesma chave de sessão).
- Eventos próprios: `OfertaVista`, `OfertaAceita`, `OfertaRecusada` (com `oferta` e `de`) e `InitiateCheckout` ao clicar em "Sim". Dá para medir a taxa de aceite de cada oferta.
- A compra do upsell em si é registrada pela página de obrigado do produto comprado (configurar a página de agradecimento de cada produto).

## Antes de ligar
1. Confirmar na Hotmart o limite de order bumps e se o upsell/downsell nativo atende o que você quer; estas páginas funcionam sem ele (o botão leva ao checkout).
2. O link do Diagnóstico é o da página do marketplace; trocar pelo link de pagamento direto se preferir.
3. Não ligar durante o teste de criativos da campanha dos e-books, para não misturar os resultados.
4. Páginas com `noindex`. Nenhuma delas aparece no Google.
