# Ata — Apuração do Google Analytics da Eleva
**RECRIA Marketing, 23/11/2026 (apuração só de leitura, nada alterado)**

---

## Resumo

1. O Analytics que a Eleva usava (`G-PZ63FC1V16`) fica numa conta "Eleva" dentro da organização "Considere Feito" (ex-agência).
2. 99% dos dados vêm de outro site: `www.confiancacondo.com.br` (Confiança Administradora de Condomínios), que usa o mesmo ID por engano. Os relatórios estavam misturados.
3. Por isso o tráfego dos anúncios quase não aparecia: em 28 dias, 1 sessão "google / cpc" e nenhuma de mídia paga da Meta.
4. Em 23/11, o site já foi trocado para um Analytics novo (`G-B3F2ZB845M`), numa conta própria da Eleva. Falta concluir: acesso da Amanda, vínculo com o Google Ads e limpeza de uma sobra no site.

## Propriedade antiga (não usar mais)

- Organização: Considere Feito. Conta: Eleva (354443537). Propriedade: Eleva (488353717), criada em 07/05/2025.
- Fluxo de dados: 1 só, "Site", `https://elevags.com.br`, ID `G-PZ63FC1V16`.
- Administradores: Amanda, Giuliano, Rene Kasper (também administrador da organização).
- Vínculo Google Ads: conta 455-373-9886, feito por Giuliano em 28/03/2026.

## Evidência da mistura (26/10 a 22/11/2026)

- Confiança Administradora de Condomínios (`www.confiancacondo.com.br`): 1.925 visualizações (99,3%), 1.010 usuários.
- Páginas da Eleva (`www.elevags.com.br`): somam 13 visualizações no total.
- Totais: 1.820 sessões, 1.016 usuários ativos, quase tudo da Confiança.
- google / cpc: 1 sessão, em 26–27/10 (antes da campanha Área Comum começar, em 09/11). Nenhuma origem "paid" da Meta.

## De onde vinha "Confiança" / "Administração de imóveis"

- É uma página real registrada no Analytics, enviada pelo site da Confiança com o ID da Eleva. Não é sugestão do Google Ads.
- A sugestão "semelhante a: Administração de imóveis" no Google Ads provavelmente vem do público "All Users" dessa propriedade (quase só visitantes da Confiança), compartilhado com a conta de anúncios pelo vínculo.

## O que está no site hoje (conferido em 23/11)

- `G-B3F2ZB845M`: Analytics novo, conta própria da Eleva, já no código de todas as páginas principais.
- `GTM-TPTQTWJK`: Tag Manager da Recria (conta "Eleva Marketing"), com o Pixel da Meta `634359929729484` (PageView + clique pro portal). Nenhuma tag de Analytics dentro dele — correto, assim deve continuar.
- Consentimento de cookies funcionando: nada carrega (Google ou Meta) antes de "Aceitar todos".

## Sobra a remover

- A página `/curso-formacao-de-sindico-profissional` ainda tem um bloco de Tag Manager antigo, `GTM-WX4W4NBX`, com código quebrado (erro de sintaxe, não carrega hoje). Contém o GA antigo e um segundo Pixel (`2782378458628105`). Precisa ser removido do Webflow antes que alguém "console" o erro e religue os dois.

## Pendências

1. Confirmar que a propriedade nova recebe dados em tempo real.
2. Dar acesso de Administrador à Amanda na conta nova.
3. Vincular o Google Ads à propriedade nova.
4. Desvincular o Google Ads da propriedade antiga (momento a decidir pelo Giuliano).
5. Conferir se a codificação automática (gclid) está ativa no Google Ads.
6. Remover o `GTM-WX4W4NBX` da página do curso.
7. Definir eventos principais no GA novo.
8. Decidir se vale conversar com a Considere Feito sobre a propriedade antiga.

## Como ler os números daqui pra frente

- A propriedade nova vai mostrar muito menos tráfego — é o número real do site, não é queda.
- O tráfego pago só aparece pra quem aceita os cookies. Pra resultado de campanha, a referência mais completa continuam sendo as conversões que o próprio portal envia ao Google Ads e à Meta.
- Não comparar com o período anterior a 23/11 (base misturada, não serve de referência).

## IDs de referência

- GA antigo (não usar): `G-PZ63FC1V16`, organização Considere Feito.
- GA novo: `G-B3F2ZB845M`, conta "Eleva (elevags.com.br)".
- Tag Manager ativo: `GTM-TPTQTWJK` (conta "Eleva Marketing").
- Pixel Meta ativo: `634359929729484`.
- Tag Manager antigo (sobra quebrada): `GTM-WX4W4NBX`.
- Google Ads Eleva: `455-373-9886`.
- Site de outra empresa usando o GA antigo: `www.confiancacondo.com.br`.
