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
def static(img,h1,sub,size=60,top=False):
    if top:
        return photo(img,f"""<div class=shade style="background:linear-gradient(0deg,rgba(30,18,14,0) 45%,rgba(30,18,14,.55) 70%,rgba(30,18,14,.85) 100%)"></div>
<div class="handle" style="top:auto;bottom:60px;left:72px;color:#fff;opacity:.9">@paticompagnoni</div>
<div class=box style="top:90px;bottom:auto"><div class=inner><h1 style="font-size:{size}px">{h1}</h1><p class=sub>{sub}</p></div>
<div><span class=pill>leia a legenda &darr;</span></div></div>""",BOX_CSS)
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
import base64
def b64(p): return 'data:image/jpeg;base64,'+base64.b64encode(open(D/'src'/p,'rb').read()).decode()
VER='<svg width="34" height="34" viewBox="0 0 24 24" style="vertical-align:-5px;margin-left:8px"><path fill="#3897F0" d="M12 1l2.6 2.2 3.4-.4.9 3.3 3 1.7-1.2 3.2 1.2 3.2-3 1.7-.9 3.3-3.4-.4L12 23l-2.6-2.2-3.4.4-.9-3.3-3-1.7L3.3 13 2.1 9.8l3-1.7.9-3.3 3.4.4z"/><path d="M7.5 12.3l3 3 6-6.3" stroke="#fff" stroke-width="2.2" fill="none"/></svg>'
def slot(n,name,handle,esp,title,bio,av,why):
    return f"""<html><head><style>{base}
body{{background:#F4EDE6;display:flex;flex-direction:column;padding:80px 80px 56px}}
.group{{flex:1;display:flex;flex-direction:column;justify-content:center}}
.tag{{align-self:flex-start;background:#B07A63;color:#fff;font:600 26px MS;letter-spacing:.06em;padding:12px 22px;border-radius:6px}}
h2{{font:600 70px/1.1 PF;margin:28px 0 8px}}
.at{{font:500 31px MS;color:#B07A63;margin-bottom:38px}}
.card{{background:#fff;border-radius:26px;padding:44px 44px 40px;box-shadow:0 18px 50px rgba(80,50,35,.12)}}
.top{{display:flex;align-items:center;gap:36px}}
.av{{width:190px;height:190px;border-radius:50%;padding:7px;background:linear-gradient(45deg,#F9CE34,#EE2A7B,#6228D7);flex:none}}
.av img{{width:100%;height:100%;border-radius:50%;border:6px solid #fff;object-fit:cover;display:block}}
.hn{{font:700 40px MS;color:#111}}.tt{{font:500 27px/1.35 MS;color:#555;margin-top:10px}}
.bio{{font:400 28px/1.45 MS;color:#262626;margin-top:30px}}
.btn{{margin-top:30px;background:#4A5DF9;color:#fff;font:600 28px MS;text-align:center;border-radius:14px;padding:18px}}
.why{{margin-top:38px;font:400 33px/1.5 MS}}.why b{{font-weight:600;color:#B07A63}}
.foot{{display:flex;justify-content:space-between;align-items:center;font:500 24px MS;letter-spacing:.06em;color:#9C7B6C;margin-top:30px}}
</style></head><body><div class=group>
<span class=tag># 0{n}</span><h2>{name}</h2><div class=at>@{handle} · {esp}</div>
<div class=card><div class=top><div class=av><img src="{b64(av)}"></div><div><div class=hn>{handle}{VER}</div><div class=tt>{title}</div></div></div>
<p class=bio>{bio}</p><div class=btn>Seguir</div></div>
<p class=why><b>Por que eu indico:</b> {why}</p>
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

def frase(img,a,b,pos=''):
    return photo(img,f"""<div class=shade></div>
