/**
 * Recria · Agendamento do 1º encontro da Mentoria Recria
 *
 * O que faz:
 *  1) A página /mentoria-obrigado/ pede os horários livres (doGet, acao=slots).
 *  2) O script monta os horários: segunda a sexta, 9h às 19h (último encontro termina às 19h),
 *     1 hora cada, sem a quarta das 15h às 17h, com antecedência mínima e respeitando a SUA agenda.
 *  3) Quando a pessoa agenda (doPost, acao=agendar), cria o evento "Mentoria Recria - <negócio ou nome>"
 *     na sua agenda, com Google Meet, convida o e-mail dela e te avisa por e-mail.
 *  4) Salva tudo na aba "Mentoria - agendamentos" da planilha _CRM Central - Agência Recria.
 *  5) (Opcional) Recebe o aviso de compra da Hotmart (webhook) e só deixa agendar quem comprou.
 *
 * Instalação (amanhã, passo a passo no chat):
 *  - script.google.com > Novo projeto > cole este código.
 *  - Serviços (+) > adicione "Google Calendar API" (Advanced Service).
 *  - Configurações do projeto > fuso horário: (GMT-03:00) Horário de Brasília.
 *  - Execute "autorizar" > aceite as permissões > Execute "testarHorarios".
 *  - Implantar > Nova implantação > App da Web > Executar como: Eu > Acesso: Qualquer pessoa.
 */

var CFG = {
  ID_PLANILHA: '1kbRl6xxqbfggIk96TopOCHZE_ehaxKCHOcKtbloC3Gc',
  ABA_AGENDAMENTOS: 'Mentoria - agendamentos',
  ABA_COMPRAS: 'Mentoria - compras',
  EMAIL_AVISO: 'amandarecria@gmail.com',
  CALENDARIO: 'primary',
  FUSO: 'America/Sao_Paulo',
  TITULO: 'Mentoria Recria',

  DURACAO_MIN: 60,
  DIAS_UTEIS: [1, 2, 3, 4, 5],                 // 0=domingo ... 6=sábado
  HORAS_INICIO: [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], // 18h + 1h = termina às 19h
  BLOQUEIOS: [ { dia: 3, ini: 15, fim: 17 } ],  // quarta das 15h às 17h (horário fixo seu)
  ANTECEDENCIA_DIAS: 3,                        // compra na segunda libera a quinta
  JANELA_DIAS: 21,                             // mostra até 21 dias à frente
  BUFFER_MIN: 0,                               // intervalo extra entre compromissos

  EXIGIR_COMPRA: false,                        // true = só agenda quem tem compra registrada pela Hotmart
  HOTMART_HOTTOK: ''                           // cole aqui o "hottok" do webhook da Hotmart (se for usar)
};

var OFFSET_MS = 3 * 3600 * 1000; // Brasília = UTC-3 (sem horário de verão)

/* ===================== LÓGICA DOS HORÁRIOS (pura, testável) ===================== */

function slotsDisponiveis_(agoraMs, ocupados, cfg) {
  var out = [];
  var minInicio = agoraMs + cfg.ANTECEDENCIA_DIAS * 86400000;
  var base = new Date(agoraMs - OFFSET_MS);
  base.setUTCHours(0, 0, 0, 0);
  var durMs = cfg.DURACAO_MIN * 60000;
  var bufMs = (cfg.BUFFER_MIN || 0) * 60000;

  for (var i = 0; i <= cfg.JANELA_DIAS; i++) {
    var dia = new Date(base.getTime() + i * 86400000);
    var dow = dia.getUTCDay();
    if (cfg.DIAS_UTEIS.indexOf(dow) < 0) continue;

    for (var k = 0; k < cfg.HORAS_INICIO.length; k++) {
      var h = cfg.HORAS_INICIO[k];
      var ini = Date.UTC(dia.getUTCFullYear(), dia.getUTCMonth(), dia.getUTCDate(), h, 0, 0) + OFFSET_MS;
      var fim = ini + durMs;
      if (ini < minInicio) continue;

      var bloqueado = false;
      for (var b = 0; b < cfg.BLOQUEIOS.length; b++) {
        var bl = cfg.BLOQUEIOS[b];
        if (bl.dia === dow && h < bl.fim && (h + cfg.DURACAO_MIN / 60) > bl.ini) { bloqueado = true; break; }
      }
      if (bloqueado) continue;

      var ocupado = false;
      for (var o = 0; o < ocupados.length; o++) {
        if (ini < ocupados[o].fim + bufMs && fim + bufMs > ocupados[o].ini) { ocupado = true; break; }
      }
      if (ocupado) continue;

      out.push({ ini: ini, fim: fim });
    }
  }
  return out;
}

