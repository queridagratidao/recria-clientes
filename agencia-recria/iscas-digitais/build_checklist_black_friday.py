import base64, pathlib
from playwright.sync_api import sync_playwright

D = pathlib.Path(__file__).parent
S = D.parent
FONTS = (S / 'c1/fonts_embedded.css').read_text()
img = lambda p, m='image/jpeg': f"data:{m};base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO = img(D / 'logo_icone.png', 'image/png')
LOGO_FULL = img(D / 'logo_sem_tagline.png', 'image/png')
LINK_MANUAL = '[link do Manual Estratégias Atraentes que Vendem]'
POSTS = {'benefit':'DRnAVTjEuN7','anna':'DQnMPomjtdl','vo':'DCotzX-xDfR','friday':'DRhcD58iGrs','inconf':'DdUofvNTq8P','burga':'DChVeNXthTk'}

# Preencher antes de enviar (links e @ dos perfis dos exemplos)
LINK_RECRIA_ADS = '[link do Recria Ads]'
LINK_RECRIA_ADS_URL = 'https://www.agenciarecria.com.br/'  # TROCAR pelo link do Recria Ads quando o curso estiver no ar
LINK_CONSULTORIA = 'agenciarecria.com.br/diagnostico-recria'
LINK_TRAFEGO = 'agenciarecria.com.br/#servicos'
HANDLES = {
    'benefit': '@benefitcosmetics', 'anna': '@anna_couto', 'vo': '@viomedspa',
    'friday': '@milla', 'inconf': '@tamarateixeira', 'burga': '@burgaofficial',
}

CSS = FONTS + """
@page{size:1080px 1350px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Lora',serif}
.pg{width:1080px;height:1350px;position:relative;padding:150px 90px 120px;overflow:hidden;page-break-after:always;display:flex;flex-direction:column}
.dark{background:radial-gradient(ellipse at 15% 0%,#2a2214 0%,#0b0b0b 55%),#0b0b0b;color:#fff}
.light{background:#F6F2EA;color:#111}
.logo{position:absolute;top:50px;left:80px;height:70px}
.foot{position:absolute;bottom:44px;left:90px;right:90px;display:flex;justify-content:space-between;font-size:20px;opacity:.7}
.dark .foot{color:#E4C988}.light .foot{color:#8a6d2c}
.kick{font-weight:600;font-size:23px;letter-spacing:.18em;text-transform:uppercase;color:#C9A24E;margin-bottom:18px}
.light .kick{color:#9a7424}
h1{font-family:'Playfair Display';font-weight:700;font-size:58px;line-height:1.12;margin-bottom:28px}
h2{font-family:'Playfair Display';font-weight:700;font-size:34px;margin:18px 0 10px}
em.g{font-style:italic;color:#E4C988}.light em.g{color:#9a7424}
p{font-size:27px;line-height:1.5;margin-bottom:16px}
.dark p,.dark li{color:#e9e4da}.light p,.light li{color:#2a2a2a}
b{font-weight:600}.dark b{color:#fff}
ul{list-style:none;margin:4px 0 14px}
li{font-size:25px;line-height:1.45;margin-bottom:12px;padding-left:38px;position:relative}
li:before{content:'';position:absolute;left:0;top:13px;width:14px;height:14px;border-radius:50%;background:#C9A24E}
li.ck:before{content:'☐';background:none;width:auto;height:auto;top:-1px;color:#C9A24E;font-size:28px;border-radius:0}
.box{background:#0b0b0b;color:#E4C988;border-left:6px solid #C9A24E;padding:22px 28px;font-family:'Playfair Display';font-style:italic;font-size:27px;line-height:1.4;margin:10px 0 14px}
.dark .box{background:rgba(201,162,78,.08);border:1.5px solid #C9A24E;border-left:6px solid #C9A24E}
.cta{background:#C9A24E;color:#0b0b0b;border-radius:6px;padding:30px 34px;margin-top:12px}
.cta .t{font-family:'Playfair Display';font-weight:700;font-size:36px;line-height:1.2;margin-bottom:10px}
.cta p{color:#1a1a1a!important;font-size:25px;margin-bottom:10px}
.cta a.l{text-decoration:none}
.cta b{color:#0b0b0b!important}
.cta .l{font-weight:600;font-size:25px;background:#0b0b0b;color:#E4C988;display:inline-block;padding:10px 18px;border-radius:4px}
table{width:100%;border-collapse:collapse;font-size:22px;margin-top:6px}
th{text-align:left;background:#0b0b0b;color:#E4C988;padding:12px 12px;font-family:'Playfair Display';font-size:22px}
td{padding:11px 12px;border-bottom:1px solid #e1d5ba;vertical-align:top;line-height:1.38;color:#2a2a2a}
td:first-child{font-weight:600;color:#5a4412;width:26%}
.grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px 22px}
.ex{text-decoration:none;display:block}
.ex .btn{display:block;font-size:17px;color:#0b0b0b;background:#C9A24E;text-decoration:none;padding:5px 10px;border-radius:3px;margin-top:6px;width:fit-content}
.ex u{display:block;font-size:17px;color:#0b0b0b;background:#C9A24E;text-decoration:none;padding:5px 10px;border-radius:3px;margin-top:6px;width:fit-content}
.ex img{width:100%;height:225px;object-fit:cover;border-radius:6px;border:2px solid #C9A24E}
.ex b{display:block;font-family:'Playfair Display';font-size:23px;margin:8px 0 2px;color:#E4C988}
.ex span{font-size:18px;line-height:1.35;color:#d9d3c7;display:block}
.ex i{font-size:17px;color:#C9A24E}
"""

