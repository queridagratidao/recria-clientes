import pathlib, asyncio
from playwright.async_api import async_playwright
D=pathlib.Path('.').resolve(); F=D/'node_modules/@fontsource'
fonts=f"""
@font-face{{font-family:PF;font-weight:500;src:url({F}/playfair-display/files/playfair-display-latin-500-normal.woff2)}}
@font-face{{font-family:PF;font-weight:600;src:url({F}/playfair-display/files/playfair-display-latin-600-normal.woff2)}}
@font-face{{font-family:PF;font-weight:500;font-style:italic;src:url({F}/playfair-display/files/playfair-display-latin-500-italic.woff2)}}
@font-face{{font-family:LO;font-weight:500;src:url({F}/lora/files/lora-latin-500-normal.woff2)}}
@font-face{{font-family:LO;font-weight:500;font-style:italic;src:url({F}/lora/files/lora-latin-500-italic.woff2)}}
@font-face{{font-family:MS;font-weight:400;src:url({F}/montserrat/files/montserrat-latin-400-normal.woff2)}}
@font-face{{font-family:MS;font-weight:500;src:url({F}/montserrat/files/montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:MS;font-weight:600;src:url({F}/montserrat/files/montserrat-latin-600-normal.woff2)}}
"""
base=fonts+"""
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;font-family:MS;color:#3B2A24}
.handle{position:absolute;font:500 24px MS;letter-spacing:.06em}
.swipe{position:absolute;right:72px;bottom:66px}
.wave{display:block}
h1,h2,h3,.sub,.num{font-feature-settings:"lnum" 1;font-variant-numeric:lining-nums}
"""
def photo(img, inner, extra=""):
    return f"""<html><head><style>{base}
.ph{{position:absolute;inset:0;background:url({D}/src/{img}) center/cover}}
{extra}</style></head><body><div class=ph></div>{inner}</body></html>"""

cover=photo('capa_crop.jpg',"""
<div class=shade></div>
<div class="handle" style="top:60px;left:72px;color:#fff;opacity:.9">@paticompagnoni</div>
<div class=box>
  <div class=inner><h1>É de graça, mas eu pagaria<br>para ter descoberto isso antes:</h1>
  <p class=sub>3 fatos sobre a pele que aprendi sendo estudante de biomedicina.</p></div>
  <span class=pill>com base em estudos científicos</span>
</div>
<div class=swipe><svg class=wave viewBox="0 0 48 30" width="64" height="40"><path d="M4 6 L13 15 L4 24" fill="none" stroke="#fff" stroke-opacity="0.3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M18 6 L27 15 L18 24" fill="none" stroke="#fff" stroke-opacity="0.6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M32 6 L41 15 L32 24" fill="none" stroke="#fff" stroke-opacity="1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>""","""
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(30,18,14,0) 38%,rgba(30,18,14,.55) 62%,rgba(30,18,14,.88) 100%)}
.box{position:absolute;left:72px;right:72px;bottom:150px;color:#fff}
h1{font:600 62px/1.15 PF;margin-bottom:26px}
.sub{font:500 34px/1.4 LO;color:#F3DDD0;margin-bottom:30px;width:0;min-width:100%}
.inner{display:inline-block}
.pill{display:inline-block;font:600 24px MS;letter-spacing:.08em;text-transform:uppercase;border:2px solid #fff;border-radius:40px;padding:12px 26px}
""")

def content(n, title, img, text):
    return f"""<html><head><style>{base}
body{{background:#F4EDE6;display:flex;flex-direction:column;padding:80px 80px 56px}}
.group{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:48px}}
h2{{font:600 60px/1.14 PF}}
.print{{width:100%;background:#fff;border-radius:22px;padding:30px;box-shadow:0 18px 50px rgba(80,50,35,.16)}}
.print img{{width:100%;display:block}}
.tag{{font:600 18px MS;letter-spacing:.12em;text-transform:uppercase;color:#B07A63;margin-bottom:16px}}
.txt{{font:400 32px/1.5 MS}}
.txt b{{font-weight:600}}
.foot{{display:flex;justify-content:space-between;align-items:center;font:500 24px MS;letter-spacing:.06em;color:#9C7B6C;margin-top:30px}}
</style></head><body>
<div class=group>
<h2>{title}</h2>
<div class=print><div class=tag>o estudo</div><img src="{D}/src/{img}"></div>
<div class=txt>{text}</div>
</div>
<div class=foot><span>@paticompagnoni</span><svg class=wave viewBox="0 0 48 30" width="64" height="40"><path d="M4 6 L13 15 L4 24" fill="none" stroke="#B07A63" stroke-opacity="0.3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M18 6 L27 15 L18 24" fill="none" stroke="#B07A63" stroke-opacity="0.6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M32 6 L41 15 L32 24" fill="none" stroke="#B07A63" stroke-opacity="1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
</body></html>"""

cards=[
 ('01-capa',cover),
 ('02-protetor',content(1,'Protetor com cor protege mais contra manchas do que o sem cor','print-protetor-crop.png',
  'Não é só o sol direto que mancha a pele: a <b>luz visível do dia</b>, que entra até pela janela, também escurece manchas e melasma. O protetor com cor tem um pigmento, o <b>óxido de ferro</b>, que funciona como uma barreira extra contra essa luz.')),
 ('03-colageno',content(2,'Tomar cápsulas de colágeno não garante que ele vá para a sua pele','print-colageno.png',
  'Quando você toma colágeno, o corpo quebra ele em pedacinhos (<b>aminoácidos</b>) e usa onde estiver precisando: pode ser na pele, nos músculos, nos órgãos… Não é ruim, porque é uma fonte de proteína. Mas, se você já se alimenta bem, ele não faz tanta diferença na pele quanto parece.')),
 ('04-sono',content(3,'A posição em que você dorme pode causar “rugas do sono”','print-sono.png',
  'Dormir de lado ou de bruços <b>amassa o rosto no travesseiro</b>, noite após noite. Com o tempo, isso pode formar as famosas rugas do sono, que são diferentes das linhas de expressão. Por isso, às vezes um lado do rosto tem mais linhas que o outro.')),
 ('05-cta',photo('cta_crop.jpg',"""
<div class=panel>
  <h3>Mulher, você<br><span style="white-space:nowrap">sabia disso? <span style="color:#B07A63">&#9825;</span></span></h3>
  <p>Me conta nos comentários se foi novidade para você ou o que mais você quer aprender sobre cuidados com a pele.</p>
  <span class=hd>@paticompagnoni</span>
</div>""","""
.ph{background-position:center top}
.panel{position:absolute;right:30px;top:50%;transform:translateY(-50%);width:392px;background:rgba(244,237,230,.94);border-radius:28px;padding:44px 40px}
h3{font:600 44px/1.15 PF;margin-bottom:22px}
.panel p{font:400 28px/1.5 MS;margin-bottom:24px}
.hd{font:600 24px MS;letter-spacing:.06em;color:#B07A63}
""")),
]
async def main():
    out=D/'out'; out.mkdir(exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium' if pathlib.Path('/opt/pw-browsers/chromium').is_file() else None)
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        for name,html in cards:
            f=D/f'{name}.html'; f.write_text(html.replace('{TOP}','400'),encoding='utf-8')
            await pg.goto(f.as_uri()); await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(500)
            await pg.screenshot(path=str(out/f'{name}.png'))
        await b.close()
asyncio.run(main())
