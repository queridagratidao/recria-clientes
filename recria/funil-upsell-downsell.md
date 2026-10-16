# Upsell e downsell dentro da página de obrigado dos e-books

**Não precisa mudar nada na Hotmart.** A oferta fica dentro da própria página de agradecimento que já está cadastrada: `https://www.agenciarecria.com.br/obrigado-ebook/?p=<slug>`.

## Fluxo (tudo na mesma página)
1. **Compra confirmada** + aviso de que o acesso foi enviado pela Hotmart + botão de WhatsApp para quem não recebeu (a parte de sempre).
2. **Upsell**, em primeira pessoa, citando o e-book comprado ("Se você acabou de comprar o Recria Post…").
3. Se a pessoa clica em "Agora não": **downsell** (mais barato).
4. Se recusar de novo: aparece o **restante da página** de sempre (comunidade, sugestões, consultoria e mentoria).
Se clicar em "Sim", o checkout abre em outra aba e o restante da página aparece embaixo.

## Dois grupos de e-books
| Grupo | E-books (`?p=`) | Upsell | Downsell |
|---|---|---|---|
| Conteúdo | calendario-de-conteudos, calendario-com-ia, post, reels, miv | **Recria Ads, R$ 97** | **Manual de Narrativas, R$ 47** |
| Negócio | negocio-local, esteira-de-produtos, 100-ideias-low-ticket, medium-ticket, high-ticket, estrutura-de-negocio | **Diagnóstico Recria, R$ 67** | **Curso Express, R$ 15** |

Sem `?p=` ou com outro produto, a página fica como antes (sem oferta).
O texto do upsell de conteúdo **não cita os calendários com IA**, para não irritar quem já comprou um calendário.
O Diagnóstico como upsell **ainda precisa da sua confirmação** (depende da agenda).

## Pixel
- **Purchase** do e-book: igual ao que já existia, uma vez só.
- Eventos próprios, com `oferta` (recria-ads, manual, diagnostico, express) e `de` (o e-book): `OfertaVista`, `OfertaAceita`, `OfertaRecusada`; e `InitiateCheckout` ao clicar em "Sim". Dá para medir a taxa de aceite de cada oferta.

## Cuidados
1. O link do Diagnóstico é o da página do marketplace; trocar pelo link de pagamento direto, se preferir.
2. Não esquecer de checar na Hotmart o limite de order bumps (a oferta da página funciona sem o upsell nativo da Hotmart).
3. Para quem comprou e-book de negócio, a seção "consultoria e mentoria" mais abaixo ainda mostra o Diagnóstico. Se ficar repetido, dá para tirar o cartão de lá.
4. Evitar ligar em paralelo ao teste de criativos da campanha, para não misturar resultados.
