import pathlib, asyncio, re
from playwright.async_api import async_playwright
src=open('build.py',encoding='utf-8').read()
ns={}
exec(src[:src.index('cover=photo(')],ns)   # reuse fonts, base styles and photo() helper
D,base,photo=ns['D'],ns['base'],ns['photo']
def chev(c):
    p=lambda x,o: f'<path d="M{x} 6 L{x+9} 15 L{x} 24" fill="none" stroke="{c}" stroke-opacity="{o}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
    return f'<svg class=wave viewBox="0 0 48 30" width="64" height="40">{p(4,.3)}{p(18,.6)}{p(32,1)}</svg>'

cover=photo('c2_capa.jpg',f"""
<div class=shade></div>
<div class="handle" style="top:60px;left:72px;color:#fff;opacity:.9">@paticompagnoni</div>
<div class=box><div class=inner>
  <h1>Hábitos que eu jamais tiro<br>da minha rotina depois dos <span class=n>40</span></h1>
  <p class=sub>São simples, mas nem sempre fáceis.<br>E a sua saúde agradece.</p>
</div></div>
<div class=swipe>{chev('#fff')}</div>""","""
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(30,18,14,0) 42%,rgba(30,18,14,.55) 64%,rgba(30,18,14,.9) 100%)}
.box{position:absolute;left:72px;right:72px;bottom:150px;color:#fff}
.inner{display:inline-block}
h1{font:600 60px/1.15 PF;margin-bottom:24px}
.n{font-family:LO;font-weight:500}
.sub{font:500 34px/1.4 LO;color:#F3DDD0;width:0;min-width:100%}
""")

def habit(n,name,simples,facil,estudo,ref):
    return f"""<html><head><style>{base}
body{{background:#F4EDE6;display:flex;flex-direction:column;padding:80px 80px 56px}}
.group{{flex:1;display:flex;flex-direction:column;justify-content:center}}
.tag{{align-self:flex-start;background:#B07A63;color:#fff;font:600 26px MS;letter-spacing:.06em;padding:12px 22px;border-radius:6px}}
h2{{font:600 84px/1.08 PF;margin:28px 0 46px}}
.row{{font:400 35px/1.5 MS;margin-bottom:28px}}
.row b{{font-weight:600;color:#B07A63}}
.study{{margin-top:22px;background:#fff;border-radius:22px;padding:34px 38px;box-shadow:0 18px 50px rgba(80,50,35,.12)}}
.lab{{font:600 20px MS;letter-spacing:.14em;text-transform:uppercase;color:#B07A63;margin-bottom:14px}}
.study p{{font:400 31px/1.5 MS}}
.ref{{font:500 italic 24px/1.4 LO;color:#9C7B6C;margin-top:16px}}
.foot{{display:flex;justify-content:space-between;align-items:center;font:500 24px MS;letter-spacing:.06em;color:#9C7B6C;margin-top:30px}}
</style></head><body>
<div class=group>
 <span class=tag># 0{n}</span>
 <h2>{name}</h2>
 <p class=row><b>Simples:</b> {simples}</p>
 <p class=row><b>Fácil?</b> {facil}</p>
 <div class=study><div class=lab>o que a ciência diz</div><p>{estudo}</p><p class=ref>{ref}</p></div>
</div>
<div class=foot><span>@paticompagnoni</span>{chev('#B07A63')}</div>
</body></html>"""

cards=[('c2-01-capa',cover),
 ('c2-02-treinar',habit(1,'Treinar','é ir até a academia e se movimentar, com orientação de um profissional.','Nem sempre, a preguiça aparece.',
   'Num estudo com 61 mulheres que não faziam exercício, 16 semanas de musculação melhoraram a elasticidade da pele e deixaram a pele mais firme.','Nishikori et al., Scientific Reports, 2023')),
 ('c2-03-dormir',habit(2,'Dormir cedo','se organizar para finalizar as tarefas e ir para a cama mais cedo.','Nem sempre, com faculdade, casa, família e outros compromissos.',
   'Mulheres que dormiam mal tinham mais sinais de envelhecimento na pele, e a pele delas se recuperava mais devagar.','Oyetakin-White et al., Clinical and Experimental Dermatology, 2015')),
 ('c2-04-protetor',habit(3,'Protetor solar todo dia','leva menos de um minuto.','Nem sempre a gente lembra, principalmente dentro de casa e em dias nublados.',
   'Num estudo com 903 adultos acompanhados por quatro anos e meio, quem usou protetor todos os dias teve 24% menos envelhecimento da pele.','Hughes et al., Annals of Internal Medicine, 2013')),
 ('c2-05-arrumar',habit(4,'Cuidar da minha autoestima','um protetor com cor, um blush, uma roupa que eu gosto.','Nem sempre dá vontade.',
   'Num estudo brasileiro, mulheres que passaram a se maquiar com frequência tiveram melhora no humor e na autoimagem.','Veçoso et al., Dermatology and Therapy, 2024')),
 ('c2-06-aprender',habit(5,'Continuar aprendendo','abrir um livro, fazer um curso, voltar a estudar.','Nem sempre, mas foi assim que voltei para a faculdade e hoje faço biomedicina.',
   'Num estudo com 221 adultos de 60 a 90 anos, quem aprendeu uma habilidade nova e desafiadora por 3 meses melhorou a memória. E, segundo a revista The Lancet, até 45% dos casos de demência poderiam ser evitados ou adiados cuidando de 14 fatores, entre eles a baixa escolaridade. A recomendação: manter o cérebro ativo ao longo da vida.','Park et al., Psychological Science, 2014 · Comissão The Lancet sobre demência, 2024')),
 ('c2-07-cta',photo('c2_cta.jpg',"""
<div class=panel>
  <h3>Mulher, qual desses hábitos já faz parte da sua rotina? <span style="color:#B07A63">&#9825;</span></h3>
  <p>Me conta nos comentários.</p>
  <span class=hd>@paticompagnoni</span>
</div>""","""
.panel{position:absolute;left:26px;top:50%;transform:translateY(-50%);width:338px;background:rgba(244,237,230,.94);border-radius:28px;padding:44px 40px}
h3{font:600 41px/1.18 PF;margin-bottom:22px}
.panel p{font:400 29px/1.5 MS;margin-bottom:24px}
.hd{font:600 24px MS;letter-spacing:.06em;color:#B07A63}
""")),
]
async def main():
    out=D/'out2'; out.mkdir(exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium' if pathlib.Path('/opt/pw-browsers/chromium').is_file() else None)
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        for name,html in cards:
            f=D/f'{name}.html'; f.write_text(html,encoding='utf-8')
            await pg.goto(f.as_uri()); await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(500)
            await pg.screenshot(path=str(out/f'{name}.png'))
        await b.close()
asyncio.run(main())
