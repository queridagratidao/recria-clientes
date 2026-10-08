#!/usr/bin/env python3
"""Remonta os PDFs de todos os e-books aplicando os links de links.json.
Uso (dentro de recria/ebooks): python3 build-all.py"""
import json, pathlib, subprocess, sys
base = pathlib.Path(__file__).parent
livros = json.loads((base / "livros.json").read_text(encoding="utf-8"))
for pasta, pdf in livros.items():
    if (base / pasta / "ebook.html").exists():
        subprocess.run([sys.executable, str(base / "build.py"), pasta, pdf], check=True)
