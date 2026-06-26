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

add_week("SEMANA 1 · 01 a 09/07, Eficiência operacional (Fornecedor)")

add_day("01/07 (QUA), Reaproveitamento Instagram 09/06 → LinkedIn (copy idêntica, arte já pronta) — Programado", [
    dict(time="19h", channel="LINKEDIN", tipo="VENDA (link → curso Fornecedor)",
         origem="Carrossel Instagram 09/06, publicado em junho só no Instagram (6 slides, 4 condutas). Reaproveitado aqui para o LinkedIn, mesma arte, legenda do post conforme original.",
         ancoragem="Caps 3 (Compliance / Pasta), 7 (LCC), 2.2 e 9 (Hub de Escala) do curso Fornecedor",
         formato="Carrossel (6 cards)", persona="Fornecedor / Prestador de Serviços para Condomínios",
         headline="O padrão observado entre fornecedores que constroem carteiras consistentes no mercado condominial.",
         subheadline="Não é preço. Não é sorte. É uma conduta específica documentada em 43 casos reais, em quatro frentes diferentes.",
         cta=None,
         cards=[
             dict(titulo="1. Chegam documentados antes do orçamento",
                  corpo="A maioria espera o síndico pedir a proposta e depois corre atrás das certidões. Os fornecedores que constroem carteira mantêm uma pasta digital sempre atualizada, apólice de RC, ARTs, certidões fiscais e trabalhistas, treinamentos de NR-10 e NR-35. Quando a proposta chega com essa pasta anexada, o síndico já tem o argumento técnico para defender a escolha no conselho."),
             dict(titulo="2. Operam com Custo do Ciclo de Vida (LCC), não com preço de aquisição",
                  corpo="LCC é o cálculo que tira o fornecedor da disputa de preço e o coloca na discussão de valor. Em vez de competir no orçamento de compra, demonstra o custo total ao longo da vida útil: manutenção, eficiência, durabilidade. O mais barato hoje pode ser o mais caro em três anos."),
             dict(titulo="3. Entregam dossiê digital ao final da intervenção",
                  corpo="O pós-obra é o início do próximo contrato. Fornecedores de alta performance entregam, ao fim de cada intervenção, um dossiê digital organizado: fotos antes e depois, laudos, certificados de garantia e ARTs. Esse material vira a pasta de prestação de contas que o síndico apresenta ao conselho fiscal."),
             dict(titulo="4. Operam o Hub de Escala",
                  corpo="Um Síndico Profissional gerencia uma carteira com dezenas de condomínios. Conquistar a confiança desse hub não é fechar um contrato, é abrir acesso a uma carteira inteira, com CAC próximo de zero a partir do segundo."),
         ],
         card_final=dict(
             headline="Esses padrões foram documentados em 43 casos reais no curso Multiplicar Vendas para Condomínios.",
             subheadline=None,
             cta="Toque no link abaixo: " + FORNECEDOR_LINK,
         ),
         legenda="O padrão que diferencia fornecedores que constroem carteira no mercado condominial está em quatro frentes, não em uma. Documentação técnica antes do orçamento, raciocínio de custo do ciclo de vida (LCC) em vez de disputa de preço, dossiê digital ao fim de cada intervenção e operação consciente do Hub de Escala. Cada uma dessas condutas foi documentada por Giuliano Spolavori em 43 casos reais, empresas de segmentos, portes e regiões distintas. O denominador comum não estava no produto. Estava em como esses fornecedores se posicionaram em quatro dimensões diferentes do ciclo comercial. Arrasta o carrossel. Para receber o conteúdo completo documentado nesses 43 casos, toque no link abaixo: " + FORNECEDOR_LINK,
         hashtags="#FornecedoresCondominiais #MercadoCondominial #VendaParaCondomínios #ElevaGS"),
])

