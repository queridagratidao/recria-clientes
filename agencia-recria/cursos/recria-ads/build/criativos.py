import pathlib, base64
from playwright.sync_api import sync_playwright
S=pathlib.Path(__file__).parent
OUT=pathlib.Path('/home/user/recria-clientes/agencia-recria/cursos/recria-ads/criativos'); OUT.mkdir(parents=True,exist_ok=True)
F=(S/'c1/fonts_embedded.css').read_text()
b64=lambda p:'data:image/png;base64,'+base64.b64encode(pathlib.Path(p).read_bytes()).decode()
ICON=b64(S/'ck/logo_icone.png')
CSS=F+"""*{margin:0;padding:0;box-sizing:border-box}
.c{width:1080px;height:1350px;position:relative;padding:130px 96px 130px;display:flex;flex-direction:column;justify-content:center;font-family:'Lora';overflow:hidden}
.d{background:radial-gradient(ellipse at 15% 0%,#2a2214 0%,#0b0b0b 55%),#0b0b0b;color:#fff}
.l{background:#F6F2EA;color:#111}
.logo{position:absolute;top:56px;left:96px;height:74px}
.tag{position:absolute;top:78px;right:96px;font-size:22px;letter-spacing:.2em;font-weight:600;color:#C9A24E}
.foot{position:absolute;bottom:52px;left:96px;right:96px;display:flex;justify-content:space-between;font-size:22px;color:#C9A24E;opacity:.85}
.l .foot{color:#8a6d2c}
h1{font-family:'Playfair Display';font-weight:700;font-size:116px;line-height:1.04;margin-bottom:34px}
h2{font-family:'Playfair Display';font-weight:700;font-size:86px;line-height:1.1;margin-bottom:30px}
em{font-style:italic;color:#E4C988}.l em{color:#9a7424}
p{font-size:43px;line-height:1.42;margin-bottom:20px}.d p{color:#e9e4da}.l p{color:#2a2a2a}
.box{background:#0b0b0b;color:#E4C988;border-left:8px solid #C9A24E;padding:30px 36px;font-family:'Playfair Display';font-style:italic;font-size:44px;line-height:1.35;margin:18px 0}
.d .box{background:rgba(201,162,78,.08);border:2px solid #C9A24E;border-left:8px solid #C9A24E}
.cta{display:inline-block;background:#C9A24E;color:#0b0b0b;font-weight:700;font-size:34px;padding:22px 40px;border-radius:8px;margin-top:22px;align-self:flex-start}
ul{list-style:none}li{font-size:42px;line-height:1.4;margin-bottom:18px;padding-left:58px;position:relative}
li:before{content:'☐';position:absolute;left:0;color:#C9A24E}
li.ok:before{content:'✓'}
.post{background:#fff;border-radius:14px;padding:30px 34px;margin-bottom:28px;box-shadow:0 4px 18px rgba(0,0,0,.08);font-size:39px;line-height:1.35}
.post small{display:block;font-size:22px;color:#8a6d2c;letter-spacing:.12em;margin-bottom:10px;font-weight:600}
.seal{width:250px;height:250px;border-radius:50%;border:6px solid #C9A24E;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#C9A24E;font-family:'Playfair Display';font-weight:700;font-size:120px;line-height:1;margin-bottom:40px;padding-top:10px}
.seal small{font-size:30px;letter-spacing:.15em;line-height:1;margin-top:6px}
.n{font-family:'Playfair Display';font-size:30px;color:#C9A24E;letter-spacing:.1em;margin-bottom:16px}
"""
def card(cls,body,tag='RECRIA ADS',n=''):
    return f'<div class="c {cls}"><img class="logo" src="{ICON}"><div class="tag">{tag}</div>{body}<div class="foot"><span>@agencia.recria × @amandarecria</span><span>{n}</span></div></div>'
