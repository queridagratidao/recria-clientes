# Agencia Recria de ponta a ponta

Mapa do fluxo completo, do onboarding ao relatorio. Status em 21/10/2026.

| Etapa | Skill | Status | Entrega |
|---|---|---|---|
| 1. Onboarding | `questionario-cliente` | Externa (existe, fora deste repositorio) | `[cliente]/questionario-onboarding.md` |
| 2. Diagnostico | `estrategista-cliente` | Externa | `[cliente]/diagnostico-estrategico.md` |
| 3. Marca | `branding-cliente` | **Nova** | `DESIGN.md` ou `manual-de-marca.md` |
| 4. Pesquisa de referencias e ganchos | `pesquisador-ganchos` | **Nova** | banco de ideias, tendencias |
| 5. Estrategia de conteudo do mes | `estrategista-conteudo-cliente` | **Nova** | `conteudo/calendario-AAAA-MM.md` |
| 6. Rotina de gravacao (agenda do cliente) | `claquete-rotina-gravacao` | **Nova** | `conteudo/rotina-gravacao-AAAA-MM.md` |
| 7. Copy (roteiros, legendas, anuncios) | `copywriter-cliente` | Externa | `copies/` |
| 8. Revisao de claims | `revisor-claims-cliente` | **Nova** | `conteudo/revisao-AAAA-MM.md` |
| 9. Planner para aprovacao | `planner-clicavel` | **Nova** | `conteudo/planner-AAAA-MM-*.html` |
| 10. Criativos de social media | `design-social-media-cliente` | Externa | `social-media/` |
| 11. Criativos e briefing de trafego | `design-trafego-cliente` | Externa | `trafego-pago/` |
| 12. Gestao de campanhas | `gestor-trafego-cliente` | **Nova** | `trafego-pago/plano-*.md` |
| 13. Automacao Youze | `automacao-youze-cliente` | **Nova** | `conteudo/automacao-youze.md` |
| 14. Comercial (SDR) | `comercial-sdr-cliente` | **Nova** | `comercial/playbook-*.md` |
| 15. Producao da Amanda (lote) | `plano-gravacao-lote` | **Nova** | `conteudo/gravacao-AAAA-MM.md` |
| 16. Resultados e aprendizados | `analista-resultados` | **Nova** | `conteudo/resultados/AAAA-MM.md`, `decisoes.md` |
| 17. Relatorio ao cliente | `relatorio-mensal-cliente` | **Nova** | `conteudo/relatorio-cliente-AAAA-MM.md` |
| 18. Proposta comercial | `proposta-comercial-cliente` | **Nova** | `propostas/[prospecto]-AAAA-MM.md` |
| Orquestrador | `agencia-recria` | **Nova** | indica a proxima etapa; roda o "mes completo" |

## Skills externas
As marcadas "Externa" nao estao em `.claude/skills/` neste repositorio. Para a equipe ficar toda no GitHub, trazer os arquivos delas para esta pasta, mantendo os mesmos nomes. Enquanto isso, o orquestrador avisa quando uma etapa depende delas.

## Principios
- A personalizacao vem dos arquivos do cliente, nao da memoria da conversa: toda skill comeca lendo `[cliente]/conteudo/contexto.md` e faz prova de leitura.
- A aprovacao final e sempre da Amanda.
- Nao fabricar prova social. Sem promessa de resultado em saude.
- Medir por mediana por video, separando organico de anuncio.
- Yoga da Amanda e Amanda Recria sao clientes da agencia (conteudo e anuncio).