/* ===================== AGENDA ===================== */

function ocupadosNaAgenda_(deMs, ateMs) {
  var cal = CFG.CALENDARIO === 'primary' ? CalendarApp.getDefaultCalendar() : CalendarApp.getCalendarById(CFG.CALENDARIO);
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
  return json_({ ok: true, mensagem: 'Recria · agenda da mentoria no ar' });
}

function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(25000);
    var d = lerJson_(e);

    // Aviso de compra da Hotmart (webhook)
    if (d && d.event && d.data) return registrarCompraHotmart_(d, e);

    if (d.acao !== 'agendar') return json_({ ok: false, erro: 'ação inválida' });

    var nome = limpar_(d.nome), negocio = limpar_(d.negocio), email = limpar_(d.email).toLowerCase(), zap = limpar_(d.whatsapp);
    if (nome.length < 2) return json_({ ok: false, erro: 'Informe o seu nome.' });
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return json_({ ok: false, erro: 'Informe um e-mail válido.' });
    var dig = zap.replace(/\D/g, '');
    if (dig.indexOf('55') === 0 && dig.length > 11) dig = dig.substring(2);
    if (dig.length < 10 || dig.length > 11) return json_({ ok: false, erro: 'Informe o WhatsApp com DDD.' });

    if (CFG.EXIGIR_COMPRA && !compraRegistrada_(email)) {
      return json_({ ok: false, erro: 'Não encontramos uma compra com esse e-mail. Use o e-mail da compra ou fale com a Amanda no WhatsApp.' });
    }
    if (jaAgendou_(email)) {
      return json_({ ok: false, erro: 'Já existe um encontro agendado para esse e-mail. Para trocar o horário, fale com a Amanda no WhatsApp.' });
    }

    var iniMs = new Date(d.inicio).getTime();
    var livre = horariosLivres_().filter(function (s) { return s.ini === iniMs; });
    if (!livre.length) return json_({ ok: false, erro: 'Esse horário acabou de ser ocupado. Escolha outro, por favor.' });

    var titulo = CFG.TITULO + ' - ' + (negocio || nome);
    var descricao =
      'Primeiro encontro da Mentoria Recria.\n\n' +
      'Nome: ' + nome + '\n' +
      (negocio ? 'Negócio: ' + negocio + '\n' : '') +
      'WhatsApp: ' + zap + '\n' +
      'E-mail: ' + email + '\n\n' +
      'Encontro de 1 hora, por Google Meet.';

    var evento = Calendar.Events.insert({
      summary: titulo,
      description: descricao,
      start: { dateTime: new Date(livre[0].ini).toISOString(), timeZone: CFG.FUSO },
      end: { dateTime: new Date(livre[0].fim).toISOString(), timeZone: CFG.FUSO },
      attendees: [{ email: email, displayName: nome }],
      conferenceData: { createRequest: { requestId: Utilities.getUuid(), conferenceSolutionKey: { type: 'hangoutsMeet' } } },
      reminders: { useDefault: false, overrides: [{ method: 'email', minutes: 1440 }, { method: 'popup', minutes: 30 }] }
    }, 'primary', { conferenceDataVersion: 1, sendUpdates: 'all' });

    var quando = Utilities.formatDate(new Date(livre[0].ini), CFG.FUSO, "dd/MM/yyyy 'às' HH:mm");
    abaAgendamentos_().appendRow([new Date(), nome, negocio, d.whatsapp, email, new Date(livre[0].ini), evento.hangoutLink || '', titulo, 'Agendado']);
    MailApp.sendEmail(CFG.EMAIL_AVISO, 'Novo agendamento: ' + titulo,
      'Entrou um agendamento da Mentoria Recria.\n\n' + descricao + '\n\nQuando: ' + quando + '\nMeet: ' + (evento.hangoutLink || '(gerando)') +
      '\n\nPlanilha: https://docs.google.com/spreadsheets/d/' + CFG.ID_PLANILHA + '/edit');

    return json_({ ok: true, quando: quando, meet: evento.hangoutLink || '', titulo: titulo });
  } catch (err) {
    return json_({ ok: false, erro: 'Não foi possível agendar agora. Fale com a Amanda no WhatsApp. (' + String(err).substring(0, 120) + ')' });
  } finally {
    try { lock.releaseLock(); } catch (x) {}
  }
}

