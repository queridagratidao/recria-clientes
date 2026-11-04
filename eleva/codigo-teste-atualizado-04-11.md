# Código de teste atualizado
**RECRIA Marketing, 04/11/2026**
**Urgente — para repassar ao Claude do Giuliano antes do teste de hoje**

---

O código de teste da Meta muda com o tempo (expira depois de um período sem uso). O código que passamos antes (`TEST41558`) não vale mais.

**Novo código de teste**: `TEST67208`

Por favor, usar esse novo código na chamada de teste do servidor, em vez do anterior. Sem isso, o evento de teste não vai aparecer na tela "Eventos de teste" do Gerenciador de Eventos.

## Onde ajustar, passo a passo

1. No código do portal, localizar a parte que faz a chamada para a API de Conversões da Meta (a função que dispara os eventos `CompleteRegistration` e `Purchase`).
2. Nessa chamada, o corpo da requisição tem um campo chamado **`test_event_code`** — é um parâmetro geral da chamada, no mesmo nível dos dados do evento (não dentro de cada evento individual).
3. Atualizar o valor desse campo para `TEST67208`, no lugar do código antigo (`TEST41558`).
4. Salvar e publicar essa alteração no servidor.
5. Com isso pronto, já é possível disparar o cadastro de teste e a contratação de teste durante a reunião, e acompanhar em tempo real na aba "Eventos de teste" do Gerenciador de Eventos.
6. **Depois que o teste for confirmado** (os dois eventos aparecendo certinho, com origem "Servidor"), é só remover ou deixar vazio o campo `test_event_code` — daí os eventos passam a contar como reais, valendo para as campanhas a partir de 09/11.
