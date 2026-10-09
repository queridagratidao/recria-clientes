const {chromium}=require('/opt/node-tools/node_modules/playwright');const fs=require('fs');
const D=__dirname;const F="file:///home/user/recria-clientes/recria/ebooks/_base/fonts/";
const ICON="file:///home/user/-site-institucional-recria/assets/icone.png";
const CSS=`
@font-face{font-family:'Lora';font-weight:400;src:url(${F}lora-latin-400-normal.woff2)}
@font-face{font-family:'Playfair Display';font-weight:700;font-style:normal;src:url(${F}playfair-display-latin-700-normal.woff2)}
@font-face{font-family:'Playfair Display';font-weight:700;font-style:italic;src:url(${F}playfair-display-latin-700-italic.woff2)}
*{box-sizing:border-box;margin:0}
html,body{width:1080px;height:1350px;background:#0b0b0b}
.c{position:relative;width:1080px;height:1350px;background:radial-gradient(circle at 20% 0%,#2b2112 0%,#0b0b0b 65%);border:3px solid #C9A24E;outline:16px solid #0b0b0b;outline-offset:-19px;color:#fff;font-family:'Lora',serif;padding:90px 90px 80px;display:flex;flex-direction:column}
.ic{width:92px}
.k{margin-top:70px;letter-spacing:.24em;font-size:27px;color:#C9A24E;text-transform:uppercase}
h1{font-family:'Playfair Display',serif;font-weight:700;font-size:@@SIZE@@px;line-height:1.08;margin-top:28px}
h1 em{color:#E4C988}
.s{font-size:37px;line-height:1.42;color:#e9e4da;margin-top:40px}
.b{margin-top:auto}
.p{display:inline-block;border:2px solid #C9A24E;color:#E4C988;font-family:'Playfair Display',serif;font-size:40px;padding:10px 26px;border-radius:8px;margin-bottom:26px}
.cta{background:#C9A24E;color:#0b0b0b;font-weight:700;font-size:40px;text-align:center;padding:30px;border-radius:10px;letter-spacing:.02em}
.f{margin-top:26px;text-align:center;font-size:24px;letter-spacing:.2em;color:#9d927c}
`;
const items=JSON.parse(fs.readFileSync(D+'/criativos.json','utf8'));
function html(it){const [n,k,h,s,p,c]=it;const t=h.replace(/<[^>]*>/g,"").length;const SIZE=t<40?112:t<58?98:t<75?84:t<100?74:66;
 const css=CSS.replace("@@SIZE@@",SIZE);
 return `<!doctype html><meta charset="utf-8"><style>${css}</style><div class="c"><img class="ic" src="${ICON}"><div class="k">${k}</div><h1>${h}</h1><div class="s" style="font-size:${s.length>200?31:s.length>150?34:37}px">${s}</div><div class="b">${p?`<div class="p">${p}</div>`:''}<div class="cta">${c}</div></div></div>`;}
(async()=>{fs.mkdirSync(D+'/png',{recursive:true});const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const pg=await b.newPage({viewport:{width:1080,height:1350}});
for(const it of items){fs.writeFileSync(D+'/_t.html',html(it));await pg.goto('file://'+D+'/_t.html');await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(300);await pg.screenshot({path:D+'/png/'+it[0]+'.png'});}
fs.unlinkSync(D+'/_t.html');await b.close();console.log(items.length);})();
