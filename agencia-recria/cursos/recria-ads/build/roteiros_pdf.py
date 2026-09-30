import pathlib, markdown, base64
from playwright.sync_api import sync_playwright
S=pathlib.Path(__file__).parent
R=pathlib.Path('/home/user/recria-clientes/agencia-recria/cursos/recria-ads/roteiros-completos')
FONTS=(S/'c1/fonts_embedded.css').read_text()
LOGO='data:image/png;base64,'+base64.b64encode((S/'ck/logo_sem_tagline.png').read_bytes()).decode()
md=''.join((R/f).read_text()+'\n\n' for f in ['00-legenda.md','01-modulo-0.md','02-modulo-1.md','03-modulo-2.md'])
body=markdown.markdown(md,extensions=['tables'])
css=FONTS+"""
@page{size:A4;margin:18mm 16mm 18mm}
body{font-family:'Lora',serif;font-size:12.5pt;line-height:1.6;color:#1d1d1d}
h1{font-family:'Playfair Display';font-size:26pt;color:#0b0b0b;border-bottom:3px solid #C9A24E;padding-bottom:6px;margin-top:0;page-break-before:always}
h1:first-of-type{page-break-before:avoid}
h2{font-family:'Playfair Display';font-size:17pt;background:#0b0b0b;color:#E4C988;padding:8px 12px;margin-top:22px;page-break-after:avoid}
p{margin:7px 0} strong{color:#5a4412}
p strong:first-child{color:#8a6d2c}
table{border-collapse:collapse;width:100%;font-size:11pt;margin:8px 0}
th{background:#0b0b0b;color:#E4C988;text-align:left;padding:6px}
td{border-bottom:1px solid #e1d5ba;padding:6px;vertical-align:top}
hr{border:none;border-top:1px dashed #C9A24E;margin:18px 0}
li{margin:3px 0}
.capa{height:250mm;display:flex;flex-direction:column;justify-content:center;background:#0b0b0b;color:#fff;padding:0 18mm;margin:-18mm -16mm 0;page-break-after:always}
.capa h1{color:#fff;border:none;font-size:38pt;page-break-before:avoid}
.capa p{color:#E4C988;font-size:14pt}
"""
capa=f'<div class="capa"><img src="{LOGO}" style="height:90px;align-self:flex-start;margin-bottom:40px"><p>RECRIA ADS · ROTEIROS DE GRAVAÇÃO</p><h1>Módulos 0, 1 e 2</h1><p>11 aulas · liberadas no dia da compra · gravar até 13/10</p></div>'
html=f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{capa}{body}</body></html>'
out='/home/user/recria-clientes/agencia-recria/cursos/recria-ads/Roteiros Recria Ads - Modulos 0 a 2.pdf'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'); pg=b.new_page()
    pg.set_content(html,wait_until='networkidle'); pg.evaluate('document.fonts.ready'); pg.pdf(path=out,format='A4',print_background=True); b.close()
import pymupdf; d=pymupdf.open(out); print(d.page_count)
d[1].get_pixmap(dpi=60).save(str(S/'rot_p2.png')); d[4].get_pixmap(dpi=60).save(str(S/'rot_p5.png'))
