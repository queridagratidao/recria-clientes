# -*- coding: utf-8 -*-
"""Gera os 4 criativos estáticos (2 conceitos x 2 formatos) pro anúncio
Eleva - Multiplicar Vendas para Condomínios, com Pillow, controle exato
de cor de marca (#0A0C0F / #E09C3B) e tipografia Sora."""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = r"C:\Users\amand\AppData\Local\Temp\claude\C--Users-amand-OneDrive-Documentos-Agencia-de-IA\3fe07fba-9f71-405e-8476-7a4a9a1a0aab\scratchpad\fonts\Sora-ExtraBold.ttf"
LOGO_PATH = os.path.join(BASE, "logo-eleva-branco.png")

BG = (10, 12, 15)       # #0A0C0F
ORANGE = (224, 156, 59)  # #E09C3B
WHITE = (245, 245, 245)
GRAY = (170, 173, 178)
NAVY = (10, 12, 15)

CTA_TEXT = "Toque no botão para saber mais"
PUSH_LINE = "Aprenda de uma vez por todas a multiplicar vendas para condomínio"
TAG_TEXT = "FORNECEDOR E PRESTADOR DE SERVIÇOS"

_LOGO_SRC = Image.open(LOGO_PATH).convert("RGBA")


def font(size, variation="ExtraBold"):
    f = ImageFont.truetype(FONT_PATH, size)
    try:
        f.set_variation_by_name(variation)
    except Exception:
        pass
    return f


def compute_lines(draw, text, fnt, max_width):
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
    return lines


def line_height(fnt, line_spacing=1.25):
    bbox = fnt.getbbox("Ay")
    return (bbox[3] - bbox[1]) * line_spacing


def wrap_draw(draw, text, fnt, max_width, x, y, fill, line_spacing=1.25, align="left"):
    """Quebra texto em linhas que cabem em max_width e desenha, retorna y final."""
    lines = compute_lines(draw, text, fnt, max_width)
    line_h = line_height(fnt, line_spacing)
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


def draw_tag(draw, pad, y, tag_font):
    """Tag/etiqueta de segmento (ex: FORNECEDOR E PRESTADOR DE SERVIÇOS), fundo laranja, texto navy."""
    text = TAG_TEXT
    text_w = draw.textlength(text, font=tag_font)
    bbox = tag_font.getbbox("Ay")
    text_h = bbox[3] - bbox[1]
    pad_x, pad_y = 18, 10
    box = [pad, y, pad + text_w + pad_x * 2, y + text_h + pad_y * 2]
    draw.rounded_rectangle(box, radius=6, fill=ORANGE)
    draw.text((pad + pad_x, y + pad_y - bbox[1]), text, font=tag_font, fill=NAVY)
    return box[3]


def bottom_block(img, draw, pad, content_width, push_font, cta_font, logo_width, bottom_floor, floor_gap=60):
    """Desenha (de cima pra baixo, ancorado pela base): linha de reforço (push), CTA e logo,
    sempre encostados na base disponível (bottom_floor), respeitando floor_gap."""
    push_lines = compute_lines(draw, PUSH_LINE, push_font, content_width)
    push_line_h = line_height(push_font, 1.3)
    push_h = push_line_h * len(push_lines)

    cta_bbox = cta_font.getbbox("Ay")
    cta_h = cta_bbox[3] - cta_bbox[1]

    ratio = _LOGO_SRC.height / _LOGO_SRC.width
    logo_h = int(logo_width * ratio)

    gap_push_cta = 22
    gap_cta_logo = 30

    total_h = push_h + gap_push_cta + cta_h + gap_cta_logo + logo_h
    block_bottom = bottom_floor - floor_gap
    y = block_bottom - total_h

    for line in push_lines:
        draw.text((pad, y), line, font=push_font, fill=WHITE)
        y += push_line_h
    y += gap_push_cta

    draw.text((pad, y), CTA_TEXT.upper(), font=cta_font, fill=ORANGE)
    y += cta_h + gap_cta_logo

    logo = _LOGO_SRC.resize((logo_width, logo_h), Image.LANCZOS)
    img.alpha_composite(logo, (pad, int(y)))


