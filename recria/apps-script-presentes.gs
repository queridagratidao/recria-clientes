/**
 * Recria · Captura dos materiais gratuitos (presentes)
 *
 * Um único script atende as páginas de captura e manda cada lead para a planilha do material certo:
 *  - Checklist Instagram            -> planilha "Checklist IG isca digital"
 *  - Checklist Venda sem Parecer Chato -> planilha "checklist-venda-sem-parecer-chato- isca digital"
 *  - Direcional de Marketing        -> planilha "Direcional de mkt e negocio - - isca digital"
 *  - Checklist Black Friday         -> (provisório) aba do CRM, até a planilha própria existir
 * Cada lead vira uma linha com a coluna "Material baixado", e um e-mail de aviso chega em amandarecria@gmail.com.
 *
 * Como instalar: script.google.com > Novo projeto > cole este código > Salvar.
 * Rode a função "autorizar" uma vez e aceite as permissões.
 * Implantar > Nova implantação > Tipo: App da Web > Executar como: Eu > Quem pode acessar: Qualquer pessoa.
 * Copie o URL do app da Web e envie para a Claude colocar nas páginas.
 */

// Para onde vai cada material. Para a Black Friday, quando criar a planilha dela, troque o "id" abaixo.
var PROVISORIO = { id: '1kbRl6xxqbfggIk96TopOCHZE_ehaxKCHOcKtbloC3Gc', aba: 'Checklist IG isca digital' }; // _CRM Central (aba antiga)
var DESTINOS = {
  'Checklist Instagram': { id: '1YsU2_zv4IK2qEyCXSitvNKBAwrVBiVqr1Z7GNaQ5ME4', aba: 'Leads' },
  'Checklist Venda sem Parecer Chato': { id: '19UW2CztDNRGLg5JFc7vW1TH_SjdLguhkM7ru4v4xklA', aba: 'Leads' },
  'Direcional de Marketing': { id: '1OxPIoQrFA0BArkwV7Xfa5WjcspGBFn8DbxTemFy1omg', aba: 'Leads' },
  'Checklist Black Friday': PROVISORIO
};
var EMAIL_AVISO = 'amandarecria@gmail.com';
var CABECALHO = ['Data e hora', 'Nome', 'WhatsApp', 'Link do WhatsApp', 'E-mail', 'Origem (canal)', 'Origem (utm)', 'Página', 'Situação', 'Material baixado'];

function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
    var d = lerDados_(e);
    var erro = validar_(d);
    if (erro) return resposta_({ ok: false, erro: erro });

    var material = material_(d);
    var dest = DESTINOS[material] || PROVISORIO;
    var aba = abaDestino_(dest);
    var situacao = jaBaixou_(aba, d.email, material) ? 'Repetido' : 'Novo';
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
      situacao,
      material
    ]);

    if (situacao === 'Novo') avisar_(d, zap, material, dest);
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

function abaDestino_(dest) {
  var planilha = SpreadsheetApp.openById(dest.id);
  var aba = planilha.getSheetByName(dest.aba);
  if (!aba) {
    var todas = planilha.getSheets();
    if (todas.length === 1 && todas[0].getLastRow() === 0) {
      aba = todas[0];
      aba.setName(dest.aba);
    } else {
      aba = planilha.insertSheet(dest.aba);
    }
  }
  if (aba.getLastRow() === 0) {
    aba.appendRow(CABECALHO);
    aba.getRange(1, 1, 1, CABECALHO.length).setFontWeight('bold').setBackground('#f3e9cf');
    aba.setFrozenRows(1);
    aba.getRange('A:A').setNumberFormat('dd/MM/yyyy HH:mm');
    aba.getRange('C:C').setNumberFormat('@');
  }
  if (aba.getLastRow() > 0 && !aba.getRange(1, CABECALHO.length).getValue()) {
    aba.getRange(1, CABECALHO.length).setValue(CABECALHO[CABECALHO.length - 1]).setFontWeight('bold').setBackground('#f3e9cf');
  }
  return aba;
}

/** Descobre qual material a pessoa baixou: pelo campo "momento" que a página envia, ou pelo endereço da página. */
function material_(d) {
  var m = String(d.momento || '').replace(/\s*-\s*Captura\s*$/i, '').trim();
  return m || materialPelaPagina_(d.pagina);
}

function materialPelaPagina_(pagina) {
  var p = String(pagina || '').toLowerCase();
  if (p.indexOf('checklist-bf') > -1) return 'Checklist Black Friday';
  if (p.indexOf('direcional-marketing') > -1) return 'Direcional de Marketing';
  if (p.indexOf('venda-sem-parecer-chato') > -1) return 'Checklist Venda sem Parecer Chato';
  if (p.indexOf('checklist-instagram') > -1) return 'Checklist Instagram';
  return 'Não identificado';
}

/** "Repetido" = mesmo e-mail pedindo o mesmo material de novo. Outro material do mesmo e-mail conta como Novo. */
function jaBaixou_(aba, email, material) {
  var ultima = aba.getLastRow();
  if (ultima < 2) return false;
  var n = CABECALHO.length;
  var linhas = aba.getRange(2, 1, ultima - 1, n).getValues();
  for (var i = 0; i < linhas.length; i++) {
    if (String(linhas[i][4]).toLowerCase() !== email) continue;
    var m = String(linhas[i][n - 1] || '').trim() || materialPelaPagina_(linhas[i][7]);
    if (m === material) return true;
  }
  return false;
}

function avisar_(d, zap, material, dest) {
  var assunto = 'Novo lead: ' + material;
  var corpo =
    'Entrou uma pessoa nova para baixar: ' + material + '.\n\n' +
    'Nome: ' + d.nome + '\n' +
    'WhatsApp: ' + d.whatsapp + (zap ? '  (https://wa.me/' + zap + ')' : '') + '\n' +
    'E-mail: ' + d.email + '\n' +
    'Origem: ' + (d.canal || 'não informada') + (d.utm ? ' | ' + d.utm : '') + '\n\n' +
    'Ela já foi salva na aba "' + dest.aba + '" da planilha deste material:\n' +
    'https://docs.google.com/spreadsheets/d/' + dest.id + '/edit';
  MailApp.sendEmail(EMAIL_AVISO, assunto, corpo);
}

function resposta_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

/* ---------- utilitários para você ---------- */

/** Rode uma vez para autorizar as permissões (planilha e e-mail). */
function autorizar() {
  var ids = {};
  Object.keys(DESTINOS).forEach(function (k) { ids[DESTINOS[k].id] = true; });
  Object.keys(ids).forEach(function (id) { Logger.log(SpreadsheetApp.openById(id).getName()); });
  MailApp.getRemainingDailyQuota();
  Logger.log('Permissões ok.');
}

/** Rode para testar: cria uma linha de teste na planilha do Direcional e manda o e-mail de aviso. Depois apague a linha de teste. */
function testar() {
  var e = { postData: { contents: JSON.stringify({
    nome: 'Teste Recria',
    whatsapp: '(51) 99999-9999',
    email: 'teste+' + new Date().getTime() + '@exemplo.com',
    canal: 'Teste',
    utm: 'utm_source=teste',
    pagina: 'https://www.agenciarecria.com.br/direcional-marketing/',
    momento: 'Direcional de Marketing - Captura'
  }) } };
  var r = doPost(e);
  Logger.log(r.getContent());
}
