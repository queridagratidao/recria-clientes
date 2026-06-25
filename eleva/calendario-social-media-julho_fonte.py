# -*- coding: utf-8 -*-
# JULHO 2026
# Regras: sem WhatsApp (calendario separado da Eleva). LinkedIn nunca usa gatilho "Comente X"
# (ManyChat) -- sempre link direto. Instagram usa gatilho de comentario quando fizer sentido.
# Nunca usar travessao (regra de marca Eleva).

FORNECEDOR_LINK = "https://www.elevags.com.br/cursos-multiplicar-vendas-condominios"
SINDICO_LINK = "https://www.elevags.com.br/cursos-de-sindico-profissional-a-gestor-de-ativos"
MENTORIA_SINDICO_LINK = "https://www.elevags.com.br/mentoria/sindicos-profissionais"
MENTORIA_EXEC_LINK = "https://www.elevags.com.br/mentoria/executiva"

add_month("JULHO 2026")

add_week("SEMANA 1 · 06 a 09/07, Eficiência operacional (Fornecedor)")

add_day("07/07 (TER), Semana 1, Reaproveitamento LinkedIn 17/06 → Instagram", [
    dict(time="18h", channel="INSTAGRAM", tipo="ENGAJAMENTO (ManyChat → SESSÃO ESTRATÉGICA)",
         origem="Post LinkedIn 17/06 (Imobiliária de Aluguéis), publicado em junho no LinkedIn, reaproveitado aqui para o Instagram em julho, com a mesma arte e legenda levemente ajustada para o formato do Instagram (no LinkedIn não havia automação de comentário, era só link).",
         ancoragem=None, formato="Carrossel (5 cards)", persona="Diretor / Sócio de Imobiliária de Aluguéis",
         headline="Existe um contrato escondido dentro de cada imóvel alugado, e quase nenhuma imobiliária cobra por ele.",
         subheadline="5 fontes de receita que já existem na sua carteira, sem precisar de mais um imóvel.",
         cta="Comente SESSÃO ESTRATÉGICA e olhe o seu direct.",
         legenda="CARD 2, Título: Consultoria fiscal e patrimonial. Corpo: o proprietário reduz carga tributária e maximiza a valorização do imóvel; a imobiliária cobra por hora ou por projeto. CARD 3, Título: Gestão integral de reformas. Corpo: o proprietário recebe obra conduzida e imóvel valorizado, sem usar o próprio tempo; a imobiliária cobra taxa sobre o valor da obra. CARD 4, Título: Seguro residencial + concierge para inquilinos. Corpo: comissionamento recorrente, sem operação adicional, o cliente percebe como diferencial, não como custo. CARD FINAL, HEADLINE: A receita só é sustentável quando o cliente final recebe valor proporcional ao preço. SUBHEADLINE: As imobiliárias que crescem não acharam um mercado novo, acharam o valor que já existia na própria carteira. CTA: Comente SESSÃO ESTRATÉGICA para um diagnóstico direcionado à sua carteira. LEGENDA DO POST: Arrasta o carrossel até o final, 5 fontes de receita que a maioria das imobiliárias de aluguéis deixa inativadas.",
         hashtags="#ImobiliáriaDeAluguéis #ReceitaRecorrente #GestaoImobiliária #ElevaGS"),
])

