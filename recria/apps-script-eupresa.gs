/**
 * Recria · Recria EUpresa: alerta de nova contratação
 *
 * A página /eupresa-obrigado/ envia os dados da pessoa que acabou de pagar na Hotmart.
 * Este script salva a linha na aba "EUpresa - contratações" da planilha _CRM Central - Agência Recria
 * e envia um e-mail de aviso para amandarecria@gmail.com, com todos os dados para você chamar a pessoa.
 *
 * Instalação (mesmo processo do checklist):
 *  - script.google.com > Novo projeto > cole este código > Salvar.
 *  - Execute "autorizar" e aceite as permissões.
 *  - Implantar > Nova implantação > App da Web > Executar como: Eu > Acesso: Qualquer pessoa.
 *  - Copie a URL do app da Web e envie para a Claude colocar na página (window.EUPRESA.API).
 */
var ID_PLANILHA = '1kbRl6xxqbfggIk96TopOCHZE_ehaxKCHOcKtbloC3Gc';
var NOME_ABA = 'EUpresa - contratações';
var EMAIL_AVISO = 'amandarecria@gmail.com';
var CABECALHO = ['Data e hora', 'Nome', 'Negócio', 'WhatsApp', 'Link do WhatsApp', 'E-mail', 'Instagram', 'Período contratado', 'Verba por semana', 'Destino do anúncio', 'Observação', 'Situação'];

function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
    var d = lerDados_(e);
    var erro = validar_(d);
    if (erro) return resposta_({ ok: false, erro: erro });
    var aba = abaDestino_();
    var zap = soDigitos_(d.whatsapp);
    if (zap.length === 10 || zap.length === 11) zap = '55' + zap;
    aba.appendRow([new Date(), d.nome, d.negocio, d.whatsapp, zap ? 'https://wa.me/' + zap : '', d.email, d.instagram, d.plano, d.verba, d.destino, d.obs, 'Novo - chamar']);
    avisar_(d, zap);
    return resposta_({ ok: true });
  } catch (err) {
    return resposta_({ ok: false, erro: String(err) });
  } finally {
    try { lock.releaseLock(); } catch (x) {}
  }
}

function doGet() { return resposta_({ ok: true, mensagem: 'Recria EUpresa · captura no ar' }); }

function lerDados_(e) {
  var bruto = (e && e.postData && e.postData.contents) ? e.postData.contents : '';
  var d = {};
  try { d = JSON.parse(bruto); } catch (x) { d = (e && e.parameter) ? e.parameter : {}; }
  var o = {};
  ['nome', 'negocio', 'whatsapp', 'email', 'instagram', 'plano', 'verba', 'destino', 'obs'].forEach(function (k) { o[k] = limpar_(d[k]); });
  o.email = o.email.toLowerCase();
  return o;
}
function limpar_(v) { return (v === undefined || v === null) ? '' : String(v).replace(/[\r\n\t]+/g, ' ').trim().substring(0, 400); }
function soDigitos_(v) { return String(v || '').replace(/\D/g, ''); }
function validar_(d) {
  if (d.nome.length < 2) return 'nome inválido';
  if (d.negocio.length < 2) return 'negócio inválido';
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
    aba.getRange('D:D').setNumberFormat('@');
  }
  return aba;
}
function avisar_(d, zap) {
  var assunto = 'Você acabou de vender: Recria EUpresa (' + d.plano + ') · ' + d.negocio;
  var corpo =
    'Nova contratação do Recria EUpresa.\n\n' +
    'Nome: ' + d.nome + '\n' +
    'Negócio: ' + d.negocio + '\n' +
    'Instagram: ' + (d.instagram || 'não informado') + '\n' +
    'WhatsApp: ' + d.whatsapp + (zap ? '  (https://wa.me/' + zap + ')' : '') + '\n' +
    'E-mail: ' + d.email + '\n\n' +
    'Período contratado: ' + d.plano + '\n' +
    'Verba de anúncio: ' + d.verba + '\n' +
    'Levar as pessoas para: ' + d.destino + '\n' +
    'Observação: ' + (d.obs || '-') + '\n\n' +
    'Salvo na aba "' + NOME_ABA + '":\nhttps://docs.google.com/spreadsheets/d/' + ID_PLANILHA + '/edit';
  MailApp.sendEmail(EMAIL_AVISO, assunto, corpo);
}
function resposta_(obj) { return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON); }

function autorizar() { SpreadsheetApp.openById(ID_PLANILHA).getName(); MailApp.getRemainingDailyQuota(); Logger.log('Permissões ok.'); }
function testar() {
  var r = doPost({ postData: { contents: JSON.stringify({ nome: 'Teste Recria', negocio: 'Salão Teste', whatsapp: '(51) 99999-9999', email: 'teste@exemplo.com', instagram: '@teste', plano: '2 semanas', verba: 'R$ 75 por semana', destino: 'WhatsApp', obs: 'teste' }) } });
  Logger.log(r.getContent());
}
