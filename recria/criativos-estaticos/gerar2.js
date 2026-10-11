const {chromium}=require('/opt/node-tools/node_modules/playwright');const fs=require('fs');
const D=__dirname;const F="file:///home/user/recria-clientes/recria/ebooks/_base/fonts/";
const ICON="file:///home/user/-site-institucional-recria/assets/icone.png";
const FORMATS={
 'feed-1x1':{w:1080,h:1080,pad:'64px 76px 60px',ic:62,k:22,kmt:26,h1:[84,50],s:[34,24],pill:32,cta:34,ctap:22,gap:20},
 'stories-9x16':{w:1080,h:1920,pad:'270px 84px 350px',ic:92,k:28,kmt:70,h1:[112,64],s:[42,30],pill:40,cta:44,ctap:30,gap:30}
};
function css(f){return `
@font-face{font-family:'Lora';font-weight:400;src:url(${F}lora-latin-400-normal.woff2)}
@font-face{font-family:'Playfair Display';font-weight:700;font-style:normal;src:url(${F}playfair-display-latin-700-normal.woff2)}
@font-face{font-family:'Playfair Display';font-weight:700;font-style:italic;src:url(${F}playfair-display-latin-700-italic.woff2)}
*{box-sizing:border-box;margin:0}
html,body{width:${f.w}px;height:${f.h}px;background:#0b0b0b}
.c{position:relative;width:${f.w}px;height:${f.h}px;background:radial-gradient(circle at 20% 0%,#2b2112 0%,#0b0b0b 65%);color:#fff;font-family:'Lora',serif;padding:${f.pad};display:flex;flex-direction:column;overflow:hidden}
.bd{position:absolute;inset:0;border:3px solid #C9A24E;outline:16px solid #0b0b0b;outline-offset:-19px;pointer-events:none}
.ic{width:${f.ic}px}
.k{margin-top:${f.kmt}px;letter-spacing:.22em;font-size:${f.k}px;color:#C9A24E;text-transform:uppercase}
h1{font-family:'Playfair Display',serif;font-weight:700;font-size:${f.h1[0]}px;line-height:1.08;margin-top:${f.gap}px}
h1 em{color:#E4C988}
.s{font-size:${f.s[0]}px;line-height:1.4;color:#e9e4da;margin-top:${f.gap+6}px}
.b{margin-top:auto;padding-top:${f.gap}px}
.p{display:inline-block;border:2px solid #C9A24E;color:#E4C988;font-family:'Playfair Display',serif;font-size:${f.pill}px;padding:8px 22px;border-radius:8px;margin-bottom:${f.gap}px}
.cta{background:#C9A24E;color:#0b0b0b;font-weight:700;font-size:${f.cta}px;text-align:center;padding:${f.ctap}px;border-radius:10px;letter-spacing:.02em}
`;}
function html(it,f){const [n,k,h,s,p,c]=it;
 return `<!doctype html><meta charset="utf-8"><style>${css(f)}</style><div class="c"><img class="ic" src="${ICON}"><div class="k">${k}</div><h1>${h}</h1><div class="s">${s}</div><div class="b">${p?`<div class="p">${p}</div>`:''}<div class="cta">${c}</div></div><div class="bd"></div></div>`;}
(async()=>{const items=JSON.parse(fs.readFileSync(D+'/criativos.json','utf8'));
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const [fn,f] of Object.entries(FORMATS)){fs.mkdirSync(`${D}/${fn}`,{recursive:true});
 const pg=await b.newPage({viewport:{width:f.w,height:f.h}});
 for(const it of items){fs.writeFileSync(D+'/_t.html',html(it,f));await pg.goto('file://'+D+'/_t.html');await pg.evaluate(()=>document.fonts.ready);
  const r=await pg.evaluate(([h1max,h1min,smax,smin])=>{const c=document.querySelector('.c'),h=document.querySelector('h1'),s=document.querySelector('.s');
   let a=h1max,bb=smax;const over=()=>c.scrollHeight>c.clientHeight+1;
   while(over()&&a>h1min){a-=2;h.style.fontSize=a+'px';if(over()&&bb>smin&&a<h1max-10){bb-=1;s.style.fontSize=bb+'px';}}
   while(over()&&bb>smin){bb-=1;s.style.fontSize=bb+'px';}
   return [a,bb,over()];},[f.h1[0],f.h1[1],f.s[0],f.s[1]]);
  if(r[2])console.log('OVERFLOW',fn,it[0],r);
  await pg.screenshot({path:`${D}/${fn}/${it[0]}.png`});}
 await pg.close();}
fs.unlinkSync(D+'/_t.html');await b.close();console.log('ok');})();