<div class="handle" style="top:60px;left:72px;color:#fff;opacity:.9">@paticompagnoni</div>
<div class=fr><span class=fa>{a}</span><br><span class=fb>{b}</span></div>
<div class=swipe>{chev('#fff')}</div>""",BOX_CSS+"""
.fr{position:absolute;left:72px;right:72px;bottom:170px;text-align:center}
.fa{display:inline-block;background:#F4EDE6;color:#3B2A24;font:600 56px/1.2 PF;padding:16px 30px;margin-bottom:14px;border-radius:6px}
.fb{display:inline-block;background:rgba(244,237,230,.94);color:#3B2A24;font:500 37px/1.45 MS;padding:18px 30px;border-radius:6px;max-width:900px}""")
ICONS={'livro':'<path d="M4 4h6a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4z M20 4h-6a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h7z" fill="none" stroke="#B07A63" stroke-width="1.6" stroke-linejoin="round"/>',
 'podcast':'<rect x="9" y="3" width="6" height="11" rx="3" fill="none" stroke="#B07A63" stroke-width="1.6"/><path d="M5.5 11a6.5 6.5 0 0 0 13 0M12 17.5V21M8.5 21h7" fill="none" stroke="#B07A63" stroke-width="1.6" stroke-linecap="round"/>',
 'série':'<rect x="3" y="5" width="18" height="12" rx="2" fill="none" stroke="#B07A63" stroke-width="1.6"/><path d="M8 21h8M10.5 8.5v5l4-2.5z" fill="none" stroke="#B07A63" stroke-width="1.6" stroke-linejoin="round"/>'}
def ind(n,kind,title,by,sobre,why):
    return f"""<html><head><style>{base}
body{{background:#F4EDE6;display:flex;flex-direction:column;padding:80px 80px 56px}}
.group{{flex:1;display:flex;flex-direction:column;justify-content:center}}
.tag{{align-self:flex-start;background:#B07A63;color:#fff;font:600 26px MS;letter-spacing:.06em;padding:12px 22px;border-radius:6px;text-transform:uppercase}}
.ic{{width:120px;height:120px;margin:40px 0 8px}}
h2{{font:600 72px/1.1 PF;margin:10px 0 14px}}
.at{{font:500 31px MS;color:#B07A63;margin-bottom:40px}}
.card{{background:#fff;border-radius:22px;padding:38px 40px;box-shadow:0 18px 50px rgba(80,50,35,.12);font:400 33px/1.5 MS}}
.why{{margin-top:38px;font:400 33px/1.5 MS}}.why b{{font-weight:600;color:#B07A63}}
.foot{{display:flex;justify-content:space-between;align-items:center;font:500 24px MS;letter-spacing:.06em;color:#9C7B6C;margin-top:30px}}
</style></head><body><div class=group>
<span class=tag># 0{n} · {kind}</span><svg class=ic viewBox="0 0 24 24">{ICONS[kind]}</svg><h2>{title}</h2><div class=at>{by}</div>
<div class=card>{sobre}</div><p class=why><b>Por que eu indico:</b> {why}</p>
</div><div class=foot><span>@paticompagnoni</span>{chev('#B07A63')}</div></body></html>"""

cards=[
 ('nb-11',static('n5_nb11.jpg','Sou estudante de biomedicina e estes são 3 hábitos que eu sigo à risca para cuidar da minha pele','e que você também pode aprender.',56)),
 ('nb-25',static('n5_nb25.jpg','Você não envelhece aos poucos, você envelhece em saltos…','E como usar isso a seu favor?',62)),
 ('d03-1',cover('n5_nb11.jpg','3 profissionais da estética que eu recomendo de olhos fechados','E que me inspiram na profissional que eu estou me tornando.')),
 ('d03-2',slot(1,'Patrícia Manfroi','drapatimanfroi','harmonização facial e corporal','Dra. Patrícia Manfroi | Harmonização Facial e Corporal','+ de 9 anos entregando resultados naturais para quem valoriza elegância. Porto Alegre.','av_manfroi.jpg','ela mostra que uma harmonização bem feita valoriza quem você já é, com naturalidade e elegância.')),
 ('d03-3',slot(2,'Letícia Fridel','draleticiafridel','harmonização facial 40+','Dra. Letícia Fridel | Harmonização Facial 40+ · Dois Irmãos RS','Rejuvenescimento e gerenciamento facial, estratégia, naturalidade e elegância sem transformar seus traços.','av_fridel.jpg','ela fala com a mulher de 40+ e mostra que dá para rejuvenescer sem deixar de ser você.')),
 ('d03-4',slot(3,'Bel Guerra','drabelguerra','harmonização full face','Bel Guerra | Harmonização Facial · São Paulo','Especialista em harmonização facial full face.','av_bel.jpg','ela é uma das grandes referências da harmonização no Brasil e compartilha muito conhecimento sobre o rosto e a pele.')),
 ('d03-5',cta('n6_d03cta.jpg','Mulher, qual profissional você também indica?','Me conta nos comentários e marca ela aqui.',left=False,bottom=True)),
 ('d10',static('n5_d10.jpg','A sua pele sabe quando você está estressada.','E isso afeta a proteção e a cicatrização dela. Mas dá para reduzir os danos.',62,top=True)),
 ('d17-1',cover('cta_crop.jpg','4 coisas sobre o sol que quase ninguém sabe','Antes de curtir o verão, arrasta para o lado.')),
 ('d17-2',sol(1,'Você provavelmente passa só um terço do protetor','A proteção do rótulo é testada com uma camada bem mais grossa do que a maioria das pessoas usa.',
   'Na prática, as pessoas aplicam cerca de um terço da quantidade testada e recebem só uns 40% da proteção esperada.','Young et al., Acta Dermato-Venereologica, 2018')),
 ('d17-3',sol(2,'O sol atravessa o vidro do carro','O vidro da janela segura boa parte dos raios que queimam, mas deixa passar o UVA, ligado ao envelhecimento da pele.',
   'Um caminhoneiro de 69 anos, que dirigiu por mais de 25 anos, tinha o lado do rosto virado para a janela muito mais envelhecido.','Gordon & Brieva, New England Journal of Medicine, 2012')),
 ('d17-4',sol(3,'Limão e sol podem manchar a pele por meses','O suco do limão na pele (na caipirinha, no tempero, na praia) reage com o sol.',
   'Substâncias do limão, as furocumarinas, junto com o sol causam a fitofotodermatite: vermelhidão, bolhas e manchas que podem durar meses.','National Capital Poison Center (EUA)')),
 ('d17-5',sol(4,'Não precisa fugir do sol, precisa não se queimar','O risco está nas queimaduras. A recomendação é evitar o sol das 10h às 16h e ficar de olho nas pintas.',
   'Mulheres com 5 ou mais queimaduras com bolhas entre os 15 e os 20 anos tiveram 80% mais risco de melanoma na vida adulta.','Wu et al., Cancer Epidemiology, Biomarkers & Prevention, 2014 · Sociedade Brasileira de Dermatologia')),
 ('d17-6',cta('n6_sun.jpg','Mulher, qual dessas foi novidade para você?','Me conta nos comentários e salva para o verão.')),
 ('d24',static('n5_d24.jpg','Encontrar as amigas no fim de ano também é cuidar da saúde.','E a ciência tem números para isso.',60)),
 ('j07-1',cover('n6_snow.jpg','Depois dos 40, eu falo muito que…','Arrasta para o lado e me diz se você também.')),
 ('j07-2',frase('n6_corr.jpg','Tá calor aqui ou sou eu?','Já sei, já sei… é o climatério dando oi.')),
 ('j07-3',frase('n7_cracha45.jpg','Protetor solar?','Já passei. E daqui a pouco eu reaplico.')),
 ('j07-4',frase('n6_vald.jpg','Só uma tacinha.','E uma boa conversa que renova a semana inteira.')),
 ('j07-5',frase('c2_cta.jpg','Não tenho mais idade para isso.','Mentira. Eu tenho idade para tudo o que eu quiser.')),
 ('j07-6',frase('n_d10b.jpg','Voltei a estudar.','E não acho que é tarde. Acho que é a hora.')),
 ('j07-7',frase('c2_capa.jpg','Me arrumo para mim.','Se alguém mais gostar, é bônus.')),
 ('j07-8',cta('capa_crop.jpg','Mulher, qual dessas você também fala?','Me conta nos comentários e manda para aquela amiga que vai se identificar.',left=False,bottom=True)),
 ('j21-1',cover('n6_pool.jpg','3 indicações para curtir as suas férias','Um livro, um podcast e uma série que fazem bem para a cabeça e para a autoestima.')),
 ('j21-2',ind(1,'livro','Mulheres que correm com os lobos','Clarissa Pinkola Estés · Editora Rocco','Por meio de mitos e contos, a autora fala sobre a força e a intuição que toda mulher carrega, e que muitas vezes a gente deixa adormecidas.','é para ler devagar, um pouquinho por dia, e se reencontrar a cada capítulo.')),
 ('j21-3',ind(2,'podcast','Bom dia, Obvious','com Marcela Ceribelli · Spotify e outras plataformas','Conversas leves e profundas sobre autoestima, relacionamentos, carreira e saúde mental, com uma convidada diferente a cada episódio.','é perfeito para ouvir na caminhada, no carro ou na beira da praia.')),
 ('j21-4',ind(3,'série','Grace and Frankie','Netflix · 7 temporadas','Duas mulheres na casa dos 70 anos precisam recomeçar a vida do zero, e descobrem que nunca é tarde para se reinventar.','é divertida, leve e prova que a vida não tem prazo de validade.')),
 ('j21-5',cta('n6_sun.jpg','Mulher, qual indicação você me dá de volta?','Me conta nos comentários: livro, podcast ou série.')),
 ('j28',static('n7_golden.jpg','Sou estudante de biomedicina e estes são 3 hábitos que eu sigo à risca para cuidar da minha pele','e que você também pode aprender.',56)),
]
async def main():
    out=D/'out6'; out.mkdir(exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium' if pathlib.Path('/opt/pw-browsers/chromium').is_file() else None)
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        for name,html in cards:
            f=D/f'{name}.html'; f.write_text(html,encoding='utf-8')
            await pg.goto(f.as_uri()); await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=str(out/f'{name}.png'))
        await b.close()
asyncio.run(main())
