# Retorno — Medição dos anúncios do Área Comum
**RECRIA Marketing, 03/11/2026**
**Em resposta a "Medição dos anúncios do Área Comum", 03/11/2026**

---

## 1 · Chave da API de Conversões

É o mesmo token que já tínhamos enviado na semana passada (28/10), junto com o passo a passo de como usar — se esse passo a passo já foi seguido e o token já está colado no servidor, não precisa fazer nada, pode ignorar esse item.

Se ainda não foi usado: o link antigo tinha validade de 3 dias e já expirou, por isso segue um link novo, com o mesmo token, pronto para uso:

https://us.onetimesecret.com/secret/fv8qmsg1oldxkamunia50cx5g57psuleu06j718fn6lwq1ohf9uvkigupm8toe

**Como esse link funciona, explicando bem simples**: ele é uma página que mostra o token **uma única vez**. Assim que alguém clicar e abrir essa página, o conteúdo aparece na tela — e, no mesmo instante, o link já deixa de funcionar para sempre. Se clicar de novo depois, ou se outra pessoa tentar abrir, não vai aparecer mais nada, porque já foi "gasto".

Por isso, o cuidado é: **só clicar nesse link no exato momento em que for usar o token** (ou seja, na hora de colar ele no servidor do portal, com o Claude). Não é para abrir antes só para conferir, nem para guardar o link para depois — tem que ser clique e uso, na sequência, sem demora.

**Não precisa de chamada para isso.** Esse link já resolve o problema de segurança sozinho: só quem clicar nele vai ver o token (e só uma vez, como explicado acima). Então o Giuliano pode fazer isso direto, no momento que for mais conveniente para ele: clica no link, copia o token que aparece na tela, e já cola direto no Claude dele para instalar no portal — sem precisar agendar nada com a gente.

## 2 · Respondendo às perguntas do ponto 3

Os pontos abaixo já foram especificados desde a configuração das campanhas:

- **Destino dos anúncios**: tanto no Google Ads quanto no Meta Ads, o anúncio leva a pessoa pra `www.elevags.com.br/area-comum-portal-do-condominio`. É essa mesma página nas duas plataformas. A partir daí, quando a pessoa clica em "Começar teste grátis" dentro da página, aí sim acontece um segundo redirecionamento, pro cadastro no portal.
- **Parâmetros UTM** (`utm_source`, `utm_medium`, `utm_campaign`): configurados em todos os anúncios, Google e Meta.
- **Marcação automática (auto-tagging)**: ligada no Google Ads, pra o clique trazer o `gclid`.

## 3 · Exemplos de endereço final de cada plataforma

O código completo do link (com `gclid` ou `fbclid`) só aparece de verdade no momento em que alguém clica no anúncio — e muda a cada clique, porque é um código único por pessoa. Como a campanha ainda não está ativa, não tem como mostrar um exemplo real agora. Mas a estrutura vai ser essa:

- **Google Ads**: `https://www.elevags.com.br/area-comum-portal-do-condominio?utm_source=google&utm_medium=cpc&utm_campaign=area-comum-pesquisa&utm_content={ID_DO_GRUPO}&utm_term={PALAVRA_CHAVE}&gclid={CÓDIGO_DO_CLIQUE}`
- **Meta Ads**: `https://www.elevags.com.br/area-comum-portal-do-condominio?utm_source=meta&utm_medium=paid&utm_campaign=area-comum&utm_content={ID_DO_ANÚNCIO}&fbclid={CÓDIGO_DO_CLIQUE}`

Assim que a campanha estiver ativa, fica fácil mostrar um exemplo real de cada plataforma.