add_day("08/07 (QUA), Semana 1", [
    dict(time="19h", channel="LINKEDIN", tipo="VENDA (link → curso Fornecedor)",
         ancoragem="Capítulo 5 do curso, Matriz de Vantagem Competitiva",
         formato="Post Estático", persona="Fornecedor / Prestador de Serviços para Condomínios",
         headline="Existem quatro tipos de vantagem competitiva no ecossistema condominial. A maioria dos fornecedores só conhece um, e aposta justamente no que menos dura.",
         subheadline="Preço, escopo, reputação e eficiência. Só uma dessas quatro se reforça com o tempo.",
         cta=None,
         legenda="A vantagem por preço se esgota na primeira cotação melhor. A vantagem por escopo depende de manter o portfólio sempre ampliado. A vantagem por reputação demora anos para se consolidar. Existe uma quarta, e é a única que se reforça com o tempo: cada contrato bem executado reduz o custo do próximo, melhora a margem sem competir por ela e libera capacidade para atender mais carteira sem custo proporcional. O curso \"Multiplicar Vendas para Condomínios\" da Eleva (audiobook + ebook como material complementar) descreve, no Capítulo 5, como construir essa vantagem de forma deliberada, com os 43 casos reais documentados por Giuliano Spolavori. Acesse: " + FORNECEDOR_LINK,
         hashtags="#VantagemCompetitiva #MercadoCondominial #FornecedoresCondominiais #ElevaGS"),
])

# Tema original desta semana (Geração Distribuída, Cap 5+7, case 4.9 Evolua Energia) fica no
# Banco de Conteúdo de setembro.

add_week("SEMANA 2 · 13 a 16/07, Gestor de Ativos: os 3 estágios do síndico (Curso Síndico)")

add_day("14/07 (TER), Semana 2, Conteúdo baseado no curso de Síndico", [
    dict(time="18h", channel="INSTAGRAM", tipo="VALOR + VENDA (ManyChat → Gestor de ativos)",
         ancoragem="Cap 3.1 (Os três estágios da sindicatura profissional) + Cap 3.2 (IGMI-R)",
         formato="Carrossel (5 cards)", persona="Síndico Profissional",
         headline="Existem 3 estágios na carreira de um síndico. A maioria passa a vida inteira presa no segundo.",
         subheadline="E o que separa quem avança não é tempo de carreira. É uma virada de mentalidade bem específica.",
         cta="Comente GESTOR DE ATIVOS e olhe o seu direct.",
         legenda="CARD 2, Título: Estágio 1, O Executor. Corpo: mede o próprio trabalho em tarefas, o que foi feito, que chamado foi atendido. Aprendizado necessário, mas insuficiente: trabalho medido em tarefa compete com qualquer morador que \"também consegue fazer isso\". CARD 3, Título: Estágio 2, O Resolvedor de Problemas. Corpo: é valorizado porque, com ele, os problemas se resolvem. Mas vive de reatividade, não controla a agenda, a agenda é controlada pelos problemas. CARD 4, Título: Estágio 3, O Gestor de Ativos. Corpo: a unidade de análise deixa de ser tarefa ou problema e passa a ser o patrimônio sob gestão. O IGMI-R (índice da FGV/Abecip) registrou valorização de 18,6% em 12 meses, quase 4 vezes o IPCA do período. É o argumento patrimonial que o Gestor de Ativos usa para justificar honorário, e que o executor nunca aprende a usar. CARD FINAL, HEADLINE: A progressão entre os três estágios não é cronológica. É estrutural. SUBHEADLINE: Há síndico com 20 anos de carteira ainda no estágio 1. E síndico com 5 anos de carteira já operando no estágio 3. CTA: Comente GESTOR DE ATIVOS para conhecer o curso que estrutura essa transição. LEGENDA DO POST: O tempo na função não promove o profissional. O método promove. Arrasta o carrossel.",
         hashtags="#GestorDeAtivos #SíndicoProfissional #MercadoCondominial #ElevaGS"),
])

