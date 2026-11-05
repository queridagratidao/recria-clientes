# Melhorias nos eventos do servidor
**RECRIA Marketing, 05/11/2026**

---

Giuliano, com o `CompleteRegistration` já chegando certinho no teste de hoje, seguem 4 ajustes recomendados pela própria Meta para melhorar o reconhecimento e a otimização das campanhas. Pode mandar esse documento direto pro seu Claude.

## Passo a passo para o Claude do Giuliano

**1. Mandar mais dados do usuário, para a Meta reconhecer melhor quem converteu**

Hoje, só com o e-mail, a Meta reconhece poucas pessoas — isso piora a otimização e a medição das campanhas. Incluir também, sempre com hash SHA-256:
- Telefone, com DDI 55.
- Nome e sobrenome.
- `external_id`, que pode ser o próprio ID do Airtable.

**2. Mandar dados do navegador, sem hash**

- Os cookies `fbp` e `fbc` do navegador do usuário.
- O IP do usuário (`client_ip_address`).
- O navegador/user agent do usuário (`client_user_agent`) — para eventos de site, esse campo é **obrigatório** pela documentação da Meta.

**3. Evitar contagem em dobro (deduplicação)**

Se o Pixel do site também disparar o `CompleteRegistration` (além do servidor), os dois precisam enviar o **mesmo ID de evento** (`event_id`). Sem isso, a Meta conta cada cadastro duas vezes — uma vinda do navegador, outra vinda do servidor.

**4. Tirar o código de teste antes de ir ao ar**

Enquanto o `TEST67208` estiver no envio, os eventos aparecem só na aba "Eventos de teste" e não entram na otimização das campanhas. Lembrando que o combinado é remover esse campo até sexta, 06/11, antes das campanhas começarem em 09/11.
