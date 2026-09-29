import base64, pathlib, html
from playwright.sync_api import sync_playwright

S = pathlib.Path(__file__).parent
R = pathlib.Path('/home/user/recria-clientes/agencia-recria/social-media')
FONTS = (S / 'c1/fonts_embedded.css').read_text()
LOGO = 'data:image/png;base64,' + base64.b64encode((S / 'c1/logo.png').read_bytes()).decode()

CONSULT = [
    ('Resposta no comentário', 'Enviamos no seu direct! 📩'),
    ('Mensagem 2 (após o clique)', 'Funciona assim: em uma reunião online, entendemos o seu negócio e os seus objetivos, mapeamos os gargalos que estão travando o seu crescimento e mostramos as alavancas que podem fazer diferença. Depois da reunião, você recebe tudo documentado, para saber exatamente o que fazer. E, como prometido, aqui está o seu presente: o Direcional de Marketing e Negócios da Agência Recria. 🎁 [PDF: Direcional de Marketing e Negocios - Agencia Recria]'),
    ('Mensagem 3', 'Para agendar a sua reunião, é só clicar no botão abaixo e escolher o melhor horário. [Botão: Quero agendar → link]'),
    ('Mensagem 4 (23h depois, se não agendou)', 'Oi, [Nome]! Passando para lembrar que as vagas da agenda são limitadas. Se ficou alguma dúvida sobre a consultoria, é só responder aqui que explicamos. 😊'),
]