pages = []
def page(cls, body, n):
    pages.append(f'<div class="pg {cls}"><img class="logo" src="{LOGO}">{body}<div class="foot"><span>Checklist Black Friday 2026 · Agência Recria</span><span>{n:02d}</span></div></div>')

# 1 capa
pages.append(f'''<div class="pg dark" style="justify-content:center;padding-top:0"><img style="height:190px;align-self:flex-start;margin-bottom:70px" src="{LOGO_FULL}">
<div class="kick" style="font-size:28px">Presente Agência Recria</div>
<h1 style="font-size:92px;line-height:1.02">Checklist<br><em class="g">Black Friday 2026</em></h1>
<p style="font-size:34px;max-width:820px">O passo a passo para atrair e aquecer o seu público, preparar as suas campanhas e vender muito mais no período mais disputado do ano.</p>
<div style="width:180px;height:3px;background:#C9A24E;margin:30px 0"></div>
<p style="font-size:24px;color:#E4C988">@agencia.recria × @amandarecria</p></div>''')

page('light', '''<div class="kick">Antes de tudo</div><h1>Por que começar <em class="g">o quanto antes?</em></h1>
<p><b>Anúncio é leilão.</b> Em novembro, todas as empresas disputam o mesmo espaço, algumas o mês inteiro, outras só a semana da Black. Quanto maior a disputa, mais caro fica aparecer. <b>Se você deixar para novembro, tudo fica mais caro</b>: aparecer, receber cliques e vender.</p>
<p><b>Toda campanha passa por uma fase de aprendizado</b>, que costuma levar de 7 a 15 dias. Quanto mais cedo ela começa, mais dados tem sobre quem de fato compra de você, e com custo menor.</p>
<p><b>Desconto não vende sozinho.</b> Quem nunca ouviu falar de você não compra só porque viu um "50% off". O público precisa ser aquecido antes.</p>
<div class="box">A meta: ativar as campanhas até o dia 20 de outubro, para que até o fim de novembro tudo já esteja fluindo.</div>''', 2)

