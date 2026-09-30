import ebook_lib
from ebook_lib import Book
ebook_lib.CSS += """
.ln{border-bottom:1.5px solid #cdbf9f;height:46px}
.dark .ln{border-bottom:1.5px solid rgba(201,162,78,.45)}
.fill td{height:64px;border:1.5px solid #d8c9a6}
.dark .fill td{border:1.5px solid rgba(201,162,78,.4)}
.q{font-family:'Playfair Display';font-weight:700;font-size:27px;margin:18px 0 4px;color:#5a4412}
.dark .q{color:#E4C988}
.grid{display:grid;grid-template-columns:repeat(7,1fr);gap:10px;margin-top:10px}
.grid div{border:1.5px solid #C9A24E;border-radius:6px;height:92px;font-size:19px;padding:8px;color:#8a6d2c}
.mono{font-family:monospace;font-size:19px;background:#0b0b0b;color:#E4C988;padding:22px;border-radius:6px;white-space:pre-wrap;line-height:1.45}
"""
def lines(n): return '<div>'+''.join('<div class="ln"></div>' for _ in range(n))+'</div>'
def filltable(headers, n, widths=None):
    th=''.join(f'<th>{h}</th>' for h in headers)
    num = headers[0] in ('#','Dia')
    tr=''.join('<tr>'+''.join(f'<td>{i+1 if (num and j==0) else ""}</td>' for j,_ in enumerate(headers))+'</tr>' for i in range(n))
    return f'<table class="fill"><tr>{th}</tr>{tr}</table>'
OUT='/home/user/recria-clientes/agencia-recria/cursos/recria-ads/materiais/'