# ---------- Criativo 1: Objeção Invertida ----------

def objecao_invertida_feed():
    W = H = 1080
    img, d = base_canvas((W, H))
    pad = 80

    title_font = font(56)
    sub_font = font(32)
    push_font = font(30)
    cta_font = font(27)

    y = 110
    quote = "“Fornecedor bom não precisa saber vender. Precisa entregar bem.”"
    y = wrap_draw(d, quote, title_font, W - 2 * pad, pad, y, WHITE, line_spacing=1.2)

    y += 40
    sub = "Se você acredita nisso, está perdendo contratos todo mês sem perceber."
    wrap_draw(d, sub, sub_font, W - 2 * pad, pad, y, ORANGE, line_spacing=1.3)

    bottom_block(img, d, pad, W - 2 * pad, push_font, cta_font, logo_width=300, bottom_floor=H)
    return img


def objecao_invertida_story():
    W, H = 1080, 1920
    img, d = base_canvas((W, H))
    pad = 90

    title_font = font(60)
    sub_font = font(34)
    push_font = font(32)
    cta_font = font(29)

    top_safe = int(H * 0.14)
    bottom_safe = H - int(H * 0.14)

    y = top_safe + 80
    quote = "“Fornecedor bom não precisa saber vender. Precisa entregar bem.”"
    y = wrap_draw(d, quote, title_font, W - 2 * pad, pad, y, WHITE, line_spacing=1.22)

    y += 60
    sub = "Se você acredita nisso, está perdendo contratos todo mês sem perceber."
    wrap_draw(d, sub, sub_font, W - 2 * pad, pad, y, ORANGE, line_spacing=1.32)

    bottom_block(img, d, pad, W - 2 * pad, push_font, cta_font, logo_width=320, bottom_floor=bottom_safe, floor_gap=40)
    return img


# ---------- Criativo 2: Perda Silenciosa ----------

def perda_silenciosa_feed():
    W = H = 1080
    img, d = base_canvas((W, H))
    pad = 80

    tag_font = font(20)
    title_font = font(46)
    body_font = font(28, variation="Regular")
    push_font = font(30)
    cta_font = font(27)

    y = 90
    y = draw_tag(d, pad, y, tag_font)

    y += 30
    title = "Quantos contratos com condomínio você perdeu nos últimos 6 meses sem nem saber por quê?"
    y = wrap_draw(d, title, title_font, W - 2 * pad, pad, y, WHITE, line_spacing=1.22)

    y += 36
    body = ("O síndico e gestor não te ligou de volta. A reunião não evoluiu. "
            "Você enviou a proposta e sem nenhum retorno ou retorno negativo.")
    wrap_draw(d, body, body_font, W - 2 * pad, pad, y, GRAY, line_spacing=1.32)

    bottom_block(img, d, pad, W - 2 * pad, push_font, cta_font, logo_width=300, bottom_floor=H)
    return img


def perda_silenciosa_story():
    W, H = 1080, 1920
    img, d = base_canvas((W, H))
    pad = 90

    tag_font = font(22)
    title_font = font(50)
    body_font = font(30, variation="Regular")
    push_font = font(32)
    cta_font = font(29)

    top_safe = int(H * 0.14)
    bottom_safe = H - int(H * 0.14)

    y = top_safe + 70
    y = draw_tag(d, pad, y, tag_font)

    y += 36
    title = "Quantos contratos com condomínio você perdeu nos últimos 6 meses sem nem saber por quê?"
    y = wrap_draw(d, title, title_font, W - 2 * pad, pad, y, WHITE, line_spacing=1.25)

    y += 44
    body = ("O síndico e gestor não te ligou de volta. A reunião não evoluiu. "
            "Você enviou a proposta e sem nenhum retorno ou retorno negativo.")
    wrap_draw(d, body, body_font, W - 2 * pad, pad, y, GRAY, line_spacing=1.35)

    bottom_block(img, d, pad, W - 2 * pad, push_font, cta_font, logo_width=320, bottom_floor=bottom_safe, floor_gap=40)
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
