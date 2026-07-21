# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                 KeepTogether, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from xml.sax.saxutils import escape
import re

NAVY = colors.HexColor('#5A1042')
ORANGE = colors.HexColor('#9C1256')
LIGHTGRAY = colors.HexColor('#F4F4F4')
CARDGRAY = colors.HexColor('#FBEEF7')
BORDER = colors.HexColor('#E0B8D6')
CH_COLOR = {
    'INSTAGRAM': colors.HexColor('#9C1256'),
    'WHATSAPP': colors.HexColor('#1F8A4C'),
}

styles = getSampleStyleSheet()

def P(text, **kw):
    base = dict(parent=styles['Normal'], fontName='Helvetica', fontSize=9.3, leading=12.6)
    base.update(kw)
    st = ParagraphStyle('p%d' % len(styles.byName), **base)
    return Paragraph(bolditalic(text), st)

def bolditalic(text):
    text = escape(text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.*?)__', r'<i>\1</i>', text)
    return text

def month_title(text):
    return Paragraph(escape(text), ParagraphStyle('month', fontName='Helvetica-Bold', fontSize=20,
                      textColor=NAVY, spaceBefore=6, spaceAfter=16))

def week_bar(text):
    t = Table([[Paragraph(escape(text), ParagraphStyle('wk', fontName='Helvetica-Bold', fontSize=11.5,
               textColor=colors.white))]], colWidths=[17.4*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), ORANGE),
        ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    return t

def day_bar(text):
    t = Table([[Paragraph(escape(text), ParagraphStyle('day', fontName='Helvetica-Bold', fontSize=10.5,
               textColor=colors.white))]], colWidths=[17.4*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    return t

def _card_box(label, flows, label_color=ORANGE):
    """Mini bordered box used for each carousel card (capa, meio, final)."""
    rows = [[P("**%s**" % label, fontSize=8.3, textColor=label_color, spaceAfter=3)]]
    for f in flows:
        rows.append([f])
    t = Table(rows, colWidths=[16.6*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARDGRAY),
        ('BOX', (0,0), (-1,-1), 0.8, BORDER),
        ('LEFTPADDING', (0,0), (-1,-1), 9), ('RIGHTPADDING', (0,0), (-1,-1), 9),
        ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    return t

def capa_card(label, headline, subheadline, cta):
    flows = [P("**HEADLINE:** " + headline, fontSize=9.6, leading=13, spaceAfter=3)]
    if subheadline:
        flows.append(P("**SUBHEADLINE:** " + subheadline, fontSize=9, leading=12, spaceAfter=3))
    if cta:
        flows.append(P("**CTA:** " + cta, fontSize=8.8, textColor=ORANGE))
    return _card_box(label, flows)

def mid_card(num, titulo, corpo):
    flows = []
    if titulo:
        flows.append(P("**" + titulo + "**", fontSize=9.3, leading=12.5, spaceAfter=2))
    flows.append(P(corpo, fontSize=9, leading=12.3))
    return _card_box("CARD %s" % num, flows, label_color=colors.HexColor('#666666'))

def meta_bar(time, channel, tipo, accent):
    meta = "%s  ·  %s  ·  %s" % (time, channel, tipo)
    t = Table([[Paragraph(escape(meta), ParagraphStyle('metaw', fontName='Helvetica-Bold', fontSize=9.3,
               textColor=colors.white))]], colWidths=[17.4*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), accent),
        ('TOPPADDING', (0,0), (-1,-1), 5), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 1, BORDER),
    ]))
    return t

