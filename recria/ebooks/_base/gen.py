# -*- coding: utf-8 -*-
"""Componentes para gerar o HTML dos e-books Recria. Uso: from gen import *"""
import html as _h
def esc(t): return t  # texto já vem com HTML simples (<b>, <i>, <em>)
def table(headers, rows, cls="compacta"):
    th = "".join(f"<th>{h}</th>" for h in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}"><tr>{th}</tr>{tr}</table>\n'
def ul(items, cls=""): return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>\n"
def ol(items, cls=""): return f'<ol class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ol>\n"
def check(items): return ul(items, "check")
def box(t): return f'<div class="box">{t}</div>\n'
def dica(t, tit="Dica"): return f'<div class="dica"><b>{tit}:</b> {t}</div>\n'
def alerta(t, tit="Atenção"): return f'<div class="alerta"><b>{tit}.</b> {t}</div>\n'
def prompt(rot, t): return f'<div class="prompt"><span class="rot">{rot}</span>{t}</div>\n'
def q(label, lines=1):
    r = '<div class="r"></div>' + '<div class="r2"></div>' * (lines - 1)
    return f'<div class="q"><div class="l">{label}</div>{r}</div>\n'
def cols2(sim_t, sim, nao_t, nao):
    return f'<div class="cols2"><div class="b sim"><h3>{sim_t}</h3>{sim}</div><div class="b nao"><h3>{nao_t}</h3>{nao}</div></div>\n'
def passos(items):
    n = len(items)
    c = "".join(f'<div class="passo"><div class="n">{i+1}</div><b>{a}</b><br>{b}</div>' for i, (a, b) in enumerate(items))
    return f'<div class="passos" style="grid-template-columns:repeat({n},1fr)">{c}</div>\n'
def sec(kick, title, body, cap=False):
    k = f'<div class="kick" style="margin-top:7mm">{kick}</div>\n' if kick else ""
    return f'<section class="{"cap" if cap else "flow"}">\n{k}<h1>{title}</h1>\n{body}</section>\n\n'
def cont(title, body):  # continuação sem quebra de página
    return f'<section class="flow">\n<h2 style="margin-top:0">{title}</h2>\n{body}</section>\n\n'
def head(titulo):
    return f'<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8">\n<title>{titulo}</title>\n<link rel="stylesheet" href="../_base/ebook.css">\n</head><body>\n\n'
def cover(tag, h1, sub):
    return f'''<section class="cover">
<img src="../_base/logo.png" alt="Recria">
<div>
<div class="tag">{tag}</div>
<h1>{h1}</h1>
<p>{sub}</p>
</div>
<div class="preco">Recria · Recriando marketing, simplificando vendas</div>
</section>

'''
def card(t, desc, preco_link):
    return f'<div class="c"><h3>{t}</h3><p>{desc}</p><p><i>Preço bem acessível.</i></p><a class="btn" href="{preco_link}">Quero conhecer</a></div>'
