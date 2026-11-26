const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-claude/b2736a22-a7a5-5ef9-a4fc-d023deb3f6f7/scratchpad';
const D=require(S+'/dez/dez.json');const only=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1080,height:1350}});
await pg.goto('file://'+S+'/feed-dez/_r.html',{waitUntil:'load'});
for(const p of D){if(p.t==='vid')continue;if(only.length&&!only.includes(p.d))continue;
 const o=S+'/dez/out/'+p.d.replace('/','-').replace(' ','_');fs.rmSync(o,{recursive:true,force:true});fs.mkdirSync(o,{recursive:true});
 for(let i=0;i<p.slides.length;i++){
  await pg.evaluate(([p,i])=>{document.getElementById('c').innerHTML=Cards.card(p,i,'')},[p,i]);
  await pg.evaluate(()=>Promise.all([...document.images].map(im=>im.complete?1:new Promise(r=>im.onload=im.onerror=r))));await pg.evaluate(()=>document.fonts.ready);
  await pg.screenshot({clip:{x:0,y:0,width:1080,height:1350},path:o+`/card-${String(i+1).padStart(2,'0')}.png`});}}
console.log(await pg.evaluate(()=>[document.fonts.check('700 20px Quicksand'),document.fonts.check('400 20px "Courier Prime"')]));await b.close()})();
