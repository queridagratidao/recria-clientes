import base64, pathlib, sys, subprocess
from playwright.sync_api import sync_playwright
import imageio_ffmpeg

D = pathlib.Path(__file__).parent
IMG = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None
VIDEO = '/root/.claude/uploads/aab0d86f-b2b3-5ec4-a49a-0609f7853360/a01dc814-snapinsta-1790619124144.mp4'
CUTS = [(0, 58), (58, 105), (105, None)]  # cortes nas pausas naturais: antes de "É aí que entra" e de "E foi por isso"
b64 = lambda p, m: f"data:{m};base64," + base64.b64encode(p.read_bytes()).decode()
LOGO = b64(D / 'logo.png', 'image/png')
COVER = b64(IMG, 'image/jpeg' if IMG and IMG.suffix.lower() in ('.jpg', '.jpeg') else 'image/png') if IMG else ''
TOTAL = 10
VX, VY, VW, VH = 96, 250, 405, 720

CSS = (D / "fonts_embedded.css").read_text() + """
*{margin:0;padding:0;box-sizing:border-box}
:root{--gold:#C9A24E;--gold2:#E4C988;--paper:#F6F2EA}
body{width:1080px;height:1350px;overflow:hidden;font-family:'Lora',serif}
.card{position:relative;width:1080px;height:1350px;padding:150px 96px 130px;display:flex;flex-direction:column;justify-content:center}
.dark{background:radial-gradient(ellipse at 15% 0%,#2a2214 0%,#0b0b0b 55%),#0b0b0b;color:#fff}
.light{background:var(--paper);color:#111}
.logo{position:absolute;top:56px;left:80px;height:80px}
.foot{position:absolute;bottom:52px;left:96px;right:96px;display:flex;justify-content:space-between;font-size:22px;letter-spacing:.04em;opacity:.75}
.dark .foot{color:var(--gold2)} .light .foot{color:#8a6d2c}
.kick{font-weight:600;font-size:26px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);margin-bottom:22px}
.light .kick{color:#9a7424}
h1{font-family:'Playfair Display';font-weight:700;font-size:60px;line-height:1.13;margin-bottom:30px}
p{font-size:31px;line-height:1.5;margin-bottom:20px}
.dark p{color:#e9e4da} .light p{color:#2a2a2a}
b{font-weight:600} .dark b{color:#fff}
em.g{font-style:italic;color:var(--gold2)} .light em.g{color:#9a7424}
q{quotes:none;font-family:'Playfair Display';font-style:italic} .dark q{color:var(--gold2)} .light q{color:#7a5c1c}
.next{font-family:'Playfair Display';font-style:italic;font-size:31px;color:var(--gold2);margin-top:8px}
.light .next{display:inline-block;align-self:flex-start;background:#0b0b0b;color:var(--gold2);padding:22px 30px;border-left:6px solid var(--gold);margin-top:14px;line-height:1.35}
ul,ol{margin:4px 0 16px}
ul{list-style:none}
li{font-size:29px;line-height:1.42;margin-bottom:16px;padding-left:40px;position:relative}
ul li:before{content:'';position:absolute;left:0;top:15px;width:15px;height:15px;border-radius:50%;background:var(--gold)}
ol{list-style:none;counter-reset:n} ol li{counter-increment:n} ol li:before{content:counter(n);position:absolute;left:0;top:0;font-family:'Playfair Display';font-weight:700;color:var(--gold)}
.dark li{color:#e9e4da} .light li{color:#2a2a2a}
.cm{border-left:4px solid var(--gold);padding:14px 22px;margin-bottom:16px;background:rgba(201,162,78,.08);font-size:27px;line-height:1.4}
.cm small{display:block;font-size:20px;color:var(--gold);margin-top:6px;font-style:normal}
.box{border:2px solid var(--gold);padding:24px 40px;margin:6px 0 26px;background:rgba(201,162,78,.06)}
.box small{display:block;font-weight:600;font-size:22px;letter-spacing:.2em;color:var(--gold);margin-bottom:4px}
.box strong{font-family:'Playfair Display';font-weight:700;font-size:78px;color:var(--gold2)}
.side{margin-left:452px;width:436px}
.side p{font-size:26px;margin-bottom:14px}
.side .next{font-size:27px}
"""

