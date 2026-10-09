# Mentoria Recria · agendamento do 1º encontro (estrutura)

## Como funciona
1. Pessoa compra na Hotmart → cai em `https://www.agenciarecria.com.br/mentoria-obrigado/`.
2. A página busca os horários livres no Apps Script (`?acao=slots`), que lê a sua Google Agenda de verdade.
3. Ela preenche nome, negócio, WhatsApp, e-mail, escolhe dia e horário.
4. O script cria o evento **"Mentoria Recria - <negócio ou nome>"** na sua agenda, com Google Meet, convida o e-mail dela, grava na aba "Mentoria - agendamentos" e te avisa por e-mail.
5. Os encontros seguintes são marcados manualmente.

## Regras já configuradas (`apps-script-mentoria.gs`, bloco `CFG`)
- Segunda a sexta, 9h às 19h (último encontro começa 18h), 1 hora cada.
- Quarta das 15h às 17h bloqueada.
- Antecedência mínima: 3 dias (compra na segunda libera a quinta). Ajustável em `ANTECEDENCIA_DIAS`.
- Mostra 21 dias à frente. Eventos da sua agenda (exceto os recusados) bloqueiam o horário.
- Um agendamento por e-mail. Horário rechecado na hora de confirmar (evita choque).
- Opcional: `EXIGIR_COMPRA` + webhook da Hotmart, para só agendar quem comprou.

## Testado
Lógica dos horários testada em Node (antecedência, quarta bloqueada, evento ocupando horário, janela até 19h).

## Amanhã: instalar (≈10 min)
1. script.google.com → Novo projeto → colar `apps-script-mentoria.gs`.
2. Serviços (+) → adicionar **Google Calendar API**.
3. Configurações do projeto → fuso **(GMT-03:00) Brasília**.
4. Executar `autorizar` (aceitar permissões) e depois `testarHorarios` (ver o log).
5. Implantar → Nova implantação → App da Web → Executar como: **Eu** · Acesso: **Qualquer pessoa** → copiar a URL.
6. Me mandar a URL: eu coloco em `window.MENTORIA.API` da página e publico.
7. Na Hotmart, página de agradecimento da Mentoria = `https://www.agenciarecria.com.br/mentoria-obrigado/`.

## A confirmar
- Antecedência: 3 dias basta? (compra na sexta cai na segunda; você falou terça/quarta → usar 4.)
- Gravação: o Google Meet só grava em planos pagos do Workspace; senão, trocar por "ata e material direcional".
- Formato: 6 meses, 1 encontro individual/mês, WhatsApp em horário comercial.
