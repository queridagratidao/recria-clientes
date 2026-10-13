# Identidade visual Strategia Síndicos Profissionais

Resumo prático extraído do `Brandbook_Strategia_Sindicos_2025.pdf` (salvo nesta pasta),
para consulta rápida sem precisar reabrir o PDF.

## Paleta de cores

### Tons de azul
| Nome | Hex |
|---|---|
| Azul da Meia Noite | `#011633` |
| Azul Escuro | `#001F4B` |
| Azul Neutro | `#05399C` |
| Azul Médio | `#0543CC` |
| Azul Claro | `#155DFD` |

### Tons complementares
| Nome | Hex |
|---|---|
| Bege | `#FFFDFA` |
| Laranja | `#ED2F05` |
| Cinza Escuro | `#1E1D1F` |
| Cinza Médio | `#575757` |
| Cinza Claro | `#A8A5A5` |

## Tipografia

- **Principal (títulos, subtítulos, marcações, destaques): Neometric** — fonte comercial,
  não disponível no Google Fonts. Ainda não conseguimos uma licença/arquivo para uso
  automatizado; nas artes geradas por código usamos **Overpass ExtraBold/Black** como
  substituta mais próxima.
- **Secundária (textos grandes, parágrafos): Overpass** — Google Font, usada normalmente.

## Logo

- Ícone: quadrado em Azul da Meia Noite (`#011633`), com arco em Laranja (`#ED2F05`) e
  3 barras horizontais em Azul Claro/Médio.
- Wordmark: "strategia" (minúsculo, bold) + "SÍNDICOS PROFISSIONAIS" (caixa alta, tracking largo).
- Versão recriada em SVG: `logo-recriado.svg` (aproximação — ideal é usar o arquivo oficial
  quando a cliente enviar o pacote de logos).
- **Nunca**: logo branco em fundo claro, logo escuro em fundo escuro, distorcer, trocar cor,
  separar o ícone do wordmark, ou alterar a tipografia do wordmark.

## Elemento de apoio: losango quadriculado

Padrão recorrente em todas as artes: um "leque" triangular de losangos (quadrados rotacionados
45°) alternando duas cores (normalmente branco/azul-claro ou duas tonalidades de azul),
posicionado no canto superior esquerdo e/ou inferior direito das peças, em arranjo diagonal
crescente (mais losangos conforme se afasta do canto).

## Referência de aplicação (cards de carrossel)

- Fundo: geralmente sólido ou gradiente leve em tom de azul da paleta.
- Foto de pessoas/condomínio real, com overlay/bloco sólido por baixo para o texto.
- Headline grande, peso bold/black, com destaque de palavra-chave em caixa sólida laranja
  (texto branco).
- CTA em caixa laranja sólida ("Comente: PALAVRA").
- Losango quadriculado + logo (canto inferior esquerdo) + seta em círculo laranja
  (canto inferior direito, indicando "arraste/avance").

## Carrossel de teste (30/10 — Halloween do síndico)

Script de geração: `/tmp/.../scratchpad/halloween_cards/render.js` (roda com Playwright,
renderiza HTML/CSS para PNG 1080x1350). Ainda no scratchpad da sessão — não commitado no
repo porque depende de fontes baixadas localmente (Overpass) e de iteração em andamento.
