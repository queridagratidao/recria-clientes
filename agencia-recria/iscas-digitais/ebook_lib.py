"""Base visual dos e-books/iscas digitais da Agência Recria (1080x1350, preto/off-white/dourado)."""
import base64, pathlib
from playwright.sync_api import sync_playwright

S = pathlib.Path(__file__).parent
FONTS = (S / 'c1/fonts_embedded.css').read_text()
_b64 = lambda p: 'data:image/png;base64,' + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
ICON = _b64(S / 'ck/logo_icone.png')
FULL = _b64(S / 'ck/logo_sem_tagline.png')

AULAO = 'https://www.agenciarecria.com.br/aula-mkt-para-negocios/'
DIAG = 'https://www.agenciarecria.com.br/diagnostico-recria/'
SERV = 'https://www.agenciarecria.com.br/#servicos'
PACOTE = 'https://www.agenciarecria.com.br/pacote-mkt-inicial/'

CSS = FONTS + """
@page{size:1080px 1350px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Lora',serif}
.pg{width:1080px;height:1350px;position:relative;padding:150px 90px 120px;overflow:hidden;page-break-after:always;display:flex;flex-direction:column}
.dark{background:radial-gradient(ellipse at 15% 0%,#2a2214 0%,#0b0b0b 55%),#0b0b0b;color:#fff}
.light{background:#F6F2EA;color:#111}
.logo{position:absolute;top:50px;left:80px;height:70px}
.foot{position:absolute;bottom:44px;left:90px;right:90px;display:flex;justify-content:space-between;font-size:20px;opacity:.7}
.dark .foot{color:#E4C988}.light .foot{color:#8a6d2c}
.kick{font-weight:600;font-size:23px;letter-spacing:.18em;text-transform:uppercase;color:#C9A24E;margin-bottom:16px}
.light .kick{color:#9a7424}
h1{font-family:'Playfair Display';font-weight:700;font-size:54px;line-height:1.12;margin-bottom:24px}
h2{font-family:'Playfair Display';font-weight:700;font-size:32px;margin:16px 0 8px}
em.g{font-style:italic;color:#E4C988}.light em.g{color:#9a7424}
p{font-size:26px;line-height:1.5;margin-bottom:14px}
.dark p,.dark li{color:#e9e4da}.light p,.light li{color:#2a2a2a}
b{font-weight:600}.dark b{color:#fff}
ul{list-style:none;margin:4px 0 12px}
li{font-size:24px;line-height:1.45;margin-bottom:11px;padding-left:36px;position:relative}
li:before{content:'';position:absolute;left:0;top:12px;width:13px;height:13px;border-radius:50%;background:#C9A24E}
li.ck:before{content:'☐';background:none;width:auto;height:auto;top:-2px;color:#C9A24E;font-size:27px;border-radius:0}
.box{background:#0b0b0b;color:#E4C988;border-left:6px solid #C9A24E;padding:20px 26px;font-family:'Playfair Display';font-style:italic;font-size:25px;line-height:1.4;margin:8px 0 12px}
.dark .box{background:rgba(201,162,78,.08);border:1.5px solid #C9A24E;border-left:6px solid #C9A24E}
.src{font-size:17px!important;opacity:.75;font-style:italic;margin-top:4px}
.cta{background:#C9A24E;color:#0b0b0b;border-radius:6px;padding:26px 32px;margin-top:10px}
.cta .t{font-family:'Playfair Display';font-weight:700;font-size:33px;line-height:1.2;margin-bottom:10px}
.cta p{color:#1a1a1a!important;font-size:23px;margin-bottom:10px}
.cta b{color:#0b0b0b!important}
.cta .l{font-weight:600;font-size:23px;background:#0b0b0b;color:#E4C988;display:inline-block;padding:10px 18px;border-radius:4px;text-decoration:none}
table{width:100%;border-collapse:collapse;font-size:21px;margin-top:4px}
th{text-align:left;background:#0b0b0b;color:#E4C988;padding:11px 12px;font-family:'Playfair Display';font-size:21px}
td{padding:10px 12px;border-bottom:1px solid #e1d5ba;vertical-align:top;line-height:1.38;color:#2a2a2a}
td:first-child{font-weight:600;color:#5a4412;width:27%}
.dark td{color:#e9e4da;border-bottom:1px solid rgba(201,162,78,.3)} .dark td:first-child{color:#E4C988}
.stat{display:flex;gap:22px;margin:6px 0 16px}
.stat div{flex:1;border:1.5px solid #C9A24E;border-radius:6px;padding:18px 20px}
.stat strong{display:block;font-family:'Playfair Display';font-size:58px;color:#C9A24E;line-height:1}
.light .stat strong{color:#9a7424}
.stat span{font-size:20px;line-height:1.35;display:block;margin-top:8px}
"""


class Book:
    def __init__(self, title, footer):
        self.title, self.footer, self.pages = title, footer, []

    def cover(self, kicker, h, sub):
        self.pages.append(f'''<div class="pg dark" style="justify-content:center;padding-top:0"><img style="height:190px;align-self:flex-start;margin-bottom:64px" src="{FULL}">
<div class="kick" style="font-size:27px">{kicker}</div><h1 style="font-size:84px;line-height:1.04">{h}</h1>
<p style="font-size:32px;max-width:840px">{sub}</p><div style="width:180px;height:3px;background:#C9A24E;margin:28px 0"></div>
<p style="font-size:23px;color:#E4C988">@agencia.recria × @amandarecria</p></div>''')

    def page(self, cls, body):
        n = len(self.pages) + 1
        self.pages.append(f'<div class="pg {cls}"><img class="logo" src="{ICON}">{body}<div class="foot"><span>{self.footer}</span><span>{n:02d}</span></div></div>')

    def render(self, out):
        html = f'<!doctype html><html><head><meta charset="utf-8"><title>{self.title}</title><style>{CSS}</style></head><body>{"".join(self.pages)}</body></html>'
        out = pathlib.Path(out); out.parent.mkdir(parents=True, exist_ok=True)
        with sync_playwright() as p:
            br = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
            pg = br.new_page(); pg.set_content(html, wait_until='networkidle'); pg.evaluate('document.fonts.ready')
            pg.pdf(path=str(out), width='1080px', height='1350px', print_background=True)
            br.close()
        print(out, len(self.pages), 'páginas')


def fechamento(utm):
    return f'''<p style="margin-top:6px;font-family:'Playfair Display';font-style:italic;font-size:28px;color:#9a7424;margin-bottom:2px">Com carinho,<br>Amanda, CEO da Agência Recria</p>
<p style="font-size:21px;color:#5a4412">@agencia.recria · @amandarecria</p>
<div class="cta" style="margin-top:14px;padding:22px 28px"><div class="t" style="font-size:28px">🎁 Mais um presente para você</div><p style="font-size:22px">Para você dar continuidade aos seus estudos: um <b>aulão de Marketing para Negócios</b>, totalmente gratuito. Clique no link abaixo e bons estudos!</p><a class="l" href="{AULAO}?utm_source={utm}">▶ Assistir ao aulão gratuito</a></div>'''
