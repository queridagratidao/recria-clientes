# O caminho certo dos eventos de rastreamento
**RECRIA Marketing, 23/10/2026**
**Para colar no chat do Claude do Giuliano**

Explicando de forma simples os três momentos que precisam ser rastreados, e o nome certo de cada evento.

---

## Os três momentos

**1. A pessoa clica em "Começar teste grátis"**

Ela viu o anúncio, clicou no botão — mas ainda não deu nenhum dado, não criou conta, pode até desistir no meio do caminho.

→ Evento: **`CliqueTesteGratis`**
→ Só serve para enxergar o funil (quantos clicaram vs. quantos realmente se cadastraram). Não é usado para a campanha aprender nada.

**2. A pessoa preenche o cadastro no portal e a conta é criada**

Agora sim ela deu os dados (nome, e-mail, senha) e passou a ter acesso de verdade ao Área Comum — o teste grátis começou.

→ Evento: **`CompleteRegistration`**
→ **É esse evento que a campanha de Meta Ads usa pra aprender e escolher pra quem mostrar mais anúncio.** Não pode ser nenhum outro nome.

**3. Até 30 dias depois, a pessoa vira assinante paga**

→ Evento: **`Purchase`**
→ Usado para avisar a Meta e o Google que aquele cadastro específico virou venda, e devolver o valor pago.

---

## Por que não dá pra usar "Lead" no lugar de "CompleteRegistration"

"Lead" é o nome certo para quando alguém só demonstra interesse, sem completar nada — por exemplo, preencher um formulário pedindo pra ser contatado depois. Não é o caso aqui: ou a pessoa cria a conta, ou não cria. Não existe meio-termo. Por isso o nome certo do momento 2 é `CompleteRegistration`, não `Lead`.

## Resumo para implementar

| Quando | Onde acontece | Nome do evento |
|---|---|---|
| Clique em "Começar teste grátis" | Na landing page (site) | `CliqueTesteGratis` |
| Conta criada com sucesso | No portal | `CompleteRegistration` |
| Assinatura paga | No portal | `Purchase` |

A campanha já está configurada esperando o evento `CompleteRegistration` no momento 2 — por isso pedimos para manter esse nome, e não trocar para `Lead`.