page('dark', f'''<div class="kick">O funil</div><h1>Topo, meio e fundo: <em class="g">o que fazer em cada etapa</em></h1>
<h2>Topo · atrair</h2><p>Conteúdo que gera identificação e alcança quem ainda não conhece você: dores, curiosidades, bastidores, tendências, humor. Objetivo: <b>ser visto e lembrado</b>.</p>
<h2>Meio · engajar e nutrir</h2><p>Demonstração, como funciona, comparação, prova social, depoimentos, antes e depois. Objetivo: <b>aumentar o nível de consciência e gerar desejo</b>.</p>
<h2>Fundo · vender</h2><p>Oferta clara, quebra de objeções, bônus, garantia, contagem regressiva, escassez real. Objetivo: <b>converter</b>.</p>
<div class="box">Formatos que funcionam: estático, carrossel, vídeo curto, antes e depois, depoimento, bastidor, "unboxing". O melhor depende do seu negócio.</div>
<p style="font-size:23px;margin-top:6px">Explicamos em detalhes como trabalhar cada etapa do funil, com neurociência e comportamento do consumidor, no <b>Manual Estratégias Atraentes que Vendem</b>: <span style="color:#E4C988">{LINK_MANUAL}</span></p>''', 3)

page('light', '''<div class="kick">Passo a passo</div><h1 style="margin-bottom:14px">O calendário até a <em class="g">Black Friday</em></h1>
<p style="font-size:24px">Está vendo este conteúdo de outubro em diante? Isto é o que ainda dá para fazer. <b>Quanto antes você começar, melhor.</b></p>
<table><tr><th>Quando</th><th>O que fazer</th></tr>
<tr><td>Até 20/10</td><td>Campanhas ativas para o público frio. Pixel e API de conversões conferidos. Oferta da Black decidida.</td></tr>
<tr><td>Fim de outubro</td><td>Topo de funil: identificação, conexão, prova social, demonstração. Começar a gerar expectativa: "vem aí a nossa melhor Black".</td></tr>
<tr><td>Início de novembro</td><td>Meio de funil: reforçar desejo e diferenciais, mostrar por que você é diferente do concorrente. Abrir a lista VIP / grupo de ofertas.</td></tr>
<tr><td>Meados de novembro</td><td>Quebrar objeções. Contagem regressiva. Remarketing para quem engajou e visitou.</td></tr>
<tr><td>Semana da Black</td><td>Fundo de funil: oferta, oferta, oferta. Últimas peças, escassez real, urgência. Acesso antecipado para a lista VIP.</td></tr>
<tr><td>Pós-Black</td><td>Giftback e comunicação pós-compra para gerar recompra e não despencar em dezembro.</td></tr></table>''', 4)

ex = lambda k, title, desc, cat: f'<div class="ex"><a href="https://www.instagram.com/p/{POSTS[k]}/"><img src="{img(D / (k + ".jpg"))}"></a><b>{title}</b><span>{desc}</span><i>{cat} · {HANDLES[k]}</i><a class="btn" href="https://www.instagram.com/p/{POSTS[k]}/">▶ Assistir no Instagram</a></div>'
page('dark', f'''<div class="kick">Inspiração</div><h1 style="font-size:48px;margin-bottom:12px">Exemplos de criativos <em class="g">para se inspirar</em></h1><p style="font-size:21px;margin-bottom:16px">Toque em cada exemplo para assistir ao vídeo no perfil da marca.</p>
<div class="grid">
{ex('benefit','Desejo antes do preço','Os produtos "caem do céu" direto na sacola. Gera desejo sem falar de desconto.','E-commerce')}
{ex('anna','A equipe aquecendo','Cada funcionária num canto da loja, "aquecendo para a nossa maior Black da história".','Loja física / negócio local')}
{ex('vo','Teaser elegante','Uma sacola passando de mão em mão e "Black Friday is coming". Sem preço, só expectativa.','Marca premium / estética')}
{ex('friday','Oferta em forma de cardápio','Uma marca de moda transformou as ofertas num "cardápio" servido na mesa.','Moda · ótima ideia para alimentação')}
{ex('inconf','A Black vira evento','"Não é só mais uma promoçãozinha": uma Black com nome, data e personalidade.','Infoproduto / serviços')}
{ex('burga','Contagem regressiva','"Ready? 18/11, 18h." Gera expectativa com data e hora marcadas.','Qualquer negócio')}
</div>''', 5)

