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

*(Os próximos passos serão adicionados aqui conforme a configuração avançar do lado da Amanda.)*
