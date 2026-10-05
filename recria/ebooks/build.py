#!/usr/bin/env python3
"""Gera o PDF de um e-book Recria: capa (sem margem) + miolo + página de upsell (sem margem).
Uso (dentro de recria/ebooks): python3 build.py calendario-com-ia ebook-calendario-com-ia.pdf
Requer: playwright (node) com chromium, e pdfunite (poppler)."""
import re, subprocess, sys, pathlib
d = pathlib.Path(__file__).parent / sys.argv[1]
out = d / sys.argv[2]
html = (d / "ebook.html").read_text(encoding="utf-8")
def pop(cls):
    ms = re.findall(r'<section class="%s">.*?</section>' % cls, html, re.S)
    return "\n".join(ms) if ms else None
cover, upsell = pop("cover"), pop("upsell")
body = html
for cls in ("cover", "upsell"):
    for blk in re.findall(r'<section class="%s">.*?</section>' % cls, html, re.S):
        body = body.replace(blk, "")
head = html.split("<body>")[0]
full = ('<style>@page{margin:0;background:#0b0b0b;@bottom-center{content:none}}'
        'html,body{background:#0b0b0b}'
        'section{margin:0!important;height:209.5mm!important;overflow:hidden;break-after:page!important;break-before:avoid!important}section:last-child{break-after:auto!important}'
        '.upsell{padding:12mm 14mm!important}.cover{padding:16mm 14mm!important}</style>')
js = pathlib.Path(__file__).parent / "_base" / "pdf.js"
pdfs = []
for name, content in (("cover", cover), ("body", body), ("upsell", upsell)):
    if not content: continue
    doc = content if name == "body" else head.replace("</head>", full + "</head>") + "<body>" + content + "</body></html>"
    f = d / f"_{name}.html"; f.write_text(doc, encoding="utf-8")
    p = d / f"_{name}.pdf"
    subprocess.run(["node", str(js), str(f), str(p)], check=True)
    pdfs.append(p); f.unlink()
subprocess.run(["pdfunite", *map(str, pdfs), str(out)], check=True)
for p in pdfs: p.unlink()
print("ok", out)
