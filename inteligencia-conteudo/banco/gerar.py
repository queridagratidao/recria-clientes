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
