# Análise de Campanha — Compra de Carteiras Imobiliárias (Meta Ads)
**Recria - Agência de Marketing, 15/09/2026**
**Cliente:** Eleva

## 1. Objetivo e contexto

**Objetivo de negócio:** captar imobiliárias/administradoras em **Porto Alegre e Canoas (RS)** interessadas em vender sua carteira de aluguéis e/ou condomínios, para a Eleva intermediar a negociação de compra — sem expor publicamente que a Eleva atua como intermediadora (o anúncio fala em nome da Eleva como compradora direta, e a intermediação acontece na prática, dentro da conversa).

**Ação desejada:** clique no anúncio, gerando conversa iniciada no WhatsApp da Eleva.

**Restrição geográfica:** só Porto Alegre e Canoas — público bem restrito, o que impacta CPM e velocidade de aprendizado da campanha (ver seção 5).

**Criativos:** já temos 2 artes prontas pra começar, aprovadas pelo Giuliano.

## 2. Estrutura recomendada da campanha

| Nível | Configuração |
|---|---|
| **Campanha** | Objetivo: **Mensagens** (conversas no WhatsApp) |
| **Conjunto de anúncios** | 1 único conjunto — Porto Alegre + Canoas (segmentação por cluster, seção 3), orçamento diário **R$50** |
| **Anúncios** | Os 2 criativos dentro do **mesmo conjunto** |

**Por que orçamento no nível do conjunto, e não dividido por anúncio ou por campanha separada:** com R$50/dia e só 15 dias, dividir o orçamento em dois conjuntos separados (R$25 cada) arrisca nenhum dos dois sair da fase de aprendizado do Meta, que precisa de um volume mínimo de eventos por semana pra otimizar entrega. Deixando os 2 criativos dentro do mesmo conjunto, o algoritmo direciona a verba pra quem estiver performando melhor automaticamente, e ainda assim é possível comparar o resultado **por anúncio** no relatório (Meta reporta CTR, CPM e conversas iniciadas por criativo, mesmo compartilhando o mesmo orçamento). É a forma mais eficiente de descobrir qual criativo entrega mais sem desperdiçar o teto de teste.

## 3. Segmentação geográfica por cluster de bairro

Em vez de segmentar as cidades inteiras, foi feito um levantamento das imobiliárias e administradoras reais de Porto Alegre e Canoas (fontes: SECOVI-RS/AGADEMI e Google Maps, 63 empresas ao todo — planilha em anexo). Os endereços se concentram fortemente em poucos bairros, o que permite trocar a segmentação por cidade inteira por **pins de raio nos clusters onde o público real está**, reduzindo desperdício de verba com quem está fora da área de interesse.

**Porto Alegre (48 empresas no levantamento):**

| Cluster (pin) | Raio sugerido | Empresas cobertas | Bairros na área |
|---|---|---|---|
| Centro / Centro Histórico | ~4 km | 17 diretas + cobre a maioria das demais | Centro, Centro Histórico, Bom Fim, Farroupilha, Independência, Azenha, Moinhos de Vento, Floresta, Auxiliadora, Mont'Serrat, Menino Deus, Bela Vista, Rio Branco |
| Cristo Redentor / Passo d'Areia | ~3 km | 6 | Cristo Redentor, Passo d'Areia |
| Cristal | ~2 km | 2 | Cristal |

**Canoas (15 empresas no levantamento):**

| Cluster (pin) | Raio sugerido | Empresas cobertas |
|---|---|---|
| Centro | ~2 km | 6 |
| Marechal Rondon | ~2 km | 6 |

**Cobertura pelos 3 clusters de Porto Alegre + 2 de Canoas:** ~61 das 63 empresas listadas, após confirmar o bairro das 8 que estavam sem essa informação na planilha original (a maioria caiu dentro dos clusters já existentes, só 1 exigiu ajuste no raio do cluster Centro pra incluir o bairro Auxiliadora).

**Pins individuais adicionais (empresas fora dos clusters):** como não é trabalhoso adicionar mais pins e a ideia é explorar todas as possibilidades, as empresas que ficam fora dos clusters acima recebem um pin próprio, direto no endereço, com raio pequeno (~1 km):

