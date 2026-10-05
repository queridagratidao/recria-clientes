const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async()=>{
 const [,, inp, out]=process.argv;
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const pg=await b.newPage();
 await pg.goto('file://'+inp);
 await pg.evaluate(()=>document.fonts.ready);
 await pg.pdf({path:out,preferCSSPageSize:true,printBackground:true});
 await b.close();
})();
