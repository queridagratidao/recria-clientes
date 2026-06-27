# Briefing de Tráfego Pago — Eleva — Multiplicar Vendas para Condomínios

**Objetivo:** cliques/conversão para a LP do curso (público de fornecedores/prestadores de serviço de condomínio)
**Público-alvo:** fornecedores e prestadores de serviço de condomínio (limpeza, segurança, manutenção, tecnologia), autônomos ou pequenas empresas que crescem só por indicação e têm dificuldade em vender pra quem decide no condomínio
**Oferta:** curso "Multiplicar Vendas para Condomínios" — ebook + audiobook, 9 aulas, R$150 promocional (de R$293), 43 casos reais
**Destino:** https://www.elevags.com.br/cursos-multiplicar-vendas-condominios

## Copies (texto estático no criativo — definido pela usuária)

### Criativo 1 — Objeção Invertida
- Texto principal: "Fornecedor bom não precisa saber vender. Precisa entregar bem."
- Sub-headline: Se você acredita nisso, está perdendo contratos todo mês sem perceber.
- CTA visual no criativo: Toque no botão para saber mais

### Criativo 2 — Perda Silenciosa
- Texto principal: Quantos contratos com condomínio você perdeu nos últimos 6 meses sem nem saber por quê?
- Texto de apoio: O gestor não te ligou de volta. A reunião não evoluiu. Você mandou proposta e ficou no silêncio.
- CTA visual no criativo: Toque no botão para saber mais

## Legendas do anúncio (variações A/B)
Ver `../../copies/2026-06-27_copy-trafego-fornecedores.md` (2 variações de legenda por criativo, headline e CTA pro gestor de tráfego escolher/testar).

## Criativos
- Objeção Invertida — Feed 1:1: `01_objecao-invertida_feed-1x1.png`
- Objeção Invertida — Stories/Reels 9:16: `02_objecao-invertida_story-9x16.png`
- Perda Silenciosa — Feed 1:1: `03_perda-silenciosa_feed-1x1.png`
- Perda Silenciosa — Stories/Reels 9:16: `04_perda-silenciosa_story-9x16.png`

Identidade visual aplicada: fundo #0A0C0F, destaque laranja #E09C3B, tipografia Sora, sem fotografia, logo branco da Eleva (`logo-eleva-branco.png`, extraído do MIV) no canto inferior esquerdo.

## CTA e destino
Link da LP do curso (Hotmart) — botão "Saiba mais" / "Comprar agora" conforme placement.

## Nota técnica
Criativos gerados com Pillow (script `build_creatives.py` nesta mesma pasta) em vez do pipeline padrão `gerar-imagem`, porque o ambiente atual (Windows) não tem `codex` CLI nem `GEMINI_API_KEY` configurados — o script padrão depende de `fcntl` (Unix-only) e desses providers. Abordagem alternativa garante texto exato e cor de marca precisa (#0A0C0F / #E09C3B), sem risco de erro de OCR do gerador de imagem em IA.
