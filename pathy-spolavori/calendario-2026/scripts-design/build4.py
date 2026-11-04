import pathlib, asyncio
from playwright.async_api import async_playwright
src=open('build2.py',encoding='utf-8').read()
ns={}; exec(src[:src.index('cards=[')],ns)
D,base,photo,chev,habit=ns['D'],ns['base'],ns['photo'],ns['chev'],ns['habit']
BOX_CSS="""
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(30,18,14,0) 40%,rgba(30,18,14,.55) 62%,rgba(30,18,14,.9) 100%)}
.box{position:absolute;left:72px;right:72px;bottom:120px;color:#fff}
.inner{display:inline-block}
h1{font:600 60px/1.15 PF;margin-bottom:22px}
.n{font-family:LO;font-weight:500}
.sub{font:500 34px/1.4 LO;color:#F3DDD0;width:0;min-width:100%}
.pill{display:inline-block;margin-top:28px;font:600 24px MS;letter-spacing:.06em;border:2px solid #fff;border-radius:40px;padding:12px 26px}
"""
def static(img,h1,sub,size=60):
    return photo(img,f"""<div class=shade></div>
<div class="handle" style="top:60px;left:72px;color:#fff;opacity:.9">@paticompagnoni</div>
<div class=box><div class=inner><h1 style="font-size:{size}px">{h1}</h1><p class=sub>{sub}</p></div>
<div><span class=pill>leia a legenda &darr;</span></div></div>""",BOX_CSS)
def cover(img,h1,sub):
    return photo(img,f"""<div class=shade></div>
<div class="handle" style="top:60px;left:72px;color:#fff;opacity:.9">@paticompagnoni</div>
<div class=box style="bottom:150px"><div class=inner><h1>{h1}</h1><p class=sub>{sub}</p></div></div>
<div class=swipe>{chev('#fff')}</div>""",BOX_CSS)
def cta(img,h3,p,left=True,bottom=False):
    side=('left:26px' if left else 'right:26px')+(';top:auto;bottom:40px;transform:none' if bottom else '')
    return photo(img,f"""<div class=panel><h3>{h3} <span style="color:#B07A63">&#9825;</span></h3><p>{p}</p><span class=hd>@paticompagnoni</span></div>""",f"""
.panel{{position:absolute;top:50%;transform:translateY(-50%);{side};width:350px;background:rgba(244,237,230,.94);border-radius:28px;padding:44px 40px}}
h3{{font:600 41px/1.18 PF;margin-bottom:22px}}
.panel p{{font:400 29px/1.5 MS;margin-bottom:24px}}
.hd{{font:600 24px MS;letter-spacing:.06em;color:#B07A63}}""")
def slot(n):
    return f"""<html><head><style>{base}
body{{background:#F4EDE6;display:flex;flex-direction:column;padding:80px 80px 56px}}
.group{{flex:1;display:flex;flex-direction:column;justify-content:center}}
.tag{{align-self:flex-start;background:#B07A63;color:#fff;font:600 26px MS;letter-spacing:.06em;padding:12px 22px;border-radius:6px}}
h2{{font:600 72px/1.1 PF;margin:28px 0 8px;color:#9C7B6C}}
.at{{font:500 32px MS;color:#B07A63;margin-bottom:34px}}
.print{{height:470px;border:3px dashed #D4B9AA;border-radius:22px;display:flex;align-items:center;justify-content:center;text-align:center;font:500 30px/1.4 MS;color:#9C7B6C;background:#FBF7F3}}
.why{{margin-top:34px;font:400 33px/1.5 MS}}.why b{{font-weight:600;color:#B07A63}}
.foot{{display:flex;justify-content:space-between;align-items:center;font:500 24px MS;letter-spacing:.06em;color:#9C7B6C;margin-top:30px}}
</style></head><body><div class=group>
<span class=tag># 0{n}</span><h2>[Nome da profissional]</h2><div class=at>@perfil · especialidade</div>
<div class=print>Print do perfil aqui<br><small style="font-size:24px">(a Pathy envia a indicação)</small></div>
<p class=why><b>Por que eu indico:</b> [uma frase da Pathy sobre o que aprende com ela]</p>
</div><div class=foot><span>@paticompagnoni</span>{chev('#B07A63')}</div></body></html>"""
def sol(n,title,text,study,ref):
    return f"""<html><head><style>{base}
body{{background:#F4EDE6;display:flex;flex-direction:column;padding:80px 80px 56px}}
.group{{flex:1;display:flex;flex-direction:column;justify-content:center}}
.tag{{align-self:flex-start;background:#B07A63;color:#fff;font:600 26px MS;letter-spacing:.06em;padding:12px 22px;border-radius:6px}}
h2{{font:600 68px/1.12 PF;margin:28px 0 36px}}
.row{{font:400 34px/1.5 MS}}
.study{{margin-top:40px;background:#fff;border-radius:22px;padding:34px 38px;box-shadow:0 18px 50px rgba(80,50,35,.12)}}
.lab{{font:600 20px MS;letter-spacing:.14em;text-transform:uppercase;color:#B07A63;margin-bottom:14px}}
.study p{{font:400 31px/1.5 MS}}.ref{{font:500 italic 24px/1.4 LO;color:#9C7B6C;margin-top:16px}}
.foot{{display:flex;justify-content:space-between;align-items:center;font:500 24px MS;letter-spacing:.06em;color:#9C7B6C;margin-top:30px}}
</style></head><body><div class=group><span class=tag># 0{n}</span><h2>{title}</h2><p class=row>{text}</p>
<div class=study><div class=lab>o que a ciência diz</div><p>{study}</p><p class=ref>{ref}</p></div></div>
<div class=foot><span>@paticompagnoni</span>{chev('#B07A63')}</div></body></html>"""

