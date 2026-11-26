// node compose.js [names...] — custom-layout posts rendered to dez/out/<slug>/card-01.png
const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-claude/b2736a22-a7a5-5ef9-a4fc-d023deb3f6f7/scratchpad';const F=S+'/fonts/node_modules/@fontsource/';const I=S+'/feed-dez/img/';
const BASE=`@font-face{font-family:CP;font-weight:400;src:url(${F}courier-prime/files/courier-prime-latin-400-normal.woff2)}@font-face{font-family:CP;font-weight:700;src:url(${F}courier-prime/files/courier-prime-latin-700-normal.woff2)}
@font-face{font-family:Q;font-weight:600;src:url(${F}quicksand/files/quicksand-latin-600-normal.woff2)}@font-face{font-family:Q;font-weight:700;src:url(${F}quicksand/files/quicksand-latin-700-normal.woff2)}
*{box-sizing:border-box}body{margin:0}.c{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:CP;color:#5A1042;background:#FCEAF1}
.hl{display:inline-block;white-space:nowrap;background:#A71874;color:#fff;font-weight:700;padding:2px 14px;border-radius:8px}
.sig{position:absolute;left:0;right:0;text-align:center;color:#A71874;font:700 22px CP}
.pill{display:inline-block;background:#A71874;color:#fff;font:700 24px CP;letter-spacing:.06em;padding:8px 22px;border-radius:30px}`;
const P={
'11-12':`<style>.top{position:absolute;left:0;right:0;top:0;height:430px;background:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 70px;gap:26px;font-size:42px;line-height:1.3;font-weight:700}
.im{position:absolute;left:0;right:0;top:430px;bottom:0;background:url(${I}ia-gatos.jpg) center 40%/cover}.sig{top:30px}</style>
<div class="top"><div>Eu: "só entra gente doida<br>na minha vida"</div><div>Minha psicóloga:<br>"e quem é que <span class="hl">abre a porta</span>?"</div></div><div class="im"></div><span class="sig">@psicamilasartori</span>`,
'23-12':`<style>.im{position:absolute;inset:0;background:url(${I}ia-chihuahua.jpg) center bottom/cover}
.t{position:absolute;left:50px;right:50px;top:50px;text-align:center;display:flex;flex-direction:column;gap:20px;font-size:36px;line-height:1.3;background:rgba(255,255,255,.88);border-radius:28px;padding:34px 30px}.t b{font-size:41px}.sig{bottom:28px;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.35)}</style>
<div class="im"></div><div class="t"><b>Gostaria de ser removida do programa "O que não te mata te fortalece"</b><div>Já concluí o curso, fiz as provas e aprendi as lições</div><div>Agora quero entrar no programa de paz, tranquilidade e <span class="hl">coisas boas</span></div></div><span class="sig">@psicamilasartori</span>`,
'FIXO_3':`<style>.tagw{position:absolute;top:44px;left:0;right:0;text-align:center}.tagw .pill{font-size:23px;padding:10px 24px}
.im{position:absolute;left:0;right:0;top:118px;height:610px;background:url(${I}ia-cha.jpg) center 35%/cover}
.t{position:absolute;left:70px;right:70px;top:760px;bottom:80px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:26px}
.a{font-weight:700;font-size:38px;line-height:1.3}.b{font-size:31px;line-height:1.3}.bl{display:flex;gap:14px;flex-wrap:wrap;justify-content:center}.bl span{background:#fff;border:2px solid #E07A9A;color:#A71874;font:700 25px CP;padding:8px 18px;border-radius:24px}
.e{font-size:29px;font-weight:700}.sig{bottom:30px}</style>
<div class="tagw"><span class="pill">COMUNIDADE DE AUTOCONHECIMENTO PARA MULHERES</span></div><div class="im"></div>
<div class="t"><div class="a">Se conheça mais, entenda os seus padrões, aprenda a colocar limites e construa relações mais saudáveis</div><div class="b">consigo mesma, no amor, no trabalho, com a família e com os amigos</div>
<div class="bl"><span>Aulas rápidas</span><span>Atividades práticas</span><span>Acompanhamento em grupo</span></div><div class="e">7 dias de garantia · <span class="hl">link na bio</span></div></div><span class="sig">@psicamilasartori</span>`,
'FIXO_2':`<style>.im{position:absolute;left:0;right:0;top:0;height:720px;background:url(${I}poltrona.jpg) center 30%/cover}
.fd{position:absolute;left:0;right:0;top:560px;height:170px;background:linear-gradient(180deg,rgba(252,234,241,0),#FCEAF1)}
.t{position:absolute;left:70px;right:70px;top:690px;bottom:80px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:20px}
.h{font:700 50px/1.15 Q;color:#A71874}.b{font-size:30px;line-height:1.3}.c2{font-size:31px;line-height:1.3;font-weight:700}.sig{bottom:30px}</style>
<div class="im"></div><div class="fd"></div><div class="t"><span class="pill">VAGAS ABERTAS</span><div class="h">Psicoterapia individual online</div>
<div class="b">Abordagens: TCC e Terapia do Esquema<br>com a psicóloga Camila Sartori, mestre em Psicologia Clínica e doutoranda em Psicologia</div>
<div class="c2">Quer saber mais? Comente <span class="hl">TERAPIA</span><br>ou fale comigo pelo link da bio</div></div><span class="sig">@psicamilasartori</span>`
};
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1080,height:1350}});
for(const n of (process.argv.slice(2).length?process.argv.slice(2):Object.keys(P))){
 const f=S+'/dez/_c.html';fs.writeFileSync(f,`<html><head><meta charset="utf-8"><style>${BASE}</style></head><body><div class="c">${P[n]}</div></body></html>`);
 await pg.goto('file://'+f,{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);
 const o=S+'/dez/out/'+n;fs.rmSync(o,{recursive:true,force:true});fs.mkdirSync(o,{recursive:true});
 await pg.screenshot({path:o+'/card-01.png',clip:{x:0,y:0,width:1080,height:1350}});}
await b.close()})();
