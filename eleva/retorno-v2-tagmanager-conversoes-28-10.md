# Retorno ao v2 — Tag Manager e conversões
**RECRIA Marketing, 28/10/2026**
**Em resposta a "Resposta à Recria · Tag Manager e conversões", v2, 27/10/2026**

---

## 1 · Tag Manager no site (atrás do aceite de cookies)

De acordo com tudo — a decisão de só carregar depois do aceite está certa (LGPD), assim como tirar o `<noscript>` e corrigir o PageView duplicado que vocês identificaram no site. Avisem quando publicar que a gente confirma com o Tag Assistant.

## 2 · No portal (sem Tag Manager, envio pelo servidor)

De acordo com a decisão de não rodar script de terceiro no portal — faz sentido pela regra de segurança de vocês. A alternativa (levar os códigos de clique pela URL do botão, sem vinculação entre domínios) resolve o mesmo problema sem abrir exceção na regra. Sem objeções.

## 3 · Nome do evento — CompleteRegistration

Confirmado, sem pendência.

## 4 · Lista semanal para o Google Ads

Segue em anexo o modelo de planilha (`modelo-planilha-conversoes-google-ads.csv`), no formato que o Google Ads espera:

| Coluna | O que vai |
|---|---|
| Google Click ID | o `gclid`, quando houver (deixar em branco se vier por GBRAID/WBRAID) |
| GBRAID / WBRAID | usados em casos específicos (app/iOS) — preencher só uma das três colunas de identificador por linha |
| Conversion Name | `Área Comum · conta criada` ou `Área Comum · assinatura` (nomes exatos) |
| Conversion Time | data e hora do evento, formato `MM/DD/AAAA HH:MM:SS` |
| Conversion Value | só na assinatura (valor pago); em branco no cadastro |
| Conversion Currency | sempre `BRL` |

Sobre o fuso horário: a conta do Google Ads usa o fuso configurado nela (a confirmar se é Horário de Brasília) — por favor, gerar a lista já nesse fuso horário.

## 5 · Teste antes de ligar o envio à Meta

De acordo, sem pendência.

## 6 · Acessos no portfólio "Eleva"

- **Fator.ag e René Kasper**: removendo, incluindo o acesso de faturamento, como autorizado.
- **Kommo**: provavelmente uma integração de CRM ativa (talvez de quando testaram a plataforma) — vamos verificar com calma antes de decidir, sem pressa de remover agora.
- **Considere Feito**: é a empresa vinculada ao René Kasper — como ainda é uma parceria ativa de vocês, mantemos o acesso, mesmo removendo o acesso individual do René e da Fator.ag.
- **Solutions Engineering Team**: pode remover, sem uso identificado.

---

## Próximos passos

- **Eleva**: publicar o site com o Tag Manager (atrás do aceite) e o botão levando os códigos de clique — nos avisar quando estiver no ar.
- **Recria**: conferir o container após a publicação; acesso de Fator.ag/René Kasper/Solutions Engineering Team sendo removido; acesso da Considere Feito mantido; Kommo em verificação.
- **Juntos**: o teste na tela "Eventos de teste", assim que o envio pelo servidor estiver pronto do lado de vocês.
