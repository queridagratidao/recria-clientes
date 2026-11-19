"""Gera artes, Reels, calendario .md e feed simulado de novembro v2. Uso: python3 gerar.py <saida>"""
import sys, os, subprocess, json, base64, io, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
import visual as V
from dados import ITENS, STORIES, DEZEMBRO, PERFIL, WHATSAPP_AGENCIA

OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
TMP = os.path.join(OUT, '_tmp'); os.makedirs(TMP, exist_ok=True)
br = lambda d: datetime.date.fromisoformat(d).strftime('%d/%m')

def slug(it): return f"{it['data'][8:10]}-11"

for it in ITENS:
    a = it['arte']; base = slug(it); it['imagens'] = []
    if a[0] == 'foto':
        _, foto, tit, sub, kick, kw = a
        f = f'{base}_{it["id"][-1].lower()}.jpg'
        V.post_foto(os.path.join(OUT, f), foto, tit, sub, kicker=kick, **kw); it['imagens'].append(f)
        if it.get('reel'):
            fundo = os.path.join(TMP, base + '_fundo.jpg'); texto = os.path.join(TMP, base + '_texto.png')
            V.post_foto(fundo, foto, tit, sub, kicker=kick, w=1080, h=1920, camada='fundo', **kw)
            V.post_foto(texto, foto, tit, sub, kicker=kick, w=1080, h=1920, camada='texto', botao=None, **kw)
            mp4 = f'{base}_reel.mp4'
            # zoom lento de 8 s no fundo + texto entrando em fade aos 0,6 s
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', fundo, '-loop', '1', '-i', texto,
                '-filter_complex',
                "[0:v]scale=2160:3840,zoompan=z='1+0.0009*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=240:s=1080x1920:fps=30[bg];"
                "[1:v]format=rgba,fade=in:st=0.6:d=0.9:alpha=1[tx];[bg][tx]overlay=0:0:shortest=1,format=yuv420p[v]",
                '-map', '[v]', '-t', '8', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-movflags', '+faststart',
                os.path.join(OUT, mp4)], check=True)
            it['video'] = mp4
    else:
        for i, c in enumerate(a[1]):
            f = f'{base}_carrossel-{i + 1}.jpg'
            if c[0] == 'capa':
                _, foto, tit, sub, kick, kw = c
                V.post_foto(os.path.join(OUT, f), foto, tit, sub, kicker=kick, botao='arrasta >', **kw)
            else:
                _, tg, tit, corpo, cor, ref = c
                V.card_texto(os.path.join(OUT, f), tg, tit, corpo, cor, ref=ref, n=i, total=len(a[1]))
            it['imagens'].append(f)
    print('ok', it['id'], it['imagens'], it.get('video', ''))

# ---------- calendario .md ----------
md = ['# Calendário Refúgio dos 4 Elementos · Novembro 2026 (v2, 1 post por dia de 19 a 30/11)', '',
      'Recuperação do mês: 1 post por dia até 30/11. Visual novo (foto inteira + título por cima, cards de texto limpos), 2 Reels e 1 carrossel (ciência).', '',
      '| Data | Formato | Tema | CTA |', '|---|---|---|---|']
for it in ITENS: md.append(f"| {it['dia'][:3]} {br(it['data'])} | {it['tipo']} | {it['tema']} | {it['cta']} |")
md.append('')
for it in ITENS:
    md += [f"## {br(it['data'])} · {it['dia']} · {it['tema']}", f"**Formato:** {it['tipo']} · **Arquivos:** {', '.join(it['imagens'] + ([it['video']] if it.get('video') else []))}",
           f"**Foto:** {it['foto']}", f"**Objetivo:** {it['objetivo']}", '', '**Legenda:**', '', it['legenda'], '', f"**Nota:** {it['nota']}", '']
