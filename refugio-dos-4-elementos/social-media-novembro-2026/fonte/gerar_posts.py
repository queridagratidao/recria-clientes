"""Gera as artes de novembro/2026 do Refugio dos 4 Elementos no padrao visual de outubro.
Uso: python3 gerar_posts.py <pasta_fotos> <pasta_saida> <post_setembro_slide2_para_icone>
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

FOTOS, OUT, ICON_SRC = sys.argv[1], sys.argv[2], sys.argv[3]
F = '/home/claude/fonts/'
os.makedirs(OUT, exist_ok=True)

W, H, PH = 1080, 1350, 985
CREME = (247, 243, 236); MARROM = (59, 46, 42)
LILAS = (120, 82, 160); VERDE = (46, 120, 69); TERRA = (184, 90, 46); AZUL = (74, 154, 181)

def font(n, s): return ImageFont.truetype(F + n + '.ttf', s)

# icone dos 4 elementos recortado do carrossel de setembro (escuro sobre creme) -> mascara
src = Image.open(ICON_SRC).convert('L').crop((944, 70, 1028, 154))
mask = ImageOps.invert(src).point(lambda v: 0 if v < 40 else min(255, int((v - 40) * 1.35)))
mask = mask.resize((96, 96), Image.LANCZOS)

def icon(img, xy, cor, sombra=False):
    if sombra:
        sh = Image.new('RGBA', img.size, (0, 0, 0, 0))
        g = Image.new('RGBA', (220, 220), (0, 0, 0, 0)); d = ImageDraw.Draw(g)
        d.ellipse((30, 30, 190, 190), fill=(40, 30, 30, 70)); g = g.filter(ImageFilter.GaussianBlur(28))
        sh.paste(g, (xy[0] - 62, xy[1] - 62), g); img.alpha_composite(sh)
    layer = Image.new('RGBA', mask.size, cor + (255,)); layer.putalpha(mask)
    img.alpha_composite(layer, xy)

def wrap(d, txt, f, maxw):
    if '\n' in txt:
        return [l for parte in txt.split('\n') for l in wrap(d, parte, f, maxw)]
    linhas, cur = [], ''
    for w in txt.split():
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: linhas.append(cur); cur = w
    linhas.append(cur); return linhas

def pill(d, x, y, txt, cor):
    f = font('QS-700', 30); tw = d.textlength(txt, font=f)
    d.rounded_rectangle((x, y, x + tw + 58, y + 62), radius=31, fill=cor)
    d.text((x + 29, y + 31), txt, font=f, fill=(255, 255, 255), anchor='lm')

def foto(nome, foco_y=0.15, foco_x=0.5, zoom=1.0, pb=False):
    im = Image.open(os.path.join(FOTOS, nome)).convert('RGB')
    if pb: im = ImageOps.grayscale(im).convert('RGB')
    s = W * zoom / im.width; im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = int((im.width - W) * foco_x); y = int((im.height - PH) * foco_y)
    return im.crop((x, y, x + W, y + PH))

def post(arq, nome_foto, label, titulo, sub, botao, cor, **kw):
    global PH
    img = Image.new('RGBA', (W, H), CREME + (255,))
    d = ImageDraw.Draw(img)
    nt = len(wrap(d, titulo, font('CG-600', 52), 952)); ns = len(wrap(d, sub, font('LO-400', 30), 952))
    bloco = 55 + 46 + nt * 58 + 14 + ns * 40 + 20 + 62 + 60
    PH = H - bloco
    img.paste(foto(nome_foto, **kw), (0, 0))
    d = ImageDraw.Draw(img)
    d.line((0, PH, W, PH), fill=(225, 218, 208), width=2)
    icon(img, (928, 66), (255, 255, 255), sombra=True)
    d = ImageDraw.Draw(img)
    y = PH + 55
    d.text((64, y), label.upper(), font=font('QS-600', 27), fill=MARROM); y += 46
    ft = font('CG-600', 52)
    for l in wrap(d, titulo, ft, 952): d.text((64, y), l, font=ft, fill=cor); y += 58
    y += 14
    fs = font('LO-400', 30)
    for l in wrap(d, sub, fs, 952): d.text((64, y), l, font=fs, fill=(85, 72, 66)); y += 40
    pill(d, 64, y + 20, botao, cor)
    assert y + 82 < H - 30, arq + ' estourou a altura'
    img.convert('RGB').save(os.path.join(OUT, arq), quality=92)

def card(arq, n, total, label, titulo, corpo, cor, cta=None):
    img = Image.new('RGBA', (W, H), CREME + (255,)); d = ImageDraw.Draw(img)
    icon(img, (930, 70), MARROM); d = ImageDraw.Draw(img)
    y = 300
    d.text((80, y), label.upper(), font=font('QS-600', 28), fill=cor); y += 56
    ft = font('CG-600', 70)
    for l in wrap(d, titulo, ft, 920): d.text((80, y), l, font=ft, fill=cor); y += 78
    y += 34
    fb = font('LO-400', 36)
    for par in corpo:
        for l in wrap(d, par, fb, 920): d.text((80, y), l, font=fb, fill=MARROM); y += 52
        y += 22
    if cta: pill(d, 80, y + 20, cta, cor); y += 90
    assert y < 1200, arq + ' estourou a altura'
    for i in range(total):
        cx = 92 + i * 26
        d.ellipse((cx - 7, 1270 - 7, cx + 7, 1270 + 7) if i == n else (cx - 5, 1270 - 5, cx + 5, 1270 + 5),
                  fill=LILAS if i == n else (205, 192, 214))
    if n < total - 1: d.text((1000, 1270), 'ARRASTE >', font=font('QS-700', 24), fill=MARROM, anchor='rm')
    img.convert('RGB').save(os.path.join(OUT, arq), quality=92)

J = lambda n: f'{n}_Jean_Amorim_27-07-26.jpg'

post('post02_06-11_louvacao-novembro.jpg', J(182), 'Louvação · Novembro',
     'Um encontro mensal de fé, cura e gratidão.',
     'Sábado, 28/11 · Quintal de Ogum, Cuiabá', 'Leia a legenda', TERRA, foco_y=0.30, foco_x=0.45)

# carrossel: capa com foto + cards so texto
post('post03_11-11_carrossel-capa.jpg', J(211), 'Antes de começar',
     'O Refúgio não é para todo mundo. E tudo bem.',
     'Arraste e veja se ele é pra você.', 'Arraste >', LILAS, foco_y=0.18)
cards = [
    ('É pra você se...', 'Você carrega um peso que não consegue nomear.',
     ['Aquele cansaço que não passa com descanso. A sensação de que algo está fora do lugar, mesmo quando tudo parece bem por fora.'], VERDE),
    ('É pra você se...', 'A mesma história se repete na sua vida.',
     ['Nos relacionamentos, no trabalho, com dinheiro. Você muda o cenário, mas o roteiro parece sempre o mesmo.'], VERDE),
    ('É pra você se...', 'Você está atravessando exaustão, ansiedade, luto ou uma grande mudança.',
     ['E sente que o que já tentou até aqui não deu conta de tudo.'], VERDE),
    ('É pra você se...', 'Você tem curiosidade, mesmo cheia(o) de dúvidas.',
     ['Não precisa chegar sabendo o que é Constelação ou Reiki. A gente explica tudo antes, sem pressa e sem julgamento.'], VERDE),
    ('Não é pra você se...', 'Você procura cura milagrosa ou com prazo marcado.',
     ['Aqui o cuidado é um processo, no seu tempo.', 'E se você está em crise aguda, o primeiro passo é procurar atendimento médico de urgência.'], TERRA),
    ('Não é pra você se...', 'Você busca o ritual de uma religião específica.',
     ['Nosso trabalho é universalista. Todas as crenças são bem-vindas, e nenhuma é exigida.'], TERRA),
    ('Se reconheceu?', 'Você não precisa estar pronta(o). Só precisa estar aberta(o).',
     ['Salve este post e mande pra alguém que precisa ler isso hoje.'], LILAS),
]
for i, (lb, t, c, cor) in enumerate(cards, start=1):
    card(f'post03_11-11_carrossel-card{i + 1}.jpg', i, 8, lb, t, c, cor,
         cta='Comenta REFÚGIO' if i == 7 else None)

post('post04_13-11_cofundadores.jpg', J(283), 'Quem cuida de você',
     'Daniela e Joelson, de onde o Refúgio nasceu.',
     'É na casa deles que o Refúgio acolhe, há 3 anos, quem chega.', 'Conheça na legenda', LILAS, foco_y=0.20)
post('post05_18-11_antes-da-terapia.jpg', J(59), 'Como funciona',
     'Antes de qualquer terapia,\nexiste uma conversa.',
     'Para entendermos juntos qual é a melhor indicação pra você.', 'Continua na legenda', VERDE,
     foco_y=0.22, foco_x=0.55)
post('post06_20-11_ancestralidade.jpg', J(237), 'Constelação Familiar',
     'Honrar quem veio antes\ntambém é cuidar de si.',
     'Carregar crenças e traumas que limitam a sua vida, não.', 'Continua na legenda', TERRA, foco_y=0.20)
post('post07_25-11_prazer-jean.jpg', J(329), 'Quem cuida de você',
     'Prazer, Jean Carlos.',
     'Constelador, analista comportamental e mestre em Reiki.', 'Conheça na legenda', LILAS, foco_y=0.12)
post('post08_27-11_terapia-xamanica.jpg', J(219), 'Terapia Xamânica dos 4 Elementos',
     'Tem ciclos que pedem mais do que conversa para se encerrar.',
     'Terra, Água, Ar e Fogo como caminho de volta pra sua essência.', 'Leia a legenda', AZUL, foco_y=0.30)
print('ok')
