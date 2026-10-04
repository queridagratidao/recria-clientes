import pathlib, base64
from playwright.sync_api import sync_playwright
S=pathlib.Path(__file__).parent
F=(S/'c1/fonts_embedded.css').read_text()
def b64(p):
    p=pathlib.Path(p); mt='image/png' if p.suffix=='.png' else 'image/jpeg'
    return f'data:{mt};base64,'+base64.b64encode(p.read_bytes()).decode()
ICON=b64(S/'ck/logo_icone.png'); FULL=b64(S/'ck/logo_sem_tagline.png')
CSS=F+"""@page{size:1920px 1080px;margin:0}*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Lora'}
.s{width:1920px;height:1080px;position:relative;overflow:hidden;page-break-after:always;padding:150px 150px 140px;display:flex;flex-direction:column;justify-content:center}
.d{background:radial-gradient(ellipse at 12% 0%,#2a2214 0%,#0b0b0b 58%),#0b0b0b;color:#fff}.l{background:#F6F2EA;color:#111}
.ic{position:absolute;top:56px;left:150px;height:70px}
.ft{position:absolute;bottom:50px;left:150px;right:150px;display:flex;justify-content:space-between;font-size:24px;color:#C9A24E;opacity:.85}.l .ft{color:#8a6d2c}
.k{font-weight:600;font-size:30px;letter-spacing:.2em;text-transform:uppercase;color:#C9A24E;margin-bottom:26px}.l .k{color:#9a7424}
h1{font-family:'Playfair Display';font-weight:700;font-size:118px;line-height:1.05}
h2{font-family:'Playfair Display';font-weight:700;font-size:84px;line-height:1.1;margin-bottom:34px}
em{font-style:italic;color:#E4C988}.l em{color:#9a7424}
p{font-size:42px;line-height:1.45;margin-top:18px}.d p{color:#e9e4da}.l p{color:#2a2a2a}
ul{list-style:none;margin-top:10px}li{font-size:46px;line-height:1.35;margin-bottom:24px;padding-left:62px;position:relative}
li:before{content:'';position:absolute;left:0;top:20px;width:22px;height:22px;border-radius:50%;background:#C9A24E}
.d li{color:#f1ede4}.l li{color:#1d1d1d}
.big{font-family:'Playfair Display';font-weight:700;font-size:132px;line-height:1.08}
.cmp{display:flex;gap:60px;margin-top:20px}.cmp>div{flex:1;border-radius:14px;padding:44px 48px}
.cmp .a{background:rgba(255,255,255,.06);border:2px solid #555}.l .cmp .a{background:#fff;border:2px solid #d8cdb5}
.cmp .b{background:rgba(201,162,78,.12);border:3px solid #C9A24E}
.cmp small{display:block;font-size:26px;letter-spacing:.15em;text-transform:uppercase;color:#C9A24E;font-weight:600;margin-bottom:18px}
.cmp div div{font-family:'Playfair Display';font-size:52px;line-height:1.3}
.row{display:flex;gap:80px;align-items:center}.row .tx{flex:1.1}.row .im{flex:1;display:flex;justify-content:center}
.row img{max-height:700px;max-width:100%;border-radius:12px;border:3px solid #C9A24E;box-shadow:0 20px 60px rgba(0,0,0,.35)}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:26px;margin-top:10px}
.grid div{border:2px solid #C9A24E;border-radius:12px;padding:20px 24px;font-size:27px;line-height:1.28}
.grid b{display:block;font-family:'Playfair Display';font-size:34px;color:#C9A24E;margin-bottom:8px}.l .grid b{color:#9a7424}
.flow{display:flex;align-items:center;gap:22px;flex-wrap:wrap;margin-top:20px}
.flow span{border:2px solid #C9A24E;border-radius:60px;padding:20px 34px;font-size:38px}.flow i{font-style:normal;color:#C9A24E;font-size:48px}
.box{margin-top:34px;background:#0b0b0b;color:#E4C988;border-left:10px solid #C9A24E;padding:34px 44px;font-family:'Playfair Display';font-style:italic;font-size:48px;line-height:1.35}
.d .box{background:rgba(201,162,78,.1);border:2px solid #C9A24E;border-left:10px solid #C9A24E}
.src{font-size:26px!important;opacity:.7;font-style:italic;margin-top:30px!important}
.pb{position:absolute;top:70px;right:150px;font-size:24px;letter-spacing:.15em;color:#C9A24E;border:2px solid #C9A24E;border-radius:40px;padding:8px 22px}
"""
class Deck:
    def __init__(s,aula,titulo,fmt): s.aula,s.titulo,s.fmt,s.sl=aula,titulo,fmt,[]
    def _w(s,cls,body,extra=''):
        n=len(s.sl)+1
        s.sl.append(f'<div class="s {cls}"><img class="ic" src="{ICON}">{extra}{body}<div class="ft"><span>Recria Ads · Aula {s.aula}</span><span>{n:02d}</span></div></div>')
    def cover(s,kick,title,sub=''):
        n=len(s.sl)+1
        s.sl.append(f'<div class="s d"><img style="height:150px;align-self:flex-start;margin-bottom:60px" src="{FULL}"><div class="k">{kick}</div><h1>{title}</h1>{f"<p>{sub}</p>" if sub else ""}<div class="ft"><span>@agencia.recria × @amandarecria</span><span>{n:02d}</span></div></div>')
    def st(s,text,sub='',cls='d',kick=''): s._w(cls,(f'<div class="k">{kick}</div>' if kick else '')+f'<div class="big">{text}</div>'+(f'<p>{sub}</p>' if sub else ''))
    def bl(s,kick,title,items,cls='l',box=''): s._w(cls,(f'<div class="k">{kick}</div>' if kick else '')+f'<h2>{title}</h2><ul>'+''.join(f'<li>{i}</li>' for i in items)+'</ul>'+(f'<div class="box">{box}</div>' if box else ''))
    def tx(s,kick,title,text='',cls='l',box='',src=''): s._w(cls,(f'<div class="k">{kick}</div>' if kick else '')+f'<h2>{title}</h2>'+(f'<p>{text}</p>' if text else '')+(f'<div class="box">{box}</div>' if box else '')+(f'<p class="src">{src}</p>' if src else ''))
    def cmp(s,title,la,a,lb,b,cls='l',kick=''): s._w(cls,(f'<div class="k">{kick}</div>' if kick else '')+f'<h2>{title}</h2><div class="cmp"><div class="a"><small>{la}</small><div>{a}</div></div><div class="b"><small>{lb}</small><div>{b}</div></div></div>')
    def img(s,kick,title,text,path,cls='d',src=''): s._w(cls,f'<div class="row"><div class="tx">'+(f'<div class="k">{kick}</div>' if kick else '')+f'<h2>{title}</h2>'+(f'<p>{text}</p>' if text else '')+(f'<p class="src">{src}</p>' if src else '')+f'</div><div class="im"><img src="{b64(path)}"></div></div>')
    def grid(s,kick,title,cells,cls='l'): s._w(cls,f'<div class="k">{kick}</div><h2>{title}</h2><div class="grid">'+''.join(f'<div><b>{a}</b>{b}</div>' for a,b in cells)+'</div>')
    def flow(s,kick,title,steps,cls='d',box=''): s._w(cls,f'<div class="k">{kick}</div><h2>{title}</h2><div class="flow">'+'<i>→</i>'.join(f'<span>{x}</span>' for x in steps)+'</div>'+(f'<div class="box">{box}</div>' if box else ''))
    def render(s,out):
        html=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(s.sl)}</body></html>'
        with sync_playwright() as p:
            b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'); pg=b.new_page()
            pg.set_content(html,wait_until='networkidle'); pg.evaluate('document.fonts.ready')
            ov=pg.evaluate("()=>[...document.querySelectorAll('.s')].map((e,i)=>e.scrollHeight>e.clientHeight+2?i+1:0).filter(x=>x)")
            if ov: print('OVERFLOW',out,ov)
            pg.pdf(path=str(out),width='1920px',height='1080px',print_background=True); b.close()
        print(pathlib.Path(out).name,len(s.sl))
CEN=[('Eupresa','A empresa de uma pessoa só: você faz tudo'),('Negócio local','Espaço físico: loja, restaurante, salão, escola, clínica, academia'),('E-commerce','Vende online e entrega em vários lugares'),('Empresa média','Tem equipe, alguma verba e pensa em influenciadores'),('Empresa grande','Tem time de marketing interno'),('Serviços e consultoria','Atende outras empresas: conhecimento e transformação'),('Negócio digital','Cursos, mentorias, e-books e serviços online')]
