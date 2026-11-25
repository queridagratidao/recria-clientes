import json,html,os,glob,base64,io
from PIL import Image
S='/tmp/claude-0/-home-claude/b2736a22-a7a5-5ef9-a4fc-d023deb3f6f7/scratchpad/dez'
P=json.load(open(S+'/dez.json'))
e=lambda s:html.escape(s).replace('\n','<br>')
def thumb(path,w=230):
    im=Image.open(path).convert('RGB');im.thumbnail((w*2,w*3));b=io.BytesIO();im.save(b,'JPEG',quality=80)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
def slug(d): return d.replace('/','-').replace(' ','_')
CSS='''@page{size:A4;margin:16mm 14mm 18mm}*{box-sizing:border-box}body{font-family:Arial,Helvetica,sans-serif;color:#3d1530;font-size:10.5pt;line-height:1.5;margin:0}
h1{color:#A71874;font-family:Georgia,serif;font-size:30pt;margin:0 0 6px}h2{color:#A71874;font-family:Georgia,serif;font-size:17pt;margin:0 0 4px}h3{color:#A71874;margin:14px 0 4px;font-size:12pt}
.fl{color:#E07A9A;font-size:20pt;text-align:center}.sub{color:#7a4a66}.cover{text-align:center;padding-top:60px}
.pb{page-break-after:always}.post{page-break-inside:avoid;border-top:2px solid #f6d3e6;padding:12px 0 14px;display:flex;gap:16px}
.thumbs{width:250px;flex:none;display:flex;flex-wrap:wrap;gap:4px}.thumbs img{width:80px;border-radius:4px}.thumbs img.one{width:230px}
.meta{font-size:9pt;color:#A71874;font-weight:bold;text-transform:uppercase;letter-spacing:.04em}.tag{display:inline-block;background:#FFE6F4;color:#A71874;border-radius:10px;padding:1px 8px;font-size:8.5pt;margin-left:6px}
.cap{background:#fff6fb;border-left:3px solid #E07A9A;padding:8px 10px;margin-top:6px;font-size:9.6pt}
table{border-collapse:collapse;width:100%;font-size:9.5pt}td,th{border:1px solid #f0c9dd;padding:5px 7px;text-align:left;vertical-align:top}th{background:#FFE6F4;color:#A71874}
.box{background:#fff6fb;border:1px solid #f6d3e6;border-radius:8px;padding:10px 14px;margin:8px 0}
.slides{font-size:9pt;color:#5a2a4a;margin-top:4px}ul{margin:4px 0 4px 18px;padding:0}li{margin:2px 0}'''

def post_block(p):
    d=slug(p['d'])
    if p['t']=='vid':
        fr=sorted(glob.glob(f"{S}/vid/{d}/f*.png"))
        imgs=''.join(f'<img src="{thumb(f)}">' for f in fr[:2])
        art='<div class="slides"><b>Texto na tela (em sequência):</b><br>'+'<br>'.join(f'{i+1}. {e(t)} <span style="color:#999">({s:.1f}s)</span>' for i,(t,s) in enumerate(p['beats']))+'</div>'
        arq=f"video-{d}.mp4 (9:16, sem áudio)"
    else:
        fs=sorted(glob.glob(f"{S}/out/{d}/*.png"))
        imgs=''.join(f'<img class="{"one" if len(fs)==1 else ""}" src="{thumb(f)}">' for f in fs)
        art=''
        arq=(f"carrossel-{d}.zip ({len(fs)} cards)" if len(fs)>1 else f"estatico-{d}.png")
    tag=('<span class="tag">público 40+</span>' if p.get('p40') else '')+('<span class="tag">fixar no perfil · serve de anúncio</span>' if p.get('fixo') else '')
    dow={'Seg':'segunda','Qua':'quarta','Sex':'sexta'}.get(p['dow'],'')
    return f'''<div class="post"><div class="thumbs">{imgs}</div><div style="flex:1"><div class="meta">{e(p['d'])}{' · '+dow if dow else ''} · {e(p['k'])}{tag}</div>
<div style="font-size:8.5pt;color:#888">Arquivo: {arq}</div>{art}<div class="cap"><b>Legenda</b><br>{e(p['cap'])}</div></div></div>'''

grade=''.join(f"<tr><td>{p['d']}</td><td>{p['dow']}</td><td>{e(p['k'])}</td><td>{e((p.get('slides') or [p.get('beats',[['']])[0][0]])[0].replace(chr(10),' ').replace('*',''))[:90]}</td><td>{'40+' if p.get('p40') else ''}</td></tr>" for p in P if not p.get('fixo'))

