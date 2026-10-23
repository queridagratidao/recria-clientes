# Por que manter "CompleteRegistration", não trocar para "Lead"
**RECRIA Marketing, 23/10/2026**
**Para colar no chat do Claude do Giuliano**

O documento de vocês (Resposta à Recria, v5, seção 3) propõe que o portal envie o evento **"Lead"** quando a conta é criada, e **"Purchase"** quando a assinatura é paga. Mas a campanha de Meta Ads já está montada e otimizando pelo evento **"CompleteRegistration"** (aparece como "Concluir inscrição" no painel). Antes de implementar, pedimos para manter "CompleteRegistration" em vez de trocar para "Lead" — pelos motivos abaixo.

---

## O motivo técnico

Na Meta, "Lead" e "CompleteRegistration" não são a mesma coisa, mesmo os dois sendo eventos de topo de funil:

- **"Lead"** é o evento padrão para quando alguém demonstra interesse, mas ainda não completou uma ação definitiva — por exemplo, preencher um formulário pedindo contato, baixar um material, pedir um orçamento. É um sinal mais fraco: a pessoa pode nunca virar cliente.
- **"CompleteRegistration"** é o evento padrão específico para quando um cadastro/conta é criado com sucesso — exatamente o que acontece no Área Comum quando alguém começa o teste grátis. É um sinal mais forte e mais específico do que "Lead".

Como o cadastro no Área Comum é uma conta de verdade, criada com sucesso (não um formulário de interesse), "CompleteRegistration" é o evento correto — não "Lead".

## Por que isso não é só uma questão de nome

A campanha já está configurada no Gerenciador de Anúncios para otimizar pelo evento "CompleteRegistration" — é esse o sinal que o algoritmo da Meta usa para aprender que tipo de pessoa converte, e para quem mostrar mais anúncio.

Se o portal enviar "Lead" em vez de "CompleteRegistration", a campanha **nunca vai receber o evento que está configurada para esperar** — mesmo que a implementação do lado do portal esteja perfeita. Não é incompatibilidade de preferência, é incompatibilidade técnica: um evento não substitui o outro dentro do Gerenciador de Eventos.

## Por que faz mais sentido manter a estrutura de funil como está

Pensando no funil completo do Área Comum:

1. **CompleteRegistration** — a conta é criada, o teste grátis começa (o que a campanha de hoje otimiza).
2. **Purchase** — a assinatura é paga, 30 dias depois (o que track usa pra devolver qualidade do cadastro pra Meta).

Usar "Lead" no lugar de "CompleteRegistration" misturaria a semântica: "Lead" normalmente fica reservado para uma etapa ainda mais inicial que nem existe nesse funil (ninguém "demonstra interesse" sem cadastro — ou cadastra, ou não cadastra). Manter "CompleteRegistration" preserva a leitura certa de cada etapa, e é também o padrão que a própria Meta recomenda para produtos com teste grátis/cadastro gratuito.

## O que pedimos

Mantém o restante do passo a passo de vocês exatamente como está (o ajuste de consentimento via GTM, o fbc/fbp, a API de Conversões, o SHA-256 no e-mail) — só o nome do evento de cadastro muda:

| Evento | Como pedimos que fique |
|---|---|
| Clique em "Começar teste grátis" | `CliqueTesteGratis` (evento próprio, como já estava no documento de vocês) |
| Conta criada com sucesso (início do teste grátis) | `CompleteRegistration` (não `Lead`) |
| Assinatura paga | `Purchase` (como já estava) |

Se já tiver algo implementado com "Lead", é só trocar o nome do evento disparado — não muda a lógica de quando disparar, só o nome.