add_day("07/07 (TER), Semana 1, Reaproveitamento LinkedIn 17/06 → Instagram (copy idêntica, arte já pronta) — Programado", [
    dict(time="18h", channel="INSTAGRAM", tipo="ENGAJAMENTO (ManyChat → SESSÃO ESTRATÉGICA)",
         origem="Post LinkedIn 17/06, publicado em junho no LinkedIn. Copy idêntica ao original (mesma headline, subheadline e legenda completa), reaproveitada aqui para o Instagram. Arte já existente, sem necessidade de peça nova.",
         ancoragem=None, formato="Post Estático", persona="Diretor / Sócio / Executivo de Imobiliária de Aluguéis",
         headline="Quando a imobiliária de aluguéis depende quase 100% da taxa de administração: escolha ou limitação?",
         subheadline="Cada imóvel da carteira carrega pelo menos cinco fontes de receita que costumam ficar inativadas.",
         cta=None,
         legenda="A maioria das imobiliárias de aluguéis opera com um modelo de receita que tem data de validade. Quando a única fonte é a taxa de administração, a única forma de competir é reduzindo margem, uma espiral que corrói o negócio silenciosamente até o ponto em que não há mais espaço para baixar. Mas cada imóvel administrado carrega valor inativado para os dois lados, proprietário, inquilino e imobiliária: consultoria fiscal e patrimonial ao proprietário, que reduz carga tributária legalmente e maximiza a valorização do imóvel (a imobiliária cobra por hora ou por projeto, receita com baixa elasticidade ao preço, porque o ganho do proprietário é direto e mensurável); gestão integral de reformas, o proprietário recebe obra conduzida, prazo cumprido e imóvel valorizado, sem investir tempo da própria rotina (a imobiliária recebe taxa sobre o valor da obra); seguro residencial via parcerias com seguradoras, o proprietário ganha proteção patrimonial e o inquilino ganha proteção de responsabilidade civil (a imobiliária recebe comissionamento recorrente sem operação adicional); concierge para inquilinos, manutenção, mudança, decoração (a imobiliária atua como curadora, com comissão sobre cada entrega e taxas de retenção do inquilino que aumentam de forma mensurável); e relatórios premium de performance do imóvel como investimento, ROI bruto e líquido, comparativos com benchmarks de mercado, projeção de valorização. A equação é sempre a mesma: a receita só é sustentável porque o cliente final recebe valor proporcional ou superior ao preço. As imobiliárias que crescem não encontraram um mercado novo, encontraram o valor que já existia na carteira, para os dois lados da relação. Para um diagnóstico direcionado ao seu negócio, comente SESSÃO ESTRATÉGICA e olhe o seu direct.",
         hashtags="#ImobiliáriaDeAluguéis #ReceitaRecorrente #GestaoImobiliária #ElevaGS"),
])

add_day("08/07 (QUA), Semana 1, Reaproveitamento Instagram 16/06 → LinkedIn (copy idêntica, arte já pronta) — Programado", [
    dict(time="19h", channel="LINKEDIN", tipo="VENDA (link → Mentoria Executiva)",
         origem="Post Instagram 16/06, publicado em junho só no Instagram. Copy idêntica, reaproveitada aqui para o LinkedIn. Arte já existente.",
         ancoragem=None, formato="Post Estático", persona="Diretor / Sócio / Executivo de Administradora de Condomínios",
         headline="Você investiu em sistemas e automações. Treinou a equipe. E o retrabalho não parou.",
         subheadline="Tecnologia não elimina ineficiência, ela amplifica o que já existe. Sem processo, o sistema digitaliza o caos.",
         cta=None,
         legenda="Esse é o cenário mais custoso observado em administradoras que avançam em transformação digital sem mapear processo: a tecnologia é implementada antes do redesenho operacional. O resultado é sempre o mesmo, o retrabalho continua, só que agora é digital, os mesmos problemas, com interface mais moderna e custo mensal de licença. O que realmente transforma uma administradora são três elementos, nessa ordem: processo, mapeado, redesenhado e documentado antes de qualquer implementação; pessoas, treinadas para entender o porquê das mudanças, não só apertar os botões certos; tecnologia, implementada de forma gradual, sobre processo que já funciona. Quem inverte essa ordem investe alto e segue com os mesmos gargalos. Quem segue essa sequência cresce sem precisar contratar mais. A Metodologia Eleva é aplicada em administradoras em todo o Brasil, construída ao longo de 37 anos de atuação no mercado imobiliário e condominial, com base na gestão de mais de 2.200 condomínios administrados. Para expandir com método, baseado em casos reais, toque no link abaixo: https://www.elevags.com.br/sessao-estrategica-executivos",
         hashtags="#AdministradoraCondomínios #GestaoOperacional #AutomaçãoEstratégica #ElevaGS"),
])

# Conteúdos originalmente planejados para esta semana (Geração Distribuída, Cap 5+7, case 4.9
# Evolua Energia, e Vantagem Competitiva, Cap 5) ficam reservados: Geração Distribuída passa
# para setembro (01/09), Vantagem Competitiva fica no Banco de Conteúdo para outubro.

add_week("SEMANA 2 · 13 a 16/07, Gestor de Ativos: os 3 estágios do síndico (Curso Síndico)")

