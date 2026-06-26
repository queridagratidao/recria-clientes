# -*- coding: utf-8 -*-
import sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY = RGBColor(0x0A, 0x0C, 0x0F)
ORANGE = RGBColor(0xE0, 0x9C, 0x3B)
GRAY = RGBColor(0x66, 0x66, 0x66)
CARDGRAY = "F7F4EE"
CH_COLOR = {'INSTAGRAM': '7A1F40', 'LINKEDIN': '154468'}
CH_RGB = {'INSTAGRAM': RGBColor(0xC2, 0x18, 0x5B), 'LINKEDIN': RGBColor(0x15, 0x5D, 0xFD)}

doc = Document()
section = doc.sections[0]
section.page_width = Cm(21)
section.page_height = Cm(29.7)
for m in ('top_margin', 'bottom_margin', 'left_margin', 'right_margin'):
    setattr(section, m, Cm(1.5))

style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(10)

def shade_cell(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:fill'), hexcolor)
    tcPr.append(shd)

def add_run(p, text, bold=False, color=None, size=10, italic=False):
    r = p.add_run(text)
    r.bold = bold
    r.italic = italic
    r.font.size = Pt(size)
    if color:
        r.font.color.rgb = color
    return r

def month_title(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(14)
    add_run(p, text, bold=True, color=NAVY, size=20)

def week_bar(text):
    t = doc.add_table(rows=1, cols=1)
    t.autofit = False
    t.columns[0].width = Cm(18)
    cell = t.rows[0].cells[0]
    cell.width = Cm(18)
    shade_cell(cell, 'E09C3B')
    p = cell.paragraphs[0]
    add_run(p, text, bold=True, color=RGBColor(255, 255, 255), size=11.5)
    sp_after = doc.add_paragraph()
    sp_after.paragraph_format.space_after = Pt(4)

def day_bar(text):
    t = doc.add_table(rows=1, cols=1)
    t.autofit = False
    t.columns[0].width = Cm(18)
    cell = t.rows[0].cells[0]
    cell.width = Cm(18)
    shade_cell(cell, '0A0C0F')
    p = cell.paragraphs[0]
    add_run(p, text, bold=True, color=RGBColor(255, 255, 255), size=10.5)
    sp_after = doc.add_paragraph()
    sp_after.paragraph_format.space_after = Pt(4)

def meta_bar(time, channel, tipo):
    hexcolor = CH_COLOR.get(channel, '0A0C0F')
    t = doc.add_table(rows=1, cols=1)
    t.autofit = False
    t.columns[0].width = Cm(18)
    cell = t.rows[0].cells[0]
    cell.width = Cm(18)
    shade_cell(cell, hexcolor)
    p = cell.paragraphs[0]
    add_run(p, "%s   ·   %s   ·   %s" % (time, channel, tipo), bold=True, color=RGBColor(255, 255, 255), size=10)

def field_p(label, text, color=None, size=10, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    add_run(p, label + " ", bold=True, size=size, color=color, italic=italic)
    add_run(p, text, size=size, color=color, italic=italic)

def card_box(label, lines, label_color=ORANGE):
    """lines: list of (bold_prefix_or_None, text)"""
    t = doc.add_table(rows=1, cols=1)
    t.autofit = False
    t.columns[0].width = Cm(17.4)
    cell = t.rows[0].cells[0]
    cell.width = Cm(17.4)
    shade_cell(cell, CARDGRAY)
    p0 = cell.paragraphs[0]
    add_run(p0, label, bold=True, color=label_color, size=9)
    for prefix, text in lines:
        p = cell.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        if prefix:
            add_run(p, prefix + " ", bold=True, size=9.5)
        add_run(p, text, size=9.5)
    sp = doc.add_paragraph()
    sp.paragraph_format.space_after = Pt(2)

def capa_lines(headline, subheadline, cta):
    lines = [("HEADLINE:", headline)]
    if subheadline:
        lines.append(("SUBHEADLINE:", subheadline))
    if cta:
        lines.append(("CTA:", cta))
    return lines

def post_card(time, channel, tipo, ancoragem, formato, persona, headline, subheadline, cta,
              legenda, hashtags, origem=None, cards=None, card_final=None):
    meta_bar(time, channel, tipo)
    if origem:
        field_p("Origem:", origem, color=GRAY, size=8.5, italic=True)
    if ancoragem:
        field_p("Ancoragem:", ancoragem, color=GRAY, size=8.5, italic=True)
    field_p("Formato:", formato + "     Persona: " + persona, size=9)

    if cards:
        card_box("CARD 1 — CAPA", capa_lines(headline, subheadline, cta))
        for i, c in enumerate(cards, start=2):
            card_box("CARD %d" % i, [(c['titulo'], ''), (None, c['corpo'])], label_color=GRAY)
        if card_final:
            card_box("CARD FINAL", capa_lines(card_final.get('headline'), card_final.get('subheadline'), card_final.get('cta')))
        field_p("LEGENDA DO POST:", legenda, size=9.5)
    else:
        if headline:
            field_p("HEADLINE:", headline, size=10.5)
        if subheadline:
            field_p("SUBHEADLINE:", subheadline, size=9.5)
        if cta:
            field_p("CTA:", cta, color=ORANGE, size=9.5)
        field_p("LEGENDA:", legenda, size=9.5)

    field_p("HASHTAGS:", hashtags, color=GRAY, size=8.5)
    sp = doc.add_paragraph()
    sp.paragraph_format.space_after = Pt(10)

def add_month(title):
    month_title(title)

def add_week(title):
    week_bar(title)

def add_day(title, posts):
    day_bar(title)
    for p in posts:
        post_card(**p)

content_file = sys.argv[1]
output_docx = sys.argv[2]
namespace = dict(add_month=add_month, add_week=add_week, add_day=add_day)
exec(open(content_file, encoding='utf-8').read(), namespace)

doc.save(output_docx)
print("DOCX gerado:", output_docx)
