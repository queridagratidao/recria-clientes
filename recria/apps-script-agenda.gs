/**
 * Recria · Agendamento + questionário (Diagnóstico Recria e 1º encontro da Mentoria)
 *
 * O que faz:
 *  1) As páginas /diagnostico-recria/obrigado e /mentoria-obrigado/ pedem os horários livres (doGet, acao=slots&produto=...).
 *  2) Horários: segunda, terça, quinta e sexta, 9h-12h e 14h-18h, 1 hora cada, com 2 dias de antecedência,
 *     respeitando a SUA Google Agenda (qualquer evento seu bloqueia o horário). Quarta nunca é oferecida.
 *  3) Quando a pessoa envia (doPost, acao=agendar), o script:
 *       - cria o evento com Google Meet na sua agenda e convida o e-mail dela (modo "video");
 *       - OU, no modo "whatsapp" (só Diagnóstico), não cria evento: guarda as respostas para você
 *         conversar pelo WhatsApp e entregar o diagnóstico em PDF;
 *       - salva dados + todas as respostas do questionário na aba do produto;
 *       - te avisa por e-mail com tudo (dá para copiar e colar no outro agente).
 *
 * Instalação (passo a passo no chat):
 *  - Crie uma planilha NOVA (ex.: "Recria Agenda - Diagnóstico e Mentoria"), abra Extensões > Apps Script e cole este código.
 *  - Serviços (+) > adicione "Google Calendar API" (Advanced Service).
 *  - Configurações do projeto > fuso horário: (GMT-03:00) Horário de Brasília.
 *  - Execute "autorizar" > aceite as permissões > Execute "testarHorarios".
 *  - Implantar > Nova implantação > App da Web > Executar como: Eu > Acesso: Qualquer pessoa.
 */

var CFG = {
  ID_PLANILHA: '',   // vazio = usa a planilha onde o script foi criado (Extensões > Apps Script)
  EMAIL_AVISO: 'amandarecria@gmail.com',
  FUSO: 'America/Sao_Paulo',

  DURACAO_MIN: 60,
  DIAS_UTEIS: [1, 2, 4, 5],                              // seg, ter, qui, sex (quarta nunca)
  JANELAS: [ { ini: 9, fim: 12 }, { ini: 14, fim: 18 } ], // 9h-12h e 14h-18h
  ANTECEDENCIA_DIAS: 2,                                  // compra na segunda libera a quinta (quarta é bloqueada)
  JANELA_DIAS: 21,                                       // mostra até 21 dias à frente
  BUFFER_MIN: 0                                          // intervalo extra entre compromissos
};

var PRODUTOS = {
  consultoria: { nome: 'Diagnóstico Recria', titulo: 'Diagnóstico Recria', aba: 'Consultoria - agendamentos', modos: ['video', 'whatsapp'] },
  mentoria:    { nome: 'Mentoria Recria',    titulo: 'Mentoria Recria - 1º encontro', aba: 'Mentoria - agendamentos', modos: ['video'] }
};

// Perguntas do questionário (a ordem vira a ordem das colunas na planilha)
var CAMPOS = [
  { k: 'negocio',   t: 'Nome do negócio',                         obrig: true },
  { k: 'instagram', t: 'Instagram ou site do negócio',            obrig: false },
  { k: 'cidade',    t: 'Cidade e estado onde atua',               obrig: false },
  { k: 'vende',     t: 'O que você vende (principais produtos/serviços e preços)', obrig: true },
  { k: 'cliente',   t: 'Quem é o seu cliente ideal',              obrig: true },
  { k: 'vendas',    t: 'Como as vendas acontecem hoje',           obrig: true },
  { k: 'tempo',     t: 'Há quanto tempo o negócio existe',        obrig: false },
  { k: 'equipe',    t: 'Quem trabalha no negócio hoje',           obrig: false },
  { k: 'marketing', t: 'O que faz hoje de conteúdo e anúncios',   obrig: false },
  { k: 'dor',       t: 'Maior dificuldade do negócio hoje',       obrig: true },
  { k: 'tentou',    t: 'O que já tentou para resolver',           obrig: false },
  { k: 'objetivo',  t: 'Onde quer chegar nos próximos 6 meses',   obrig: true },
  { k: 'duvidas',   t: 'Dúvidas ou algo que quer que eu veja com atenção', obrig: false }
];

var OFFSET_MS = 3 * 3600 * 1000; // Brasília = UTC-3 (sem horário de verão)

/* ===================== LÓGICA DOS HORÁRIOS (pura, testável) ===================== */