# ===== Automações PADRÃO (valem para qualquer post com a mesma palavra-chave) =====
DIAG_URL = 'https://www.agenciarecria.com.br/diagnostico-recria/'
SERV_URL = 'https://www.agenciarecria.com.br/#servicos'
PACOTE_URL = 'https://www.agenciarecria.com.br/pacote-mkt-inicial/'
AULAO_URL = 'https://www.agenciarecria.com.br/aula-mkt-para-negocios/'
def _diag(k): return [
    (f'{k} · Resposta no comentário', 'Enviamos um presente no seu direct! 🎁'),
    (f'{k} · Mensagem 1 (botão: Quero o meu presente)', 'Oi, [Nome]! Que bom te ver por aqui. Separamos um presente para você olhar para o seu negócio com outros olhos: o Direcional de Marketing e Negócios da Agência Recria. Quer receber?'),
    (f'{k} · Mensagem 2', 'Aqui está: o Direcional de Marketing e Negócios, com os pilares que separam os negócios que crescem daqueles que estagnam e um autodiagnóstico para você fazer agora. 🎁 [PDF: Direcional de Marketing e Negocios - Agencia Recria]'),
    (f'{k} · Mensagem 3', 'E se você já estiver pronto(a) para dar um passo além: no Diagnóstico Recria, a nossa consultoria online personalizada, entendemos o seu negócio e os seus objetivos, mapeamos os gargalos e mostramos as alavancas de crescimento. Você recebe tudo documentado depois da reunião. No momento, com condição especial de R$ 67 por sessão. [Botão: Quero o meu diagnóstico → ' + DIAG_URL + ']'),
    (f'{k} · Mensagem 4 (23h depois, se não clicou)', 'Oi, [Nome]! Conseguiu ver o seu Direcional? O que achou?\n\nAlém disso, a condição especial do Diagnóstico Recria pode mudar a qualquer momento. O preço por sessão costuma ficar acima de R$ 100, então corre para aproveitar! [Botão: Quero meu diagnóstico → ' + DIAG_URL + ']'),
    (f'{k} · Mensagem 5 (23h depois da Mensagem 4)', 'Se preferir que cuidemos do seu marketing, conheça também todos os nossos serviços tocando no botão. [Botão: Serviços Recria → ' + SERV_URL + ']'),
]
AUTO_STD = {
 'CONSULTORIA': _diag('CONSULTORIA'),
 'DIAGNÓSTICO': _diag('DIAGNÓSTICO'),
 'RECRIA ADS': [
    ('RECRIA ADS · Resposta no comentário', 'Enviamos um presente no seu direct! 🎁'),
    ('RECRIA ADS · Mensagem 1 (botão: Quero o meu presente)', 'Oi, [Nome]! Que bom te ver por aqui. Separamos um presente para você aprender a vender sem parecer aquele vendedor chato: o checklist para criar conteúdos e anúncios sem cara de anúncio. Quer receber?'),
    ('RECRIA ADS · Mensagem 2', 'Aqui está: o checklist Venda sem Parecer Chato, com a estrutura dos anúncios sem cara de anúncio e ganchos para usar nos conteúdos do seu negócio. 🎁 [PDF: Checklist Venda sem Parecer Chato - Agencia Recria]'),
    ('RECRIA ADS · Mensagem 3', 'E, se você estiver pronto(a) para dar o próximo passo, conheça o Recria Ads: o nosso curso aprofundado de criação de conteúdos e anúncios para vender com leveza e naturalidade, sem parecer aquele vendedor chato, mesmo que o seu negócio esteja começando. Por R$ 97 em até 12x. [Botão: Quero conhecer o Recria Ads → link]'),
    ('RECRIA ADS · Mensagem 4 (23h depois, se não clicou)', 'Oi, [Nome]! Conseguiu ver o seu checklist? Gostou?\n\nSe preferir um direcional personalizado para o seu negócio, toque no botão DIAGNÓSTICO. [Botão: DIAGNÓSTICO]'),
 ],
 'CHECKLIST': [
    ('CHECKLIST · Resposta no comentário', 'Enviamos um presente no seu direct! 🎁'),
    ('CHECKLIST · Mensagem 1 (botão: Quero o meu presente)', 'Oi, [Nome]! Que bom te ver por aqui. Separamos um presente para você vender mais na Black Friday: o checklist completo de preparação. Quer receber?'),
    ('CHECKLIST · Mensagem 2', 'Aqui está: o Checklist Black Friday 2026, com o calendário até a Black, exemplos de criativos, a régua de WhatsApp e e-mail e tudo o que precisa estar pronto. 🎁 [PDF: Checklist Black Friday 2026 - Agencia Recria]'),
    ('CHECKLIST · Mensagem 3', 'E se preferir que cuidemos disso para você: na Agência Recria, fazemos a gestão de redes sociais e de tráfego pago (gestão de anúncios), o ano todo, inclusive na Black. Toque no botão para saber mais! [Botão: Conhecer os serviços → ' + SERV_URL + ']'),
    ('CHECKLIST · Mensagem 4 (23h depois, se não clicou)', 'Oi, [Nome]! Espero que esteja gostando do seu checklist! Quanto mais cedo as campanhas começam, mais barato fica vender na Black Friday.\n\nAlém disso, te convido a conhecer o nosso pacote inicial de marketing enquanto a condição especial ainda estiver disponível: ele reúne tráfego pago, social media, criação de site e treinamento comercial, tudo isso por apenas R$ 1.500/mês. Toque no botão para saber mais! [Botão: Pacote inicial → ' + PACOTE_URL + ']'),
    ('CHECKLIST · Mensagem 5 (23h depois da Mensagem 4)', 'Agora, se você já tem alguém cuidando dos anúncios e só quer um direcional personalizado para o seu negócio, toque no botão: DIAGNÓSTICO. [Botão: DIAGNÓSTICO]'),
 ],
}
def auto_for(*kws): return [m for k in kws for m in AUTO_STD[k]]

