# Inteligencia de conteudo da Recria

Pasta compartilhada pela equipe de skills de conteudo. Cada cliente tem a propria pasta (`[cliente]/conteudo/`); aqui fica o que vale para todos.

## Como chamar a equipe (Claude Code, neste repositorio)

Diga o nome da skill e o cliente. Exemplos:

- "Use o pesquisador-ganchos nestas referencias: [links ou prints]"
- "Use o estrategista-conteudo-cliente para a Camila, novembro"
- "Use o planner-clicavel para a Camila, novembro"
- "Use o revisor-claims-cliente no calendario do Refugio"
- "Use o analista-resultados no Insights de outubro da Strategia"
- "Use o plano-gravacao-lote para yoga e Amanda Recria, novembro"

Cada skill comeca perguntando o cliente, le a pasta dele e faz uma prova de leitura (resumo de 5 linhas) antes de produzir. A personalizacao vem dos arquivos do cliente, nao da memoria da conversa.

## Mapa das pastas

| Cliente / perfil | Pasta |
|---|---|
| Camila Sartori | `camila-sartori/` |
| Eleva (Giuliano Spolavori) | `eleva/` |
| Strategia Sindicos | `strategia-sindicos/` |
| Refugio dos 4 Elementos | `refugio-dos-4-elementos/` |
| Amanda Recria (marketing) e agencia Recria | `recria/` |
| Amanda yoga | `yoga-amanda/` |
| Paty | `paty/` |

Em cada uma: `conteudo/contexto.md` (fonte unica do cliente), `conteudo/decisoes.md` (aprendizados e recusas), `conteudo/calendario-AAAA-MM.md`, `conteudo/planner-AAAA-MM-*.html`, `conteudo/resultados/AAAA-MM.md`.

## Arquivos compartilhados

- `recria/conteudo/moldes-de-gancho-e-formatos.md`: formatos, moldes, banco de ganchos por perfil, restricoes por cliente, plano de teste, dados de referencia.
- `inteligencia-conteudo/banco-de-ideias.csv`: referencias classificadas (alimentado pelo `pesquisador-ganchos`).
- `inteligencia-conteudo/tendencias/AAAA-MM.md`: relatorio mensal do pesquisador.

## Fluxo e aprovacao

1. `pesquisador-ganchos` alimenta o banco.
2. `estrategista-conteudo-cliente` monta o calendario do mes.
3. `revisor-claims-cliente` confere promessas, saude, prova social e regras do cliente.
4. `planner-clicavel` gera a versao interna e a do cliente.
5. Amanda aprova (status no arquivo ou pull request mesclado). Nada vai ao cliente sem a aprovacao dela.
6. `analista-resultados` le o Insights do mes e realimenta banco e decisoes.

Roteiros e legendas: `copywriter-cliente`. Criativos: `design-social-media-cliente` e `design-trafego-cliente` (skills ja existentes, fora deste repositorio).

## Atencao: visibilidade do repositorio

O README principal diz que o repositorio e privado, mas a listagem de repositorios da conta mostrou `recria-clientes` como **publico** em 21/10/2026. Ele contem diagnosticos, valores e dados de clientes. Conferir em Settings > General > Danger Zone e, se for o caso, tornar privado.

## Limites conhecidos

- Numeros de reels de terceiros foram lidos por OCR (aproximados), sem datas e sem separar organico de pago.
- O Instagram bloqueia abertura de links; use print da capa + legenda.
- vidIQ: creditos renovaveis (teto de 150), renovacao em 05/11/2026.
