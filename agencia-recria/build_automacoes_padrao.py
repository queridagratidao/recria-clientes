import html, pathlib, base64
from playwright.sync_api import sync_playwright
src=open('legendas_pdf.py').read()
a=src.index('# ===== Automações PADRÃO'); b=src.index('posts = [')
ns={}; exec(src[a:b], ns); AUTO=ns['AUTO_STD']
FONTS=open('c1/fonts_embedded.css').read()
LOGO='data:image/png;base64,'+base64.b64encode(open('ck/logo_sem_tagline.png','rb').read()).decode()
e=html.escape
secs=[('CONSULTORIA e DIAGNÓSTICO','Mesmo fluxo para as duas palavras. Presente: Direcional de Marketing e Negócios → oferta: Diagnóstico Recria.','DIAGNÓSTICO'),
      ('RECRIA ADS','Presente: Checklist Venda sem Parecer Chato → oferta: curso Recria Ads.','RECRIA ADS'),
      ('CHECKLIST','Presente: Checklist Black Friday 2026 → oferta: gestão de tráfego / pacote inicial.','CHECKLIST')]
body=''.join(f'<h2>{e(t)}</h2><p class="d">{e(d)}</p>'+''.join(f'<div class="msg"><b>{e(k.split(" · ",1)[1])}</b>{e(v)}</div>' for k,v in AUTO[key]) for t,d,key in secs)
doc=f'''<!doctype html><html><head><meta charset="utf-8"><title>Automações padrão · Agência Recria</title><style>{FONTS}
@page{{size:A4;margin:18mm}} body{{font-family:'Lora';font-size:11pt;line-height:1.5;color:#1a1a1a}}
.head{{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #C9A24E;padding-bottom:10px;margin-bottom:14px}}
.head img{{height:54px;background:#0b0b0b;padding:8px 12px;border-radius:4px}} h1{{font-family:'Playfair Display';font-size:22pt;margin:0 0 6px}}
h2{{font-family:'Playfair Display';font-size:15pt;margin:22px 0 4px;color:#0b0b0b;break-after:avoid}} .d{{color:#9a7424;font-style:italic;margin:0 0 10px}}
.msg{{margin-bottom:10px;padding:8px 12px;background:#F6F2EA;border-left:3px solid #C9A24E;page-break-inside:avoid}} .msg b{{display:block;color:#5a4412;font-size:9.5pt}}
.intro{{background:#0b0b0b;color:#E4C988;padding:12px 16px;border-radius:4px}}</style></head><body>
<div class="head"><img src="{LOGO}"><div style="text-align:right;font-size:9pt;color:#8a6d2c;letter-spacing:.08em">AGÊNCIA RECRIA<br>AUTOMAÇÕES DO INSTAGRAM</div></div>
<h1>Automações padrão por palavra-chave</h1>
<p class="intro">Estas mensagens não citam nenhum post específico, então funcionam para qualquer carrossel que use a mesma palavra-chave. Configure uma vez por palavra e reutilize. Itens entre [colchetes] são arquivos ou links a anexar.</p>
{body}</body></html>'''
out=pathlib.Path('/home/user/recria-clientes/agencia-recria/Automacoes padrao - Agencia Recria.pdf')
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'); pg=br.new_page()
    pg.set_content(doc,wait_until='networkidle'); pg.pdf(path=str(out),format='A4',print_background=True); br.close()
print(out)
