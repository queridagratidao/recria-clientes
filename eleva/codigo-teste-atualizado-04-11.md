# Código de teste atualizado
**RECRIA Marketing, 04/11/2026**

---

Giuliano, esse código de teste da Meta muda de tempo em tempo — e já mudou desde a última vez que passamos pra você. Nada grave, é rápido de ajustar.

Pra conseguirmos fazer o evento de teste juntos na reunião de hoje à tarde, pode mandar esse documento pro seu Claude ainda hoje de manhã, pra ele atualizar o código no servidor? Assim, na hora da reunião, já está tudo pronto pra gente testar certinho.

**Novo código de teste**: `TEST67208`

## Passo a passo para o Claude do Giuliano

1. No código do portal, localizar a parte que faz a chamada para a API de Conversões da Meta (a função que dispara os eventos `CompleteRegistration` e `Purchase`).
2. Nessa chamada, o corpo da requisição tem um campo chamado **`test_event_code`** — é um parâmetro geral da chamada, no mesmo nível dos dados do evento (não dentro de cada evento individual).
3. Atualizar o valor desse campo para `TEST67208`, no lugar do código antigo (`TEST41558`).
4. Salvar e publicar essa alteração no servidor.
5. Com isso pronto, já é possível disparar o cadastro de teste e a contratação de teste durante a reunião, e acompanhar em tempo real na aba "Eventos de teste" do Gerenciador de Eventos.
6. **Depois que o teste for confirmado** (os dois eventos aparecendo certinho, com origem "Servidor"), é só remover ou deixar vazio o campo `test_event_code` — daí os eventos passam a contar como reais, valendo para as campanhas a partir de 09/11.
