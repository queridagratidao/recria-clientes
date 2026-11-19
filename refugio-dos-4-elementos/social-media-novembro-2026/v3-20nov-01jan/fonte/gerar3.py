"""Calendario 20/11 a 01/01: artes, Reels, .md, pasta do artifact (pub/) e feed interno standalone.
Uso: python3 gerar3.py <saida>"""
import sys, os, subprocess, json, base64, io, datetime, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
import visual as V
from dados3 import ITENS, STORIES, FALTA, PERFIL, WHATSAPP_AGENCIA

OUT = sys.argv[1]; ART = os.path.join(OUT, 'artes'); PUB = os.path.join(OUT, 'pub'); TMP = os.path.join(OUT, '_tmp')
for p in (ART, PUB + '/img', PUB + '/video', TMP): os.makedirs(p, exist_ok=True)
br = lambda d: datetime.date.fromisoformat(d).strftime('%d/%m')
DIAS = {'Segunda': 'seg', 'Terça': 'ter', 'Quarta': 'qua', 'Quinta': 'qui', 'Sexta': 'sex', 'Sábado': 'sab', 'Domingo': 'dom'}

def reel(base, foto, tit, sub, kick, kw):
    fundo = os.path.join(TMP, base + '_fundo.jpg'); texto = os.path.join(TMP, base + '_texto.png')
    V.post_foto(fundo, foto, tit, sub, kicker=kick, w=1080, h=1920, camada='fundo', **kw)
    V.post_foto(texto, foto, tit, sub, kicker=kick, w=1080, h=1920, camada='texto', botao=None, **kw)
    mp4 = base + '_reel.mp4'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', fundo, '-loop', '1', '-i', texto, '-filter_complex',
        "[0:v]scale=2160:3840,zoompan=z='1+0.0009*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=240:s=1080x1920:fps=30[bg];"
        "[1:v]format=rgba,fade=in:st=0.6:d=0.9:alpha=1[tx];[bg][tx]overlay=0:0:shortest=1,format=yuv420p[v]",
        '-map', '[v]', '-t', '8', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-movflags', '+faststart',
        os.path.join(ART, mp4)], check=True)
    return mp4

for it in ITENS:
    a = it['arte']; base = f"{it['data']}_{DIAS[it['dia']]}"; it['arquivos'] = []
    if a[0] == 'foto':
        _, foto, tit, sub, kick, kw = a
        f = base + '.jpg'; V.post_foto(os.path.join(ART, f), foto, tit, sub, kicker=kick, **kw); it['arquivos'].append(f)
        if it.get('reel'): it['video_arq'] = reel(base, foto, tit, sub, kick, kw)
    else:
        total = len(a[1])
        for i, c in enumerate(a[1]):
            f = f'{base}_carrossel-{i + 1}.jpg'; p = os.path.join(ART, f)
            if c[0] == 'capa':
                _, foto, tit, sub, kick, kw = c; V.post_foto(p, foto, tit, sub, kicker=kick, botao='arrasta >', **kw)
            elif c[0] == 'print':
                _, img, leg, crop = c; V.card_print(p, img, leg, crop=crop, n=i, total=total)
            else:
                _, tg, tit, corpo, cor, ref = c; V.card_texto(p, tg, tit, corpo, cor, ref=ref, n=i, total=total)
            it['arquivos'].append(f)
    print('ok', it['id'], it['arquivos'], it.get('video_arq', ''))

# ---------- calendario .md ----------
md = ['# Calendário Refúgio dos 4 Elementos · 20/11/2026 a 01/01/2027', '',
      'Cronograma de recuperação: segunda, quarta e sexta até 01/01. Visual novo, 4 Reels e 3 carrosséis (ciência, depoimentos, para quem é).', '',
      '| Data | Formato | Tema | Status |', '|---|---|---|---|']
md += [f"| {it['dia'][:3]} {br(it['data'])} | {it['tipo']} | {it['tema']} | {it['status']} |" for it in ITENS]
md += ['', '## O que falta', ''] + [f'- {f}' for f in FALTA] + ['']
for it in ITENS:
    md += [f"## {br(it['data'])} · {it['dia']} · {it['tema']}",
           f"**Formato:** {it['tipo']} · **Arquivos:** {', '.join(it['arquivos'] + ([it['video_arq']] if it.get('video_arq') else []))}",
           f"**Foto:** {it['foto']}", f"**Objetivo:** {it['objetivo']}", '', '**Legenda:**', '', it['legenda'], '', f"**Nota:** {it['nota']}", '']