md += ['## Stories', ''] + [f"- **{s['titulo']}:** " + ' → '.join(s['telas']) + f" ({s['nota']})" for s in STORIES]
md += ['', '## Pauta de dezembro (para aprovar antes das artes)', '', '| Data | Formato | Tema | Por quê |', '|---|---|---|---|']
md += [f'| {d} {s} | {f} | {t} | {p} |' for d, s, f, t, p in DEZEMBRO]
md += ['', '## Fontes do carrossel de ciência', '',
       '- Ministério da Saúde. Portaria nº 849, de 27/03/2017 (inclui Reiki, Meditação, Yoga e mais 11 práticas na PNPIC).',
       '- CONASS, 12/03/2018: Ministério inclui 10 novas práticas (Aromaterapia, Constelação Familiar, Cromoterapia...), total de 29.',
       '- Goyal M. et al. Meditation programs for psychological stress and well-being. JAMA Internal Medicine, 2014 (47 estudos, 3.515 participantes).',
       '- Guo X. et al. Therapeutic effects of Reiki on interventions for anxiety: a meta-analysis. BMC Palliative Care, 2024 (13 estudos, 824 participantes).']
open(os.path.join(OUT, 'calendario-2026-11-v2.md'), 'w').write('\n'.join(md) + '\n')

# ---------- feed simulado ----------
def b64(path, w):
    im = Image.open(path).convert('RGB'); im.thumbnail((w, w * 2)); buf = io.BytesIO()
    im.save(buf, 'JPEG', quality=80, optimize=True); return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()

def b64video(path):
    small = os.path.join(TMP, 'prev_' + os.path.basename(path))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', path, '-vf', 'scale=540:960', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '28', '-an', small], check=True)
    return 'data:video/mp4;base64,' + base64.b64encode(open(small, 'rb').read()).decode()

itens = []
for it in ITENS:
    d = {k: it[k] for k in ('id', 'data', 'dia', 'tipo', 'tema', 'objetivo', 'legenda', 'nota', 'foto')}
    d.update(dataBr=br(it['data']), status='rascunho', automacao=it['cta'],
             src=[b64(os.path.join(OUT, f), 900) for f in it['imagens']], thumb=b64(os.path.join(OUT, it['imagens'][0]), 360))
    if it.get('video'): d['video'] = b64video(os.path.join(OUT, it['video']))
    itens.append(d)
anteriores = [('04/11', '/home/claude/nov/out/post01_04-11_mito-verdade-constelacao.jpg')]
OUTUBRO = '/home/claude/w/refugio-dos-4-elementos/social-media-outubro-2026'
for f in sorted(os.listdir(OUTUBRO), reverse=True):
    if f.startswith('post0') and f.endswith('.jpg') and 'mito-verdade' not in f:
        anteriores.append((f.split('_')[1].replace('-', '/'), os.path.join(OUTUBRO, f)))
antigos = [{'thumb': b64(p, 360), 'dataBr': d} for d, p in anteriores]

TPL = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'feed_template.html')).read()
for versao in ('cliente', 'interno'):
    dados = {'versao': versao, 'whats': WHATSAPP_AGENCIA, 'perfil': PERFIL, 'antigos': antigos,
             'itens': [{k: v for k, v in i.items() if versao == 'interno' or k not in ('nota', 'objetivo', 'foto')} for i in itens],
             'stories': [{k: v for k, v in s.items() if versao == 'interno' or k != 'nota'} for s in STORIES],
             'dezembro': [dict(zip(('data', 'dia', 'formato', 'tema', 'porque'), r)) for r in DEZEMBRO]}
    page = TPL.replace('/*__DADOS__*/', 'const DADOS = ' + json.dumps(dados, ensure_ascii=False) + ';')
    page = page.replace('__VERSAO__', 'Versão interna' if versao == 'interno' else 'Para aprovação')
    open(os.path.join(OUT, f'feed-2026-11-v2-{versao}.html'), 'w').write(page)
print('feed ok')
