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
         auto=[('CONSULTORIA · Mensagem 1 (botão: Quero saber)', 'Oi, [Nome]! Vimos que o case do e-commerce que faturou R$ 1,2 milhão sem tráfego pago chamou a sua atenção. Quer saber como funciona o diagnóstico da Agência Recria para o seu negócio?')] + CONSULT),
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
         auto=[
            ('RECRIA ADS · Resposta no comentário', 'Enviamos no seu direct! 📩'),
            ('RECRIA ADS · Mensagem 1 (botão: Quero o presente)', 'Oi, [Nome]! Vimos que o anúncio da Toyota te inspirou. Quer receber o passo a passo para criar conteúdos e anúncios sem cara de anúncio para o seu negócio?'),
            ('RECRIA ADS · Mensagem 2', 'Aqui está o seu presente: o checklist Venda sem Parecer Chato, o passo a passo para criar conteúdos e anúncios sem cara de anúncio. 🎁 [PDF: Checklist Venda sem Parecer Chato - Agencia Recria]'),
            ('RECRIA ADS · Mensagem 3', 'E, se você está pronto(a) para dar o próximo passo, conheça o Recria Ads: o nosso curso aprofundado de criação de conteúdos e anúncios para vender com leveza e naturalidade, sem parecer aquele vendedor chato, mesmo que o seu negócio esteja começando. Por R$ 97 em até 12x. [Botão: Quero conhecer o Recria Ads → link]'),
            ('RECRIA ADS · Mensagem 4 (23h depois, se não clicou)', 'Oi, [Nome]! Conseguiu ver o seu presente? Se preferir um direcional personalizado para o seu negócio, é só tocar no botão: CONSULTORIA aqui que explicamos como funciona.'),
            ('CONSULTORIA · Mensagem 1 (botão: Quero saber)', 'Oi, [Nome]! Vimos que você quer um olhar mais de perto para o seu negócio. Quer saber como funciona a consultoria da Agência Recria?'),
         ] + CONSULT[1:]),
    dict(folder='2026-10-21_carrossel-black-friday-1', nome='Post 21.10 - Black Friday 1 - legenda e automacao.pdf', post='Post 21.10', data='Quarta-feira, 21/10/2026', titulo='Black Friday 1: se a sua Black começa em novembro, ela já começou atrasada',
         arquivos='card-01.png a card-10.png (10 imagens)', palavras='CHECKLIST, DIAGNÓSTICO e RECRIA ADS',
         marcar='Collab: @agencia.recria × @amandarecria (adicionar após publicar)',
         legenda="""Sua Black Friday não começa no fim de novembro. Ela começa agora. ⏳

Anúncio é leilão: em novembro, todo mundo disputa o mesmo espaço e o custo para aparecer sobe. Quem ativa a campanha na véspera, para um público frio, só queima dinheiro.

Nesse carrossel mostramos como aquecer o seu público, a sequência de conteúdo até a Black e o que precisa estar pronto ainda esta semana.

👉 Comente CHECKLIST e receba no seu direct o checklist completo para se preparar para a Black. 🎁
👉 Quer um direcional para o seu negócio? Comente DIAGNÓSTICO.
👉 Quer vender com leveza, sem parecer que está vendendo? Comente RECRIA ADS.""",
         auto=[
            ('CHECKLIST · Resposta no comentário', 'Enviamos no seu direct! 📩'),
            ('CHECKLIST · Mensagem 1 (botão: Quero o checklist)', 'Oi, [Nome]! Vimos que você quer se preparar para vender mais nesta Black Friday. Quer receber o checklist completo?'),
            ('CHECKLIST · Mensagem 2', 'Aqui está o seu presente: o Checklist Black Friday 2026, com o calendário até a Black, exemplos de criativos, a régua de WhatsApp e e-mail e tudo o que precisa estar pronto. 🎁 [PDF: Checklist Black Friday 2026 - Agencia Recria]'),
            ('CHECKLIST · Mensagem 3', 'E se preferir que cuidemos disso para você: na Agência Recria, fazemos a gestão do seu tráfego pago (gestão de anúncios) no Google e no Instagram, do aquecimento do público à semana da Black. Toque no botão para conhecer os nossos serviços. [Botão: Conhecer os serviços → https://www.agenciarecria.com.br/#servicos]'),
            ('CHECKLIST · Mensagem 4 (23h depois, se não clicou)', 'Oi, [Nome]! Quanto mais cedo as campanhas começam, mais barato fica vender na Black. Enquanto estiver disponível, o nosso pacote inicial reúne tráfego pago, social media, site e treinamento comercial por R$ 1.500/mês. Se você já tem alguém cuidando dos anúncios e só quer um direcional, toque em DIAGNÓSTICO. [Botão: Pacote inicial → https://www.agenciarecria.com.br/pacote-mkt-inicial/] [Botão: DIAGNÓSTICO]'),
            ('DIAGNÓSTICO · Resposta no comentário', 'Enviamos no seu direct! 📩'),
            ('DIAGNÓSTICO · Mensagem 1 (botão: Quero saber)', 'Oi, [Nome]! Vimos que você quer um direcional para o seu negócio nesta Black Friday. Quer saber como funciona o Diagnóstico Recria?'),
            ('DIAGNÓSTICO · Mensagem 2', 'Funciona assim: em uma reunião online, entendemos o seu negócio e os seus objetivos, mapeamos os gargalos que estão travando o seu crescimento e mostramos as alavancas que podem fazer diferença. Depois da reunião, você recebe tudo documentado, para saber exatamente o que fazer.'),
            ('DIAGNÓSTICO · Mensagem 3', 'Para garantir o seu Diagnóstico Recria, é só tocar no botão abaixo. [Botão: Quero o meu diagnóstico → https://www.agenciarecria.com.br/diagnostico-recria/]'),
            ('DIAGNÓSTICO · Mensagem 4 (23h depois, se não clicou)', 'Oi, [Nome]! Passando para lembrar que as vagas da agenda são limitadas, e a Black está chegando. Se ficou alguma dúvida sobre o Diagnóstico Recria, é só responder aqui que explicamos. 😊'),
            ('RECRIA ADS · Mensagem 1 (botão: Quero o presente)', 'Oi, [Nome]! Vimos que você quer vender com leveza, sem parecer aquele vendedor chato. Quer receber o passo a passo para criar conteúdos e anúncios sem cara de anúncio?'),
            ('RECRIA ADS · Mensagem 2', 'Aqui está o seu presente: o checklist Venda sem Parecer Chato, o passo a passo para criar conteúdos e anúncios sem cara de anúncio. 🎁 [PDF: Checklist Venda sem Parecer Chato - Agencia Recria]'),
            ('RECRIA ADS · Mensagem 3', 'E, se você está pronto(a) para dar o próximo passo, conheça o Recria Ads: o nosso curso aprofundado de criação de conteúdos e anúncios para vender com leveza e naturalidade, sem parecer aquele vendedor chato, mesmo que o seu negócio esteja começando. Por R$ 97 em até 12x. [Botão: Quero conhecer o Recria Ads → link]'),
            ('RECRIA ADS · Mensagem 4 (23h depois, se não clicou)', 'Oi, [Nome]! Conseguiu ver o seu presente? Se preferir um direcional personalizado para o seu negócio, é só tocar no botão: DIAGNÓSTICO. [Botão: DIAGNÓSTICO]'),
         ]),
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
         auto=[
            ('DIAGNÓSTICO · Resposta no comentário', 'Enviamos no seu direct! 📩'),
            ('DIAGNÓSTICO · Mensagem 1 (botão: Quero o direcional)', 'Oi, [Nome]! Vimos que você quer posicionar o seu negócio de forma criativa e coerente, como o Boticário fez. Quer receber o Direcional de Marketing e Negócios da Agência Recria?'),
            ('DIAGNÓSTICO · Mensagem 2', 'Aqui está o seu presente: o Direcional de Marketing e Negócios, com os pilares que separam os negócios que crescem dos que ficam pelo caminho e um autodiagnóstico para você fazer agora. 🎁 [PDF: Direcional de Marketing e Negocios - Agencia Recria]'),
            ('DIAGNÓSTICO · Mensagem 3', 'E se quiser que olhemos o seu negócio de perto: no Diagnóstico Recria, em uma reunião online, entendemos o seu negócio e os seus objetivos, mapeamos os gargalos e mostramos as alavancas de crescimento, inclusive de posicionamento. Você recebe tudo documentado. No momento, com condição especial de R$ 67 por sessão. [Botão: Quero o meu diagnóstico → https://www.agenciarecria.com.br/diagnostico-recria/]'),
            ('DIAGNÓSTICO · Mensagem 4 (23h depois, se não clicou)', 'Oi, [Nome]! Conseguiu ver o Direcional? A condição especial do Diagnóstico Recria pode mudar a qualquer momento. Se ficou alguma dúvida, é só responder aqui que explicamos. 😊'),
            ('RECRIA ADS · Resposta no comentário', 'Enviamos no seu direct! 📩'),
            ('RECRIA ADS · Mensagem 1 (botão: Quero o checklist)', 'Oi, [Nome]! Vimos que você quer vender sem parecer aquele vendedor chato. Quer receber o checklist para criar conteúdos e anúncios sem cara de anúncio?'),
            ('RECRIA ADS · Mensagem 2', 'Aqui está o seu presente: o checklist Venda sem Parecer Chato, com a estrutura dos anúncios sem cara de anúncio, como escolher e remunerar microinfluenciadores e ganchos para o seu negócio. 🎁 [PDF: Checklist Venda sem Parecer Chato - Agencia Recria]'),
            ('RECRIA ADS · Mensagem 3', 'E, se você está pronto(a) para dar o próximo passo, conheça o Recria Ads: o nosso curso aprofundado de criação de conteúdos e anúncios para vender com leveza e naturalidade, sem parecer aquele vendedor chato, mesmo que o seu negócio esteja começando. Por R$ 97 em até 12x. [Botão: Quero conhecer o Recria Ads → link]'),
            ('RECRIA ADS · Mensagem 4 (23h depois, se não clicou)', 'Oi, [Nome]! Conseguiu ver o seu checklist? Se preferir um direcional personalizado para o seu negócio, é só tocar no botão: DIAGNÓSTICO. [Botão: DIAGNÓSTICO]'),
         ]),
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
.msg{margin-bottom:10px;page-break-inside:avoid}
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
