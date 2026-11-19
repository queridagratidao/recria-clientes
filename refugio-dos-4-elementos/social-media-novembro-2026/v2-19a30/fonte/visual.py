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
    im = Image.open(path).convert('RGB')
    if pb: im = ImageOps.grayscale(im).convert('RGB')
    s = max(w / im.width, h / im.height) * zoom
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = int((im.width - w) * fx); y = int((im.height - h) * fy)
    return im.crop((x, y, x + w, y + h))

def gradiente(img, inicio, alpha_max=225):
    w, h = img.size
    g = Image.new('L', (1, h), 0)
    for y in range(h):
        t = 0 if y < inicio else (y - inicio) / (h - inicio)
        g.putpixel((0, y), int(alpha_max * min(1, t ** 0.85 * 1.15)))
    g = g.resize((w, h))
    escuro = Image.new('RGBA', (w, h), (34, 24, 22, 255)); escuro.putalpha(g)
    img.alpha_composite(escuro)
    topo = Image.new('L', (1, 220), 0)
    for y in range(220): topo.putpixel((0, y), int(90 * (1 - y / 220)))
    t = Image.new('RGBA', (w, 220), (20, 14, 12, 255)); t.putalpha(topo.resize((w, 220)))
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

def post_foto(out, foto, titulo, sub, botao='leia a legenda +', kicker=None, w=W, h=H, camada=None, **kw):
    """Foto inteira + gradiente + titulo serifado branco embaixo (estilo capa).
    camada='fundo' -> so foto+gradiente; camada='texto' -> so textos em PNG transparente (para Reels)."""
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    if camada != 'texto': img.paste(cover(foto, w, h, **kw), (0, 0))
    d = ImageDraw.Draw(img)
    ft = font('CG-600', 74 if w == W else 84); fs = font('LO-400', 32 if w == W else 36)
    margem = 70; maxw = w - 2 * margem
    lt = wrap(d, titulo, ft, maxw); ls = wrap(d, sub, fs, maxw) if sub else []
    alt = (46 if kicker else 0) + len(lt) * 80 + (18 + len(ls) * 44 if ls else 0) + (36 + 54 if botao else 0)
    base = h - (110 if w == W else 380)  # reels: area segura acima da interface
    y = base - alt
    if camada != 'texto': gradiente(img, max(0, y - 380))
    if camada == 'fundo':
        img.convert('RGB').save(out, quality=92); return img
    d = ImageDraw.Draw(img)
    d.text((margem, 64), HANDLE, font=font('QS-600', 24), fill=(255, 255, 255, 235))
    icon(img, (w - margem - 84, 44), (255, 255, 255)); d = ImageDraw.Draw(img)
    if kicker:
        d.text((margem, y), kicker.upper(), font=font('QS-700', 25), fill=(236, 222, 205)); y += 46
    for l in lt: d.text((margem, y), l, font=ft, fill=(255, 255, 255)); y += 80
    if ls:
        y += 18
        for l in ls: d.text((margem, y), l, font=fs, fill=(240, 232, 222)); y += 44
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
