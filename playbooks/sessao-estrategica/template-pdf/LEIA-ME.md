# Modelo do direcional em PDF (formato e-book)

Padrão visual da Recria: preto e dourado (#000000, #C9A24E, #E4C988), títulos em Playfair Display e texto em Lora, logo real em `logo.png`.

| Arquivo | Função |
|---|---|
| `capa.html` | Capa e contracapa. Trocar `{{NOME}}`, `{{MARCA}}` e `{{DATA}}` |
| `miolo.html` | Conteúdo. Cada `<section>` começa numa página nova. Componentes prontos: `kicker`, `h1` com `<em>` dourado, `lead`, listas, tabelas, `box`, `point` com etiquetas `tag me` (Com minha ajuda) e `tag solo` (Sozinha), `cta` (botão de link) e `sig` (assinatura) |
| `build.js` | Gera `capa.pdf` e `miolo.pdf` com rodapé e número de página |
| `merge.py` | Junta capa, miolo e contracapa no PDF final |

## Como gerar

```bash
npm install            # instala as fontes (Playfair Display e Lora)
NOME="Nome do Cliente" node build.js
python3 merge.py "Direcional-Nome-Cliente-Recria.pdf"
```

Precisa de Playwright com Chromium e de `pypdf`. Conferir o PDF página por página antes de enviar.
