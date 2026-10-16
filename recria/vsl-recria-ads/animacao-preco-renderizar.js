const {chromium}=require('/opt/node-tools/node_modules/playwright');
const {spawn}=require('child_process');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:410,height:400},deviceScaleFactor:2});
 await p.goto('file://'+process.cwd()+'/anim.html');
 const only=process.argv[2];
 if(only){for(const t of only.split(',')){await p.evaluate(t=>render(t),+t);await p.screenshot({path:`f_${t}.png`});}await b.close();return;}
 const fps=30,dur=16.6,n=Math.round(fps*dur);
 const ff=spawn('ffmpeg',['-y','-f','image2pipe','-framerate','30','-c:v','png','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-movflags','+faststart','preco.mp4'],{stdio:['pipe','inherit','inherit']});
 for(let i=0;i<n;i++){await p.evaluate(t=>render(t),i/fps);const buf=await p.screenshot();if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
 ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();
})();
