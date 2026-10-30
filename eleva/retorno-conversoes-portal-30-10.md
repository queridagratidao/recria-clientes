# Retorno — Conversões do portal para as campanhas
**RECRIA Marketing, 30/10/2026**
**Em resposta a "Conversões do portal para as campanhas", 30/10/2026**

---

## Confirmação da data de lançamento: 09/11

O documento confirma "o envio passa a valer para as campanhas de 09/11" — isso bate com o que já tínhamos combinado na ata de 28/10. Resolve a dúvida anterior sobre 03/11 x 09/11.

## Respostas às 4 perguntas

**1 · Valor**: de acordo com o valor total do plano (não a parcela). É o critério certo — a parcela faria a campanha parecer "no prejuízo", e o valor total reflete o retorno real, além de ajudar o algoritmo a priorizar quem fecha os planos maiores.

**2 · Desistência (7 dias)**: de acordo em não mandar nada agora, **com uma melhoria sugerida para depois** — ver seção "Evento de estorno" abaixo.

**3 · Google**: sim, usar o mesmo critério de valor na lista semanal é o certo, para as duas plataformas medirem igual. Essa lista semanal é usada só para o Google — a Meta já recebe tudo automatizado, pelo servidor.

**4 · Contagem dupla**: confirmado, sem risco. O Tag Manager do site (`GTM-TPTQTWJK`) só tem duas tags: `PageView` (base) e `CliqueTesteGratis` (clique no botão) — ele não dispara `CompleteRegistration` nem `Purchase` em nenhum momento. Esses dois eventos só existem do lado do servidor do portal, são canais completamente separados do Tag Manager.

## Sobre o período de 7 dias (direito de arrependimento) — decisão

Avaliamos duas formas possíveis:

- **Sem espera** (a que está no plano hoje): o `Purchase` dispara na hora que o pagamento é confirmado, sem esperar os 7 dias passarem. Vantagem: a campanha aprende mais rápido, principalmente no lançamento, quando o volume de dado é baixo. Desvantagem: se a pessoa desistir dentro do prazo, a venda já contada permanece, sem correção.
- **Com espera**: só dispara o `Purchase` depois que passar o prazo sem cancelamento. Mais preciso, porém atrasa o aprendizado da campanha em quase uma semana e meia.

**Nossa recomendação**: seguir sem espera, como já estava no plano — a velocidade de aprendizado no lançamento pesa mais, e o volume de cancelamento tende a ser baixo. Revisamos com dado real depois de um tempo rodando.

## Evento de estorno (Refund) — melhoria sugerida, não bloqueante para o lançamento

Existe um jeito de avisar as duas plataformas quando uma venda é cancelada dentro dos 7 dias, corrigindo a contagem. Não é necessário para o dia 09/11, mas fica registrado como próximo passo depois do lançamento:

**Do lado do Claude do Giuliano, no portal:**
1. Guardar um identificador da venda (o próprio ID do pagamento/assinatura) junto com o evento `Purchase` original, para poder referenciar depois.
2. Detectar o cancelamento — escutar o aviso que o sistema de pagamento já manda quando alguém pede reembolso dentro do prazo.
3. Disparar o evento `Refund` para a Meta, pela mesma API de Conversões, usando o mesmo identificador da venda original, o valor estornado e os mesmos dados do cliente.
4. Para o Google, usar o recurso de **"Ajustes de conversões"** (Conversion Adjustments), informando o mesmo `gclid` e a conversão original, com o tipo **"Retração"**.

**Do nosso lado:**
- Meta: nada no dia a dia — é automático pelo servidor. Só confirmamos no teste que o `Refund` chega certinho.
- Google: passaria a ter uma segunda lista semanal (além da lista de conversões), com quem cancelou, para subir como retração.

Não precisa de nenhum código ou credencial nova da nossa parte para isso — é trabalho de desenvolvimento do lado do portal, e nosso papel fica só em explicar o que precisa acontecer e por quê, e acompanhar o teste depois.

## Datas do teste — confirmado

- Atualização do portal: 03/11.
- Cadastro de teste e contratação de teste: 04/11 (o Giuliano avisa antes de cada um).
- Campanhas seguem para 09/11.

Nota: o dia 04/11 também é dia de reunião entre Amanda e Giuliano — pode ser aproveitado para fazer o teste ao vivo, juntos, se der tempo dentro da reunião.
