#!/usr/bin/env python3
"""Gera o painel HTML do banco de referencias.

Uso: python3 gerar.py SAIDA.html
Le dados.json e template.html desta pasta e grava o HTML autonomo (dados embutidos).
Imagens: referenciadas por caminho relativo (img/REF-NNNN/slide-NN.jpg) na pasta da pagina publicada.
"""
import json, sys, pathlib

aqui = pathlib.Path(__file__).resolve().parent
dados = json.loads((aqui / "dados.json").read_text(encoding="utf-8"))
html = (aqui / "template.html").read_text(encoding="utf-8")
blob = json.dumps(dados, ensure_ascii=False).replace("</", "<\\/")
if "/*DADOS*/[]" not in html:
    sys.exit("template.html sem marcador /*DADOS*/[]")
saida = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else aqui / "index.html"
saida.write_text(html.replace("/*DADOS*/[]", blob), encoding="utf-8")
print("gerado:", saida, "|", len(dados), "referencias")

# documento consolidado (texto unico para copiar e colar em outra IA)
ETAPA = {"topo": "Topo de funil", "meio": "Meio de funil", "fundo": "Fundo de funil"}
def ref_text(r):
    et = [ETAPA.get(e, e) for e in r.get("etapas", [])] + (["3 em 1"] if r.get("tres_em_um") else [])
    L = [f"{r['id']} | {r['perfil']} | {r['tipo']} | {r['link']}",
         f"Gancho: {r['gancho']}",
         f"Formato: {r['formato']}. Estrutura: {r['estrutura']}",
         "Moldes: " + " || ".join(r.get("molde", [])),
         "Gatilhos: " + ", ".join(r.get("gatilhos", [])) + f". CTA: {r['cta']}",
         "Funil: " + ", ".join(et) + ". Consciencia: " + ", ".join(r.get("consciencia", [])) + ". Objetivo: " + ", ".join(r.get("objetivos", [])) + ". Anuncio: " + ", ".join(r.get("anuncio", [])) + ". " + r.get("funil_notas", ""),
         "Reaproveitamento: " + " ; ".join(f"{x['formato']} ({x['resumo']})" for x in r.get("reaproveitamento", [])),
         "Encaixe por nicho: " + " ; ".join(f"{e['nicho']} [{e['nivel']}] gancho: {e['gancho']} cuidados: {e['cuidados']}" for e in r.get("encaixe", [])),
         "Alertas: " + " | ".join(r.get("alertas", [])),
         f"Metrica: {r['metrica']}. Facilidade: {r['facilidade']}"]
    return "\n".join(L)

cabecalho = ("# Banco consolidado de referencias (para copiar e colar em outra IA)\n\n"
 "Prompt sugerido: \"Voce e estrategista de conteudo para Instagram. Abaixo estao referencias validadas da minha agencia. "
 "NICHO DO CLIENTE: [descreva]. 1) Escolha as que mais combinam e explique por que. 2) Separe por etapa: topo, meio, fundo, 3 em 1 e anuncio (dark post e feed impulsionado). "
 "3) Para cada escolhida escreva o gancho adaptado, o formato e um roteiro curto com outras palavras. 4) Aponte cuidados do nicho. 5) Diga o que nao serve.\"\n\n---\n\n")
(aqui / "banco-consolidado.md").write_text(cabecalho + "\n\n---\n\n".join(ref_text(r) for r in dados) + "\n", encoding="utf-8")
print("consolidado:", aqui / "banco-consolidado.md")
