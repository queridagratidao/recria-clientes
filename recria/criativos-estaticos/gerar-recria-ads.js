const {chromium}=require('/opt/node-tools/node_modules/playwright');const fs=require('fs');
const D=__dirname;const F="file:///home/user/recria-clientes/recria/ebooks/_base/fonts/";
const ICON="file:///home/user/-site-institucional-recria/assets/icone.png";
const P1="file://"+D+"/recria-ads/_fontes/post-7verdades.png",P2="file://"+D+"/recria-ads/_fontes/comentarios-eu-quero.png";
const FORMATS={
 'feed-1x1':{w:1080,h:1080,pad:'84px 76px 84px',ic:56,k:24,h1:[88,44],s:[38,24],pill:40,cta:34,ctap:22,gap:18}
};
const ITEMS=[
["ads-1-dor","Recria Ads","Você cria conteúdo e anúncio, mas <em>quase ninguém compra</em>?","Isso não é falta de esforço: é que o jeito de vender mudou. Aprenda a criar conteúdo e anúncio sem cara de anúncio e aumente as vendas do seu negócio.","Apenas 12x de R$ 10,03","Quero saber mais",""],
["ads-2a-historia","","Se você tem um negócio, eu preciso te mostrar uma coisa que <em>pode estar te fazendo perder dinheiro</em>.","Lá atrás, ela me fez quebrar dois negócios. Depois que eu ajustei um pequeno detalhe, tudo mudou.","","","seta1"],
["ads-2b-revelacao","","Percebeu? <em>Parabéns, você acabou de cair no anúncio.</em>","Eu retive a sua atenção, gerei identificação e fiz você arrastar para o lado para continuar lendo, mesmo sem me conhecer. E sabe por quê?","","","seta"],
["ads-2c-porque","","Todo mundo pula anúncio <em>com cara de anúncio</em>, mas para por uma boa história.","Uma história bem amarrada aos interesses e desejos de quem lê. É a neurociência: o cérebro presta atenção no que fala dele, do que ele quer e do que o interessa.||E sabe qual é o ponto mais importante disso?","","","seta"],
["ads-2d-gancho","","Você vai aprender a parar de criar conteúdo com <em>cara de vendedor chato</em>.","Aquele que não agrega, não desperta desejo, só joga o preço na cara da pessoa e te faz perder tempo com um anúncio que ninguém vai comprar no fim das contas.||Se você está pronto para criar conteúdo e anúncio e vender até quando não está vendendo… então você precisa saber o que é crucial para isso…","","","seta"],
["ads-2e-oferta","","Aprenda a criar conteúdos e anúncios <em>sem cara de anúncio</em>, como as grandes marcas.","Adaptando para o seu cenário e para o seu negócio, mesmo que você tenha baixo orçamento ou seja uma empresa pequena. Para saber mais, toque no botão.","","Quero saber mais",""],
["ads-3-prova","Recria Ads","Aprenda a criar conteúdos que <em>atraem, engajam e vendem</em>. Com leveza.","Olha esse carrossel do meu perfil de yoga: atraí as pessoas, elas se identificaram e comentaram “eu quero”. No direct, continuei a conversa com a oferta do meu curso e vendi. Tudo configurado de forma automatizada. Você também quer aprender?","","Quero saber mais","prova"]
];
function css(f){return `
@font-face{font-family:'Lora';font-weight:600;src:url(${F}lora-latin-600-normal.woff2)}
@font-face{font-family:'Lora';font-weight:400;src:url(${F}lora-latin-400-normal.woff2)}
@font-face{font-family:'Playfair Display';font-weight:700;font-style:normal;src:url(${F}playfair-display-latin-700-normal.woff2)}
@font-face{font-family:'Playfair Display';font-weight:700;font-style:italic;src:url(${F}playfair-display-latin-700-italic.woff2)}
*{box-sizing:border-box;margin:0}
html,body{width:${f.w}px;height:${f.h}px;background:#0b0b0b}
.c{position:relative;width:${f.w}px;height:${f.h}px;background:radial-gradient(circle at 20% 0%,#2b2112 0%,#0b0b0b 65%);color:#fff;font-family:'Lora',serif;padding:${f.pad};display:flex;flex-direction:column;overflow:hidden}
.bd{position:absolute;inset:0;border:3px solid #C9A24E;outline:16px solid #0b0b0b;outline-offset:-19px;pointer-events:none}
.ic{width:${f.ic}px}
.k{letter-spacing:.22em;font-size:${f.k}px;color:#C9A24E;text-transform:uppercase}
h1{font-family:'Playfair Display',serif;font-weight:700;font-size:${f.h1[0]}px;line-height:1.08;margin-top:${f.gap}px}
h1 em{color:#E4C988}
.s{font-size:${f.s[0]}px;line-height:1.4;color:#e9e4da;margin-top:${f.gap+6}px}
.mid{flex:1;display:flex;flex-direction:column;justify-content:center;gap:${f.gap*1.6}px;padding:${f.gap}px 0}.mid h1,.mid .s,.mid .ph,.mid .cta{margin-top:0}.mid .cta{margin-top:${f.gap}px}
.ph{display:flex;gap:16px;justify-content:center}
.ph img{border:3px solid #C9A24E;border-radius:12px;display:block;height:${f.h*0.3}px;width:auto;max-width:48%}

.b{padding-top:${f.gap}px}
.p{display:inline-block;border:3px solid #C9A24E;color:#E4C988;font-weight:600;font-size:${f.pill}px;line-height:1.1;padding:12px 30px;border-radius:10px;margin-bottom:${f.gap}px}
.fn{font-size:${Math.round(f.s[1]*0.7)}px;color:#a9a396;text-align:center;margin-top:-6px}
.mid .p{align-self:flex-start;margin:0}
.dq{font-family:'Playfair Display',serif;font-style:italic;font-weight:700;color:#E4C988;font-size:${Math.round(f.s[0]*1.15)}px;line-height:1.25;border-left:6px solid #C9A24E;padding-left:24px}
.sw{color:#C9A24E;font-weight:600;font-size:${Math.round(f.s[1]*1.1)}px;letter-spacing:.04em;text-align:right}
.cta{background:#C9A24E;color:#0b0b0b;font-weight:700;font-size:${f.cta}px;text-align:center;padding:${f.ctap}px;border-radius:10px;letter-spacing:.02em}
`;}
function html(it,f){const [n,k,h,s,p,c,x]=it;
 return `<!doctype html><meta charset="utf-8"><style>${css(f)}</style><div class="c">${x==='seta1'?'':`<img class="ic" src="${ICON}">`}<div class="mid">${k?`<div class="k">${k}</div>`:''}<h1>${h}</h1><div class="s">${s.split("||")[0]}</div>${s.includes("||")?`<div class="dq">${s.split("||")[1]}</div>`:""}${x==='prova'?`<div class="ph"><img src="${P1}"><img src="${P2}"></div>`:''}${p?`<div class="p">${p}</div>`:''}${c?`<div class="cta">${c}</div>`:''}${x==="seta"||x==="seta1"?'<div class="sw">Arraste para o lado →</div>':''}${x==='prova'?'<div class="fn">Caso real do meu perfil de yoga. Os resultados variam de pessoa para pessoa.</div>':''}</div><div class="bd"></div></div>`;}
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const [fn,f] of Object.entries(FORMATS)){fs.mkdirSync(`${D}/recria-ads/${fn}`,{recursive:true});
 const pg=await b.newPage({viewport:{width:f.w,height:f.h}});
 for(const it of ITEMS){fs.writeFileSync(D+'/_t.html',html(it,f));await pg.goto('file://'+D+'/_t.html');await pg.evaluate(()=>document.fonts.ready);
  const r=await pg.evaluate(([a0,amin,b0,bmin])=>{const c=document.querySelector('.c'),h=document.querySelector('h1'),s=document.querySelector('.s');let a=a0,bb=b0;const over=()=>c.scrollHeight>c.clientHeight+1;
   while(over()&&a>amin){a-=2;h.style.fontSize=a+'px';}while(over()&&bb>bmin){bb-=1;s.style.fontSize=bb+'px';}return [a,bb,over()];},[f.h1[0],f.h1[1],f.s[0],f.s[1]]);
  if(r[2])console.log('OVERFLOW',fn,it[0],r);
  await pg.screenshot({path:`${D}/recria-ads/${fn}/${it[0]}.png`});}
 await pg.close();}
fs.unlinkSync(D+'/_t.html');await b.close();console.log('ok');})();
