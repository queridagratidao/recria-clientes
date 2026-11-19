"""Sistema visual v2 do Refugio dos 4 Elementos (nov/2026): foto inteira com titulo sobreposto e cards de texto.
Inspirado no padrao atual da agencia (Pathy), com cores e fontes do manual do Refugio."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

F = '/home/claude/fonts/'
W, H = 1080, 1350
CREME = (247, 243, 236); MARROM = (59, 46, 42); TEXTO = (85, 72, 66)
LILAS = (120, 82, 160); VERDE = (46, 120, 69); TERRA = (184, 90, 46); AZUL = (60, 135, 160)
HANDLE = '@refugiodos4elementos'
_ICON_SRC = '/home/claude/w/refugio-dos-4-elementos/social-media-setembro-2026/post-set01_slide-2.jpg'

def font(n, s): return ImageFont.truetype(F + n + '.ttf', s)

_src = Image.open(_ICON_SRC).convert('L').crop((944, 70, 1028, 154))
_mask = ImageOps.invert(_src).point(lambda v: 0 if v < 40 else min(255, int((v - 40) * 1.35)))

def icon(img, xy, cor, size=84):
    m = _mask.resize((size, size), Image.LANCZOS)
    layer = Image.new('RGBA', m.size, cor + (255,)); layer.putalpha(m)
    img.alpha_composite(layer, xy)

def wrap(d, txt, f, maxw):
    if '\n' in txt:
        return [l for p in txt.split('\n') for l in wrap(d, p, f, maxw)]
    linhas, cur = [], ''
    for w in txt.split():
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: linhas.append(cur); cur = w
    linhas.append(cur); return linhas

def cover(path, w, h, fy=0.2, fx=0.5, zoom=1.0, pb=False):
    im = path.convert('RGB') if isinstance(path, Image.Image) else Image.open(path).convert('RGB')
    if pb: im = ImageOps.grayscale(im).convert('RGB')
    s = max(w / im.width, h / im.height) * zoom
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = int((im.width - w) * fx); y = int((im.height - h) * fy)
    return im.crop((x, y, x + w, y + h))

FADE = (98, 66, 46)

def gradiente(img, inicio, alpha_max=225, cor=None):
    w, h = img.size
    g = Image.new('L', (1, h), 0)
    for y in range(h):
        t = 0 if y < inicio else (y - inicio) / (h - inicio)
        g.putpixel((0, y), int(alpha_max * min(1, t ** 0.85 * 1.15)))
    g = g.resize((w, h))
    escuro = Image.new('RGBA', (w, h), (cor or FADE) + (255,)); escuro.putalpha(g)
    img.alpha_composite(escuro)
    topo = Image.new('L', (1, 220), 0)
    for y in range(220): topo.putpixel((0, y), int(90 * (1 - y / 220)))
    t = Image.new('RGBA', (w, 220), tuple(int(c * 0.85) for c in (cor or FADE)) + (255,)); t.putalpha(topo.resize((w, 220)))
    img.alpha_composite(t, (0, 0))

def pill_contorno(d, x, y, txt, cor=(255, 255, 255), s=26):
    f = font('QS-700', s); tw = d.textlength(txt, font=f)
    d.rounded_rectangle((x, y, x + tw + 44, y + s + 26), radius=(s + 26) // 2, outline=cor, width=2)
    d.text((x + 22, y + (s + 26) / 2), txt, font=f, fill=cor, anchor='lm')

def tag(d, x, y, txt, cor):
    f = font('QS-700', 24); tw = d.textlength(txt, font=f)
    d.rounded_rectangle((x, y, x + tw + 28, y + 42), radius=8, fill=cor)
    d.text((x + 14, y + 21), txt, font=f, fill=(255, 255, 255), anchor='lm')
    return y + 42

def gradiente_topo(img, fim, alpha_max=215, cor=None):
    w, h = img.size
    g = Image.new('L', (1, h), 0)
    for y in range(h):
        t = 1 - y / fim if y < fim else 0
        g.putpixel((0, y), int(alpha_max * min(1, max(0, t) ** 0.8 * 1.1)))
    escuro = Image.new('RGBA', (w, h), (cor or FADE) + (255,)); escuro.putalpha(g.resize((w, h)))
    img.alpha_composite(escuro)

def post_foto(out, foto, titulo, sub, botao='leia a legenda +', kicker=None, w=W, h=H, camada=None,
              topo=False, nome=False, encaixe=None, sem_icone=False, reel_base=None, estilo=None, cor=None, pos='baixo', fade=None, **kw):
    """topo=True: texto no alto (fotos com rostos embaixo). nome=True: subtitulo vira o nome em destaque."""
    """Foto inteira + gradiente + titulo serifado branco embaixo (estilo capa).
    camada='fundo' -> so foto+gradiente; camada='texto' -> so textos em PNG transparente (para Reels)."""
    if estilo == 'card':
        return post_card(out, foto, kicker, titulo, sub, botao, cor or LILAS, pos=pos, nome=nome, encaixe=encaixe, sem_icone=sem_icone, **kw)
    fc = fade or FADE
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    if camada != 'texto':
        if encaixe:  # foto no topo em largura total, fundo escuro embaixo (para fotos que so existem recortadas)
            img = Image.new('RGBA', (w, h), fc + (255,))
            ph = Image.open(foto).convert('RGB').crop(encaixe); ph = ph.resize((w, round(ph.height * w / ph.width)), Image.LANCZOS)
            img.paste(ph, (0, 0))
            fd = min(320, ph.height // 2)
            mf = Image.new('L', (1, fd), 0)
            for yy in range(fd): mf.putpixel((0, yy), int(255 * (yy / fd) ** 1.4))
            esc = Image.new('RGBA', (w, fd), fc + (255,)); esc.putalpha(mf.resize((w, fd)))
            img.alpha_composite(esc, (0, ph.height - fd))
        else:
            img.paste(cover(foto, w, h, **kw), (0, 0))
    d = ImageDraw.Draw(img)
    ft = font('CG-600', 74 if h == H else 84); fs = font('LO-400', 32 if h == H else 36)
    if nome: fs = font('CG-500i', 64 if h == H else 72)
    lh_s = 70 if nome else 44
    margem = 70; maxw = w - 2 * margem
    lt = wrap(d, titulo, ft, maxw); ls = wrap(d, sub, fs, maxw) if sub else []
    alt = (46 if kicker else 0) + len(lt) * 80 + (18 + len(ls) * lh_s if ls else 0) + (36 + 54 if botao else 0)
    if topo:
        y = 150 if h == H else 260
        if camada != 'texto':
            fim = y + alt + 50
            reg = img.crop((0, 0, w, fim)).filter(ImageFilter.GaussianBlur(14))
            m = Image.new('L', (1, fim), 0)
            for yy in range(fim): m.putpixel((0, yy), int(255 * min(1, max(0, (fim - yy) / 110))))
            img.paste(reg, (0, 0), m.resize((w, fim)))
            gradiente_topo(img, fim + 70, alpha_max=250, cor=fc)
            mv = Image.new('L', (1, fim + 40), 0)
            for yy in range(fim + 40): mv.putpixel((0, yy), int(95 * min(1, max(0, (fim + 40 - yy) / 160))))
            veu = Image.new('RGBA', (w, fim + 40), tuple(int(c * 0.85) for c in fc) + (255,)); veu.putalpha(mv.resize((w, fim + 40))); img.alpha_composite(veu, (0, 0))
    else:
        base = h - (110 if h == H else (reel_base or 380))  # reels: area segura acima da interface
        y = base - alt
        if camada != 'texto': gradiente(img, max(0, y - 380), alpha_max=240 if fade else 225, cor=fc)
    if camada == 'fundo':
        img.convert('RGB').save(out, quality=92); return img
    d = ImageDraw.Draw(img)
    d.text((margem, 64), HANDLE, font=font('QS-600', 24), fill=(255, 255, 255, 235))
    if not sem_icone: icon(img, (w - margem - 84, 44), (255, 255, 255))
    d = ImageDraw.Draw(img)
    if kicker:
        d.text((margem, y), kicker.upper(), font=font('QS-700', 25), fill=(236, 222, 205)); y += 46
    for l in lt: d.text((margem, y), l, font=ft, fill=(255, 255, 255)); y += 80
    if ls:
        y += 18
        for l in ls: d.text((margem, y), l, font=fs, fill=(244, 214, 170) if nome else (240, 232, 222)); y += lh_s
    if botao: pill_contorno(d, margem, y + 36, botao)
    if camada == 'texto':
        img.save(out); return img
    img = img.convert('RGB'); img.save(out, quality=92); return img

def card_texto(out, n_tag, titulo, corpo, cor, ref=None, n=0, total=0, cta=None):
    """Card de texto creme: tag numerada, titulo, corpo e quadro de referencia, centralizado na vertical."""
    img = Image.new('RGBA', (W, H), CREME + (255,))
    lay = Image.new('RGBA', (W, H * 2), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    m = 80; maxw = W - 2 * m; y = 0
    if n_tag: y = tag(d, m, y, n_tag, cor) + 38
    ft = font('CG-600', 80)
    for l in wrap(d, titulo, ft, maxw): d.text((m, y), l, font=ft, fill=MARROM); y += 86
    y += 30
    fb = font('LO-400', 38)
    for par in corpo:
        for l in wrap(d, par, fb, maxw): d.text((m, y), l, font=fb, fill=TEXTO); y += 54
        y += 20
    if ref:
        rotulo, texto, fonte = ref
        fr = font('LO-400', 34); fl = font('QS-700', 23); ff = font('QS-600', 25)
        lr = wrap(d, texto, fr, maxw - 72); lf = wrap(d, fonte, ff, maxw - 72)
        hbox = 40 + 34 + len(lr) * 48 + 20 + len(lf) * 34 + 34
        y += 14
        sh = Image.new('RGBA', lay.size, (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
        sd.rounded_rectangle((m, y + 8, W - m, y + hbox + 8), radius=24, fill=(59, 46, 42, 30))
        lay.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12))); d = ImageDraw.Draw(lay)
        d.rounded_rectangle((m, y, W - m, y + hbox), radius=24, fill=(255, 255, 255))
        yy = y + 40
        d.text((m + 36, yy), rotulo.upper(), font=fl, fill=cor); yy += 34
        for l in lr: d.text((m + 36, yy), l, font=fr, fill=MARROM); yy += 48
        yy += 20
        for l in lf: d.text((m + 36, yy), l, font=ff, fill=cor); yy += 34
        y += hbox
    if cta:
        y += 44; f = font('QS-700', 30); tw = d.textlength(cta, font=f)
        d.rounded_rectangle((m, y, m + tw + 60, y + 66), radius=33, fill=cor)
        d.text((m + 30, y + 33), cta, font=f, fill=(255, 255, 255), anchor='lm'); y += 66
    topo, base = 170, H - 150
    assert y <= base - topo, f'{out}: conteudo alto demais ({y})'
    off = topo + (base - topo - y) // 2
    img.alpha_composite(lay.crop((0, 0, W, H)), (0, off)) if off + H <= H * 2 else None
    d = ImageDraw.Draw(img)
    icon(img, (W - m - 70, 70), MARROM, 70); d = ImageDraw.Draw(img)
    d.text((m, 84), HANDLE, font=font('QS-600', 22), fill=(150, 135, 125))
    if total and n < total - 1:
        d.text((W - m, H - 76), 'arrasta  >>>', font=font('QS-700', 24), fill=(170, 150, 140), anchor='rm')
    img = img.convert('RGB'); img.save(out, quality=92); return img

def card_print(out, print_path, legenda, crop=None, n=0, total=0, escala=None):
    """Card creme com o print real (comentario/mensagem) em moldura com sombra."""
    img = Image.new('RGBA', (W, H), CREME + (255,)); d = ImageDraw.Draw(img)
    m = 80
    p = Image.open(print_path).convert('RGB')
    if crop: p = p.crop(crop)
    maxw, maxh = W - 2 * m, 860
    s = min(maxw / p.width, maxh / p.height)
    p = p.resize((round(p.width * s), round(p.height * s)), Image.LANCZOS)
    x = (W - p.width) // 2; y = 250
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
    sd.rounded_rectangle((x, y + 10, x + p.width, y + p.height + 10), radius=26, fill=(59, 46, 42, 45))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(16)))
    mask = Image.new('L', p.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, p.width, p.height), radius=26, fill=255)
    img.paste(p, (x, y), mask); d = ImageDraw.Draw(img)
    fl = font('QS-700', 26)
    d.text((W // 2, y + p.height + 60), legenda.upper(), font=fl, fill=LILAS, anchor='mm')
    icon(img, (W - m - 70, 70), MARROM, 70); d = ImageDraw.Draw(img)
    d.text((m, 84), HANDLE, font=font('QS-600', 22), fill=(150, 135, 125))
    if total and n < total - 1:
        d.text((W - m, H - 76), 'arrasta  >>>', font=font('QS-700', 24), fill=(170, 150, 140), anchor='rm')
    img.convert('RGB').save(out, quality=92)


def post_card(out, foto, label, titulo, sub, botao, cor, pos='baixo', fy=0.2, fx=0.5, zoom=1.0, pb=False,
              nome=False, encaixe=None, sem_icone=False, **_):
    """Padrao dos posts anteriores: foto + faixa creme com etiqueta, titulo colorido, subtitulo e botao."""
    img = Image.new('RGBA', (W, H), CREME + (255,)); d = ImageDraw.Draw(img)
    m = 64; maxw = W - 2 * m
    ft = font('CG-600', 54); fs = font('CG-500i', 46) if nome else font('LO-400', 30); lhs = 52 if nome else 40
    lt = wrap(d, titulo, ft, maxw); ls = wrap(d, sub, fs, maxw) if sub else []
    if encaixe: foto = Image.open(foto).convert('RGB').crop(encaixe)
    txt_b = {'leia a legenda +': 'Leia a legenda', 'arrasta >': 'Arrasta >'}.get(botao, botao or 'Leia a legenda')
    banda = 52 + (46 if label else 0) + len(lt) * 60 + (14 + len(ls) * lhs if ls else 0) + 22 + 62 + 56
    ph = H - banda
    if pos == 'topo':
        img.paste(cover(foto, W, ph, fy=fy, fx=fx, zoom=zoom, pb=pb), (0, banda)); y0 = 0
        d = ImageDraw.Draw(img); d.line((0, banda, W, banda), fill=(225, 218, 208), width=2)
        icon(img, (W - m - 70, 46), MARROM, 70)
    else:
        img.paste(cover(foto, W, ph, fy=fy, fx=fx, zoom=zoom, pb=pb), (0, 0)); y0 = ph
        d = ImageDraw.Draw(img); d.line((0, ph, W, ph), fill=(225, 218, 208), width=2)
        sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); g = Image.new('RGBA', (220, 220), (0, 0, 0, 0))
        ImageDraw.Draw(g).ellipse((30, 30, 190, 190), fill=(40, 30, 30, 70)); g = g.filter(ImageFilter.GaussianBlur(28))
        if not sem_icone: sh.paste(g, (W - m - 84 - 62, 46 - 62), g); img.alpha_composite(sh)
        if not sem_icone: icon(img, (W - m - 84, 46), (255, 255, 255))
    d = ImageDraw.Draw(img); y = y0 + 52
    if label:
        d.text((m, y), label.upper(), font=font('QS-600', 27), fill=MARROM); y += 46
    for l in lt: d.text((m, y), l, font=ft, fill=cor); y += 60
    if ls:
        y += 14
        for l in ls: d.text((m, y), l, font=fs, fill=cor if nome else TEXTO); y += lhs
    y += 22; f = font('QS-700', 30); tw = d.textlength(txt_b, font=f)
    d.rounded_rectangle((m, y, m + tw + 58, y + 62), radius=31, fill=cor)
    d.text((m + 29, y + 31), txt_b, font=f, fill=(255, 255, 255), anchor='lm')
    img = img.convert('RGB'); img.save(out, quality=92); return img