posts = [
    dict(folder='2026-10-07_carrossel-case-crm', nome='Post 07.10 - Case CRM - legenda e automacao.pdf', post='Post 07.10', data='Quarta-feira, 07/10/2026', titulo='Case CRM: R$ 1,2 milhão sem tráfego pago',
         arquivos='card-01.png a card-10.png (10 imagens)', palavras='CONSULTORIA', marcar='Collab: @agencia.recria × @amandarecria',
         legenda='''Tráfego pago não salvou esse negócio. A base salvou. 💸

Um e-commerce de suplementos para bariátricos, 4 anos de empresa, uma base enorme… e a empresa só falava com as clientes para mandar oferta.

Segmentamos a base pelo momento de compra e pelo estágio da bariátrica, criamos mensagens com objetivo próprio, benefícios exclusivos e uma comunidade para quem já era cliente.

Resultado: R$ 300 mil, R$ 400 mil e R$ 500 mil nos 3 meses seguintes. Sem 1 real em tráfego pago. E clientes comprando todo mês, até sem oferta.

Você já calculou quanto custa conquistar um cliente e quanto ele deixa com você ao longo do tempo? Cada negócio pede um diagnóstico.

👉 Comente CONSULTORIA que explicamos tudo no direct, e ainda enviamos um presente. 🎁

No link da bio você encontra tudo o que a Recria faz pelo seu negócio.''',
         auto=auto_for('CONSULTORIA')),
    dict(folder='2026-10-14_carrossel-toyota', nome='Post 14.10 - Toyota - legenda e automacao.pdf', post='Post 14.10', data='Quarta-feira, 14/10/2026', titulo='Toyota × Sarah Fonseca: "Passou na faculdade, ganhou um carro"',
         arquivos='card-01.png, card-02.png, card-03-video.mp4 (31s), card-04-video.mp4 (44s), card-05.png a card-10.png', palavras='RECRIA ADS e CONSULTORIA',
         marcar='Collab: @agencia.recria × @amandarecria · Marcar no post: @sarahafonseca e @toyotadobrasil',
         legenda='''"Passou na faculdade, ganhou um carro." Quase todo pai prometeu. A minoria cumpriu. 🚗😂

A Toyota pegou essa promessa, que todo brasileiro conhece, e transformou num anúncio que ninguém pulou.

Com a @sarahafonseca e o pai dela, em parceria com a @toyotadobrasil, a marca juntou marketing de oportunidade, identificação e storytelling em formato de episódio, e colocou o Yaris Cross como o desejo e solução da história, de forma leve e fluída.

Nesse carrossel explicamos a estratégia por trás desse anúncio, por que o cérebro não consegue largar uma história no meio e como adaptar isso para o seu negócio.

👉 Comente RECRIA ADS e receba um passo a passo para criar conteúdos e anúncios sem cara de anúncio. 🎁
👉 Quer um direcional personalizado? Comente CONSULTORIA.

📌 Créditos do vídeo: @sarahafonseca e @toyotadobrasil''',
         auto=auto_for('RECRIA ADS', 'CONSULTORIA')),
    dict(folder='2026-10-21_carrossel-black-friday-1', nome='Post 21.10 - Black Friday 1 - legenda e automacao.pdf', post='Post 21.10', data='Quarta-feira, 21/10/2026', titulo='Black Friday 1: se a sua Black começa em novembro, ela já começou atrasada',
         arquivos='card-01.png a card-10.png (10 imagens)', palavras='CHECKLIST, DIAGNÓSTICO e RECRIA ADS',
         marcar='Collab: @agencia.recria × @amandarecria (adicionar após publicar)',
         legenda="""Sua Black Friday não começa no fim de novembro. Ela começa agora. ⏳

Anúncio é leilão: em novembro, todo mundo disputa o mesmo espaço e o custo para aparecer sobe. Quem ativa a campanha na véspera, para um público frio, só queima dinheiro.

Nesse carrossel mostramos como aquecer o seu público, a sequência de conteúdo até a Black e o que precisa estar pronto ainda esta semana.

👉 Comente CHECKLIST e receba no seu direct o checklist completo para se preparar para a Black. 🎁
👉 Quer um direcional para o seu negócio? Comente DIAGNÓSTICO.
👉 Quer vender com leveza, sem parecer que está vendendo? Comente RECRIA ADS.""",
         auto=auto_for('CHECKLIST', 'DIAGNÓSTICO', 'RECRIA ADS')),
    dict(folder='2026-10-28_carrossel-boticario', nome='Post 28.10 - Boticario - legenda e automacao.pdf', post='Post 28.10', data='Quarta-feira, 28/10/2026', titulo='Boticário × Mari Krüger: a ciência estudou apenas o corpo masculino',
         arquivos='card-01.png, card-02-video.mp4 (58s), card-03-video.mp4 (47s), card-04-video.mp4 (27s), card-05.png a card-10.png', palavras='DIAGNÓSTICO e RECRIA ADS',
         marcar='Collab: @agencia.recria × @amandarecria (adicionar após publicar) · Marcar no post: @grupoboticario e @marikrugerb',
         legenda="""A ciência estudou apenas o corpo masculino. E o Grupo Boticário decidiu corrigir isso. 🔬

Por muito tempo, o corpo do homem foi o padrão das pesquisas. O Grupo Boticário criou o Centro de Pesquisa da Mulher e chamou a @marikrugerb, que ensina ciência com humor, para mostrar isso numa série.

O resultado: identificação, comunidade nos comentários e uma marca com décadas de mercado se diferenciando de novo.

Nesse carrossel mostramos por que funcionou, por que não é oportunismo e as 5 perguntas para responder antes de levantar qualquer bandeira no seu negócio.

👉 Quer descobrir o melhor posicionamento para o momento do seu negócio? Comente DIAGNÓSTICO e receba no seu direct um direcional de marketing e negócios da Agência Recria. 🎁
👉 Quer aprender a criar conteúdos e anúncios sem cara de anúncio? Comente RECRIA ADS e receba um presente e todas as informações sobre o nosso curso. 🎁

📌 Créditos do vídeo: @marikrugerb e @grupoboticario""",
         auto=auto_for('DIAGNÓSTICO', 'RECRIA ADS')),
    
]

