# Passo a passo — Rastrear a venda até 30 dias depois do cadastro
**RECRIA Marketing, 21/10/2026**
**Para colar no chat do Claude do Giuliano**

Objetivo: quando alguém assinar o Área Comum - portal do condomínio (mesmo que seja 30 dias depois do cadastro), conseguir saber se essa venda veio do Google ou da Meta, e devolver essa informação pras duas plataformas, pra elas aprenderem a buscar gente parecida com quem realmente compra (não só com quem se cadastra).

---

## Custo — resumindo antes de tudo

- **Google**: de graça. A importação de conversão offline é um recurso nativo do Google Ads, sem custo extra.
- **Meta**: também de graça. A Conversions API (API de Conversões) é um recurso gratuito da própria Meta — você só paga se decidir usar uma ferramenta paga de terceiros para facilitar a integração (existem conectores prontos, tipo Stape ou plugins de CRM, mas não são obrigatórios). Feito direto por quem já mexe no site/portal, como o Claude do Giuliano, não tem custo nenhum.

---

## Passo 1 — Capturar o identificador do clique, na página de destino

Isso acontece na página elevags.com.br/area-comum-portal-do-condominio (feita no Webflow), que é por onde todo clique de anúncio chega.

1. Quando a pessoa clica num anúncio do Google, a URL que ela abre já vem com um parâmetro `gclid=XXXXX` (o Google Ads adiciona isso automaticamente, com o "auto-tagging" ligado — já configurado na campanha).
2. Quando a pessoa clica num anúncio da Meta, a URL vem com `fbclid=XXXXX` (também automático).
3. **Pedir pro Claude do Giuliano**: adicionar um pequeno script na página (Webflow → Custom Code → Head Code, ou lógica no próprio formulário) que lê esses dois parâmetros da URL (`gclid` e `fbclid`) assim que a página carrega, e guarda num lugar temporário no navegador da pessoa (por exemplo, em um cookie ou no `localStorage`), para não perder essa informação enquanto ela navega até clicar em "Começar teste grátis".

## Passo 2 — Levar esse identificador até o cadastro de verdade

O cadastro em si acontece em outro sistema (portal.elevags.com.br — o próprio portal, não o Webflow). Então é preciso que esse identificador "atravesse" do site pro portal:

4. No botão "Começar teste grátis", em vez de só linkar pro portal.elevags.com.br, **anexar o `gclid` e o `fbclid` guardados como parâmetros na própria URL de destino** (por exemplo: `portal.elevags.com.br/cadastro?gclid=XXX&fbclid=YYY`).
5. **Pedir pro time técnico do portal** (pode ser o mesmo Claude, se ele também tiver acesso ao backend do portal, ou outra pessoa) **salvar esses dois valores junto com o cadastro da pessoa** no banco de dados do portal — por exemplo, como campos extras ligados à conta criada.

**Esse passo 2 é o ponto crítico**: sem isso, o identificador se perde entre o clique no anúncio e a assinatura paga 30 dias depois, e nada do resto funciona.

## Passo 3 — Quando a pessoa assinar de verdade (vira pagante), devolver a informação

### Lado Google — mais simples, pode começar manual
6. Quando alguém assinar, pegar o `gclid` salvo no cadastro dela, a data da assinatura e o valor pago.
7. No Google Ads, ir em **Ferramentas e Configurações → Conversões → Conversões offline → Fazer upload de dados de conversão**, e subir uma planilha simples com essas 3 colunas (gclid, data/hora da conversão, valor). Pode ser feito manualmente, mês a mês, enquanto o volume for baixo.
8. Mais pra frente, isso pode ser automatizado (o próprio portal manda esses dados direto pro Google via API), mas não precisa começar assim.

### Lado Meta — precisa de desenvolvimento desde o início
9. Quando alguém assinar, pegar o `fbclid` salvo no cadastro dela.
10. **Pedir pro Claude do Giuliano configurar a Conversions API** (documentação oficial: developers.facebook.com/docs/marketing-api/conversions-api): é uma chamada que o servidor do portal faz direto pra Meta, mandando o evento "Purchase" (ou "Subscribe", se fizer mais sentido), com o `fbclid`, o valor da assinatura e um e-mail/telefone da pessoa (criptografado, a própria Meta pede isso como segurança extra pra casar o evento com o usuário certo).
11. Diferente do Google, não dá pra fazer isso "manual por planilha" na Meta — precisa ser uma chamada de API, então é trabalho de desenvolvimento desde o começo, mesmo com poucas vendas.

---

## Resumo do que pedir pro Claude do Giuliano fazer

1. Capturar `gclid` e `fbclid` na página de destino e guardá-los temporariamente (cookie/localStorage).
2. Levar esses dois valores junto quando a pessoa for pro cadastro no portal, e salvá-los na conta dela.
3. Quando alguém virar assinante pagante, usar o `gclid` salvo para subir a conversão no Google (manual no início, via planilha) e configurar a Conversions API da Meta para mandar o evento de compra usando o `fbclid` salvo (precisa ser automatizado desde já, não tem versão manual fácil na Meta).

**Pergunta-chave pra fazer antes de tudo**: o portal (sistema separado do site, feito em outra tecnologia) tem como receber e guardar esses parâmetros extras no cadastro? Se o Claude do Giuliano só tiver acesso ao Webflow (o site) e não ao backend do portal, alguém com acesso ao portal também precisa estar envolvido nesse passo 2.
