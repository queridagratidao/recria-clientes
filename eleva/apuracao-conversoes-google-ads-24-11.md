# Apuração — Acessos e Conversões do Google Ads da Eleva
**RECRIA Marketing, 24/11/2026**

---

## Remoção do Rene (Considere Feito)

O Giuliano pediu a remoção de `rene@considerefeito.com` como Administrador da conta do Google Ads da Eleva (455-373-9886). O pedido exigia aprovação de outro administrador. Em 24/11, a Amanda aprovou o pedido em Adm. → Acesso e segurança → Aprovações de outras partes → Solicitações de gerenciamento de usuários. Removido com sucesso.

## Ações de conversão criadas pela Recria

A Recria cuida da conta desde abril/2026. Das 17 ações de conversão existentes na conta, ficou definido:

**Criadas pela Recria:**
- Compra Curso Síndico - Hotmart
- Formulário LP Mentoria Executiva
- Lead - Sessão Estratégica
- Inscrição
- Área Comum · assinatura
- Área Comum · conta criada

**Não é da Recria:**
- F | Click whats LP (é da Fator, outra agência)

**Genéricas, criadas automaticamente pelo próprio Google Ads (não são de nenhuma agência):**
- Lead form - Submit, Calls from ads, Contato, Clicks to call, Clique de saída, Local actions (Directions / Other engagements / Website visits), Conversation started

## Sobre o status "Configuração incorreta"

Ao conferir as 4 ações criadas pela Recria que não são do Área Comum (Compra Curso Síndico - Hotmart, Formulário LP Mentoria Executiva, Lead - Sessão Estratégica, Inscrição), todas mostravam o status "Configuração incorreta".

Isso **não é um erro de instalação ou quebra de tag**. O diagnóstico de cada uma mostra apenas que a tag não recebe sinal há mais de 7 dias ("tag não recebeu pings" ou "nunca recebeu dados"), porque não existe nenhuma campanha ativa de lead rodando para esses produtos no momento (Curso Síndico, Mentoria Executiva, Sessão Estratégica, Inscrição). Sem cliques/preenchimentos nessas páginas, não há o que a tag registrar, e o Google Ads interpreta a ausência de dado recente como "configuração incorreta", mesmo com o evento (gerenciado via Google Tag Manager) configurado corretamente.

As duas ações do Área Comum (`Área Comum · assinatura` e `Área Comum · conta criada`) aparecem com status "Conversões pendentes", não "configuração incorreta" — é o mesmo caso de falta de dado recente, sem indicação de problema técnico.

**Conclusão**: nenhuma das 4 ações precisa de ajuste agora. Assim que uma campanha de lead for reativada para algum desses produtos, a tag volta a registrar normalmente.
