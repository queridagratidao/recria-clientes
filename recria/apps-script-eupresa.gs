/**
 * Recria · Recria EUpresa: formulários (compra, contrato de 3/6/12 meses e site)
 *
 * Um único app da Web recebe os 3 formulários do site, pelo campo "tipo":
 *  - compra   → página /eupresa-obrigado/   (aba "EUpresa - contratações")
 *  - contrato → página /eupresa-contrato/   (aba "EUpresa - contratos 3-6-12 meses")
 *  - site     → página /eupresa-site/       (aba "EUpresa - site")
 * Cada envio salva uma linha na planilha _CRM Central - Agência Recria e manda um e-mail de aviso para amandarecria@gmail.com.
 *
 * Instalação (mesmo processo do checklist):
 *  - Abra a planilha _CRM Central - Agência Recria > Extensões > Apps Script > Novo projeto (ou crie em script.google.com) > cole este código > Salvar.
 *  - Execute "prepararAbas" para criar as 3 abas na planilha.
 *  - Execute "autorizar" e aceite as permissões.
 *  - Implantar > Nova implantação (ou Gerenciar implantações > editar > Nova versão) > App da Web > Executar como: Eu > Acesso: Qualquer pessoa.
 *  - Copie a URL do app da Web e envie para a Claude colocar nas páginas.
 */
var ID_PLANILHA = '1kbRl6xxqbfggIk96TopOCHZE_ehaxKCHOcKtbloC3Gc';
var EMAIL_AVISO = 'amandarecria@gmail.com';

var FORMS = {
  compra: {
    aba: 'EUpresa - contratações',
    campos: ['nome', 'negocio', 'whatsapp', 'email', 'instagram', 'plano', 'verba', 'destino', 'obs'],
    cab: ['Data e hora', 'Nome', 'Negócio', 'WhatsApp', 'Link do WhatsApp', 'E-mail', 'Instagram', 'Período contratado', 'Verba por semana', 'Destino do anúncio', 'Observação', 'Situação'],
    obrig: ['nome', 'negocio', 'whatsapp', 'email', 'plano', 'verba', 'destino'],
    assunto: function (d) { return 'Você acabou de vender: Recria EUpresa (' + d.plano + ') · ' + d.negocio; }
  },
  contrato: {
    aba: 'EUpresa - contratos 3-6-12 meses',
    campos: ['nome', 'email', 'whatsapp', 'nicho', 'prazo', 'dor'],
    cab: ['Data e hora', 'Nome', 'E-mail', 'WhatsApp', 'Link do WhatsApp', 'Nicho / negócio', 'Prazo de interesse', 'Principal dor hoje', 'Situação'],
    obrig: ['nome', 'email', 'whatsapp', 'nicho', 'dor'],
    assunto: function (d) { return 'Lead: contrato de 3, 6 ou 12 meses · ' + d.nome + ' (' + d.nicho + ')'; }
  },
  site: {
    aba: 'EUpresa - site',
    campos: ['nome', 'email', 'whatsapp', 'nicho', 'funcoes', 'motivo'],
    cab: ['Data e hora', 'Nome', 'E-mail', 'WhatsApp', 'Link do WhatsApp', 'Nicho / negócio', 'O que o site deve fazer', 'Por que precisa de um site', 'Situação'],
    obrig: ['nome', 'email', 'whatsapp', 'nicho', 'motivo'],
    assunto: function (d) { return 'Lead: site por R$ 2.000 em 12x · ' + d.nome + ' (' + d.nicho + ')'; }
  }
};

function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
    var bruto = (e && e.postData && e.postData.contents) ? e.postData.contents : '';
    var raw = {};
    try { raw = JSON.parse(bruto); } catch (x) { raw = (e && e.parameter) ? e.parameter : {}; }
    var tipo = limpar_(raw.tipo) || 'compra';
    var f = FORMS[tipo];
    if (!f) return resposta_({ ok: false, erro: 'tipo inválido' });
    var d = {};
    f.campos.forEach(function (k) { d[k] = limpar_(raw[k]); });
    d.email = (d.email || '').toLowerCase();
    var erro = validar_(d, f.obrig);
    if (erro) return resposta_({ ok: false, erro: erro });

    var zap = soDigitos_(d.whatsapp);
    if (zap.length === 10 || zap.length === 11) zap = '55' + zap;
    var aba = abaDestino_(f);
    var linha = [new Date()];
    f.campos.forEach(function (k) {
      linha.push(d[k]);
      if (k === 'whatsapp') linha.push(zap ? 'https://wa.me/' + zap : '');
    });
    linha.push('Novo - chamar');
    aba.appendRow(linha);
    avisar_(f, d, zap, tipo);
    return resposta_({ ok: true });
  } catch (err) {
    return resposta_({ ok: false, erro: String(err) });
  } finally {
    try { lock.releaseLock(); } catch (x) {}
  }
}

