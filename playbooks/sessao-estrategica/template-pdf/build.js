// Gera o direcional em PDF no padrão Recria.
// Uso: NOME="Nome do Cliente" node build.js
// Saída: capa.pdf (capa + contracapa) e miolo.pdf. Depois, rode merge.py.
const { chromium } = require('playwright');
const path = require('path');
const nome = process.env.NOME || '';

(async () => {
  const dir = __dirname;
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(dir, 'capa.html'), { waitUntil: 'networkidle' });
  await p.pdf({ path: path.join(dir, 'capa.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true });
  await p.goto('file://' + path.join(dir, 'miolo.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({
    path: path.join(dir, 'miolo.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: `<div style="width:100%;font-family:Georgia,serif;font-size:7.5pt;color:#8a6a24;display:flex;justify-content:space-between;border-top:0.6pt solid #C9A24E;margin:0 20mm;padding-top:5px;">
      <span>Instagram @agencia.recria · agenciarecria.com.br/links</span><span>Direcional · ${nome} · <span class="pageNumber"></span></span></div>`
  });
  await b.close();
})();