add_day("14/07 (TER), Semana 2, Conteúdo baseado no curso de Síndico", [
    dict(time="18h", channel="INSTAGRAM", tipo="VALOR + VENDA (ManyChat → Gestor de ativos)",
         ancoragem="Cap 3.1 (Os três estágios da sindicatura profissional) + Cap 3.2 (IGMI-R)",
         formato="Carrossel (5 cards)", persona="Síndico Profissional",
         headline="Existem 3 estágios na carreira de um síndico. A maioria passa a vida inteira presa no segundo.",
         subheadline="E o que separa quem avança não é tempo de carreira. É uma virada de mentalidade bem específica.",
         cta="Comente GESTOR DE ATIVOS e olhe o seu direct.",
         cards=[
             dict(titulo="Estágio 1, O Executor",
                  corpo="Mede o próprio trabalho em tarefas, o que foi feito, que chamado foi atendido. Aprendizado necessário, mas insuficiente: trabalho medido em tarefa compete com qualquer morador que \"também consegue fazer isso\"."),
             dict(titulo="Estágio 2, O Resolvedor de Problemas",
                  corpo="É valorizado porque, com ele, os problemas se resolvem. Mas vive de reatividade, não controla a agenda, a agenda é controlada pelos problemas."),
             dict(titulo="Estágio 3, O Gestor de Ativos",
                  corpo="A unidade de análise deixa de ser tarefa ou problema e passa a ser o patrimônio sob gestão. O IGMI-R (índice da FGV/Abecip) registrou valorização de 18,6% em 12 meses, quase 4 vezes o IPCA do período. É o argumento patrimonial que o Gestor de Ativos usa para justificar honorário, e que o executor nunca aprende a usar."),
         ],
         card_final=dict(
             headline="A progressão entre os três estágios não é cronológica. É estrutural.",
             subheadline="Há síndico com 20 anos de carteira ainda no estágio 1. E síndico com 5 anos de carteira já operando no estágio 3.",
             cta="Comente GESTOR DE ATIVOS para conhecer o curso que estrutura essa transição.",
         ),
         legenda="O tempo na função não promove o profissional. O método promove. Arrasta o carrossel.",
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
         cards=[
             dict(titulo="O que é o Hub de Escala",
                  corpo="Quando o fornecedor de alta performance conquista a confiança de um Síndico Profissional, que gerencia dezenas de condomínios, não está fechando um contrato. Está abrindo um canal."),
         ],
         card_final=dict(
             headline="\"A escala real não vem de bater em 100 portas isoladas. Vem de entrar em 1 porta que abre 100 outras.\"",
             subheadline="Existem dois Hubs no ecossistema condominial, o Síndico Profissional e a Administradora, e cada um exige uma engenharia de relacionamento diferente.",
             cta="Comente FORNECEDOR para entender essa engenharia.",
         ),
         legenda="O curso \"Multiplicar Vendas para Condomínios\" detalha, nos Capítulos 2 e 3, como conquistar cada um dos dois Hubs.",
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
         headline="O mercado da sindicatura profissional está se dividindo em dois grupos.",
         subheadline="De um lado, quem cresce. Do outro, quem fica para trás, e a distância entre os dois só aumenta.",
         cta="Veja a seguir o que separa um grupo do outro.",
         cards=[
             dict(titulo="O que o mercado efetivamente paga",
                  corpo="Honorário não é mais função apenas de quantidade de unidades, é função de como a gestão é demonstrada e documentada."),
             dict(titulo="O perfil de quem está crescendo",
                  corpo="Estrutura CRM, KPIs por condomínio, contrato com SLA e equipe de apoio, opera com método, não com presença física."),
             dict(titulo="O perfil de quem está sendo deixado para trás",
                  corpo="Mede o próprio valor pela quantidade de chamados atendidos, não pelo resultado patrimonial entregue à carteira."),
         ],
         card_final=dict(
             headline="A bifurcação já começou.",
             subheadline="O curso \"Síndico Profissional a Gestor de Ativos\" da Eleva (audiobook + ebook como material complementar) detalha as forças que vão estruturar esse mercado nos próximos anos.",
             cta="Conheça o curso clicando no link: " + SINDICO_LINK,
         ),
         legenda="O tempo de carreira não garante de qual lado da bifurcação você está. O método, sim.",
         hashtags="#SíndicoProfissional #GestorDeAtivos #MercadoCondominial #ElevaGS"),
])

# Temas originais desta semana (Atlas Schindler, case 4.8, e Protocolos de Comunicação
# Consultiva, Cap 6) ficam no Banco de Conteúdo de setembro.

# =========================================================================
# BANCO DE CONTEÚDO, encaixe em outubro/2026
#
# Vantagem Competitiva (Cap 5 do curso Fornecedor, os quatro tipos de vantagem competitiva,
# persona Fornecedor, formato LinkedIn estático), deslocado da Semana 1 de julho.
#
# Engenharia da Segurança (Cap 2.3, réplica de 02/06, persona Fornecedor, formato Post
# Estático), havia sido cotado para 08/07 numa versão anterior deste calendário; 08/07 passou
# a usar o reaproveitamento de 16/06 conforme instrução da Eleva, então esse conteúdo de
# Engenharia da Segurança também fica reservado para outubro.