def page(cls, inner, n, extra='', frame=False):
    foot = f'<div class="foot"><span>@agencia.recria &nbsp;×&nbsp; @amandarecria</span><span>{n:02d} / {TOTAL:02d}</span></div>'
    fr = f'<div style="position:absolute;left:{VX-8}px;top:{VY-8}px;width:{VW+16}px;height:{VH+16}px;border:2px solid var(--gold);border-radius:6px"></div>' if frame else ''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{extra}</style></head><body><div class="card {cls}"><img class="logo" src="{LOGO}">{inner}{fr}{foot}</div></body></html>'

cards = []
cards.append(f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
.cover{{position:relative;width:1080px;height:1350px;background:#000 url({COVER}) center top/cover no-repeat}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,0) 18%,rgba(0,0,0,0) 46%,rgba(0,0,0,.85) 64%,#000 80%)}}
.txt{{position:absolute;left:84px;right:84px;bottom:108px}}
.ck{{font-weight:600;font-size:25px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold2);margin-bottom:18px}}
.t1{{font-family:'Playfair Display';font-weight:800;font-size:58px;line-height:1.08;color:#fff}}
.t1 em{{font-style:italic;color:var(--gold)}}
.sub{{font-family:'Playfair Display';font-style:italic;font-size:29px;line-height:1.35;color:#eee;margin-top:22px}}
.sub b{{color:var(--gold2);font-style:normal}}
.rule{{width:170px;height:3px;background:var(--gold);margin:22px 0 0}}
</style></head><body><div class="cover"><div class="shade"></div><img class="logo" src="{LOGO}">
<div class="txt"><div class="ck">Marketing de causa + inimigo em comum</div><div class="t1">A ciência estudou apenas o corpo masculino. <em>O Boticário decidiu corrigir isso.</em></div><div class="rule"></div>
<div class="sub">Como a marca usou a credibilidade da <b>Mari Krüger</b> para se diferenciar no mercado da beleza e cativar o público feminino →</div></div>
<div class="foot" style="color:var(--gold2)"><span>@agencia.recria &nbsp;×&nbsp; @amandarecria</span><span>01 / {TOTAL:02d}</span></div></div></body></html>''')

cards.append(page('dark', '''<div class="side">
<div class="kick">O POV</div>
<p>A bióloga e criadora de conteúdo Mari Krüger (<span style="color:var(--gold2)">@marikrugerb</span>) abre com um POV: <q>"Fecha essa perna. Emagrece, mas não demais. Seja você mesma. Não, assim também não."</q></p>
<p>Nenhuma marca aparece. Só identificação.</p>
<p>E logo vem o <b>vilão em comum</b>: por muito tempo, a ciência tratou o corpo do homem como padrão.</p>
<div class="next">Mulheres são diagnosticadas mais tarde em mais de 700 condições →</div></div>''', 2, frame=True))

cards.append(page('light', '''<div class="side">
<div class="kick">A virada</div>
<p>Aí entra o Grupo Boticário: o <b>Centro de Pesquisa da Mulher</b>, dedicado ao corpo feminino e aos seus ciclos.</p>
<p>Uma das pesquisas ouviu <b>1.200 brasileiras de 14 a 65 anos</b> sobre o ciclo menstrual: 38% relataram espinhas, 19% mudanças na pele e mais de 11% mudanças no cabelo.</p>
<div class="next" style="font-size:25px">Não é só campanha. É produto pensado a partir do corpo de quem compra.</div></div>''', 3, frame=True))

cards.append(page('dark', '''<div class="side">
<div class="kick">Por que a Mari?</div>
<ul>
<li style="font-size:25px">ela já ensina ciência com humor para mais de 3 milhões de pessoas</li>
<li style="font-size:25px">a credibilidade dela vira a credibilidade da marca</li>
<li style="font-size:25px">é uma <b>série</b>: o primeiro episódio já promete os próximos (loop aberto)</li>
<li style="font-size:25px">e fecha pedindo participação: <q>"Opinião vocês já receberam demais. Agora eu quero dado."</q></li>
</ul></div>''', 4, frame=True))

cards.append(page('light', '''
<h1>O público <em class="g">respondeu.</em></h1>
<div class="cm">"Existem mais estudos sobre calvície masculina do que sobre endometriose!"<small>3.900 curtidas no comentário</small></div>
<div class="cm">"Até o cinto de segurança e a temperatura do ar-condicionado foram pensados no corpo do homem."</div>
<div class="cm">"Orgulho dessa iniciativa! Vamos juntas."<small>@eudora, marca do próprio grupo</small></div>
<p style="margin-top:8px">E o Grupo Boticário respondeu os comentários, puxando os próximos capítulos.</p>
<div class="next">Comunidade não se compra. Se constrói.</div>''', 5))

cards.append(page('dark', '''
<h1>"Mas isso não é <em class="g">oportunismo?</em>"</h1>
<p>Seria, se fosse só discurso. Aqui a causa é coerente com:</p>
<ul>
<li><b>o público:</b> majoritariamente feminino</li>
<li><b>o produto:</b> cosméticos que agem na pele e no cabelo, que mudam ao longo do ciclo</li>
<li><b>a prova:</b> pesquisa com dado, não só opinião</li>
</ul>
<div class="next">Causa sem coerência vira tiro no pé. Com coerência, vira diferenciação.</div>''', 6))

cards.append(page('light', '''
<div class="kick">Quando falta coerência</div>
<h1 style="font-size:52px">Levantar uma bandeira que você não sustenta custa caro.</h1>
<p style="font-size:28px">Em abril de 2023, a cerveja Bud Light fez uma ação com uma influenciadora que não conversava com o seu público central. Veio o boicote. E a marca, em vez de sustentar a escolha, recuou, e desagradou os dois lados.</p>
<p style="font-size:28px">As vendas caíram mais de 25% em poucas semanas, e em junho ela perdeu o posto de cerveja mais vendida dos EUA, que ocupava havia mais de 20 anos.</p>
<div class="next" style="font-size:28px">O problema não é se posicionar. É se posicionar sem coerência e sem sustentação.</div>''', 7))

cards.append(page('dark', '''
<h1 style="font-size:54px">Antes de levantar uma bandeira, <em class="g">responda:</em></h1>
<ol>
<li>O meu público se importa com isso de verdade?</li>
<li>Tem a ver com o que eu vendo?</li>
<li>Consigo provar com ação, não só com post?</li>
<li>Consigo sustentar por meses, não por um dia?</li>
<li>Estou preparada para quem discordar?</li>
</ol>
<div class="next">Poucas causas, bem defendidas, valem mais que todas as pautas do momento.</div>''', 8))

cards.append(page('light', '''
<h1>Uma marca com décadas de mercado, <em class="g">ainda se reinventando.</em></h1>
<p>E você não precisa ser grande para fazer o mesmo:</p>
<ul>
<li>uma pesquisa com os seus próprios clientes</li>
<li>uma dor que o seu mercado ignora</li>
<li>uma pessoa de confiança contando a história: você, alguém da equipe ou um influenciador local</li>
</ul>
<div class="next">Posicionamento não é tamanho. É coerência e criatividade.</div>''', 9))

cards.append(page('dark', '''
<h1 style="font-size:50px;margin-bottom:22px">Quer descobrir o melhor posicionamento <em class="g">para o momento do seu negócio?</em></h1>
<div class="box"><small>COMENTE:</small><strong>DIAGNÓSTICO</strong></div>
<p style="font-size:27px">E receba um presente direto no seu direct: um <b>direcional de marketing e negócios</b> da Agência Recria. 🎁 E, se você já estiver pronta para dar um passo além, te apresentamos o Diagnóstico Recria, a nossa consultoria online personalizada para o seu negócio.</p>
<p style="font-size:26px;font-style:italic;color:var(--gold2);margin-bottom:0">Quer aprender a criar conteúdos e anúncios sem cara de anúncio? Comente <b style="color:var(--gold2)">RECRIA ADS</b> e receba um presente e todas as informações sobre o nosso curso.</p>''', 10))

out = D / 'out'; out.mkdir(exist_ok=True)
with sync_playwright() as p:
    br = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg = br.new_page(viewport={'width': 1080, 'height': 1350})
    for i, html in enumerate(cards, 1):
        if i == 1 and not IMG:
            continue
        pg.set_content(html, wait_until='networkidle'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        pg.screenshot(path=str(out / f'card-{i:02d}.png'))
    br.close()

FF = imageio_ffmpeg.get_ffmpeg_exe()
for n, (a, b) in zip((2, 3, 4), CUTS):
    base = out / f'card-{n:02d}.png'
    (out / f'card-{n:02d}-base-para-canva.png').write_bytes(base.read_bytes())
    t = ['-t', str(b - a)] if b else []
    subprocess.run([FF, '-y', '-loglevel', 'error', '-loop', '1', '-i', str(base), '-ss', str(a), *t, '-i', VIDEO,
        '-filter_complex', f'[1:v]scale={VW}:{VH}[v];[0:v][v]overlay={VX}:{VY}:shortest=1,format=yuv420p[o]',
        '-map', '[o]', '-map', '1:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-r', '30',
        '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', str(out / f'card-{n:02d}-video.mp4')], check=True)
print('done')
