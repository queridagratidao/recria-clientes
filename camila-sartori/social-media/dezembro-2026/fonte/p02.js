const {chromium}=require('playwright');const S='/tmp/claude-0/-home-claude/b2736a22-a7a5-5ef9-a4fc-d023deb3f6f7/scratchpad';const F=S+'/fonts/node_modules/@fontsource/';
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
require('fs').writeFileSync(S+'/dez/p02.html',`<html><head><meta charset="utf-8"><style>
@font-face{font-family:CP;font-weight:400;src:url(${F}courier-prime/files/courier-prime-latin-400-normal.woff2)}@font-face{font-family:CP;font-weight:700;src:url(${F}courier-prime/files/courier-prime-latin-700-normal.woff2)}
body{margin:0}.c{position:relative;width:1080px;height:1350px;background:url(${S}/feed-dez/img/ia-multi.jpg) center/cover;font-family:CP;color:#5A1042}
.tag{position:absolute;bottom:26px;left:50%;transform:translateX(-50%);color:#A71874;font:700 22px CP}
.t{position:absolute;left:70px;right:70px;top:950px;bottom:70px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:16px}
.a{font-weight:700;font-size:44px;line-height:1.25}.b{font-size:36px;line-height:1.3}.hl{display:inline-block;white-space:nowrap;background:#A71874;color:#fff;font-weight:700;padding:2px 14px;border-radius:8px;margin-top:6px}
</style></head><body><div class="c"><span class="tag">@psicamilasartori</span><div class="t"><div class="a">Você pode fazer tudo<br>Você só não pode fazer<br><span class="hl">tudo ao mesmo tempo</span></div><div class="b">minha florzinha proativa,<br>multitarefada e ansiosa</div></div></div></body></html>`);
await p.goto('file://'+S+'/dez/p02.html',{waitUntil:'load'});await p.evaluate(()=>document.fonts.ready);
await p.screenshot({path:S+'/dez/out/02-12/card-01.png',clip:{x:0,y:0,width:1080,height:1350}});await b.close()})();
