import pathlib, asyncio, base64
from PIL import Image, ImageEnhance
from playwright.async_api import async_playwright
src=open('build.py',encoding='utf-8').read(); ns={}; exec(src[:src.index('cover=photo(')],ns)
fonts=ns['base'].split('*{margin')[0]
D=pathlib.Path('.').resolve()
def prep(f,out,cx=0.5,top=0.0,bright=1.03):
    im=Image.open('src/'+f).convert('RGB'); w,h=im.size
    if h/w>=16/9: tw,th=w,int(w*16/9)
    else: tw,th=int(h*9/16),h
    x=int((w-tw)*cx); y=int((h-th)*top)
    im=im.crop((x,y,x+tw,y+th)).resize((1080,1920),Image.LANCZOS)
    ImageEnhance.Brightness(im).enhance(bright).save('src/'+out,quality=92)
def html(img,h1,sub,pill,trans=False,top=False):
    bg='transparent' if trans else f"url(src/{img}) center/cover"
    return f"""<html><head><style>{fonts}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:{bg}}}
.g{{position:absolute;left:0;right:0;bottom:0;height:1050px;background:linear-gradient(180deg,rgba(30,18,14,0),rgba(30,18,14,.7) 50%,rgba(30,18,14,.88))}}
.hd{{position:absolute;top:330px;left:80px;font:600 28px MS;letter-spacing:.08em;color:#fff;opacity:.9;text-shadow:0 1px 8px rgba(0,0,0,.4)}}
.b{{position:absolute;left:80px;right:80px;bottom:330px;color:#fff}}
.k{{display:inline-block;background:#B07A63;color:#fff;font:600 26px MS;letter-spacing:.08em;text-transform:uppercase;padding:12px 22px;border-radius:6px;margin-bottom:28px}}
h1{{font:600 80px/1.12 PF;margin-bottom:24px;text-shadow:0 2px 14px rgba(0,0,0,.35)}}
p{{font:500 44px/1.35 LO;color:#F3DDD0;margin-bottom:34px}}
span.pl{{display:inline-block;font:600 30px MS;letter-spacing:.06em;border:2px solid #fff;border-radius:50px;padding:14px 30px}}
{".g{top:0;bottom:auto;height:1000px;background:linear-gradient(0deg,rgba(30,18,14,0),rgba(30,18,14,.6) 45%,rgba(30,18,14,.8))} .b{top:250px;bottom:auto} .b p{display:none} .hd{top:auto;bottom:300px}" if top else ""}</style></head><body><div class=g></div>{'' if trans else '<div class=hd>@paticompagnoni</div>'}<div class=b>
<h1>{h1}</h1><p>{sub}</p><span class=pl>{pill}</span></div></body></html>"""
prep('fr_12.jpg','cv_12.jpg',cx=0.5)
prep('n_nb11.jpg','cv_26.jpg',cx=0.5)
prep('n5_d24.jpg','cv_24.jpg',cx=0.85)     # pink dress
prep('fr_14.jpg','cv_14.jpg')
C=[('capa-12-11','cv_12.jpg','Depois dos 40, eu voltei a estudar.','E esse crachá diz muito sobre onde eu quero chegar.','assista &#9654;'),
   ('capa-26-11','cv_26.jpg','Você não envelhece aos poucos, você envelhece em saltos…','E como usar isso a seu favor?','assista &#9654;'),
   ('capa-24-12','cv_24.jpg','2026 foi o ano em que eu escolhi investir em mim.','E você, no que investiu este ano?','assista &#9654;'),
   ('capa-14-01','cv_14.jpg','5 mitos sobre a pele depois dos 40','que muita gente ainda acredita.','assista &#9654;')]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium' if pathlib.Path('/opt/pw-browsers/chromium').is_file() else None)
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        (D/'out7').mkdir(exist_ok=True)
        for n,img,h,s,pl in C:
            f=D/f'{n}.html'; f.write_text(html(img,h,s,pl,top=(n=='capa-12-11')),encoding='utf-8')
            await pg.goto(f.as_uri()); await pg.wait_for_timeout(500); await pg.screenshot(path=f'out7/{n}.png')
        f=D/'ov3.html'; f.write_text(html('','5 mitos sobre a pele depois dos 40','que muita gente ainda acredita.','leia a legenda &darr;',trans=True),encoding='utf-8')
        await pg.goto(f.as_uri()); await pg.wait_for_timeout(500); await pg.screenshot(path='ov3.png',omit_background=True)
        await b.close()
asyncio.run(main())