page('light', f'''<div class="kick">Criatividade que vende</div><h1>Oferta, sim. <em class="g">Mas com criatividade.</em></h1>
<p>Repare: todos esses exemplos são anúncios de oferta. Mas nenhum é aquela oferta sem graça. Eles usam <b>humor, surpresa, expectativa e criatividade</b> para chamar a atenção antes de mostrar o desconto.</p>
<p>E dá para ir além: criar conteúdos e anúncios com <b>cara de conteúdo</b>, que o público de fato quer assistir.</p>
<div class="cta"><div class="t">Quer aprender isso em detalhes?</div><p>No <b>Recria Ads</b>, ensinamos a criar anúncios sem cara de anúncio, utilizando <b>neuromarketing, neurociência e comportamento do consumidor aplicados às vendas</b>. Um método construído em mais de 10 anos de experiência em marketing, atendendo de pequenas a grandes empresas, inclusive marcas conhecidas dos nichos de banheiras e de moda.</p><p style="font-size:22px">Quer saber mais sobre o Recria Ads? Clique no botão abaixo:</p><a class="l" href="{LINK_RECRIA_ADS_URL}">Quero conhecer o Recria Ads</a></div>''', 6)

page('dark', '''<div class="kick">Base e relacionamento</div><h1>A sua base é o seu <em class="g">atalho</em></h1>
<p>Quem já comprou de você é quem mais compra na Black. E sai muito mais barato do que conquistar um cliente novo no período mais caro do ano.</p>
<ul>
<li class="ck">Segmente os clientes pela última compra, frequência e valor gasto (matriz RFM)</li>
<li class="ck">Crie um <b>grupo VIP no WhatsApp</b> ou um espaço fechado para ofertas exclusivas</li>
<li class="ck">Monte uma <b>lista VIP</b> com acesso antecipado às ofertas</li>
<li class="ck">Ofereça o produto certo para quem já comprou algo relacionado</li>
<li class="ck">Prepare uma régua de <b>WhatsApp + e-mail</b> (próxima página)</li>
</ul>
<div class="box">Foi essa lógica que fez um e-commerce que atendemos faturar R$ 1,2 milhão em 3 meses, sem tráfego pago.</div>''', 7)

page('light', '''<div class="kick">Régua de comunicação</div><h1>WhatsApp + e-mail: <em class="g">intercalando as etapas</em></h1>
<table><tr><th>Etapa</th><th>Exemplo de mensagem</th></tr>
<tr><td>Atração</td><td>"Separamos 3 erros que quase todo mundo comete ao comprar [produto]."</td></tr>
<tr><td>Engajamento</td><td>"Qual desses você mais quer ver com desconto na Black? Responde aqui 👇"</td></tr>
<tr><td>Nutrição</td><td>Conteúdo que ensina: como usar, como escolher, diferenças entre os produtos.</td></tr>
<tr><td>Consciência</td><td>Depoimentos, antes e depois, por que o seu produto é diferente.</td></tr>
<tr><td>Expectativa</td><td>"Faltam 7 dias. Quem está na lista VIP vê as ofertas primeiro."</td></tr>
<tr><td>Venda</td><td>"Abrimos! Ofertas exclusivas para você, só até meia-noite."</td></tr></table>
<p style="margin-top:18px">Intercale: <b>não mande oferta em todas as mensagens</b>. Quem só recebe oferta para de ler.</p>''', 8)