SOBRAS=[
('Vídeo com foto (humor)',[
 '"Ninguém vem te salvar…" → "minha psi vem" (com a foto da Camila sorrindo)',
 '"Você chega na terapia achando que precisa mudar algo em você, mas acaba…" (resposta na legenda)',
 '"Nossa, você lidou tão bem com isso" → "na verdade, minha psicóloga me ouviu falar disso por 27 sessões seguidas"',
 '"Um dia comum de terapia: a paciente no começo da sessão" → "hoje não tenho nada para falar" → (sessão inteira)',
 '"Da série: lugares aleatórios de onde a paciente faz a sessão online" (carro, banheiro, estacionamento)',
 'POV: a psicóloga acompanhando a vida amorosa da paciente → "amanhã eu caso" → "assinei o divórcio" → "é amor mesmo" → "eu estava dormindo com o demônio"',
 '"Bom dia para todos, menos para quem foi babaca com as minhas pacientes" (só orgânico, tom leve)',
 '"Já estou bem, acho que nem preciso mais de terapia" → "eu, 3 dias depois:"',
 '"O quão emocionada você é?" (história recontada em texto na tela, sem usar o corte do podcast)',
 'POV: você ouvindo a conversa do date na mesa ao lado (o cara explicando a pronúncia do próprio nome)']),
('Carrossel',[
 'Mecanismos de defesa com humor: esquiva, catastrofização, "em minha defesa, eu pensei bem pior do que falei" (com imagens próprias, sem memes de terceiros)',
 '"Quando a pessoa fala mal da ex, ela está te mostrando como vai falar de você" (versão neutra)',
 'Coerência: "não quero nada sério", mas trata como namoro (o problema não é não querer, é a incoerência)',
 '"O apego ansioso no seu dia mais tranquilo" (as mensagens que a mente escreve quando a outra pessoa demora a responder)',
 'Ter uma vida própria (versão saudável da "ausência"): não é joguinho, é não girar em torno de ninguém',
 '"A coisa mais romântica é permanecer e trabalhar em mim" (amor maduro)',
 '40+: "Mulheres, não tenham medo de mostrar o que vocês sabem" (currículo, conquistas, sem palavrão)',
 '40+: a gangorra do relacionamento tóxico (intensidade, queda, volta), com base em artigos científicos',
 '40+: casamento longo, traição e recomeço: "eu saí de um e caí em outro igual"',
 '40+: sinais de alerta de que a relação está te fazendo duvidar de você (sem entrar em violência física)']),
('Estático / frase',[
 '"Não foque em superar. Foque em atravessar" (um dia depois do outro)',
 '"Dê às pessoas o direito de não te quererem"',
 '"Pela sua própria sanidade, siga em frente como se nunca tivesse conhecido essa pessoa"',
 '"Quem atravessou um inferno e escolheu a bondade"',
 '"Bóra, senhora! O sonho é teu. Não dá para terceirizar" (40+)',
 '"A gata que quer virar leoa precisa perder o apetite por rato" (frase popular)',
 '"Tô com medo de sair daqui e doer muito" / "mas a dor de sair passa, a de ficar não" (ilustração própria)',
 '"Queria poder cobrar de quem desregula meus pacientes" (só orgânico, sem citar valor)'])]
sob=''.join(f"<h3>{t}</h3><ul>"+''.join(f"<li>{e(x)}</li>" for x in L)+"</ul>" for t,L in SOBRAS)

