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

NAVY = colors.HexColor('#0A0C0F')
ORANGE = colors.HexColor('#E09C3B')
LIGHTGRAY = colors.HexColor('#F4F4F4')
BORDER = colors.HexColor('#D9D9D9')
CH_COLOR = {
    'INSTAGRAM': colors.HexColor('#C2185B'),
    'LINKEDIN': colors.HexColor('#155DFD'),
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
                      textColor=NAVY, spaceBefore=10, spaceAfter=4))

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

def post_card(time, channel, tipo, ancoragem, formato, persona, headline, subheadline, cta, legenda, hashtags, origem=None):
    accent = CH_COLOR.get(channel, NAVY)
    meta = "%s  ·  %s  ·  %s" % (time, channel, tipo)
    body_flow = []
    if origem:
        body_flow.append(P("__Origem:__ " + origem, fontSize=8.3, textColor=colors.HexColor('#666666'), spaceAfter=3))
    if ancoragem:
        body_flow.append(P("__Ancoragem:__ " + ancoragem, fontSize=8.3, textColor=colors.HexColor('#666666'), spaceAfter=3))
    body_flow.append(P("__Formato:__ " + formato + "    __Persona:__ " + persona, fontSize=8.6, spaceAfter=5))
    if headline:
        body_flow.append(P("**HEADLINE:** " + headline, fontSize=10, leading=13.5, spaceAfter=4))
    if subheadline:
        body_flow.append(P("**SUBHEADLINE:** " + subheadline, fontSize=9.3, leading=12.5, spaceAfter=4))
    if cta:
        body_flow.append(P("**CTA:** " + cta, fontSize=9, textColor=ORANGE, spaceAfter=5))
    body_flow.append(P("**LEGENDA:** " + legenda, fontSize=9, leading=12.8, spaceAfter=5))
    body_flow.append(P("**HASHTAGS:** " + hashtags, fontSize=8.2, textColor=colors.HexColor('#666666')))

    inner = Table([[bf] for bf in body_flow], colWidths=[17.0*cm])
    inner.setStyle(TableStyle([
        ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1.5), ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))

    t = Table([
        [Paragraph(escape(meta), ParagraphStyle('metaw', fontName='Helvetica-Bold', fontSize=9.3, textColor=colors.white))],
        [inner],
    ], colWidths=[17.4*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), accent),
        ('TOPPADDING', (0,0), (0,0), 5), ('BOTTOMPADDING', (0,0), (0,0), 5),
        ('LEFTPADDING', (0,0), (0,0), 10), ('RIGHTPADDING', (0,0), (0,0), 10),
        ('BACKGROUND', (0,1), (0,1), colors.white),
        ('TOPPADDING', (0,1), (0,1), 8), ('BOTTOMPADDING', (0,1), (0,1), 8),
        ('LEFTPADDING', (0,1), (0,1), 10), ('RIGHTPADDING', (0,1), (0,1), 10),
        ('BOX', (0,0), (-1,-1), 1, BORDER),
        ('LINEBELOW', (0,0), (0,0), 1, BORDER),
    ]))
    return t

def build_calendar(content_file, output_pdf):
    story = []

    def add_month(title):
        story.append(month_title(title))

    def add_week(title):
        story.append(Spacer(1, 0.15*cm))
        story.append(week_bar(title))
        story.append(Spacer(1, 0.1*cm))

    def add_day(title, posts):
        story.append(day_bar(title))
        story.append(Spacer(1, 0.12*cm))
        for p in posts:
            story.append(post_card(**p))
            story.append(Spacer(1, 0.18*cm))
        story.append(Spacer(1, 0.05*cm))

    namespace = dict(add_month=add_month, add_week=add_week, add_day=add_day)
    exec(open(content_file, encoding='utf-8').read(), namespace)

    doc = SimpleDocTemplate(output_pdf, pagesize=A4,
                             topMargin=1.3*cm, bottomMargin=1.3*cm, leftMargin=1.3*cm, rightMargin=1.3*cm)
    doc.build(story)
    print("PDF gerado:", output_pdf)
