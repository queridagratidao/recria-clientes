// usage: node vid.js <date> ; renders bg + text layers, then ffmpeg mp4 (no audio)
const {chromium}=require('playwright');const fs=require('fs');const {execSync}=require('child_process');
const S='/tmp/claude-0/-home-claude/b2736a22-a7a5-5ef9-a4fc-d023deb3f6f7/scratchpad';
const P=require(S+'/dez/dez.json').find(p=>p.d===process.argv[2]);
const F=S+'/fonts/node_modules/@fontsource/poppins/files/poppins-latin-';
const out=S+'/dez/vid/'+P.d.replace('/','-');fs.rmSync(out,{recursive:true,force:true});fs.mkdirSync(out,{recursive:true});
const css=`@font-face{font-family:P;font-weight:700;src:url(${F}700-normal.woff2)}@font-face{font-family:P;font-weight:800;src:url(${F}800-normal.woff2)}@font-face{font-family:P;font-weight:600;src:url(${F}600-normal.woff2)}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1920px;background:transparent}`;
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1080,height:1920}});
 // background: photo cover + soft gradient
 fs.writeFileSync(out+'/p.html',`<html><head><style>${css}
 .bg{position:absolute;inset:0;background:url(file://${S}/feed-dez/img/${P.bg}.jpg) center/cover}
 .g{position:absolute;inset:0;background:linear-gradient(180deg,rgba(40,8,30,.10) 0%,rgba(40,8,30,.05) 45%,rgba(40,8,30,.55) 75%,rgba(40,8,30,.75) 100%)}
 .sig{position:absolute;left:0;right:0;bottom:120px;text-align:center;color:#fff;font:600 34px P;opacity:.9}</style></head>
 <body><div class="bg"></div><div class="g"></div><div class="sig">@psicamilasartori</div></body></html>`);await pg.goto('file://'+out+'/p.html',{waitUntil:'load'});
 await pg.waitForTimeout(400);await pg.screenshot({path:out+'/bg.png'});
 for(let i=0;i<P.beats.length;i++){const [t]=P.beats[i];const big=t.length<22;
  fs.writeFileSync(out+'/p.html',`<html><head><style>${css}
  .t{position:absolute;left:90px;right:90px;top:${P.vt==="top"?330:P.vt==="low"?1390:(big?1180:1080)}px;text-align:center;color:#fff;font:800 ${big?96:76}px/1.18 P;text-shadow:0 4px 24px rgba(30,6,20,.55)}
  .t span{background:rgba(167,24,116,.0)}</style></head><body><div class="t">${t}</div></body></html>`);await pg.goto('file://'+out+'/p.html',{waitUntil:'load'});
  await pg.evaluate(()=>document.fonts.ready);
  await pg.screenshot({path:out+`/t${i}.png`,omitBackground:true});}
 await b.close();
 const D=P.beats.reduce((a,x)=>a+x[1],0);const fps=30;const N=Math.round(D*fps);
 let inp=`-loop 1 -t ${D} -i ${out}/bg.png `;let flt=`[0:v]scale=1188:2112,zoompan=z='min(1+0.10*on/${N},1.10)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=${N}:s=1080x1920:fps=${fps}[b0];`;
 let last='b0',t0=0;
 P.beats.forEach(([_,d],i)=>{inp+=`-loop 1 -t ${D} -i ${out}/t${i}.png `;const a=t0.toFixed(2),e=(t0+d).toFixed(2);
  flt+=`[${last}][${i+1}:v]overlay=0:0:enable='between(t,${a},${e})'[b${i+1}];`;last='b'+(i+1);t0+=d;});
 flt=flt.slice(0,-1);
 execSync(`ffmpeg -y -loglevel error ${inp} -filter_complex "${flt}" -map "[${last}]" -t ${D} -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -r ${fps} ${out}/video.mp4`,{stdio:'inherit'});
 console.log(P.d,D+'s');
})();