add_day("15/07 (QUA), Semana 2", [
    dict(time="19h", channel="LINKEDIN", tipo="VENDA (link → curso Fornecedor)",
         ancoragem="Cap 6 do curso (Protocolos de Comunicação), cases 4.20 e 4.23",
         formato="Post Estático", persona="Fornecedor / Prestador de Serviços",
         headline="RC, ART e NR-10 não fecham contrato sozinhos. Mas decidem qual proposta o Conselho Fiscal aprova primeiro.",
         subheadline="A diferença entre apresentar documentação e apresentar argumento.",
         cta=None,
         legenda="Fornecedores que documentam apólice de RC, ARTs e treinamentos de NR-10 e NR-35 não estão apenas cumprindo exigência, estão entregando ao síndico o argumento que ele precisa para defender a contratação no Conselho Fiscal. Os cases 4.20 (Impermeabilização Predial) e 4.23 (Manutenção Elétrica) do curso documentam como esse arsenal técnico vira critério de decisão, não apenas de conformidade. Os fornecedores que entendem isso saem da disputa de preço. O curso \"Multiplicar Vendas para Condomínios\" (audiobook + ebook) detalha a estrutura completa no Capítulo 6. Acesse: " + FORNECEDOR_LINK,
         hashtags="#EngenhariaDaSegurança #FornecedoresCondominiais #MercadoCondominial #ElevaGS"),
])

# Tema original desta semana (Compliance / Alfândega Técnica, Cap 6 + 3.3) fica no Banco de
# Conteúdo de setembro.

add_week("SEMANA 3 · 20 a 23/07, Hub de Escala (Fornecedor)")

add_day("21/07 (TER), Semana 3", [
    dict(time="18h", channel="INSTAGRAM", tipo="VENDA (ManyChat → Fornecedor)",
         ancoragem="Cap 2.2 (Síndico Profissional como Hub) + Cap 3.4 (Administradora como Canal)",
         formato="Carrossel (3 cards)", persona="Fornecedor / Prestador de Serviços",
         headline="1 contrato pode virar 30. A maioria dos fornecedores nunca percebe quando está na frente dessa porta.",
         subheadline="Não é sorte. É reconhecer a posição de quem está do outro lado da mesa.",
         cta="Comente FORNECEDOR e olhe o seu direct.",
         legenda="CARD 2, Título: O que é o Hub de Escala. Corpo: quando o fornecedor de alta performance conquista a confiança de um Síndico Profissional, que gerencia dezenas de condomínios, não está fechando um contrato. Está abrindo um canal. CARD FINAL, HEADLINE: \"A escala real não vem de bater em 100 portas isoladas. Vem de entrar em 1 porta que abre 100 outras.\" SUBHEADLINE: Existem dois Hubs no ecossistema condominial, o Síndico Profissional e a Administradora, e cada um exige uma engenharia de relacionamento diferente. CTA: Comente FORNECEDOR para entender essa engenharia. LEGENDA DO POST: O curso \"Multiplicar Vendas para Condomínios\" detalha, nos Capítulos 2 e 3, como conquistar cada um dos dois Hubs.",
         hashtags="#HubDeEscala #FornecedoresCondominiais #MercadoCondominial #ElevaGS"),
])

add_day("22/07 (QUA), Semana 3", [
    dict(time="19h", channel="LINKEDIN", tipo="VENDA (link → curso Fornecedor)",
         ancoragem="Caps 2 e 9 do curso, CAC e LTV no ecossistema condominial",
         formato="Post Estático", persona="Fornecedor / Prestador de Serviços (LinkedIn analítico)",
         headline="Em B2B convencional, todo contrato novo custa o mesmo esforço comercial do anterior. No ecossistema condominial, existe uma exceção que poucos fornecedores exploram.",
         subheadline="O CAC do segundo contrato em diante pode cair para perto de zero. Mas só para quem entende uma coisa específica sobre o primeiro contrato.",
         cta=None,
         legenda="Em B2B convencional, custo de aquisição de cliente (CAC) e valor do tempo de vida do cliente (LTV) se cruzam para definir margem, cada novo contrato exige novo esforço comercial proporcional. No ecossistema condominial, um único esforço bem-feito junto a um Síndico Profissional ou Administradora pode abrir dezenas de contratos por indicação orgânica. O CAC unitário do segundo contrato em diante tende a zero, mas só para quem entende que o primeiro contrato não é uma venda isolada: é uma porta de entrada para uma carteira inteira. Os Capítulos 2 e 9 do curso \"Multiplicar Vendas para Condomínios\" descrevem essa lógica em detalhe. Acesse: " + FORNECEDOR_LINK,
         hashtags="#CAC #HubDeEscala #VendaB2B #ElevaGS"),
])

