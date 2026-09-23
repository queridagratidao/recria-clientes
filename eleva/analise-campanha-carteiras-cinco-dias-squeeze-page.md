# Análise dos 5 Primeiros Dias — Campanha Compra de Carteiras + Proposta de Squeeze Page
**RECRIA Marketing, 23/09/2026**
**Cliente:** Eleva

## Contexto

A campanha "AM | Eleva - Compra de Carteiras Imobiliárias" está ativa desde 18/09/2026, levando o clique direto para uma conversa no WhatsApp. Abaixo estão os números dos primeiros 5 dias de veiculação (18/09 a 23/09) e a conclusão sobre o principal gargalo identificado, seguida da proposta de squeeze page para resolver esse gargalo.

### Big numbers dos 5 dias

| Métrica | Campanha (total) | Ads 1 | Ads 2 |
|---|---|---|---|
| Resultados (conversas por mensagem) | 7 | 6 | 1 |
| Alcance | 2.253 | 2.231 | 152 |
| Frequência | 2,18 | 2,09 | 1,57 |
| Custo por resultado | R$36,94 | R$40,56 | R$15,18 |
| Valor gasto | R$258,55 | R$243,37 | R$15,18 |
| Segmentação | Porto Alegre + Canoas + São Leopoldo + Novo Hamburgo | — | — |

### Conclusão da análise

Em volume bruto, os 7 resultados em 5 dias estão dentro do cenário conservador projetado originalmente (R$35 por conversa). O problema não está no público, na segmentação nem no criativo. **O gargalo é a ausência de filtro antes do WhatsApp**: qualquer pessoa pode clicar no anúncio e abrir uma conversa, sem nenhuma etapa de qualificação prévia (nome, se é dono/decisor, tipo de imóvel). Isso permite que curiosos, concorrentes testando o anúncio e gente fora do perfil entrem na mesma métrica de "conversa iniciada" que os leads reais, o que suja a leitura do algoritmo e a real taxa de conversão da campanha. Reforça isso o fato de a frequência já estar em 2,18 no dia 5, quando o teto estimado para o público inteiro de 15 dias era 2,5, sinal de que o público pequeno está saturando rápido e sendo impactado repetidas vezes sem uma etapa que filtre quem realmente tem interesse.

### Novo processo proposto

1. A pessoa vê o criativo do anúncio (estático, carrossel ou vídeo).
2. Clica e vai para a squeeze page.
3. Deixa os dados dela no formulário.
4. Em seguida, abre um botão de WhatsApp para ela chamar a Eleva, ou a Eleva já consegue entrar em contato direto pelos dados que ela preencheu, mesmo que ela não clique no WhatsApp na hora.

Isso garante que todo lead que chega ao WhatsApp já passou por uma etapa mínima de identificação, e nenhum dado se perde mesmo se a pessoa não completar a conversa.

## Mockup da página

![Mockup da squeeze page](lp-mockup-full.png)

*Mockup de referência visual, o Giuliano monta a versão final direto no Webflow usando o prompt abaixo.*

## Prompt para o Giuliano criar a LP no Webflow (squeeze page)

**Objetivo da página:** captar lead qualificado (dono/decisor de imobiliária ou administradora) antes de liberar o contato direto no WhatsApp, filtrando curiosos e gente fora do perfil.

**Seção 1 — Confirma a promessa do criativo**

Tag: "Porto Alegre, Canoas, São Leopoldo e Novo Hamburgo"

Headline: "Você é dono de imobiliária ou administradora? A Eleva está adquirindo empresas e carteiras de aluguéis e condomínios na sua região."

Subheadline: "Processo direto, seguro e sigiloso."

Botão: "Quero saber mais" (âncora rolando para o formulário, seção 4)

**Seção 2 — Quem está por trás, autoridade do Giuliano**