cards=[
 ('nb-11',static('n_nb11.jpg','Sou estudante de biomedicina e estes são 3 hábitos que eu sigo à risca para cuidar da minha pele','e que você também pode aprender.',56)),
 ('nb-25',static('n_nb25.jpg','Você não envelhece aos poucos, você envelhece em saltos…','E como usar isso a seu favor?',62)),
 ('d03-1',cover('n_d03capa.jpg','Profissionais da estética que eu sigo de olhos fechados','E que vão te ensinar muito sobre pele.')),
 ('d03-2',slot(1)),('d03-3',slot(2)),('d03-4',slot(3)),
 ('d03-5',cta('n_d03cta.jpg','Mulher, qual profissional você também indica?','Me conta nos comentários e marca ela aqui.',left=False,bottom=True)),
 ('d10',static('n_d10b.jpg','A sua pele sabe quando você está estressada.','E isso afeta a proteção e a cicatrização dela. Mas dá para reduzir os danos.',62)),
 ('d17-1',cover('n_d17capa.jpg','4 coisas sobre o sol que quase ninguém sabe','Antes de curtir o verão, arrasta para o lado.')),
 ('d17-2',sol(1,'Você provavelmente passa só um terço do protetor','A proteção do rótulo é testada com uma camada bem mais grossa do que a maioria das pessoas usa.',
   'Na prática, as pessoas aplicam cerca de um terço da quantidade testada e recebem só uns 40% da proteção esperada.','Young et al., Acta Dermato-Venereologica, 2018')),
 ('d17-3',sol(2,'O sol atravessa o vidro do carro','O vidro da janela segura boa parte dos raios que queimam, mas deixa passar o UVA, ligado ao envelhecimento da pele.',
   'Um caminhoneiro de 69 anos, que dirigiu por mais de 25 anos, tinha o lado do rosto virado para a janela muito mais envelhecido.','Gordon & Brieva, New England Journal of Medicine, 2012')),
 ('d17-4',sol(3,'Limão e sol podem manchar a pele por meses','O suco do limão na pele (na caipirinha, no tempero, na praia) reage com o sol.',
   'Substâncias do limão, as furocumarinas, junto com o sol causam a fitofotodermatite: vermelhidão, bolhas e manchas que podem durar meses.','National Capital Poison Center (EUA)')),
 ('d17-5',sol(4,'Não precisa fugir do sol, precisa não se queimar','O risco está nas queimaduras. A recomendação é evitar o sol das 10h às 16h e ficar de olho nas pintas.',
   'Mulheres com 5 ou mais queimaduras com bolhas entre os 15 e os 20 anos tiveram 80% mais risco de melanoma na vida adulta.','Wu et al., Cancer Epidemiology, Biomarkers & Prevention, 2014 · Sociedade Brasileira de Dermatologia')),
 ('d17-6',cta('c2_cta.jpg','Mulher, qual dessas foi novidade para você?','Me conta nos comentários e salva para o verão.')),
 ('d24',static('n_d24b.jpg','Encontrar as amigas no fim de ano também é cuidar da saúde.','E a ciência tem números para isso.',60)),
]
async def main():
    out=D/'out4'; out.mkdir(exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium' if pathlib.Path('/opt/pw-browsers/chromium').is_file() else None)
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        for name,html in cards:
            f=D/f'{name}.html'; f.write_text(html,encoding='utf-8')
            await pg.goto(f.as_uri()); await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=str(out/f'{name}.png'))
        await b.close()
asyncio.run(main())
