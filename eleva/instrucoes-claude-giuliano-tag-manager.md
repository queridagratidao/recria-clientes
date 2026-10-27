# Instruções para o Claude do Giuliano — Instalação do Tag Manager
**RECRIA Marketing, 27/10/2026**
**Para colar no chat do Claude do Giuliano**

Este documento reúne, em ordem, tudo que o Claude do Giuliano precisa fazer para deixar o rastreamento do Área Comum - portal do condomínio funcionando antes do lançamento (09/11). Vá seguindo os passos na ordem — cada um será adicionado aqui conforme a Amanda for configurando a parte dela.

---

## Passo 1 — Instalar o Google Tag Manager no Webflow

Criamos um novo container do Google Tag Manager (o anterior, de outra agência, não está mais instalado em nenhuma página do site, e ninguém do lado da Eleva/Recria tem acesso a ele). O novo container é: **GTM-TPTQTWJK**.

1. No Webflow, ir em **Site Settings → Custom Code**.
2. Colar este código no campo **Head Code**, o mais alto possível:

```
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TPTQTWJK');</script>
<!-- End Google Tag Manager -->
```

3. Colar este outro código no campo **Body Code** (logo após a abertura do `<body>`, ou no campo equivalente a "before `</body>` tag" do Webflow):

```
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TPTQTWJK"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
```

4. Publicar o site.
5. Confirmar que o código está em **todas as páginas** do site, principalmente na página do Área Comum - portal do condomínio (`elevags.com.br/area-comum-portal-do-condominio`).
6. Testar com a extensão **Tag Assistant** (Chrome) para confirmar que o container `GTM-TPTQTWJK` aparece rodando na página.

---

## Passo 2 — Instalar o mesmo tipo de rastreamento no portal (portal.elevags.com.br)

O portal é um **subdomínio separado** do site principal (`portal.elevags.com.br`, diferente de `elevags.com.br`). Isso significa que o Pixel/tags instalados na landing **não chegam sozinhos** até o portal — precisa de uma instalação própria lá também.

1. Instalar o **mesmo container do Google Tag Manager** (`GTM-TPTQTWJK`) também nas páginas do portal, do mesmo jeito que foi instalado na landing (Passo 1), se o portal permitir inserir esse tipo de código no `<head>`/`<body>`. Se o portal não for Webflow, perguntar à Amanda o snippet de instalação equivalente pra tecnologia usada.
2. Ativar a **vinculação entre domínios** (cross-domain measurement / linker) entre `elevags.com.br` e `portal.elevags.com.br`, nas configurações da tag do Google (Google Tag / GA4). Isso faz o Google decorar automaticamente os links entre as duas páginas com um parâmetro próprio, carregando a origem do clique sem precisar programar nada manualmente.
3. No código do portal, disparar os seguintes eventos, nos momentos exatos:
   - `fbq('track', 'CompleteRegistration')` — no momento em que uma conta **nova** é criada com sucesso (início do teste grátis). Não disparar em login de quem já tem conta.
   - Evento de conversão do Google Ads equivalente, no mesmo momento (a Amanda vai passar o ID/label da ação de conversão assim que criá-la no Google Ads).
   - Evento `Purchase` (Meta) e o segundo evento de conversão do Google Ads, no momento em que a assinatura é efetivamente paga.
4. Enviar os mesmos eventos também pela **API de Conversões da Meta**, direto do servidor do portal (chamada backend, não é tag de navegador) — usando o `fbc`/`fbp` capturados e o e-mail da pessoa com hash SHA-256. É esse canal que torna o envio pra Meta automático, sem necessidade de planilha.
5. **Gerar, periodicamente (sugestão: semanal), uma lista/exportação com as contas criadas e assinaturas pagas**, contendo: o identificador de clique do Google (gclid/gbraid/wbraid, se tiver sido capturado), a data do evento, e o valor (no caso de assinatura). Essa lista é o que vai permitir à Amanda subir a conversão no Google Ads (processo de "importação", explicado no Passo 3). **Se não tiver acesso ao código/banco do portal para fazer este passo, avisar antes de prosseguir, para o Giuliano liberar o acesso.**

## Passo 3 — Conversões de importação no Google Ads (lado da Amanda, só para referência)

A Amanda vai criar, dentro do Google Ads, duas ações de conversão do tipo "Importação": **"Área Comum · conta criada"** e **"Área Comum · assinatura"**. Toda semana, ela vai pegar a lista gerada no Passo 2.5 e subir manualmente nessas ações (Ferramentas e Configurações → Conversões → Conversões offline → Fazer upload de dados de conversão). No futuro, esse processo pode ser automatizado via API, mas o Claude do Giuliano não precisa se preocupar com essa parte — só com gerar a lista corretamente.

---

*(Mais passos serão adicionados aqui conforme a configuração avançar do lado da Amanda.)*