md += ['## Fontes do carrossel de ciência', '',
       '- Ministério da Saúde. Portaria nº 849, de 27/03/2017 (Reiki, Meditação, Yoga e mais 11 práticas na PNPIC).',
       '- CONASS, 12/03/2018: 10 novas práticas no SUS (Aromaterapia, Constelação Familiar, Cromoterapia...), total de 29.',
       '- Goyal M. et al. JAMA Internal Medicine, 2014 (47 estudos, 3.515 participantes).',
       '- Guo X. et al. BMC Palliative Care, 2024 (13 estudos, 824 participantes).']
open(os.path.join(OUT, 'calendario-20nov-01jan.md'), 'w').write('\n'.join(md) + '\n')

# ---------- imagens para o feed ----------
def salvar_jpg(src, dst, w):
    im = Image.open(src).convert('RGB'); im.thumbnail((w, w * 2)); im.save(dst, 'JPEG', quality=82, optimize=True)

def b64(path):
    return 'data:image/jpeg;base64,' + base64.b64encode(open(path, 'rb').read()).decode()

def video_prev(src, dst):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-vf', 'scale=720:1280', '-c:v', 'libx264', '-preset', 'veryfast',
                    '-crf', '26', '-an', '-movflags', '+faststart', '-pix_fmt', 'yuv420p', dst], check=True)

itens_pub, itens_int = [], []
for it in ITENS:
    d = {k: it[k] for k in ('id', 'data', 'dia', 'tipo', 'tema', 'objetivo', 'legenda', 'nota', 'foto', 'status', 'cta')}
    d['dataBr'] = br(it['data'])
    imgs, thumb = [], None
    for j, f in enumerate(it['arquivos']):
        salvar_jpg(os.path.join(ART, f), os.path.join(PUB, 'img', f), 900); imgs.append('img/' + f)
    t = 'img/t_' + it['arquivos'][0]; salvar_jpg(os.path.join(ART, it['arquivos'][0]), os.path.join(PUB, t), 360)
    d_pub = dict(d, imagens=imgs, thumb=t)
    if it.get('video_arq'):
        video_prev(os.path.join(ART, it['video_arq']), os.path.join(PUB, 'video', it['video_arq'])); d_pub['video'] = 'video/' + it['video_arq']
    itens_pub.append({k: v for k, v in d_pub.items() if k not in ('nota', 'objetivo', 'foto')})
    d_int = dict(d, imagens=[b64(os.path.join(PUB, p)) for p in imgs], thumb=b64(os.path.join(PUB, t)))
    if it.get('video_arq'):
        d_int['video'] = 'data:video/mp4;base64,' + base64.b64encode(open(os.path.join(PUB, 'video', it['video_arq']), 'rb').read()).decode()
    itens_int.append(d_int)

ant = [('04/11', '/home/claude/nov/out/post01_04-11_mito-verdade-constelacao.jpg')]
OUTB = '/home/claude/w/refugio-dos-4-elementos/social-media-outubro-2026'
ant += [(f.split('_')[1].replace('-', '/'), os.path.join(OUTB, f)) for f in sorted(os.listdir(OUTB), reverse=True)
        if f.startswith('post0') and f.endswith('.jpg') and 'mito-verdade' not in f]
antigos_pub, antigos_int = [], []
for i, (dt, p) in enumerate(ant):
    f = f'img/antigo_{i}.jpg'; salvar_jpg(p, os.path.join(PUB, f), 360)
    antigos_pub.append({'thumb': f, 'dataBr': dt}); antigos_int.append({'thumb': b64(os.path.join(PUB, f)), 'dataBr': dt})
av = Image.open('/home/claude/refugio-site/img/equipe-r.jpg').convert('RGB'); s = min(av.size)
av.crop(((av.width - s) // 2, int((av.height - s) * 0.55), (av.width + s) // 2, int((av.height - s) * 0.55) + s)).resize((200, 200)).save(os.path.join(PUB, 'img/avatar.jpg'), quality=85)

TPL = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'feed_artifact_template.html')).read()
def pagina(versao, itens, antigos):
    dados = {'versao': versao, 'whats': WHATSAPP_AGENCIA, 'perfil': PERFIL, 'itens': itens, 'antigos': antigos,
             'stories': [{k: v for k, v in s.items() if k != 'nota'} for s in STORIES]}
    return TPL.replace('/*__DADOS__*/', 'const DADOS = ' + json.dumps(dados, ensure_ascii=False) + ';').replace(
        '__VERSAO__', 'Versão interna (com notas)' if versao == 'interno' else 'Para aprovação')
open(os.path.join(PUB, 'index.html'), 'w').write(pagina('cliente', itens_pub, antigos_pub))
interno = pagina('interno', itens_int, antigos_int).replace('src="img/avatar.jpg"', 'src="' + b64(os.path.join(PUB, 'img/avatar.jpg')) + '"')
open(os.path.join(OUT, 'feed-interno-20nov-01jan.html'), 'w').write(
    '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>' + interno + '</body></html>')
print('pub ok', sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(PUB) for f in fs) // 1024, 'KB')
