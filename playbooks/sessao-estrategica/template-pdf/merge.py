"""Junta capa, miolo e contracapa num PDF só.
Uso: python3 merge.py "Direcional-Nome-Cliente-Recria.pdf"
"""
import sys
from pypdf import PdfReader, PdfWriter

saida = sys.argv[1] if len(sys.argv) > 1 else "Direcional-Recria.pdf"
capa = PdfReader("capa.pdf")
miolo = PdfReader("miolo.pdf")
w = PdfWriter()
w.add_page(capa.pages[0])
for pagina in miolo.pages:
    w.add_page(pagina)
w.add_page(capa.pages[1])
w.write(saida)
print("Gerado:", saida, "-", len(miolo.pages) + 2, "páginas")
