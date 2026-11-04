import pathlib, asyncio
from playwright.async_api import async_playwright
src=open('build.py',encoding='utf-8').read(); ns={}; exec(src[:src.index('cover=photo(')],ns)
fonts=ns['base'].split('*{margin')[0]
html=f"""<html><head><style>{fonts}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:transparent;width:1080px;height:1920px;overflow:hidden}}
.g{{position:absolute;left:0;right:0;bottom:0;height:900px;background:linear-gradient(180deg,rgba(30,18,14,0),rgba(30,18,14,.75) 55%,rgba(30,18,14,.85))}}
.b{{position:absolute;left:80px;right:80px;bottom:330px;color:#fff;font-family:PF}}
h1{{font:600 74px/1.14 PF;margin-bottom:26px;text-shadow:0 2px 14px rgba(0,0,0,.35)}}
p{{font:500 44px/1.35 LO;color:#F3DDD0;margin-bottom:34px}}
span{{display:inline-block;font:600 30px MS;letter-spacing:.06em;border:2px solid #fff;border-radius:50px;padding:14px 30px;color:#fff}}
</style></head><body><div class=g></div><div class=b>
<h1>Nem tudo o que eu aprendo está nos livros.</h1><p>Algumas das melhores aulas acontecem nos corredores de um congresso.</p><span>leia a legenda &darr;</span></div></body></html>"""
async def main():
    f=pathlib.Path('ov2.html').resolve(); f.write_text(html,encoding='utf-8')
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium' if pathlib.Path('/opt/pw-browsers/chromium').is_file() else None)
        pg=await b.new_page(viewport={'width':1080,'height':1920}); await pg.goto(f.as_uri()); await pg.wait_for_timeout(600)
        await pg.screenshot(path='ov2.png',omit_background=True); await b.close()
asyncio.run(main())