page('dark', '''<div class="kick">Parte técnica</div><h1>Checklist <em class="g">das campanhas</em></h1>
<ul>
<li class="ck">Pixel e API de conversões instalados e registrando compras</li>
<li class="ck">Catálogo de produtos atualizado (e-commerce)</li>
<li class="ck">Público semelhante (<b>lookalike</b>) alimentado com quem já comprou de você, com o máximo de dados possível</li>
<li class="ck">Remarketing: quem visitou o site, engajou com o perfil, assistiu aos vídeos ou abandonou o carrinho</li>
<li class="ck">Negócio local: <b>segmentação por região</b>, alcançando quem mora, trabalha ou circula perto de você</li>
<li class="ck">Criativos diferentes para topo, meio e fundo de funil</li>
<li class="ck">Orçamento separado para aquecimento e para a semana da Black</li>
</ul>''', 9)

page('light', f'''<div class="kick">Um olhar para o seu negócio</div><h1>Cada negócio pede <em class="g">uma estratégia</em></h1>
<p>Um e-commerce, uma loja de bairro, um restaurante e um infoprodutor não fazem a mesma Black Friday. A oferta, o canal e o público mudam tudo.</p>
<div class="cta"><div class="t">Quer um direcional para o seu negócio?</div><p>No <b>Diagnóstico Recria</b>, entendemos o seu negócio e os seus objetivos, mapeamos os gargalos, mostramos as alavancas de crescimento e entregamos tudo documentado depois de uma reunião online.</p><a class="l" href="https://www.agenciarecria.com.br/diagnostico-recria/?utm_source=checklist_black">{LINK_CONSULTORIA}</a></div>''', 10)

page('dark', '''<div class="kick">Oferta e operação</div><h1>Antes de <em class="g">abrir as vendas</em></h1>
<ul>
<li class="ck">Oferta decidida, com a <b>margem calculada</b> (desconto que dá prejuízo não é estratégia)</li>
<li class="ck">Prefira kits, combos e bônus a desconto no item isolado</li>
<li class="ck">Estoque, frete e prazo de entrega claros na página</li>
<li class="ck">Atendimento preparado no WhatsApp e no direct, com respostas prontas</li>
<li class="ck">Site testado no celular, do anúncio até o pagamento</li>
</ul>
<div class="box">Não seja a "Black Fraude": subir o preço antes para "dar 50%" depois é a famosa metade do dobro. O cliente pesquisa histórico de preço, e a reputação que você perde vale mais que a venda de um dia.</div>''', 11)

page('light', f'''<div class="kick">Tráfego pago</div><h1 style="font-size:48px;margin-bottom:18px">As métricas que <em class="g">você precisa acompanhar</em></h1>
<table><tr><th>Métrica</th><th>O que mostra</th></tr>
<tr><td style="padding:7px 12px;font-size:20px">CPM</td><td style="padding:7px 12px;font-size:20px">Quanto custa aparecer mil vezes. Sobe muito na semana da Black.</td></tr>
<tr><td style="padding:7px 12px;font-size:20px">CTR</td><td style="padding:7px 12px;font-size:20px">Quantas pessoas clicam depois de ver o anúncio. Mede o poder do criativo.</td></tr>
<tr><td style="padding:7px 12px;font-size:20px">CPC</td><td style="padding:7px 12px;font-size:20px">Quanto custa cada clique.</td></tr>
<tr><td style="padding:7px 12px;font-size:20px">CPA</td><td style="padding:7px 12px;font-size:20px">Quanto custa cada venda (ou cada lead).</td></tr>
<tr><td style="padding:7px 12px;font-size:20px">ROAS</td><td style="padding:7px 12px;font-size:20px">Quanto volta de faturamento para cada real investido.</td></tr></table>
<p style="margin-top:14px;font-size:24px;margin-bottom:10px">Ler essas métricas e ajustar as campanhas todos os dias faz diferença, na Black e no ano inteiro.</p>
<div class="cta" style="margin-top:6px;padding:24px 30px"><div class="t" style="font-size:31px">Quer alguém cuidando das suas campanhas o ano todo?</div><p style="font-size:22px">Na Agência Recria, cuidamos das suas campanhas de <b>tráfego pago</b> no Google e no Instagram o ano inteiro, não só na Black Friday. Veja o serviço de tráfego pago e todos os nossos serviços:</p><a class="l" href="https://www.agenciarecria.com.br/?utm_source=checklist_black#servicos">{LINK_TRAFEGO}</a>
<p style="font-size:22px;margin-top:16px"><b>Aproveite enquanto está disponível:</b> o nosso <b>pacote inicial</b> reúne tráfego pago (Google e Instagram), social media, site ou página de vendas e treinamento do time comercial por <b>R$ 1.500/mês</b>. É uma oferta por tempo limitado: se o link não abrir, o pacote já saiu do ar.</p>
<a class="l" href="https://www.agenciarecria.com.br/pacote-mkt-inicial/?utm_source=checklist_black">Quero o pacote inicial</a></div>''', 12)