add_week("SEMANA 4 · 27 a 30/07, Curso de Síndico em foco")

add_day("28/07 (TER), Semana 4, Conteúdo baseado no curso de Síndico", [
    dict(time="18h", channel="INSTAGRAM", tipo="VALOR + VENDA (ManyChat → Gestor de ativos)",
         ancoragem="Cap 7.1, Hub Estratégico: posição, acesso e confiança",
         formato="Post Estático", persona="Síndico Profissional",
         headline="Dois síndicos começam a carreira no mesmo ano, com a mesma carteira. Cinco anos depois, um tem o dobro de condomínios e foi procurado para vender a operação. O outro ainda compete em preço.",
         subheadline="A diferença não foi esforço. Foi entender que a posição que o síndico ocupa é, ela mesma, um ativo.",
         cta="Comente GESTOR DE ATIVOS e olhe o seu direct.",
         legenda="O síndico não é apenas um prestador de serviço, é o filtro e o catalisador de todas as relações comerciais que passam pelo condomínio: administradoras chegam pelo síndico, fornecedores dependem da sua indicação, seguradoras e fintechs precisam da sua adesão para chegar ao condomínio. É o que o curso chama de Hub Estratégico. Mas ocupar essa posição não é o mesmo que construí-la como ativo, essa construção tem método, e está no Capítulo 7. Comente GESTOR DE ATIVOS para conhecer o curso.",
         hashtags="#HubEstratégico #GestorDeAtivos #SíndicoProfissional #ElevaGS"),
])

add_day("29/07 (QUA), Semana 4, Conteúdo baseado no curso de Síndico", [
    dict(time="19h", channel="LINKEDIN", tipo="VENDA (link → curso Síndico)",
         ancoragem="Cap 1, O Mercado da Sindicatura Profissional Hoje (bifurcação)",
         formato="Carrossel (5 cards)", persona="Síndico Profissional / Gestor de Ativos",
         headline="O mercado da sindicatura profissional está se dividindo em dois grupos. Cinco anos a partir de agora, a distância entre eles vai ser irreversível.",
         subheadline=None,
         cta=None,
         legenda="CARD 1, CAPA. HEADLINE: O mercado da sindicatura profissional está se dividindo em dois grupos. SUBHEADLINE: De um lado, quem cresce. Do outro, quem fica para trás, e a distância entre os dois só aumenta. CTA: Veja a seguir o que separa um grupo do outro. CARD 2, Título: O que o mercado efetivamente paga. Corpo: honorário não é mais função apenas de quantidade de unidades, é função de como a gestão é demonstrada e documentada. CARD 3, Título: O perfil de quem está crescendo. Corpo: estrutura CRM, KPIs por condomínio, contrato com SLA e equipe de apoio, opera com método, não com presença física. CARD 4, Título: O perfil de quem está sendo deixado para trás. Corpo: mede o próprio valor pela quantidade de chamados atendidos, não pelo resultado patrimonial entregue à carteira. CARD FINAL, HEADLINE: A bifurcação já começou. SUBHEADLINE: O curso \"Síndico Profissional a Gestor de Ativos\" da Eleva (audiobook + ebook como material complementar) detalha as forças que vão estruturar esse mercado nos próximos anos. CTA: Conheça o curso clicando no link: " + SINDICO_LINK + " LEGENDA DO POST: O tempo de carreira não garante de qual lado da bifurcação você está. O método, sim.",
         hashtags="#SíndicoProfissional #GestorDeAtivos #MercadoCondominial #ElevaGS"),
])

# Temas originais desta semana (Atlas Schindler, case 4.8, e Protocolos de Comunicação
# Consultiva, Cap 6) ficam no Banco de Conteúdo de setembro.
