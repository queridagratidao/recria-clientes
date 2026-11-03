# Retorno — Medição dos anúncios do Área Comum
**RECRIA Marketing, 03/11/2026**
**Em resposta a "Medição dos anúncios do Área Comum", 03/11/2026**

---

## 1 · Chave da API de Conversões

Já tínhamos enviado o token, na semana passada (28/10), por um link do onetimesecret.com — mas esse link tinha validade de 3 dias, e já expirou antes do uso.

**Pergunta**: você chegou a salvar aquele token em algum lugar? Se sim, não precisa de nada novo.

Se não salvou, segue um **novo link**, já gerado, com o mesmo cuidado de segurança de antes:

https://us.onetimesecret.com/secret/fv8qmsg1oldxkamunia50cx5g57psuleu06j718fn6lwq1ohf9uvkigupm8toe

Esse link só abre **uma vez** — clique nele só na hora de colar o token direto no servidor do portal, com o Claude do Giuliano.

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