function doGet() { return resposta_({ ok: true, mensagem: 'Recria EUpresa · formulários no ar' }); }

function limpar_(v) { return (v === undefined || v === null) ? '' : String(v).replace(/[\r\n\t]+/g, ' ').trim().substring(0, 800); }
function soDigitos_(v) { return String(v || '').replace(/\D/g, ''); }

function validar_(d, obrig) {
  for (var i = 0; i < obrig.length; i++) { if (!d[obrig[i]] || d[obrig[i]].length < 2) return 'campo obrigatório: ' + obrig[i]; }
  var z = soDigitos_(d.whatsapp);
  if (z.indexOf('55') === 0 && z.length > 11) z = z.substring(2);
  if (z.length < 10 || z.length > 11) return 'whatsapp inválido (use com DDD)';
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(d.email)) return 'e-mail inválido';
  return '';
}

function abaDestino_(f) {
  var planilha = SpreadsheetApp.openById(ID_PLANILHA);
  var aba = planilha.getSheetByName(f.aba);
  if (!aba) aba = planilha.insertSheet(f.aba);
  if (aba.getLastRow() === 0) {
    aba.appendRow(f.cab);
    aba.getRange(1, 1, 1, f.cab.length).setFontWeight('bold').setBackground('#f3e9cf');
    aba.setFrozenRows(1);
    aba.getRange('A:A').setNumberFormat('dd/MM/yyyy HH:mm');
  }
  return aba;
}

function avisar_(f, d, zap, tipo) {
  var linhas = [];
  f.campos.forEach(function (k, i) { linhas.push(f.cab[1 + i + (f.campos.indexOf('whatsapp') < i ? 1 : 0)] + ': ' + (d[k] || '-')); });
  var corpo = 'Novo envio (' + tipo + ').\n\n' + linhas.join('\n') +
    (zap ? '\n\nChamar no WhatsApp: https://wa.me/' + zap : '') +
    '\n\nSalvo na aba "' + f.aba + '":\nhttps://docs.google.com/spreadsheets/d/' + ID_PLANILHA + '/edit';
  MailApp.sendEmail(EMAIL_AVISO, f.assunto(d), corpo);
}

function resposta_(obj) { return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON); }

/** Cria agora as 3 abas (com cabeçalho) na planilha _CRM Central, sem esperar o primeiro envio. Rode uma vez. */
function prepararAbas() { Object.keys(FORMS).forEach(function (k) { abaDestino_(FORMS[k]); }); Logger.log('Abas criadas na planilha.'); }

function autorizar() { SpreadsheetApp.openById(ID_PLANILHA).getName(); MailApp.getRemainingDailyQuota(); Logger.log('Permissões ok.'); }

/** Testes: rode cada um e confira a planilha e o e-mail. Depois apague as linhas de teste. */
function testarCompra() { Logger.log(doPost({ postData: { contents: JSON.stringify({ tipo: 'compra', nome: 'Teste Recria', negocio: 'Salão Teste', whatsapp: '(51) 99999-9999', email: 'teste@exemplo.com', instagram: '@teste', plano: '2 semanas', verba: 'R$ 75 por semana', destino: 'WhatsApp', obs: 'teste' }) } }).getContent()); }
function testarContrato() { Logger.log(doPost({ postData: { contents: JSON.stringify({ tipo: 'contrato', nome: 'Teste Recria', email: 'teste@exemplo.com', whatsapp: '(51) 99999-9999', nicho: 'Salão de beleza', prazo: '6 meses', dor: 'Poucos clientes novos' }) } }).getContent()); }
function testarSite() { Logger.log(doPost({ postData: { contents: JSON.stringify({ tipo: 'site', nome: 'Teste Recria', email: 'teste@exemplo.com', whatsapp: '(51) 99999-9999', nicho: 'Clínica', funcoes: 'Receber contatos; Agendar', motivo: 'Não tenho onde mostrar meus serviços' }) } }).getContent()); }
