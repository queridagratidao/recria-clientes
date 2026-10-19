const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage();await p.goto('file://'+__dirname+'/_t.html');await p.pdf({path:__dirname+'/Legendas-Recria-Ads.pdf',format:'A4',margin:{top:'18mm',bottom:'18mm',left:'16mm',right:'16mm'}});await b.close();})();