/* ===================== COMPRAS (Hotmart, opcional) ===================== */

function registrarCompraHotmart_(d, e) {
  var token = (e && e.parameter && e.parameter.hottok) || (d.hottok || '');
  if (CFG.HOTMART_HOTTOK && token !== CFG.HOTMART_HOTTOK) return json_({ ok: false, erro: 'token inválido' });
  var evento = String(d.event || '');
  if (evento.indexOf('PURCHASE_APPROVED') < 0 && evento.indexOf('PURCHASE_COMPLETE') < 0) return json_({ ok: true, ignorado: evento });
  var data = d.data || {}, buyer = data.buyer || {}, produto = data.product || {}, compra = data.purchase || {};
  var aba = abaCompras_();
  aba.appendRow([new Date(), String(buyer.name || ''), String(buyer.email || '').toLowerCase(), String(produto.name || ''), String(compra.transaction || ''), evento]);
  return json_({ ok: true });
}

function compraRegistrada_(email) {
  var aba = abaCompras_(); var n = aba.getLastRow();
  if (n < 2) return false;
  var v = aba.getRange(2, 3, n - 1, 1).getValues();
  for (var i = 0; i < v.length; i++) if (String(v[i][0]).toLowerCase() === email) return true;
  return false;
}

/* ===================== PLANILHA ===================== */

function aba_(nome, cabecalho) {
  var p = SpreadsheetApp.openById(CFG.ID_PLANILHA);
  var a = p.getSheetByName(nome) || p.insertSheet(nome);
  if (a.getLastRow() === 0) {
    a.appendRow(cabecalho);
    a.getRange(1, 1, 1, cabecalho.length).setFontWeight('bold').setBackground('#f3e9cf');
    a.setFrozenRows(1);
  }
  return a;
}
function abaAgendamentos_() { return aba_(CFG.ABA_AGENDAMENTOS, ['Data do pedido', 'Nome', 'Negócio', 'WhatsApp', 'E-mail', 'Início do encontro', 'Link do Meet', 'Título do evento', 'Situação']); }
function abaCompras_() { return aba_(CFG.ABA_COMPRAS, ['Data', 'Nome', 'E-mail', 'Produto', 'Transação', 'Evento']); }

function jaAgendou_(email) {
  var a = abaAgendamentos_(); var n = a.getLastRow();
  if (n < 2) return false;
  var v = a.getRange(2, 5, n - 1, 5).getValues();
  for (var i = 0; i < v.length; i++) if (String(v[i][0]).toLowerCase() === email && String(v[i][4]) === 'Agendado') return true;
  return false;
}

/* ===================== UTIL ===================== */

function lerJson_(e) {
  var b = (e && e.postData && e.postData.contents) ? e.postData.contents : '';
  try { return JSON.parse(b); } catch (x) { return (e && e.parameter) ? e.parameter : {}; }
}
function limpar_(v) { return (v === undefined || v === null) ? '' : String(v).replace(/[\r\n\t]+/g, ' ').trim().substring(0, 200); }
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

/** Rode uma vez para autorizar (agenda, planilha e e-mail). */
function autorizar() {
  CalendarApp.getDefaultCalendar().getName();
  SpreadsheetApp.openById(CFG.ID_PLANILHA).getName();
  MailApp.getRemainingDailyQuota();
  Logger.log('Permissões ok.');
}

/** Rode para ver os próximos horários que o site vai mostrar. */
function testarHorarios() {
  var s = horariosLivres_();
  Logger.log(s.length + ' horários livres. Primeiros:');
  for (var i = 0; i < Math.min(8, s.length); i++) Logger.log(Utilities.formatDate(new Date(s[i].ini), CFG.FUSO, 'EEE dd/MM HH:mm'));
}