| Empresa | Cidade | Endereço | Bairro |
|---|---|---|---|
| Alfa City Adm. de Condomínios | Porto Alegre | Av. Assis Brasil, 4550 | São Sebastião |
| A Diretriz Adm. de Imóveis e Condomínios | Porto Alegre | R. Joaquim Silveira, 396 | São Sebastião (mesmo pin do Alfa City) |
| Administradora Rio Grandense | Porto Alegre | R. Santa Flora, 1482 | Nonoai |
| Innove Imóveis e Seguros | Porto Alegre | Av. Bento Gonçalves | Partenon |
| Imobiliária Farrapos | Porto Alegre | Rua Conde de Porto Alegre | Navegantes |
| Talla Adm. de Condomínios | Porto Alegre | Av. Protásio Alves, 1880 | Petrópolis |
| Inovar Gestão Imobiliária | Canoas | Rua Lajeado, 1621 | Niterói |
| R2 Síndicos Profissionais | Canoas | Rua Paes Lemes, 715 Sl 01 | Rio Branco (Canoas) |
| Da Vinci Gestão Imobiliária | Canoas | Rua Nazaré, 600 | Nossa Sra. das Graças |

**Total de pins no conjunto de anúncios:** 5 clusters + 8 pins individuais (o de São Sebastião cobre 2 empresas) = 13 pins, cobrindo as 63 empresas do levantamento.

**Como usar no Meta Ads:** no conjunto de anúncios, em "Localização", adicionar cada um dos pins acima (busca por bairro/endereço de referência no mapa do Gerenciador de Anúncios) com o raio indicado, em vez de selecionar "Porto Alegre" e "Canoas" como cidades inteiras.

## 4. Público sugerido (demografia e interesses)

- **Localização:** os pins da seção 3 (5 clusters + pins individuais)
- **Idade:** 30–65 anos
- **Gênero:** todos
- **Interesses (segmentação detalhada manual, combinados com "OU" — sem estreitar):** Mercado imobiliário, Corretagem de imóveis, Gestão de propriedades, Investimento imobiliário, Administração de condomínios
- **Expansão de detalhamento de público:** **desativada** — com orçamento de R$50/dia e público já hiperlocal, deixar o Meta "expandir" pra fora dos interesses definidos arrisca gastar verba testando gente fora do perfil antes de aprender.
- **Posicionamento:** manual — selecionar diretamente Feed do Instagram e Facebook + Stories (os formatos mais diretos pra esse tipo de anúncio), em vez de deixar no automático (Advantage+ Posicionamentos). Com pouca verba e só 15 dias, não vale gastar tempo de aprendizado do algoritmo testando posicionamento — melhor já ir direto no que costuma performar melhor pra esse tipo de campanha.

**Reforço no criativo/legenda:** usar termos como "dono de imobiliária", "administradora de aluguéis e condomínios", "carteira de imóveis" na legenda, pra quem não se identificar simplesmente ignorar o anúncio — essa é a segmentação "de verdade" nesse caso.

## 5. Cronograma e orçamento do teste

- **Duração:** 15 dias corridos
- **Orçamento diário:** R$50
- **Orçamento total do teste:** R$750
- **Critério de decisão ao final:** se o custo por conversa iniciada estiver dentro do razoável (seção 6) e/ou já surgir pelo menos 1 conversa qualificada (imobiliária real, carteira real), aumentar o orçamento. Se não houver nenhuma conversa qualificada em 15 dias, revisar público e/ou criativo antes de aumentar verba.

## 6. Projeção de métricas (cenários, acumulado dos 15 dias) — estimativa, não dado real

**Premissa:** sem CPM histórico desse público específico (por não haver dado da campanha anterior nesta BM), a projeção usa benchmark geral de Meta Ads B2B no Brasil, ajustado pra cima pela restrição geográfica forte (público pequeno tende a aumentar CPM), e pra baixo pela segmentação por cluster (seção 3), que deve melhorar a eficiência frente a segmentar a cidade inteira.

