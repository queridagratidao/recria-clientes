# Instrução para o Claude do Giuliano — Atribuir venda ao cadastro de até 30 dias atrás
**RECRIA Marketing, 21/10/2026**
**Para colar no chat do Claude do Giuliano**

Objetivo: quando alguém assinar o Área Comum - portal do condomínio (mesmo que seja até 30 dias depois do cadastro), conseguir saber se essa venda veio de um anúncio do Google ou da Meta, e devolver essa informação pras duas plataformas, pra elas aprenderem a buscar gente parecida com quem realmente paga (não só com quem se cadastra).

**Não há desenvolvedor humano no meio — você (Claude) é quem vai implementar isso, do lado do site (Webflow) e do lado do portal (onde o cadastro de fato acontece).** Se você não tiver acesso a alguma das duas partes, a primeira coisa a fazer é avisar, pra o Giuliano liberar.

Sem custo: tanto a importação de conversão pro Google quanto a Conversions API da Meta são recursos gratuitos das próprias plataformas.

---

## Passo 1 — Capturar o identificador do clique, no site (Webflow)

Na página elevags.com.br/area-comum-portal-do-condominio, que é por onde todo clique de anúncio chega:

1. Os links dos anúncios do Google chegam com `?gclid=XXXXX` na URL (automático, pelo auto-tagging já ligado na campanha).
2. Os links dos anúncios da Meta chegam com `?fbclid=XXXXX` na URL (também automático).
3. Adicionar um script no **Site Settings → Custom Code → Head Code** do Webflow que, ao carregar a página, lê esses dois parâmetros da URL e os guarda em um cookie (ou `localStorage`), para não perder essa informação enquanto a pessoa navega pela página até decidir se cadastrar.
4. No botão "Começar teste grátis", anexar esses dois valores guardados como parâmetros na URL de destino do portal — por exemplo: `portal.elevags.com.br/cadastro?gclid=XXX&fbclid=YYY`.

## Passo 2 — Guardar o identificador junto com o cadastro, no portal

Esta parte acontece no sistema do portal (não no Webflow) — por isso você precisa ter acesso ao código/banco de dados do portal para fazer isso. Se não tiver, avisar antes de continuar.

5. No formulário/fluxo de cadastro do portal, ler os parâmetros `gclid` e `fbclid` da URL de entrada.
6. Salvar esses dois valores como campos extras ligados à conta da pessoa que está se cadastrando, junto com a data do cadastro.

**Esse é o passo crítico**: sem isso, a informação de origem se perde entre o clique no anúncio e a assinatura paga, que pode acontecer só 30 dias depois.

## Passo 3 — Quando a pessoa assinar de verdade, devolver a conversão

### Lado Google
7. No momento em que alguém virar assinante pagante, buscar o `gclid` salvo na conta dela (passo 2).
8. Subir essa conversão no Google Ads, em **Ferramentas e Configurações → Conversões → Conversões offline → Fazer upload de dados de conversão**, com 3 informações: o `gclid`, a data/hora da assinatura, e o valor pago.
9. No início, com poucas assinaturas, isso pode ser feito manualmente (uma planilha simples, enviada periodicamente). Se o volume crescer, automatizar esse envio direto do portal para a API do Google Ads (Offline Conversion Import via API).

### Lado Meta
10. No mesmo momento, buscar o `fbclid` salvo na conta da pessoa.
11. Implementar a **Conversions API da Meta** (documentação: developers.facebook.com/docs/marketing-api/conversions-api) — uma chamada que o próprio servidor do portal faz para a Meta, enviando o evento "Purchase" (ou "Subscribe"), com o `fbclid`, o valor pago, e um identificador da pessoa (e-mail ou telefone, que precisa ser enviado com hash SHA-256 — a Meta exige isso por segurança).
12. Diferente do Google, não existe upload manual por planilha na Meta — precisa ser essa chamada de API, então essa parte já nasce automatizada, mesmo com poucas vendas no início.

---

## Checklist rápido para o Claude do Giuliano

- [ ] Confirmar se tenho acesso tanto ao Webflow (site) quanto ao código/banco de dados do portal (onde o cadastro acontece). Se não, avisar o Giuliano antes de prosseguir.
- [ ] Capturar `gclid` e `fbclid` na página de destino (Webflow) e guardá-los até o clique em "Começar teste grátis".
- [ ] Levar esses dois valores para a URL de cadastro do portal.
- [ ] Salvar `gclid` e `fbclid` junto com a conta da pessoa, no banco de dados do portal.
- [ ] Quando alguém assinar, subir a conversão no Google (manual, por planilha, para começar).
- [ ] Implementar a Conversions API da Meta, para enviar o evento de compra automaticamente.
