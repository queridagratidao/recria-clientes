"""Gera calendario-2026-11.md e o feed simulado (cliente e interno) a partir de dados.py.
Uso: python3 gerar_feed.py <pasta_artes_nov> <pasta_posts_outubro> <pasta_saida>
"""
import sys, os, json, base64, io, datetime, html
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from dados import ITENS, STORIES, PERFIL, WHATSAPP_AGENCIA

ART, OUTUBRO, OUT = sys.argv[1:4]
os.makedirs(OUT, exist_ok=True)
DIAS = {'2026-11-04': '04/11'}

def b64(path, w):
    im = Image.open(path).convert('RGB'); im.thumbnail((w, w * 2))
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=80, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()

def br(d): return datetime.date.fromisoformat(d).strftime('%d/%m')

# ---------- calendario .md ----------
md = ['# Calendário editorial · Novembro 2026 · Refúgio dos 4 Elementos', '',
      'Ritmo: 2 posts por semana (quarta e sexta). 1ª semana só sexta (quarta 04/11 já agendada). 1 carrossel no mês (capa com foto, demais cards só texto). Fotos novas do ensaio em todas as capas.', '',
      '| Data | ID | Tipo | Tema | Objetivo | CTA / automação | Status |', '|---|---|---|---|---|---|---|']
for it in ITENS:
    md.append(f"| {it['dia'][:3]} {br(it['data'])} | {it['id']} | {it['tipo']} | {it['tema']} | {it['objetivo']} | {it['automacao']} | {it['status']} |")
md.append('')
for it in ITENS:
    md += [f"## {br(it['data'])} · {it['dia']} · {it['tema']}", f"**ID:** {it['id']} · **Tipo:** {it['tipo']} · **Status:** {it['status']}",
           f"**Artes:** {', '.join(it['imagens'])}"]
    if it.get('foto'): md.append(f"**Foto:** {it['foto']}")
    md += ['', '**Legenda:**', '', it['legenda'], '', f"**Automação:** {it['automacao']}", f"**Nota interna:** {it['nota']}", '']
md += ['## Stories sugeridos', '']
for s in STORIES:
    md.append(f"- **{s['id']} · {s['titulo']}:** " + ' → '.join(s['telas']) + f" ({s['nota']})")
md += ['', '## Pendências', '', '- Tema da Louvação de 28/11: será revelado no decorrer do mês (story de revelação).', '- Confirmar qual post está agendado para 04/11.',
       '- Palavra CONSTELAÇÃO na automação (ou trocar por REFÚGIO no post de 20/11).', '- Validar com Jean, Daniela e Joelson os textos de apresentação.',
       '- Validar com Daniela e Joelson o texto da Terapia Xamânica (27/11) e se ela também é feita online.']
open(os.path.join(OUT, 'calendario-2026-11.md'), 'w').write('\n'.join(md) + '\n')

# ---------- feed simulado ----------
itens = []
for it in ITENS:
    d = dict(it); d['dataBr'] = br(it['data'])
    d['src'] = [b64(os.path.join(ART, f), 900) for f in it['imagens']]
    d['thumb'] = b64(os.path.join(ART, it['imagens'][0]), 360)
    itens.append(d)
antigos = []
for f in sorted(os.listdir(OUTUBRO), reverse=True):
    if f.startswith('post0') and f.endswith('.jpg') and 'mito-verdade' not in f:
        antigos.append({'thumb': b64(os.path.join(OUTUBRO, f), 360), 'dataBr': f.split('_')[1].replace('-', '/')})

TEMPLATE = open(os.path.join(os.path.dirname(__file__), 'feed_template.html')).read()
for versao in ('cliente', 'interno'):
    dados = {'versao': versao, 'whats': WHATSAPP_AGENCIA, 'perfil': PERFIL,
             'itens': [{k: v for k, v in i.items() if versao == 'interno' or k not in ('nota', 'objetivo')} for i in itens],
             'antigos': antigos,
             'stories': [{k: v for k, v in s.items() if versao == 'interno' or k != 'nota'} for s in STORIES]}
    page = TEMPLATE.replace('/*__DADOS__*/', 'const DADOS = ' + json.dumps(dados, ensure_ascii=False) + ';')
    page = page.replace('__VERSAO__', 'Versão interna' if versao == 'interno' else 'Para aprovação')
    open(os.path.join(OUT, f'feed-2026-11-{versao}.html'), 'w').write(page)
print('ok')