function slotsDisponiveis_(agoraMs, ocupados, cfg) {
  var out = [];
  var minInicio = agoraMs + cfg.ANTECEDENCIA_DIAS * 86400000;
  var base = new Date(agoraMs - OFFSET_MS);
  base.setUTCHours(0, 0, 0, 0);
  var durH = cfg.DURACAO_MIN / 60;
  var durMs = cfg.DURACAO_MIN * 60000;
  var bufMs = (cfg.BUFFER_MIN || 0) * 60000;

  for (var i = 0; i <= cfg.JANELA_DIAS; i++) {
    var dia = new Date(base.getTime() + i * 86400000);
    if (cfg.DIAS_UTEIS.indexOf(dia.getUTCDay()) < 0) continue;

    for (var j = 0; j < cfg.JANELAS.length; j++) {
      var jn = cfg.JANELAS[j];
      for (var h = jn.ini; h + durH <= jn.fim; h += durH) {
        var hh = Math.floor(h), mm = Math.round((h - hh) * 60);
        var ini = Date.UTC(dia.getUTCFullYear(), dia.getUTCMonth(), dia.getUTCDate(), hh, mm, 0) + OFFSET_MS;
        var fim = ini + durMs;
        if (ini < minInicio) continue;

        var ocupado = false;
        for (var o = 0; o < ocupados.length; o++) {
          if (ini < ocupados[o].fim + bufMs && fim + bufMs > ocupados[o].ini) { ocupado = true; break; }
        }
        if (ocupado) continue;
        out.push({ ini: ini, fim: fim });
      }
    }
  }
  return out;
}

/* ===================== AGENDA ===================== */

function ocupadosNaAgenda_(deMs, ateMs) {
  var cal = CalendarApp.getDefaultCalendar();
  var evs = cal.getEvents(new Date(deMs), new Date(ateMs));
  var out = [];
  for (var i = 0; i < evs.length; i++) {
    var ev = evs[i];
    try { if (ev.getMyStatus() === CalendarApp.GuestStatus.NO) continue; } catch (x) {}
    out.push({ ini: ev.getStartTime().getTime(), fim: ev.getEndTime().getTime() });
  }
  return out;
}

function horariosLivres_() {
  var agora = new Date().getTime();
  var ate = agora + (CFG.JANELA_DIAS + 2) * 86400000;
  return slotsDisponiveis_(agora, ocupadosNaAgenda_(agora - 86400000, ate), CFG);
}

/* ===================== WEB APP ===================== */

function doGet(e) {
  var acao = (e && e.parameter && e.parameter.acao) || '';
  if (acao === 'slots') {
    var slots = horariosLivres_().map(function (s) {
      return { inicio: new Date(s.ini).toISOString(), fim: new Date(s.fim).toISOString() };
    });
    return json_({ ok: true, fuso: CFG.FUSO, slots: slots });
  }
  return json_({ ok: true, mensagem: 'Recria · agenda no ar' });
}