**Todos os números abaixo são o total acumulado dos 15 dias de campanha (R$750 no total, não por dia).**

| Métrica | Conservador | Realista | Otimista |
|---|---|---|---|
| CPM (custo por mil impressões) | R$35 | R$25 | R$15 |
| Impressões (total, 15 dias) | ~21.400 | ~30.000 | ~50.000 |
| Frequência estimada | 2,5 | 2,0 | 1,6 |
| Alcance estimado | ~8.500 | ~15.000 | ~31.000 |
| CTR (todos os cliques) | 1,0% | 1,8% | 2,5% |
| Cliques estimados (total) | ~214 | ~540 | ~1.250 |
| Custo por conversa iniciada (WhatsApp) | R$35 | R$22 | R$12 |
| Conversas iniciadas estimadas (total) | ~21 | ~34 | ~62 |

**Sobre conversão (conversa até virar negócio):** não há histórico suficiente pra estimar com segurança essa etapa. Como hipótese de trabalho, sugiro considerar que de cada 5 a 10 conversas iniciadas, 1 tende a ser uma imobiliária real e qualificada (dono de fato interessado em vender, não curioso ou concorrente testando o anúncio) — e dessas, uma fração menor avança pra negociação de valores. Recomendo tratar isso como algo a **medir durante o teste**, não como projeção confiável, e ajustar a régua depois dos primeiros 15 dias com dado real.

## 7. Legenda do anúncio

Como as duas artes têm exatamente o mesmo texto na imagem (só muda a foto do Giuliano), a recomendação é manter a **mesma legenda nos dois anúncios** — isso isola a variável que está sendo testada (qual foto/visual performa melhor), sem misturar com variação de copy ao mesmo tempo. Testar duas coisas ao mesmo tempo (foto E texto) com uma base de R$50/dia não dá volume suficiente pra saber o que realmente fez diferença.

**Legenda (texto principal do anúncio):**

> Você é dono de imobiliária ou administradora em Porto Alegre ou Canoas?
>
> A Eleva está adquirindo empresas e carteiras de aluguéis e condomínios na região, negociação direta com Giuliano Spolavori: +35 anos no mercado imobiliário, +2.200 condomínios geridos, +20 operações de M&A, +8 mil imóveis locados.
>
> Se interessou e quer saber como funciona?
> Toque no botão abaixo para conversar conosco através do WhatsApp.

**Botão do anúncio:** Fale conosco

## 8. Riscos e observações

- **Público pequeno pode saturar rápido:** com frequência estimada de até 2,5 em 15 dias, vale monitorar se a mesma pessoa está vendo o anúncio repetidamente sem agir — sinal de já ter esgotado o público qualificado da região.
- **Sem dado histórico é um risco assumido conscientemente:** os criativos já tiveram resultado em outro contexto/BM, mas isso não garante repetição de performance — pode ser público, período ou plataforma diferentes. Os 15 dias servem exatamente pra validar isso aqui, com esse público restrito.
- **Qualidade da conversa importa mais que quantidade:** dado o nicho ser tão específico (só quem realmente tem carteira pra vender), vale orientar quem for atender o WhatsApp a documentar rapidamente se cada conversa é "lead real" ou "curioso", pra conseguirmos calcular a taxa de conversão de verdade depois dos 15 dias.
- **Levantamento de imobiliárias é uma foto do momento:** dados públicos (SECOVI-RS, Google Maps) podem mudar — vale confirmar informação antes de qualquer contato direto, e tratar a lista como apoio de segmentação, não como mala direta.

## 9. Próximos passos

1. Giuliano aprova público, segmentação por cluster, orçamento e legenda.
2. Subir a campanha com a estrutura da seção 2, usando os pins da seção 3.
3. Rodar os 15 dias sem mexer (evitar reiniciar aprendizado do Meta).
4. Ao final, comparar resultado real com os 3 cenários da seção 6, e decidir sobre aumento de verba com base em custo por conversa qualificada, não só custo por conversa iniciada.