C={}
C['estatico-01-todo-mundo-pula-anuncio']=card('d','<h1>Todo mundo pula anúncio. <em>Inclusive você.</em></h1><p>Mas para por uma boa história. Aprenda a criar conteúdos e anúncios que as pessoas param para ver.</p><div class="cta">Conheça o Recria Ads</div>')
C['estatico-02-qual-voce-pararia']=card('l','<h2>Qual você <em>pararia para ler?</em></h2><div class="post"><small>POST A</small>🔥 PROMOÇÃO IMPERDÍVEL! 20% OFF só hoje!!! Corre!!!</div><div class="post"><small>POST B</small>"A cliente entrou aqui dizendo que já tinha tentado de tudo. E saiu chorando de alegria…"</div><p>No Recria Ads, você aprende a criar o post B. <b>Todo santo dia.</b></p>')
C['estatico-03-10-minutos']=card('d','<h1>10 minutos por dia. <em>1 mês.</em></h1><p>É o que você precisa para ter o seu marketing sem cara de anúncio aplicado no seu negócio.</p><ul><li class="ok">1 aula curta por dia</li><li class="ok">1 módulo por semana, com atividades</li><li class="ok">Calendário e Plano de 30 dias prontos</li></ul>')
C['estatico-04-checklist-cara-de-anuncio']=card('l','<h2>O seu conteúdo tem <em>cara de anúncio</em> se:</h2><ul><li>Começa falando do produto</li><li>Tem preço no primeiro segundo</li><li>Usa "imperdível" e "corre"</li><li>Ninguém comenta</li><li>Nem você pararia para ver</li></ul><div class="box">Marcou 2 ou mais? O Recria Ads é para você.</div>')
C['estatico-05-metodologia-da-agencia']=card('d','<p style="font-size:34px;color:#C9A24E;letter-spacing:.15em">PELA PRIMEIRA VEZ</p><h2>"Eu vou abrir a <em>metodologia da minha agência</em> para você."</h2><p>A mesma que hoje só os nossos clientes têm acesso. Mais de 10 anos de prática, agora para você aplicar no seu negócio.</p><p style="font-family:\'Playfair Display\';font-style:italic;color:#E4C988">Amanda, CEO da Agência Recria</p>')
C['estatico-06-verba-de-marca-grande']=card('l','<h2>Você não precisa da verba de uma <em>marca grande.</em></h2><div class="box">Precisa de uma boa história.</div><p>Aprenda a vender sem parecer vendedor chato, com o seu celular e com o orçamento que você tem.</p><div class="cta">Conheça o Recria Ads</div>')
# remarketing
C['remarketing-01-ainda-pensando']=card('d','<h1>Ainda <em>pensando?</em></h1><p>São só 10 minutos por dia. Em cerca de 1 mês, você terá tudo aplicado no seu negócio.</p><div class="box">E você tem 7 dias de garantia.</div><div class="cta">Quero entrar</div>','REMARKETING')
C['remarketing-02-nao-gosto-de-aparecer']=card('l','<h2>"Eu não gosto de <em>aparecer.</em>"</h2><p>Você não precisa. No Recria Ads você aprende a criar conteúdo com:</p><ul><li class="ok">As suas mãos e o seu processo</li><li class="ok">A sua equipe</li><li class="ok">Os bastidores</li><li class="ok">Microinfluenciadores</li></ul>','REMARKETING')
C['remarketing-03-garantia']=card('d','<div class="seal">7<small>DIAS</small></div><h2>Garantia de <em>7 dias.</em></h2><p>Se não for para você, é só pedir o reembolso. Simples assim.</p><div class="cta">Começar o Recria Ads</div>','REMARKETING')
C['remarketing-04-sem-verba']=card('l','<h2>"Não tenho verba para <em>anúncio.</em>"</h2><p>Tem estratégia para quem investe R$ 0 e para quem já investe. Toda aula mostra como adaptar ao seu cenário.</p><div class="box">Eupresa · negócio local · e-commerce · empresa média · empresa grande · serviços</div>','REMARKETING')
# carrossel
car=[('d','<p class="n">RECRIA ADS</p><h1>Você posta todo dia e <em>ninguém compra?</em></h1><p>Não é o algoritmo. Arrasta →</p>'),
('l','<h2>O problema: o seu post tem <em>cara de anúncio.</em></h2><p>E o cérebro de quem rola o feed aprendeu a pular anúncio no automático.</p>'),
('d','<h2>A emoção decide. <em>A razão justifica.</em></h2><p>Primeiro a pessoa sente. Depois ela procura argumentos para comprar. Se o seu post começa pela ficha técnica, ela nem chega a sentir.</p>'),
('l','<h2>Olha a <em>diferença:</em></h2><div class="post"><small>ANÚNCIO</small>"Bolo de ninho com morango. R$ 90. Encomende!"</div><div class="post"><small>HISTÓRIA</small>"A mãe chegou com a foto de um bolo que ela viu no aniversário dos 7 anos…"</div>'),
('d','<h2>As marcas que mais vendem <em>já entenderam isso.</em></h2><p>Toyota, Boticário, Burger King: venderam sem parecer que estavam vendendo.</p>'),
('l','<h2>E dá para fazer <em>no seu negócio.</em></h2><p>Com o seu celular. Com o orçamento que você tem. Em 10 minutos por dia.</p>'),
('d','<p class="n">RECRIA ADS</p><h2>Aprenda a criar conteúdos e anúncios <em>sem cara de anúncio.</em></h2><p>A metodologia da Agência Recria, aberta pela primeira vez.</p><div class="cta">Toque em Saiba mais</div>')]
for i,(cls,body) in enumerate(car,1): C[f'carrossel-card-{i:02d}']=card(cls,body,'',f'{i:02d}/07')
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg=b.new_page(viewport={'width':1080,'height':1350})
    for k,h in C.items():
        pg.set_content(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{h}</body></html>'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(150)
        # check overflow
        ov=pg.evaluate("()=>{const c=document.querySelector('.c');return c.scrollHeight>c.clientHeight+2}")
        if ov: print('OVERFLOW',k)
        pg.screenshot(path=str(OUT/f'{k}.png'))
    b.close()
print(len(C))
