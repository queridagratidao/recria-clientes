# -*- coding: utf-8 -*-
"""Gera os 4 criativos estáticos (2 conceitos x 2 formatos) pro anúncio
Eleva - Multiplicar Vendas para Condomínios, com Pillow, controle exato
de cor de marca (#0A0C0F / #E09C3B) e tipografia Sora."""
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = r"C:\Users\amand\AppData\Local\Temp\claude\C--Users-amand-OneDrive-Documentos-Agencia-de-IA\3fe07fba-9f71-405e-8476-7a4a9a1a0aab\scratchpad\fonts\Sora-ExtraBold.ttf"
LOGO_PATH = os.path.join(BASE, "logo-eleva-branco.png")

BG = (10, 12, 15)       # #0A0C0F
ORANGE = (224, 156, 59)  # #E09C3B
WHITE = (245, 245, 245)
GRAY = (170, 173, 178)

CTA_TEXT = "Toque no botão para saber mais"
_LOGO_SRC = Image.open(LOGO_PATH).convert("RGBA")


def font(size, variation="ExtraBold"):
    f = ImageFont.truetype(FONT_PATH, size)
    try:
        f.set_variation_by_name(variation)
    except Exception:
        pass
    return f


def wrap_draw(draw, text, fnt, max_width, x, y, fill, line_spacing=1.25, align="left"):
    """Quebra texto em linhas que cabem em max_width e desenha, retorna y final."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=fnt) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)

    bbox = fnt.getbbox("Ay")
    line_h = (bbox[3] - bbox[1]) * line_spacing
    for line in lines:
        if align == "center":
            lw = draw.textlength(line, font=fnt)
            draw.text((x - lw / 2, y), line, font=fnt, fill=fill)
        else:
            draw.text((x, y), line, font=fnt, fill=fill)
        y += line_h
    return y


def base_canvas(size):
    img = Image.new("RGBA", size, BG + (255,))
    return img, ImageDraw.Draw(img)


def draw_cta(draw, y, cta_font, pad=46):
    draw.text((pad, y), CTA_TEXT.upper(), font=cta_font, fill=ORANGE)


def paste_logo(img, pad, logo_width, bottom_margin):
    """Cola o logo branco da Eleva no canto inferior esquerdo, mantendo a proporção original."""
    ratio = _LOGO_SRC.height / _LOGO_SRC.width
    logo_h = int(logo_width * ratio)
    logo = _LOGO_SRC.resize((logo_width, logo_h), Image.LANCZOS)
    x = pad
    y = img.height - bottom_margin - logo_h
    img.alpha_composite(logo, (x, y))
    return y


# ---------- Criativo 1: Objeção Invertida ----------

def objecao_invertida_feed():
    W = H = 1080
    img, d = base_canvas((W, H))
    pad = 80

    title_font = font(58)
    sub_font = font(34)
    cta_font = font(28)

    y = 130
    quote = "“Fornecedor bom não precisa saber vender. Precisa entregar bem.”"
    y = wrap_draw(d, quote, title_font, W - 2 * pad, pad, y, WHITE, line_spacing=1.22)

    y += 48
    sub = "Se você acredita nisso, está perdendo contratos todo mês sem perceber."
    wrap_draw(d, sub, sub_font, W - 2 * pad, pad, y, ORANGE, line_spacing=1.3)

    draw_cta(d, H - 150, cta_font, pad)
    paste_logo(img, pad, logo_width=220, bottom_margin=60)
    return img


def objecao_invertida_story():
    W, H = 1080, 1920
    img, d = base_canvas((W, H))
    pad = 90

    title_font = font(62)
    sub_font = font(36)
    cta_font = font(30)

    top_safe = int(H * 0.14)
    bottom_safe = H - int(H * 0.14)

    y = top_safe + 90
    quote = "“Fornecedor bom não precisa saber vender. Precisa entregar bem.”"
    y = wrap_draw(d, quote, title_font, W - 2 * pad, pad, y, WHITE, line_spacing=1.25)

    y += 70
    sub = "Se você acredita nisso, está perdendo contratos todo mês sem perceber."
    wrap_draw(d, sub, sub_font, W - 2 * pad, pad, y, ORANGE, line_spacing=1.35)

    draw_cta(d, bottom_safe - 150, cta_font, pad)
    paste_logo(img, pad, logo_width=240, bottom_margin=(H - bottom_safe) + 40)
    return img


# ---------- Criativo 2: Perda Silenciosa ----------

def perda_silenciosa_feed():
    W = H = 1080
    img, d = base_canvas((W, H))
    pad = 80

    title_font = font(50)
    body_font = font(30, variation="Regular")
    cta_font = font(28)

    y = 120
    title = "Quantos contratos com condomínio você perdeu nos últimos 6 meses sem nem saber por quê?"
    y = wrap_draw(d, title, title_font, W - 2 * pad, pad, y, WHITE, line_spacing=1.25)

    y += 50
    body = "O gestor não te ligou de volta. A reunião não evoluiu. Você mandou proposta e ficou no silêncio."
    wrap_draw(d, body, body_font, W - 2 * pad, pad, y, GRAY, line_spacing=1.35)

    draw_cta(d, H - 150, cta_font, pad)
    paste_logo(img, pad, logo_width=220, bottom_margin=60)
    return img


def perda_silenciosa_story():
    W, H = 1080, 1920
    img, d = base_canvas((W, H))
    pad = 90

    title_font = font(54)
    body_font = font(32, variation="Regular")
    cta_font = font(30)

    top_safe = int(H * 0.14)
    bottom_safe = H - int(H * 0.14)

    y = top_safe + 100
    title = "Quantos contratos com condomínio você perdeu nos últimos 6 meses sem nem saber por quê?"
    y = wrap_draw(d, title, title_font, W - 2 * pad, pad, y, WHITE, line_spacing=1.28)

    y += 70
    body = "O gestor não te ligou de volta. A reunião não evoluiu. Você mandou proposta e ficou no silêncio."
    wrap_draw(d, body, body_font, W - 2 * pad, pad, y, GRAY, line_spacing=1.4)

    draw_cta(d, bottom_safe - 150, cta_font, pad)
    paste_logo(img, pad, logo_width=240, bottom_margin=(H - bottom_safe) + 40)
    return img


if __name__ == "__main__":
    out = BASE
    jobs = [
        ("01_objecao-invertida_feed-1x1.png", objecao_invertida_feed),
        ("02_objecao-invertida_story-9x16.png", objecao_invertida_story),
        ("03_perda-silenciosa_feed-1x1.png", perda_silenciosa_feed),
        ("04_perda-silenciosa_story-9x16.png", perda_silenciosa_story),
    ]
    for name, fn in jobs:
        img = fn().convert("RGB")
        path = os.path.join(out, name)
        img.save(path, "PNG")
        print("salvo:", path)
