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

## 2 · Confirmação dos itens do ponto 3

Os três pontos abaixo já estavam especificados desde a configuração original das campanhas (passo a passo que seguimos para montar tanto o Google Ads quanto o Meta Ads):

- **Destino de todos os anúncios**: `www.elevags.com.br/area-comum-portal-do-condominio`, configurado como landing page padrão em ambas as plataformas.
- **Parâmetros UTM** (`utm_source`, `utm_medium`, `utm_campaign`) em todos os anúncios, Google e Meta.
- **Marcação automática (auto-tagging) ligada** no Google Ads, para o clique trazer o `gclid`.

Esses três pontos já foram configurados assim desde o início — **ainda não foram revisados pessoalmente**, só pelo Claude in Chrome que montou as campanhas seguindo nossas instruções. A Amanda vai revisar tudo linha por linha nesta sexta-feira (06/11), antes do lançamento, e confirma por aqui se encontrar qualquer divergência.

## 3 · Exemplos de endereço final de cada plataforma

- **Google Ads**: `https://www.elevags.com.br/area-comum-portal-do-condominio?utm_source=google&utm_medium=cpc&utm_campaign=area-comum-pesquisa&utm_content={ID_DO_GRUPO}&utm_term={PALAVRA_CHAVE}&gclid={CÓDIGO_DO_CLIQUE}`
- **Meta Ads**: `https://www.elevags.com.br/area-comum-portal-do-condominio?utm_source=meta&utm_medium=paid&utm_campaign=area-comum&utm_content={ID_DO_ANÚNCIO}&fbclid={CÓDIGO_DO_CLIQUE}`

Os trechos entre chaves (`gclid`, `fbclid`, nome do grupo/anúncio) só aparecem de verdade quando alguém clica no anúncio real — por isso não dá pra mandar um link clicável de exemplo antes do lançamento. Assim que a Amanda revisar as campanhas na sexta, ela confirma a estrutura exata de cada anúncio.
