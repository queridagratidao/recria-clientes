/**
 * Recria · Captura do Checklist de Revisão do Instagram
 *
 * O que faz:
 *  1) Recebe os dados da página /checklist-instagram/ (nome, WhatsApp e e-mail);
 *  2) Salva uma linha na aba "Checklist IG isca digital" da planilha _CRM Central - Agência Recria;
 *  3) Envia um e-mail de aviso para amandarecria@gmail.com.
 *
 * Como instalar (resumo; o passo a passo completo está no chat):
 *  - Abra a planilha > Extensões > Apps Script > cole este código no lugar do que estiver lá > Salvar.
 *  - Execute a função "autorizar" uma vez e aceite as permissões.
 *  - Implantar > Nova implantação > Tipo: App da Web > Executar como: Eu > Quem pode acessar: Qualquer pessoa.
 *  - Copie o URL do app da Web e envie para a Claude colocar na página.
 */

var ID_PLANILHA = '1kbRl6xxqbfggIk96TopOCHZE_ehaxKCHOcKtbloC3Gc';
var NOME_ABA = 'Checklist IG isca digital';
var EMAIL_AVISO = 'amandarecria@gmail.com';
var CABECALHO = ['Data e hora', 'Nome', 'WhatsApp', 'Link do WhatsApp', 'E-mail', 'Origem (canal)', 'Origem (utm)', 'Página', 'Situação'];

function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
    var d = lerDados_(e);
    var erro = validar_(d);
    if (erro) return resposta_({ ok: false, erro: erro });

    var aba = abaDestino_();
    var situacao = emailJaExiste_(aba, d.email) ? 'Repetido' : 'Novo';
    var zap = soDigitos_(d.whatsapp);
    if (zap.length === 10 || zap.length === 11) zap = '55' + zap;

    aba.appendRow([
      new Date(),
      d.nome,
      d.whatsapp,
      zap ? 'https://wa.me/' + zap : '',
      d.email,
      d.canal || '',
      d.utm || '',
      d.pagina || '',
      situacao
    ]);

    if (situacao === 'Novo') avisar_(d, zap);
    return resposta_({ ok: true });
  } catch (err) {
    return resposta_({ ok: false, erro: String(err) });
  } finally {
    try { lock.releaseLock(); } catch (x) {}
  }
}

function doGet() {
  return resposta_({ ok: true, mensagem: 'Recria · captura do checklist no ar' });
}

/* ---------- apoio ---------- */

function lerDados_(e) {
  var bruto = (e && e.postData && e.postData.contents) ? e.postData.contents : '';
  var d = {};
  try { d = JSON.parse(bruto); } catch (x) { d = (e && e.parameter) ? e.parameter : {}; }
  return {
    nome: limpar_(d.nome),
    whatsapp: limpar_(d.whatsapp),
    email: limpar_(d.email).toLowerCase(),
    canal: limpar_(d.canal),
    utm: limpar_(d.utm),
    pagina: limpar_(d.pagina),
    momento: limpar_(d.momento)
  };
}

function limpar_(v) {
  return (v === undefined || v === null) ? '' : String(v).replace(/[\r\n\t]+/g, ' ').trim().substring(0, 300);
}

function soDigitos_(v) {
  return String(v || '').replace(/\D/g, '');
}

function validar_(d) {
  if (d.nome.length < 2) return 'nome inválido';
  var z = soDigitos_(d.whatsapp);
  if (z.indexOf('55') === 0 && z.length > 11) z = z.substring(2);
  if (z.length < 10 || z.length > 11) return 'whatsapp inválido';
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(d.email)) return 'e-mail inválido';
  return '';
}

function abaDestino_() {
  var planilha = SpreadsheetApp.openById(ID_PLANILHA);
  var aba = planilha.getSheetByName(NOME_ABA);
  if (!aba) aba = planilha.insertSheet(NOME_ABA);
  if (aba.getLastRow() === 0) {
    aba.appendRow(CABECALHO);
    aba.getRange(1, 1, 1, CABECALHO.length).setFontWeight('bold').setBackground('#f3e9cf');
    aba.setFrozenRows(1);
    aba.getRange('A:A').setNumberFormat('dd/MM/yyyy HH:mm');
    aba.getRange('C:C').setNumberFormat('@');
  }
  return aba;
}

function emailJaExiste_(aba, email) {
  var ultima = aba.getLastRow();
  if (ultima < 2) return false;
  var emails = aba.getRange(2, 5, ultima - 1, 1).getValues();
  for (var i = 0; i < emails.length; i++) {
    if (String(emails[i][0]).toLowerCase() === email) return true;
  }
  return false;
}

function avisar_(d, zap) {
  var assunto = 'Novo lead: Checklist de Revisão do Instagram';
  var corpo =
    'Entrou uma pessoa nova para baixar o Checklist de Revisão do Instagram.\n\n' +
    'Nome: ' + d.nome + '\n' +
    'WhatsApp: ' + d.whatsapp + (zap ? '  (https://wa.me/' + zap + ')' : '') + '\n' +
    'E-mail: ' + d.email + '\n' +
    'Origem: ' + (d.canal || 'não informada') + (d.utm ? ' | ' + d.utm : '') + '\n\n' +
    'Ela já foi salva na aba "' + NOME_ABA + '" da planilha _CRM Central - Agência Recria:\n' +
    'https://docs.google.com/spreadsheets/d/' + ID_PLANILHA + '/edit';
  MailApp.sendEmail(EMAIL_AVISO, assunto, corpo);
}

function resposta_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

/* ---------- utilitários para você ---------- */

/** Rode uma vez para autorizar as permissões (planilha e e-mail). */
function autorizar() {
  SpreadsheetApp.openById(ID_PLANILHA).getName();
  MailApp.getRemainingDailyQuota();
  Logger.log('Permissões ok.');
}

/** Rode para testar: cria uma linha de teste e manda o e-mail de aviso. Depois apague a linha de teste. */
function testar() {
  var e = { postData: { contents: JSON.stringify({
    nome: 'Teste Recria',
    whatsapp: '(51) 99999-9999',
    email: 'teste+' + new Date().getTime() + '@exemplo.com',
    canal: 'Teste',
    utm: 'utm_source=teste',
    pagina: 'https://www.agenciarecria.com.br/checklist-instagram/',
    momento: 'Checklist Instagram - Captura'
  }) } };
  var r = doPost(e);
  Logger.log(r.getContent());
}