CSS = FONTS + """
@page{size:A4;margin:18mm 18mm 18mm 18mm}
body{font-family:'Lora',serif;color:#1a1a1a;font-size:11.5pt;line-height:1.55}
.head{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #C9A24E;padding-bottom:10px;margin-bottom:18px}
.head img{height:58px;background:#0b0b0b;padding:8px 12px;border-radius:4px}
.head .t{text-align:right;font-size:9.5pt;color:#8a6d2c;letter-spacing:.08em;text-transform:uppercase}
h1{font-family:'Playfair Display';font-size:21pt;margin:0 0 4px;line-height:1.2}
.date{color:#9a7424;font-style:italic;margin-bottom:16px}
table{width:100%;border-collapse:collapse;margin-bottom:20px;font-size:10.5pt}
td{border-bottom:1px solid #e6dcc6;padding:7px 4px;vertical-align:top}
td:first-child{width:30%;font-weight:600;color:#5a4412}
h2{font-family:'Playfair Display';font-size:14pt;margin:22px 0 8px;color:#0b0b0b;break-after:avoid}
.auto{break-before:page}
.leg{white-space:pre-wrap;background:#F6F2EA;border-left:4px solid #C9A24E;padding:16px 18px;font-size:11.5pt}
.msg{white-space:pre-line;margin-bottom:10px;page-break-inside:avoid}
.msg b{display:block;color:#5a4412;font-size:10pt}
.foot{margin-top:24px;font-size:9pt;color:#999}
"""

with sync_playwright() as p:
    br = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg = br.new_page()
    for d in posts:
        e = html.escape
        auto = ''.join(f'<div class="msg"><b>{e(k)}</b>{e(v)}</div>' for k, v in d['auto'])
        doc = f'''<!doctype html><html><head><meta charset="utf-8"><title>{e(d["post"])} · {e(d["titulo"])}</title><style>{CSS}</style></head><body>
<div class="head"><img src="{LOGO}"><div class="t">Agência Recria<br>Calendário editorial · Outubro 2026</div></div>
<h1><span style="color:#9a7424">{e(d["post"])}</span> · {e(d["titulo"])}</h1><div class="date">{e(d["data"])}</div>
<table><tr><td>Arquivos</td><td>{e(d["arquivos"])}</td></tr>
<tr><td>Palavra(s)-chave</td><td>{e(d["palavras"])}</td></tr>
<tr><td>Marcações</td><td>{e(d["marcar"])}</td></tr></table>
<h2>Legenda (copiar e colar)</h2><div class="leg">{e(d["legenda"])}</div>
<h2 class="auto">Mensagens da automação</h2>{auto}
<div class="foot">Itens entre [colchetes] devem ser preenchidos com o link ou arquivo definitivo.</div>
</body></html>'''
        pg.set_content(doc, wait_until='networkidle'); pg.evaluate('document.fonts.ready')
        out = R / d['folder'] / d['nome']
        pg.pdf(path=str(out), format='A4', print_background=True)
        print(out)
    br.close()