def post_card(time, channel, tipo, formato, headline, subheadline, cta,
              legenda=None, ancoragem=None, persona=None, hashtags=None, origem=None,
              cards=None, card_final=None, observacao=None, cenario=None,
              label_legenda="LEGENDA:", acoes=None):
    """Returns a LIST of flowables for one post (not a single monolithic table), so
    long carrosséis can break across pages instead of overflowing a single table cell."""
    accent = CH_COLOR.get(channel, NAVY)
    flows = [meta_bar(time, channel, tipo, accent)]

    indent = dict(leftIndent=10, rightIndent=10)
    body_flow = []
    if origem:
        body_flow.append(P("__Origem:__ " + origem, fontSize=8.3, textColor=colors.HexColor('#666666'), spaceAfter=3, **indent))
    if ancoragem:
        body_flow.append(P("__Ancoragem:__ " + ancoragem, fontSize=8.3, textColor=colors.HexColor('#666666'), spaceAfter=3, **indent))
    if cenario:
        body_flow.append(P("__Cenário sugerido:__ " + cenario, fontSize=8.3, textColor=colors.HexColor('#666666'), spaceAfter=3, **indent))
    formato_persona = "__Formato:__ " + formato + ("    __Persona:__ " + persona if persona else "")
    body_flow.append(P(formato_persona, fontSize=8.6, spaceAfter=6, **indent))

    if cards:
        # Carrossel: capa, cards do meio, card final, cada um em bloco visual separado.
        body_flow.append(capa_card("CARD 1 — CAPA", headline, subheadline, cta))
        body_flow.append(Spacer(1, 0.12*cm))
        for i, c in enumerate(cards, start=2):
            body_flow.append(mid_card(i, c['titulo'], c['corpo']))
            body_flow.append(Spacer(1, 0.12*cm))
        if card_final:
            body_flow.append(capa_card("CARD FINAL", card_final.get('headline'),
                                        card_final.get('subheadline'), card_final.get('cta')))
            body_flow.append(Spacer(1, 0.12*cm))
        body_flow.append(P("**LEGENDA DO POST:** " + legenda, fontSize=9, leading=12.8, spaceAfter=5, **indent))
    else:
        if headline:
            body_flow.append(P("**HEADLINE:** " + headline, fontSize=10, leading=13.5, spaceAfter=4, **indent))
        if subheadline:
            body_flow.append(P("**SUBHEADLINE:** " + subheadline, fontSize=9.3, leading=12.5, spaceAfter=4, **indent))
        if cta:
            body_flow.append(P("**CTA:** " + cta, fontSize=9, textColor=ORANGE, spaceAfter=5, **indent))
        if acoes:
            for i, a in enumerate(acoes, start=1):
                label = "AÇÃO %d — %s" % (i, a['label'])
                body_flow.append(_card_box(label, [P(a['texto'], fontSize=9, leading=12.3)], label_color=colors.HexColor('#666666')))
                body_flow.append(Spacer(1, 0.1*cm))
        elif legenda:
            body_flow.append(P("**" + label_legenda + "** " + legenda, fontSize=9, leading=12.8, spaceAfter=5, **indent))

    if hashtags:
        body_flow.append(P("**HASHTAGS:** " + hashtags, fontSize=8.2, textColor=colors.HexColor('#666666'), spaceAfter=4, **indent))
    if observacao:
        body_flow.append(P("__Observação:__ " + observacao, fontSize=8.3, textColor=ORANGE, **indent))

    flows.extend(body_flow)
    return flows

def build_calendar(content_file, output_pdf):
    story = []

    def add_month(title):
        story.append(month_title(title))

    def add_week(title):
        story.append(Spacer(1, 0.3*cm))
        story.append(week_bar(title))
        story.append(Spacer(1, 0.12*cm))

    def add_day(title, posts):
        story.append(day_bar(title))
        story.append(Spacer(1, 0.12*cm))
        for p in posts:
            story.extend(post_card(**p))
            story.append(Spacer(1, 0.22*cm))
        story.append(Spacer(1, 0.05*cm))

    namespace = dict(add_month=add_month, add_week=add_week, add_day=add_day)
    exec(open(content_file, encoding='utf-8').read(), namespace)

    doc = SimpleDocTemplate(output_pdf, pagesize=A4,
                             topMargin=1.3*cm, bottomMargin=1.3*cm, leftMargin=1.3*cm, rightMargin=1.3*cm)
    doc.build(story)
    print("PDF gerado:", output_pdf)