Reaproveitar a seção de autoridade que já existe no site (foto, citação "Estratégia não é teoria. É experiência de quem já esteve à frente.", bio com +35 anos de atuação, +2,2 mil condomínios geridos, +8 mil locações de imóveis, +20 M&A concluídos, Metodologia Eleva, e os badges IBGC, IREM e ARM). É só copiar a estrutura que já está pronta e ajustar para esta squeeze page.

**Seção 3 — Provas sociais (carrossel já existente)**

Reaproveitar o carrossel de depoimentos/cases que já existe no site, mesma estrutura de card com selo, citação e assinatura.

**Seção 4 — Formulário com liberação do WhatsApp**

Headline: "Preencha os dados abaixo para iniciar a conversa"

Texto de apoio (antes do formulário): "Deixe seus dados aqui e, assim que enviar, você também pode chamar o Giuliano direto no WhatsApp para conversar."

Campos: Nome completo, WhatsApp com DDD, E-mail, Cidade

Depois de enviar: "Obrigado! Agora é só chamar o Giuliano." + botão "Falar agora no WhatsApp com Giuliano", pré-preenchido com uma mensagem já contextualizada (ex: "Olá Giuliano, preenchi o formulário sobre a compra de carteira imobiliária").

## Teste de criativos propostos

Com a squeeze page no ar, a sugestão é ativar três variedades de criativo levando todas para a mesma página, além dos estáticos que já estão rodando, para entender qual formato converte mais:

- **Estático** (já em veiculação)
- **Carrossel** (proposta abaixo)
- **Vídeo curto** (roteiro abaixo)

### Carrossel (anúncio, 8 slides)

1. "Você é dono de imobiliária ou administradora em Porto Alegre, Canoas, São Leopoldo ou Novo Hamburgo?"
2. "A Eleva está adquirindo empresas e carteiras de aluguéis e condomínios na sua região"
3. "Se você está pensando em vender sua carteira ou sua empresa, essa conversa é com você"
4. "A negociação é direta com Giuliano Spolavori, fundador da Eleva"
5. "+35 anos de mercado imobiliário, +2.200 condomínios geridos, +20 operações de M&A conduzidas"
6. "Processo seguro e sigiloso, sem expor sua empresa no mercado"
7. "Prefere falar direto? Chama a Eleva no WhatsApp pelo link da bio"
8. "Ou toque no botão abaixo e agende pelo formulário da página" (CTA)

### Legenda (para o post do carrossel e do vídeo)

Você é dono de imobiliária ou administradora em Porto Alegre, Canoas, São Leopoldo ou Novo Hamburgo?

A Eleva está adquirindo empresas e carteiras de aluguéis e condomínios na região, negociação direta com Giuliano Spolavori: +35 anos no mercado imobiliário, +2.200 condomínios geridos, +20 operações de M&A, +8 mil imóveis locados.

Processo seguro e sigiloso.

Se interessou e prefere já chamar direto, é só acessar o WhatsApp da Eleva pelo link na bio. Se preferir, toque no botão abaixo e agende pelo formulário da página.

### Roteiro de vídeo curto (até 2 min) para o Giuliano gravar

**Gancho + proposta (0-25s):** "Se você é dono de imobiliária ou administradora em Porto Alegre, Canoas, São Leopoldo ou Novo Hamburgo, eu tenho uma proposta para te fazer. Estamos adquirindo empresas e carteiras de aluguéis e condomínios na sua região. Se você está pensando em vender sua carteira ou sua empresa, você pode negociar diretamente comigo, o fundador da Eleva."

**Credenciais (25-60s):** "Eu sou Giuliano Spolavori, tenho mais de 35 anos no mercado imobiliário, já geri mais de 2.200 condomínios, já conduzi mais de 20 operações de M&A no setor."

**Prova/confiança (60-90s):** "Já são mais de 8 mil imóveis locados sob gestão através das operações que eu conduzi. Então, você está falando com alguém que entende exatamente o valor do que você construiu."

**CTA (90-110s):** "Se interessou, quer negociar comigo? Então, toque no botão para saber mais, ou me chama direto no WhatsApp pelo link da bio."