page('dark', '''<div class="kick">Depois da Black</div><h1>A Black não termina <em class="g">no último dia</em></h1>
<ul>
<li class="ck"><b>Giftback:</b> um crédito para a próxima compra, para trazer o cliente de volta</li>
<li class="ck">Comunicação pós-compra: como usar, o que combina, cuidados</li>
<li class="ck">Pedir avaliação e depoimento, que viram prova social para o Natal</li>
<li class="ck">Levar os novos clientes para a base e para o grupo VIP</li>
<li class="ck">Já emendar com as campanhas de Natal</li>
</ul>
<div class="box">A venda da Black é o começo do relacionamento, não o fim.</div>''', 13)

page('light', '''<div class="kick">Para concluir</div><h1>Começou agora? <em class="g">Ainda dá tempo.</em></h1>
<p>Se você está começando a se preparar em outubro, já está um pouco atrasada. Mas ainda dá para fazer acontecer: siga o calendário, ative as campanhas o quanto antes e trabalhe a sua base.</p>
<p>E para o ano que vem: <b>a Black Friday começa em agosto</b>, se não antes. É quando o público começa a ser aquecido. Quanto mais cedo você atrai, mais barato fica vender, e menos você depende de cliente novo no período mais caro e disputado do ano.</p>
<div class="box">Comece 2027 com o calendário de ações de marketing do ano inteiro pronto. O seu próximo ano, e também a próxima Black Friday, agradecem.</div>
<p style="font-size:25px">E se quiser a ajuda da Agência Recria, conheça todos os nossos serviços em <a style="color:#9a7424;font-weight:600" href="https://www.agenciarecria.com.br/?utm_source=checklist_black#servicos">agenciarecria.com.br</a></p>
<p style="margin-top:12px;font-family:'Playfair Display';font-style:italic;font-size:28px;color:#9a7424;margin-bottom:4px">Com carinho,<br>Amanda, CEO da Agência Recria</p>
<p style="font-size:21px;color:#5a4412">@agencia.recria · @amandarecria</p>
<div class="cta" style="margin-top:14px;padding:22px 28px"><div class="t" style="font-size:28px">🎁 Mais um presente para você</div><p style="font-size:22px">Para você dar continuidade aos seus estudos: um <b>aulão de Marketing para Negócios</b>, totalmente gratuito. Clique no link abaixo e bons estudos!</p><a class="l" href="https://www.agenciarecria.com.br/aula-mkt-para-negocios/?utm_source=checklist_black">▶ Assistir ao aulão gratuito</a></div>''', 14)

html = f'<!doctype html><html><head><meta charset="utf-8"><title>Checklist Black Friday 2026 · Agência Recria</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
out = pathlib.Path('/home/user/recria-clientes/agencia-recria/iscas-digitais/Checklist Black Friday 2026 - Agencia Recria.pdf')
out.parent.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    br = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg = br.new_page(); pg.set_content(html, wait_until='networkidle'); pg.evaluate('document.fonts.ready')
    pg.pdf(path=str(out), width='1080px', height='1350px', print_background=True)
    br.close()
print(out)
