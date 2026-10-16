# Recria Ads Mini Mentoria · processo, regras e pendências

**Nome decidido:** Recria Ads Mini Mentoria ("Apliquei. E agora?"). Acompanhamento de até 60 dias para aplicar o que foi ensinado no Recria Ads, com os dados do aluno analisados e um direcional do que ajustar. Preço: R$ 197. Só existe na página de obrigado do Recria Ads.
**Downsell:** Recria Ads Métricas (e-book com planilhas, R$ 67). Só aparece na página quando o link existir.

## Funil
Recria Ads (R$ 97) → **Mini Mentoria (R$ 197)** → se recusar: **Recria Ads Métricas (R$ 67)** → se recusar: convite para o grupo do WhatsApp.
Depois da Mini Mentoria, no 2º encontro, é o momento de oferecer a **Mentoria Recria (R$ 5.000)** a quem ainda não se sente seguro.

## Como funciona
1. **Até o dia 7:** primeira aula em vídeo, na plataforma, e link para agendar o encontro.
2. **Até o dia 15:** planilhas e material de apoio na plataforma.
3. **1º encontro (dias 30 a 60, contados da compra):** o aluno chega com os resultados (engajamento, vendas, Gerenciador de Anúncios). A Amanda analisa e tira as conclusões. O aluno sai com uma **tarefa personalizada** (por exemplo: testar tal criativo, tal tipo de gancho).
4. **Depois do 1º encontro:** a Amanda leva a ata da reunião para a Claude, que ajuda a montar a tarefa.
5. **2º encontro (de 1 a 2 meses depois do 1º):** análise do que foi aplicado, ajustes e fechamento; a Amanda entrega o **documento final** para o aluno seguir sozinho.
6. **Regras:** só atende quem terminou o curso e aplicou; **até 3 tentativas de agendar cada encontro** (agendamento + 2 remarcações), depois só pelo WhatsApp com a Amanda; quem não usar os encontros nos prazos recebe só um vídeo e um documento gerais.

## Já feito na página (`recria-ads/obrigado.html`)
Nome, texto "Apliquei. E agora?", calendário (dia 7, dia 15, 30–45, 45–60), régua, comparativo com o suporte do curso, tarefa personalizada, regra das 3 tentativas, downsell Métricas (condicionado ao link) e convite final ao grupo. A oferta só aparece com `window.RECRIA.OFERTA.LINK` preenchido.

## O que a Amanda precisa entregar (ver também no chat)
1. **Hotmart:** produto separado "Recria Ads Mini Mentoria" (R$ 197) e o link de pagamento; produto "Recria Ads Métricas" (R$ 67) quando o e-book existir.
2. **Confirmar** que o 2º encontro conta a partir do 1º.
3. **Vídeo da primeira aula** (roteiro em `roteiro-video-recria-ads-personalizado.md`) e **planilhas**, prontos antes do primeiro comprador (a página promete vídeo até o dia 7 e planilhas até o dia 15).
4. **Como a reunião vira ata** (gravação/transcrição ou anotações) e o aviso ao aluno.
5. **Vídeo geral e documento geral** para quem perder os prazos.
6. **Critérios de decisão reais** para o e-book de métricas (ver `recria-ads-metricas-esqueleto.md`).

## Pontos em aberto
1. **Prazos (decidido):** 1º encontro entre o dia 30 e o dia 60 da compra; 2º encontro de 1 a 2 meses depois do 1º (confirmar que é contado a partir do 1º). Total de até cerca de 4 meses.
2. **Ata das reuniões (decidido):** os encontros são gravados no Google Meet pago da Amanda (o mesmo das aulas de yoga) e transcritos (provavelmente pelo Gemini; confirmar o recurso na conta). A Amanda leva a transcrição para a Claude montar a tarefa. A página já avisa que os encontros são gravados e transcritos.
3. **Agendamento com regras.** Janela a partir do dia 30 e até 3 tentativas por encontro exigem saber a **data da compra** do aluno e contar as tentativas por e-mail. Caminho: o script de agenda recebe o aviso de compra da Hotmart (webhook), e o link de agendar valida o e-mail. É uma etapa própria, a fazer depois do produto existir.
4. **Página de obrigado do novo produto** (Hotmart): confirmação, e-mail de acesso, régua e WhatsApp de suporte. O vídeo e as planilhas ficam dentro da plataforma, não na página.
5. **Nome x Mentoria Recria (R$ 5.000):** "Mini Mentoria" ajuda a escada de valor, mas pode confundir. A página já descreve: 2 encontros em até 60 dias.
