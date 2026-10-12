# Agenda automática · Diagnóstico Recria e 1º encontro da Mentoria

Um único script (`apps-script-agenda.gs`) atende as duas páginas:
`/diagnostico-recria/obrigado.html` (produto `consultoria`) e `/mentoria-obrigado/` (produto `mentoria`).
O formulário é montado por `assets/agenda.js` no site.

## Fluxo
1. Compra na Hotmart → página de obrigado.
2. Diagnóstico: a pessoa escolhe **chamada de vídeo** ou **sem chamada (formulário + WhatsApp, diagnóstico em PDF)**. Mentoria: só chamada.
3. Preenche nome, WhatsApp, e-mail, (dia e horário, se chamada) e o questionário de 13 perguntas.
4. Chamada: o script cria o evento com Google Meet na sua agenda, convida o e-mail dela e as respostas vão na descrição do evento.
   Sem chamada: não cria evento; ela é levada ao WhatsApp para tirar dúvidas.
5. Sempre: salva uma linha na aba (Consultoria - agendamentos / Mentoria - agendamentos) da planilha _CRM Central e te manda e-mail com todas as respostas (pronto para colar no agente do diagnóstico).

## Regras (bloco `CFG`)
- Segunda, terça, quinta e sexta. Nunca quarta.
- 9h às 12h e 14h às 18h, 1 hora cada (início 9, 10, 11, 14, 15, 16, 17).
- Antecedência 2 dias: compra na segunda libera a quinta.
- Mostra 21 dias à frente. Qualquer evento seu na agenda bloqueia o horário. Um agendamento por e-mail. Horário rechecado ao confirmar.

## Instalar (≈10 min)
1. script.google.com → Novo projeto → colar `apps-script-agenda.gs`.
2. Serviços (+) → **Google Calendar API**.
3. Configurações do projeto → fuso **(GMT-03:00) Brasília**.
4. Executar `autorizar` e depois `testarHorarios`.
5. Implantar → Nova implantação → App da Web → Executar como **Eu** · Acesso **Qualquer pessoa** → copiar a URL.
6. Me mandar a URL: eu coloco em `window.AGENDA.API` das duas páginas.
7. Hotmart, página de agradecimento: Diagnóstico = `https://www.agenciarecria.com.br/diagnostico-recria/obrigado.html`; Mentoria = `https://www.agenciarecria.com.br/mentoria-obrigado/`.

## Questionário
Nome do negócio*, Instagram/site, cidade/estado, o que vende e preços*, cliente ideal*, como as vendas acontecem*, tempo de negócio, equipe, o que faz de conteúdo e anúncios, maior dificuldade*, o que já tentou, objetivo em 6 meses*, dúvidas. (* obrigatórias)