ROT=[('Gancho (0–5s)','Você é a pessoa que manda mensagem e fica olhando o celular até a resposta chegar… ou a pessoa que some justamente quando a relação começa a ficar séria?'),
('Contexto','Me pediram aqui nos comentários para explicar a diferença entre apego ansioso e apego evitativo. Então vem comigo.'),
('O que é estilo de apego','O estilo de apego é o jeito que a gente aprendeu a se vincular, lá na infância, com as primeiras pessoas que cuidaram de nós. E esse jeito costuma aparecer de novo nos nossos relacionamentos adultos.'),
('Apego ansioso','No apego ansioso, existe muito medo de ser abandonada. A pessoa precisa de bastante confirmação de que é amada, sente angústia com a distância, entende uma demora na resposta como sinal de que algo está errado e, muitas vezes, se esforça demais para não perder o outro. É aquela que recebe um "ok" seco e já pensa: o que eu fiz?'),
('Apego evitativo','No apego evitativo, é o contrário: o que assusta é a proximidade. A pessoa valoriza muito a independência, tem dificuldade de falar do que sente e, quando a relação fica mais íntima, ela se afasta, esfria ou fica ocupada demais. É quem some justamente quando tudo parecia estar indo bem.'),
('A gangorra','E sabe o que é curioso? Esses dois estilos costumam se atrair. Quanto mais um se aproxima, mais o outro se afasta. E quanto mais o outro se afasta, mais o primeiro corre atrás. Vira uma gangorra que cansa os dois.'),
('Não é defeito','Nenhum dos dois é defeito de caráter. São formas que a gente aprendeu para se proteger. Quem aprendeu que o amor podia ir embora a qualquer momento fica em alerta. Quem aprendeu que precisar de alguém era perigoso aprende a não precisar.'),
('Esperança','A boa notícia é que estilo de apego não é sentença. Com autoconhecimento e, quando necessário, com terapia, dá para caminhar para o que a gente chama de apego seguro: conseguir se aproximar sem se perder, e ter o seu espaço sem fugir.'),
('Chamada final','E você, se identifica mais com qual dos dois? Me conta aqui nos comentários. E, se quiser trabalhar isso comigo, os caminhos estão no link da bio.')]
rot=''.join(f"<p><b style='color:#A71874'>{t}</b><br>{e(x)}</p>" for t,x in ROT)
ROTCAP="Me pediram e aqui está: a diferença entre apego ansioso e apego evitativo 💭\n\nO jeito como a gente se vincula nas relações costuma ter raízes nas nossas primeiras experiências de afeto. Não é defeito: é uma forma que a gente aprendeu para se proteger. E dá para construir vínculos mais seguros.\n\nVocê se reconhece mais em qual dos dois? Me conta nos comentários 👇\n\nSe quiser trabalhar isso comigo, os caminhos estão no link da bio. 🌸"

fixos=''.join(post_block(p) for p in P if p.get('fixo'))
mes=''.join(post_block(p) for p in P if not p.get('fixo'))
H=f'''<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="cover"><div class="fl">✿</div><div class="meta">Instagram · @psicamilasartori</div><h1>Calendário de Dezembro</h1><div class="sub">3 posts por semana · carrossel na segunda, estático na quarta, humor na sexta</div>
<div class="box" style="text-align:left;margin-top:30px"><b>Como usar este material</b><ul>
<li>Todas as artes estão em 1080×1350 (feed 4:5). Os vídeos estão em 9:16, sem áudio: é só colocar uma música em alta no Instagram.</li>
<li>Uma vez por semana há um post pensado para mulheres de 40+ (marcado como <b>público 40+</b>).</li>
<li>O curso aparece como <b>"curso de autoconhecimento para mulheres"</b>, sem nome, para servir mesmo se o nome mudar.</li>
<li>As chamadas levam sempre para o <b>link da bio</b> (sem automação de comentário).</li>
<li>No final: os <b>3 posts fixos</b> (que também servem de anúncio), a <b>lista de ideias que sobraram</b> para janeiro e um <b>roteiro de vídeo</b> sobre apego ansioso e evitativo.</li></ul></div>
<h2 style="margin-top:24px">Grade do mês</h2><table><tr><th>Data</th><th>Dia</th><th>Formato</th><th>Tema</th><th></th></tr>{grade}</table></div><div class="pb"></div>
<h2>Posts de dezembro</h2>{mes}<div class="pb"></div>
<h2>3 posts fixos para o perfil</h2><p class="sub">Para fixar no topo do perfil e impulsionar alternando entre eles: o carrossel apresenta os dois caminhos, um estático vende o atendimento individual e o outro vende o curso. Sem preço no atendimento, como pede o Código de Ética. Sempre levando para o link da bio.</p>{fixos}
<div class="box"><b>Para os anúncios funcionarem sozinhos</b><ul><li>O link da bio precisa ter os três caminhos: WhatsApp, formulário de contato e página do curso.</li><li>No impulsionamento, a meta "visitas ao perfil" ou "mensagens no WhatsApp" costuma funcionar bem para o atendimento. Para o curso, "visitas ao site".</li><li>Público sugerido: mulheres, 35 a 60 anos, interesse em autoconhecimento, psicologia e desenvolvimento pessoal.</li></ul></div><div class="pb"></div>
<h2>Ideias que sobraram (para janeiro)</h2><p class="sub">Vieram das referências que a Camila e a Amanda separaram. A Camila escolhe quais usar, quando voltar a gravar ou para completar o calendário.</p>{sob}<div class="pb"></div>
<h2>Extra: roteiro de vídeo</h2><div class="meta">Apego ansioso × apego evitativo · até 3 minutos</div><p class="sub">Pedido nos comentários. Para a Camila gravar quando tiver tempo, olhando para a câmera, num tom de conversa. Dá cerca de 2min30.</p>{rot}
<div class="cap"><b>Sugestão de legenda</b><br>{e(ROTCAP)}</div>
</body></html>'''
open(S+'/cal.html','w').write(H)