BTN = 'style="padding:2mm 4mm;font-size:9pt"'
def oferta(kick, titulo, texto, link, rotulo="Quero conhecer", margem="2mm"):
    return f'''<div class="oferta" style="margin-top:{margem};padding:2.5mm 4mm">
<div class="kick" style="margin-bottom:1mm">{kick}</div>
<h3 style="margin:0 0 1mm">{titulo}</h3>
<p style="margin-bottom:2mm;font-size:9.4pt">{texto}</p>
<a class="btn" href="{link}" {BTN}>{rotulo}</a>
</div>
'''
def final1(kick, h1, intro, destaque, cards):
    """destaque = (kick, titulo, texto, link, rotulo) do próximo degrau; cards = lista de (titulo, desc, link)"""
    cs = "".join(card(*c) for c in cards)
    extra = f'<div class="kick" style="margin:3mm 0 0">Outros próximos passos</div>\n<div class="cards3" style="margin:2mm 0;font-size:7.8pt">{cs}</div>' if cards else ""
    return f'''<section class="upsell">
<div class="kick">{kick}</div>
<h1 style="font-size:16pt;margin-bottom:2mm">{h1}</h1>
<p style="margin-bottom:2mm">{intro}</p>
{oferta(*destaque, margem="2mm")}
{extra}
{oferta("Curso", "Recria Ads", "Aprenda a criar conteúdos e anúncios <b>sem cara de anúncio</b> e sem parecer aquele vendedor chato, vendendo com leveza. Curso aprofundado, com exercícios práticos.", "LINK-ADS", "Quero conhecer o Recria Ads", "2mm")}
{oferta("Comunidade gratuita", "Recriadores", "Comunidade gratuita no WhatsApp, com conteúdos exclusivos e atividades práticas toda semana, para você recriar o seu negócio e vender mais todos os meses.", "LINK-GRUPO", "Quero entrar na comunidade", "2mm")}
</section>

'''
def final2(mentoria=True, comunidade=True):
    def o(k, t, x, l): return oferta(k, t, x, l, "Quero conhecer", "1.6mm").replace('padding:2.5mm 4mm','padding:2mm 4mm')
    return f'''<section class="upsell">
<div class="kick">Quer ir além?</div>
<h1 style="font-size:15pt;margin-bottom:1mm">Cresça <em>mês a mês</em> junto com a Recria.</h1>
{(o("Comunidade paga","Comunidade Recria Business","Quer crescer mês a mês junto com a Recria? Participe da comunidade, com vários cursos: negócio, marketing, comercial, novidades do segmento, posicionamento e como recriar o seu negócio em vários níveis.","LINK-COMUNIDADE") if comunidade else "")}
{o("Consultoria","Diagnóstico Recria","Quer um direcional personalizado para o seu negócio? Conheça o Diagnóstico Recria, a nossa consultoria online individual para mapear os gargalos que estão impedindo as suas vendas e o crescimento do seu negócio.","LINK-CONSULTORIA")}
{(o("Acompanhamento","Mentoria","Quer ter uma estrutura e alguém que pegue na sua mão e ajude você em cada etapa para melhorar o seu negócio? Conheça a nossa mentoria.","LINK-MENTORIA") if mentoria else "")}
{o("Feito para você","Serviços da Recria","Quer que a gente faça por você? Conheça os serviços da Recria, como estruturação e reestruturação de negócio, tráfego pago, social media e muito mais.","LINK-SERVICOS")}
</section>

'''
def leituras(itens, aviso):
    return f'''<section class="flow">
<h2 style="margin-top:4mm">Para ir mais fundo: leituras e fontes</h2>
{ul(itens)}<p class="peq"><b>Aviso.</b> {aviso} © Agência Recria. Uso individual; proibido revender ou compartilhar sem autorização.</p>
</section>

'''
THANKS = '<section class="upsell">\n<div class="kick">Obrigada por chegar até aqui</div>\n<h1 style="font-size:17pt">Um presente para você: <em>o aulão gratuito.</em></h1>\n<p>Obrigada por ler este material até o fim. Espero, de coração, que ele ajude você a dar o próximo passo no seu negócio.</p>\n<div class="oferta" style="margin-top:3mm;padding:3mm 4mm">\n<div class="kick" style="margin-bottom:1mm">Presente</div>\n<h3 style="margin:0 0 1mm">Aulão: por que o seu marketing não funciona e o seu comercial não converte como deveria?</h3>\n<p style="margin-bottom:2mm;font-size:9.4pt">Uma aula gratuita dividindo com você mais de 10 anos de experiência em marketing e comercial, para mostrar o que quase ninguém conta de maneira gratuita.</p>\n<a class="btn" href="LINK-AULAO" style="padding:2mm 4mm;font-size:9pt">Quero assistir ao aulão</a>\n</div>\n<p style="margin-top:6mm;font-family:\'Playfair Display\',serif;font-style:italic;color:#E4C988;font-size:12pt">Com carinho,<br>Amanda Moraes, Agência Recria</p>\n</section>\n\n'
def thanks(): return THANKS
def tail(): return thanks() + "</body></html>\n"