function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(25000);
    var d = lerJson_(e);
    if (d.acao !== 'agendar') return json_({ ok: false, erro: 'ação inválida' });

    var prod = PRODUTOS[d.produto];
    if (!prod) return json_({ ok: false, erro: 'produto inválido' });
    var modo = d.modo === 'whatsapp' ? 'whatsapp' : 'video';
    if (prod.modos.indexOf(modo) < 0) return json_({ ok: false, erro: 'Opção indisponível.' });

    var nome = limpar_(d.nome), email = limpar_(d.email).toLowerCase(), zap = limpar_(d.whatsapp);
    if (nome.length < 2) return json_({ ok: false, erro: 'Informe o seu nome.' });
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return json_({ ok: false, erro: 'Informe um e-mail válido.' });
    var dig = zap.replace(/\D/g, '');
    if (dig.indexOf('55') === 0 && dig.length > 11) dig = dig.substring(2);
    if (dig.length < 10 || dig.length > 11) return json_({ ok: false, erro: 'Informe o WhatsApp com DDD.' });

    var r = d.respostas || {};
    var resp = {};
    for (var i = 0; i < CAMPOS.length; i++) {
      var c = CAMPOS[i];
      resp[c.k] = limparLongo_(r[c.k]);
      if (c.obrig && resp[c.k].length < 2) return json_({ ok: false, erro: 'Responda: ' + c.t + '.' });
    }

    var texto = 'NOME: ' + nome + '\nWHATSAPP: ' + zap + '\nE-MAIL: ' + email + '\n\n';
    for (var k = 0; k < CAMPOS.length; k++) texto += CAMPOS[k].t.toUpperCase() + ':\n' + (resp[CAMPOS[k].k] || '(não respondeu)') + '\n\n';

    var aba = aba_(prod.aba);
    var evento = null, quando = '', iniMs = 0;

    if (modo === 'video') {
      if (jaAgendou_(aba, email)) {
        return json_({ ok: false, erro: 'Já existe um horário marcado para esse e-mail. Para trocar, fale com a Amanda no WhatsApp.' });
      }
      iniMs = new Date(d.inicio).getTime();
      var livre = horariosLivres_().filter(function (s) { return s.ini === iniMs; });
      if (!livre.length) return json_({ ok: false, erro: 'Esse horário acabou de ser ocupado. Escolha outro, por favor.' });

      var titulo = prod.titulo + ' - ' + (resp.negocio || nome);
      evento = Calendar.Events.insert({
        summary: titulo,
        description: prod.nome + ' (1 hora, por Google Meet)\n\n' + texto,
        start: { dateTime: new Date(livre[0].ini).toISOString(), timeZone: CFG.FUSO },
        end: { dateTime: new Date(livre[0].fim).toISOString(), timeZone: CFG.FUSO },
        attendees: [{ email: email, displayName: nome }],
        conferenceData: { createRequest: { requestId: Utilities.getUuid(), conferenceSolutionKey: { type: 'hangoutsMeet' } } },
        reminders: { useDefault: false, overrides: [{ method: 'email', minutes: 1440 }, { method: 'popup', minutes: 30 }] }
      }, 'primary', { conferenceDataVersion: 1, sendUpdates: 'all' });
      quando = Utilities.formatDate(new Date(livre[0].ini), CFG.FUSO, "dd/MM/yyyy 'às' HH:mm");
    }

    var linha = [new Date(), modo === 'video' ? 'Chamada de vídeo' : 'WhatsApp + PDF', nome, zap, email,
                 modo === 'video' ? new Date(iniMs) : '', evento ? (evento.hangoutLink || '') : '',
                 modo === 'video' ? 'Agendado' : 'Aguardando conversa'];
    for (var m = 0; m < CAMPOS.length; m++) linha.push(resp[CAMPOS[m].k]);
    aba.appendRow(linha);

    var assunto = (modo === 'video' ? 'Novo agendamento: ' : 'Novo diagnóstico (WhatsApp + PDF): ') + prod.nome + ' - ' + (resp.negocio || nome);
    var corpo = (modo === 'video'
      ? 'Entrou um agendamento por chamada de vídeo.\nQuando: ' + quando + '\nMeet: ' + (evento.hangoutLink || '(gerando)') + '\n\n'
      : 'A pessoa escolheu SEM chamada: conversar pelo WhatsApp e receber o diagnóstico em PDF.\n\n') +
      texto + 'Planilha: ' + planilha_().getUrl();
    MailApp.sendEmail(CFG.EMAIL_AVISO, assunto, corpo);

    return json_({ ok: true, modo: modo, quando: quando, meet: evento ? (evento.hangoutLink || '') : '' });
  } catch (err) {
    return json_({ ok: false, erro: 'Não foi possível enviar agora. Fale com a Amanda no WhatsApp. (' + String(err).substring(0, 120) + ')' });
  } finally {
    try { lock.releaseLock(); } catch (x) {}
  }
}

/* ===================== PLANILHA ===================== */

function planilha_() {
  return CFG.ID_PLANILHA ? SpreadsheetApp.openById(CFG.ID_PLANILHA) : SpreadsheetApp.getActiveSpreadsheet();
}

function aba_(nome) {
  var p = planilha_();
  var a = p.getSheetByName(nome) || p.insertSheet(nome);
  if (a.getLastRow() === 0) {
    var cab = ['Data do pedido', 'Modo', 'Nome', 'WhatsApp', 'E-mail', 'Início', 'Link do Meet', 'Situação'];
    for (var i = 0; i < CAMPOS.length; i++) cab.push(CAMPOS[i].t);
    a.appendRow(cab);
    a.getRange(1, 1, 1, cab.length).setFontWeight('bold').setBackground('#f3e9cf');
    a.setFrozenRows(1);
  }
  return a;
}

function jaAgendou_(aba, email) {
  var n = aba.getLastRow();
  if (n < 2) return false;
  var v = aba.getRange(2, 1, n - 1, 8).getValues();
  for (var i = 0; i < v.length; i++) if (String(v[i][4]).toLowerCase() === email && String(v[i][7]) === 'Agendado') return true;
  return false;
}

/* ===================== UTIL ===================== */

function lerJson_(e) {
  var b = (e && e.postData && e.postData.contents) ? e.postData.contents : '';
  try { return JSON.parse(b); } catch (x) { return (e && e.parameter) ? e.parameter : {}; }
}
function limpar_(v) { return (v === undefined || v === null) ? '' : String(v).replace(/[\r\n\t]+/g, ' ').trim().substring(0, 200); }
function limparLongo_(v) { return (v === undefined || v === null) ? '' : String(v).replace(/\r/g, '').trim().substring(0, 1500); }
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

/** Rode uma vez para autorizar (agenda, planilha e e-mail). */
function autorizar() {
  CalendarApp.getDefaultCalendar().getName();
  planilha_().getName();
  MailApp.getRemainingDailyQuota();
  Logger.log('Permissões ok.');
}

/** Rode para ver os próximos horários que o site vai mostrar. */
function testarHorarios() {
  var s = horariosLivres_();
  Logger.log(s.length + ' horários livres. Primeiros:');
  for (var i = 0; i < Math.min(10, s.length); i++) Logger.log(Utilities.formatDate(new Date(s[i].ini), CFG.FUSO, 'EEE dd/MM HH:mm'));
}