# ---- Grupo dezembro v2
G=[('Mensagem de abertura do mês','Enviar junto com o conteúdo da Semana 1','',"Bom dia, mulheres donas de si! 🌸\n\nDezembro é sempre um mês corrido, então este mês vai ser mais enxuto por aqui. Antes de entrarmos de vez no clima de festas, preparei uma retrospectiva para fecharmos o ano juntas.\n\nBora começar? Segue o conteúdo da semana 👇"),
('Semana 1 (07–13/12)','Retrospectiva do ano','PDF PRÁTICO',"Bom dia, mulheres donas de si! 💕\n\nEste ano a gente trabalhou autoestima, relacionamentos e emoções aqui no grupo. Antes de virar a página para o ano novo, preparei um exercício de retrospectiva para você olhar para a sua vida pessoal, para os seus relacionamentos e para tudo o que viveu este ano, com gentileza.\n\n📎 Segue o PDF completo:\n\nSe você quer levar essa jornada mais longe em 2027, o meu curso de autoconhecimento para mulheres fica disponível o ano inteiro, com todos os conteúdos, e dá para parcelar em até 12x. O link está na bio do meu Instagram, @psicamilasartori.\n\nBom exercício! 💕"),
('Semana 2 (14–20/12)','Mensagem de boas festas','VÍDEO / ÁUDIO DA CAMILA',"Boa tarde, mulheres donas de si! 🎄\n\nAntes de entrarmos de vez no clima de festas, gravei um vídeo rapidinho para fechar o ano com vocês.\n\nSolta o play:\n\n[vídeo/áudio]\n\nBoas festas! 💕"),
('21/12 a 03/01','Recesso de fim de ano','SEM CONTEÚDO NOVO',"Boa tarde, mulheres donas de si! 🎄\n\nA gente entra agora em recesso de fim de ano por aqui, sem conteúdo novo, para vocês aproveitarem as festas com quem amam.\n\nA gente se reencontra com conteúdo novo já no dia 4 de janeiro. Boas festas! 🥂")]
ROTG="\"Eu queria vir aqui agradecer vocês por este ano inteiro de caminhada juntas.\n\nA gente falou sobre autoestima, sobre relacionamentos, sobre emoções, e eu espero de coração que alguma coisa deste ano tenha feito sentido para a sua vida.\n\nAgora é hora de descansar, celebrar e aproveitar quem vocês amam. Não se cobrem por nada neste período, nem por manter rotina, nem por \"aproveitar direito\". Só vivam o momento.\n\nA gente se reencontra por aqui com conteúdo novo já no dia 4 de janeiro. Um brinde a tudo o que vocês construíram em 2026, e ao que vem por aí. Boas festas!\""
gb=''
for t,s,lab,txt in G:
    gb+=f'<div style="page-break-inside:avoid;margin-bottom:22px"><div class="fl">✿</div><h2 style="text-align:center">{t}</h2><div class="sub" style="text-align:center">{s}</div>'+(f'<div class="meta" style="text-align:center;margin-top:4px">{lab}</div>' if lab else '')+f'<div class="cap" style="margin-top:10px"><b>Textinho de apoio (WhatsApp)</b><br>{e(txt)}</div>'
    if t.startswith('Semana 1'): gb+='<p style="font-size:9pt">📎 Material de apoio: enviar junto o PDF "Comunidade Donas de Si - Material Retrospectiva do ano".</p>'
    if t.startswith('Semana 2'): gb+=f'<h3>Roteiro (vídeo de até 90s, ou áudio)</h3><p>{e(ROTG)}</p><p style="font-size:9pt"><b>Plano B, se não der para gravar:</b> mandar a mesma mensagem em texto, em primeira pessoa, como se fosse a Camila falando no grupo.</p>'
    gb+='</div>'
GH=f'''<html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="cover" style="padding-top:20px"><div class="fl">✿</div><div class="meta">Dezembro · Comunidade Donas de Si</div><h1>Fechamento do Ano com Gentileza</h1><div class="sub">Mês mais curto, por causa das festas</div>
<div class="box" style="text-align:left;margin:18px auto;max-width:420px">✿ Semana 1: Retrospectiva do ano (PDF prático)<br>✿ Semana 2: Mensagem de boas festas (vídeo ou áudio)<br>✿ 21/12 a 03/01: recesso, sem conteúdo novo<br>✿ O grupo volta com conteúdo normal em 04/01</div></div>{gb}</body></html>'''
open(S+'/grupo.html','w').write(GH)
print('ok')
