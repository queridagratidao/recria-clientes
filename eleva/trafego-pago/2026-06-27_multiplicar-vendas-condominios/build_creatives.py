# -*- coding: utf-8 -*-
"""Gera os 4 criativos estáticos (2 conceitos x 2 formatos) pro anúncio
Eleva - Multiplicar Vendas para Condomínios, com Pillow, controle exato
de cor de marca (#0A0C0F / #E09C3B) e tipografia Sora."""
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = r"C:\Users\amand\AppData\Local\Temp\claude\C--Users-amand-OneDrive-Documentos-Agencia-de-IA\3fe07fba-9f71-405e-8476-7a4a9a1a0aab\scratchpad\fonts\Sora-ExtraBold.ttf"

BG = (10, 12, 15)       # #0A0C0F
ORANGE = (224, 156, 59)  # #E09C3B
WHITE = (245, 245, 245)
GRAY = (170, 173, 178)

CTA_TEXT = "Aprenda a multiplicar vendas para condomínios"


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


def icon_document_loss(draw, cx, cy, scale=1.0, color=ORANGE):
    """Ícone simples de documento com seta descendente (perda de contrato)."""
    w, h = 70 * scale, 90 * scale
    x0, y0 = cx - w / 2, cy - h / 2
    draw.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=6 * scale, outline=color, width=int(4 * scale))
    for i in range(3):
        ly = y0 + h * 0.3 + i * h * 0.18
        draw.line([x0 + w * 0.18, ly, x0 + w * 0.82, ly], fill=color, width=int(3 * scale))
    ax, ay = cx, y0 + h + 14 * scale
    draw.line([ax, y0 + h * 0.55, ax, ay], fill=color, width=int(5 * scale))
    draw.polygon([(ax - 12 * scale, ay - 14 * scale), (ax + 12 * scale, ay - 14 * scale), (ax, ay + 4 * scale)], fill=color)


def icon_silent_chat(draw, cx, cy, scale=1.0, color=ORANGE):
    """Balão de chat com reticências (silêncio sem resposta)."""
    w, h = 110 * scale, 70 * scale
    x0, y0 = cx - w / 2, cy - h / 2
    draw.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=16 * scale, outline=color, width=int(4 * scale))
    draw.polygon([(cx - 14 * scale, y0 + h), (cx + 14 * scale, y0 + h), (cx - 4 * scale, y0 + h + 18 * scale)], fill=color)
    r = 5 * scale
    for i, dx in enumerate([-22, 0, 22]):
        ddx = dx * scale
        draw.ellipse([cx + ddx - r, cy - r, cx + ddx + r, cy + r], fill=color)


def base_canvas(size):
    img = Image.new("RGB", size, BG)
    return img, ImageDraw.Draw(img)


def draw_cta_bar(draw, w, y, cta_font, pad=46):
    draw.text((pad, y), CTA_TEXT.upper(), font=cta_font, fill=ORANGE)
    arrow_x = pad + draw.textlength(CTA_TEXT.upper(), font=cta_font) + 18
    cy = y + cta_font.size * 0.4
    draw.line([(arrow_x, cy), (arrow_x + 28, cy)], fill=ORANGE, width=4)
    draw.polygon([(arrow_x + 22, cy - 8), (arrow_x + 22, cy + 8), (arrow_x + 34, cy)], fill=ORANGE)


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
    y = wrap_draw(d, sub, sub_font, W - 2 * pad, pad, y, ORANGE, line_spacing=1.3)

    icon_document_loss(d, W - 140, H - 200, scale=1.3)
    draw_cta_bar(d, W, H - 130, cta_font, pad)
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
    y = wrap_draw(d, sub, sub_font, W - 2 * pad, pad, y, ORANGE, line_spacing=1.35)

    icon_document_loss(d, W / 2, H / 2 + 120, scale=1.8)

    draw_cta_bar(d, W, bottom_safe - 110, cta_font, pad)
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
    y = wrap_draw(d, body, body_font, W - 2 * pad, pad, y, GRAY, line_spacing=1.35)

    icon_silent_chat(d, W - 160, H - 210, scale=1.3)
    draw_cta_bar(d, W, H - 130, cta_font, pad)
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
    y = wrap_draw(d, body, body_font, W - 2 * pad, pad, y, GRAY, line_spacing=1.4)

    icon_silent_chat(d, W / 2, H / 2 + 140, scale=1.9)

    draw_cta_bar(d, W, bottom_safe - 110, cta_font, pad)
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
        img = fn()
        path = os.path.join(out, name)
        img.save(path, "PNG")
        print("salvo:", path)
