# -*- coding: utf-8 -*-
# AGOSTO 2026
# Regras: sem WhatsApp. LinkedIn sempre com link direto, nunca gatilho de comentario.
# Instagram intercala Fornecedor (terca) e Sindico/Gestor de Ativos (quinta).
# LinkedIn de quarta fala com Executivos / Administradoras / Donos de Imobiliaria.
# Nunca usar travessao (regra de marca Eleva).

FORNECEDOR_LINK = "https://www.elevags.com.br/cursos-multiplicar-vendas-condominios"
SINDICO_LINK = "https://www.elevags.com.br/cursos-de-sindico-profissional-a-gestor-de-ativos"
MENTORIA_SINDICO_LINK = "https://www.elevags.com.br/mentoria/sindicos-profissionais"
MENTORIA_EXEC_LINK = "https://www.elevags.com.br/mentoria/executiva"

add_month("AGOSTO 2026")
add_week("Agosto: Instagram TERÇA + QUINTA, intercalando Fornecedor e Síndico/Gestor de Ativos. "
         "LinkedIn de quarta retoma o público Executivos / Administradoras / Donos de Imobiliária.")

add_week("SEMANA 1 · 03 a 06/08, Rigor operacional (Fornecedor) + Gestão por dados (Síndico)")

add_day("04/08 (TER), Semana 1, Fornecedor", [
    dict(time="18h", channel="INSTAGRAM", tipo="BRANDING (sem CTA direto)",
         ancoragem="Cap 10.1 do curso Fornecedor, Rigor Operacional", formato="Post Estático", persona="Fornecedor / Prestador de Serviços",
         headline="Tem um detalhe que separa o fornecedor que vira referência do que vira só mais um orçamento. E não é o que você imagina.",
         subheadline="Não é talento. É o que ele faz exatamente igual, toda vez.",
         cta=None,
         legenda="\"Rigor operacional não é sobre perfeição, é sobre consistência\", como define o curso. Cem visitas com checklist de encerramento. Cem relatórios entregues no prazo. É a estética da execução, indissociável do resultado técnico. O síndico que nunca precisa ligar para reclamar de algo que você fez dificilmente vai abrir processo de cotação quando o contrato vencer. Ele vai perguntar quanto custa renovar.",
         hashtags="#RigorOperacional #AltaPerformance #FornecedoresCondominiais #ElevaGS"),
])

add_day("06/08 (QUI), Semana 1, Síndico", [
    dict(time="18h", channel="INSTAGRAM", tipo="BRANDING (sem CTA direto)",
         ancoragem="Cap 11.1 do curso Síndico, Gestão por dados, não por percepção",
         formato="Post Estático", persona="Síndico Profissional",
         headline="\"Eu sinto que esse condomínio anda bem\" é a frase que separa o síndico-resolvedor do Gestor de Ativos.",
         subheadline="Um sente. O outro mede.",
         cta=None,
         legenda="Percepção é individual, não documentável e não defensável em uma renovação de mandato. KPI por condomínio, taxa de inadimplência, variação de OPEX, NPS do conselho consultivo, é o que transforma \"eu acho que estou indo bem\" em argumento objetivo diante do conselho. O síndico que mede tem munição. O que só sente, tem opinião.",
         hashtags="#GestorDeAtivos #SíndicoProfissional #ElevaGS"),
])

add_day("LINKEDIN, Semana 1 (Agosto), Executivos / Administradoras", [
    dict(time="19h", channel="LINKEDIN", tipo="BRANDING (Giuliano em primeiro plano)",
         ancoragem=None, formato="Post Estático", persona="Diretor / Sócio / Executivo de Administradora de Condomínios",
         headline="37 anos de mercado ensinaram a Giuliano que a diferença entre a administradora que escala e a que estagna nunca esteve na planilha de preços.",
         subheadline="Está em um lugar que a maioria dos executivos do setor nunca examina de frente.",
         cta=None,
         legenda="Ao longo de 37 anos no mercado imobiliário e na administração de mais de 2.200 condomínios, Giuliano observou um padrão se repetir em empresas de todos os tamanhos: o principal executivo é o melhor profissional da empresa, e por isso se torna o maior obstáculo ao crescimento dela. A transição de gestor técnico para líder estratégico é a mais difícil e a mais necessária que qualquer executivo do setor vai enfrentar. A Eleva conduz Mentoria Executiva individual para C-Level de administradoras de condomínios, diagnóstico prévio, agenda estruturada e plano para alta performance corporativa, com análise de M&A quando pertinente. Para conhecer o processo, acesse: " + MENTORIA_EXEC_LINK,
         hashtags="#Liderança #GestaoImobiliária #AdministradoraCondomínios #MentoriaExecutiva #ElevaGS"),
])

add_week("SEMANA 2 · 10 a 13/08, Do custo ao investimento (Síndico) + LCC aplicado (Fornecedor)")

add_day("11/08 (TER), Semana 2, Síndico", [
    dict(time="18h", channel="INSTAGRAM", tipo="VENDA (ManyChat → Gestor de ativos)",
         ancoragem="Cap 3.2 do curso Síndico, IGMI-R como argumento patrimonial",
         formato="Post Estático", persona="Síndico Profissional",
         headline="Existe um número que a FGV publica todo trimestre e que pode mudar a forma como você cobra honorário.",
         subheadline="O patrimônio sob sua gestão valorizou quase 4 vezes mais que a inflação no último ano. Quase nenhum síndico usa esse dado a favor da própria carreira.",
         cta=None,
         legenda="O IGMI-R (Índice Geral do Mercado Imobiliário Residencial), calculado pela FGV em parceria com a Abecip, registrou valorização de 18,6% em 12 meses, frente a um IPCA de 4,26% no mesmo período. É o argumento patrimonial que separa o síndico que se vê como prestador de serviço do Gestor de Ativos que se vê como guardião de um patrimônio que se valoriza sob sua gestão. Comente GESTOR DE ATIVOS e olhe o seu direct.",
         hashtags="#GestorDeAtivos #IGMI-R #SíndicoProfissional #ElevaGS"),
])

add_day("13/08 (QUI), Semana 2, Fornecedor", [
    dict(time="18h", channel="INSTAGRAM", tipo="VENDA (ManyChat → Fornecedor)",
         ancoragem="Cap 10.2 do curso Fornecedor, LCC aplicado",
         formato="Post Estático", persona="Fornecedor / Prestador de Serviços",
         headline="Existe uma conta de R$ 30 mil que parece cara, até alguém mostrar a conta de R$ 150 mil que ela evita.",
         subheadline="É a mesma obra. A diferença está só em como ela é apresentada.",
         cta=None,
         legenda="O fornecedor que compete por preço está estruturalmente num ciclo desfavorável: ganha o contrato com margem reduzida, compromete a qualidade, perde a renovação. Quem sai desse ciclo opera com a linguagem do LCC, Custo do Ciclo de Vida. Uma impermeabilização de R$ 30 mil que evita recuperação estrutural de R$ 150 mil não é despesa: é investimento documentado. \"A margem saudável não é consequência da qualidade, é condição para ela.\" Comente FORNECEDOR para entender como apresentar essa conta ao síndico.",
         hashtags="#LCC #EngenhariaDeValor #FornecedoresCondominiais #ElevaGS"),
])

add_day("LINKEDIN, Semana 2 (Agosto), Executivos / Administradoras", [
    dict(time="19h", channel="LINKEDIN", tipo="VENDA (link → Mentoria Executiva)",
         ancoragem=None, formato="Post Estático", persona="Diretor / Sócio / Executivo de Administradora de Condomínios",
         headline="Existem administradoras que sobrevivem à saída do fundador. E administradoras que não sobrevivem.",
         subheadline="A diferença entre as duas tem nome: governança.",
         cta=None,
         legenda="O setor de administração de condomínios no Brasil é predominantemente composto por empresas familiares, muitas delas chegaram longe com esforço e talento. Mas em determinado ponto, a estrutura que funcionou para chegar até ali passa a ser o obstáculo para ir além: decisões estratégicas que ainda dependem de uma única pessoa, processos que existem na cabeça do fundador e não no manual da empresa, dificuldade de atrair executivos externos de qualidade. Governança não significa perder o controle, significa que a empresa funciona bem mesmo na ausência da liderança fundadora. Giuliano Spolavori é conselheiro certificado pelo IBGC e conduziu esse processo ao longo de 35 anos no setor. Para conhecer a Mentoria Executiva da Eleva, acesse: " + MENTORIA_EXEC_LINK,
         hashtags="#GovernançaCorporativa #EmpresaFamiliar #AdministradoraCondomínios #ElevaGS"),
])

add_week("SEMANA 3 · 17 a 20/08, Cases emblemáticos (Fornecedor) + 41 casos documentados (Síndico)")

add_day("18/08 (TER), Semana 3, Fornecedor", [
    dict(time="18h", channel="INSTAGRAM", tipo="VENDA (ManyChat → Fornecedor)",
         ancoragem="Cap 4.11 do curso Fornecedor, Market4u", formato="Carrossel (4 cards)", persona="Fornecedor / Prestador de Serviços",
         headline="Uma empresa faturou R$ 336 milhões sem nunca sair de dentro de condomínios. E o condomínio nem precisou investir um real.",
         subheadline=None, cta=None,
         legenda="CARD 1, CAPA. HEADLINE: Uma empresa faturou R$ 336 milhões sem nunca sair de dentro de condomínios. SUBHEADLINE: E o condomínio nem precisou investir um real. CTA: Arrasta pra entender como. CARD 2, Título: A marca + o número. Corpo: Market4u faturou R$ 336 milhões operando exclusivamente dentro de condomínios. CARD 3, Título: A engenharia básica. Corpo: minimercados autônomos, o condomínio cede espaço, sem risco financeiro fora do próprio balanço. CARD FINAL, HEADLINE: O curso tem outros 42 casos como este, em segmentos diferentes. SUBHEADLINE: O método é o mesmo. O setor é circunstância. CTA: Comente FORNECEDOR para conhecer os 43 casos. LEGENDA DO POST: Esse é só um dos 43 casos documentados no curso \"Multiplicar Vendas para Condomínios\".",
         hashtags="#CasesDeSucesso #MercadoCondominial #FornecedoresCondominiais #ElevaGS"),
])

add_day("20/08 (QUI), Semana 3, Síndico", [
    dict(time="18h", channel="INSTAGRAM", tipo="VENDA (ManyChat → Gestor de ativos)",
         ancoragem="Cap 9 do curso Síndico, 41 casos documentados de alta performance",
         formato="Post Estático", persona="Síndico Profissional",
         headline="41 síndicos profissionais documentados. Segmentos diferentes, carteiras diferentes, cidades diferentes. Um padrão se repete em todos.",
         subheadline=None, cta=None,
         legenda="Rogério Cunha, Maicon Guedes, Pedro Cunha, Juliana Moreira, Sabrina Correia, perfis completamente diferentes entre si, em mercados regionais distintos, com trajetórias de carteira distintas. O curso \"Síndico Profissional a Gestor de Ativos\" documenta os 41 casos no Capítulo 9, e nomeia, na conclusão do capítulo, o que todos eles têm em comum. Comente GESTOR DE ATIVOS e olhe o seu direct.",
         hashtags="#GestorDeAtivos #SíndicoProfissional #CasesDeSucesso #ElevaGS"),
])

add_day("LINKEDIN, Semana 3 (Agosto), Executivos / Administradoras", [
    dict(time="19h", channel="LINKEDIN", tipo="VENDA (link → curso Fornecedor)",
         ancoragem="Cap 1 do curso Fornecedor, Macroeconomia do setor", formato="Post Estático", persona="Fornecedor / Prestador de Serviços + Executivo de Administradora",
         headline="Existe um mercado de R$ 170 bilhões anuais funcionando dentro dos prédios onde você já atua. A maioria enxerga só o contrato em frente.",
         subheadline=None, cta=None,
         legenda="O ecossistema condominial brasileiro, o que os cursos da Eleva chamam de Cidades Privadas, movimenta cerca de R$ 170 bilhões anuais (dados SíndicoNet). Cases como Market4u (R$ 336 milhões), CleanX e Porter Group ilustram a profundidade desse mercado quando ele é operado com método. O Capítulo 1 do curso \"Multiplicar Vendas para Condomínios\" detalha a macroeconomia do setor, e por que a demanda condominial não tem a elasticidade da maioria dos mercados B2B. Acesse: " + FORNECEDOR_LINK,
         hashtags="#MercadoCondominial #CidadesPrivadas #ElevaGS"),
])

add_week("SEMANA 4 · 24 a 27/08, Executivos (reaproveitamento M&A) + Encerramento dos 90 dias")

add_day("25/08 (TER), Semana 4, Reaproveitamento LinkedIn 24/06 → Instagram (mantido conforme já produzido)", [
    dict(time="18h", channel="INSTAGRAM", tipo="ENGAJAMENTO (ManyChat → SESSÃO ESTRATÉGICA)",
         origem="Carrossel LinkedIn 24/06, \"Crescimento orgânico ou aquisição\". Conteúdo e arte mantidos idênticos ao já produzido, só a legenda recebe pequeno ajuste de contexto para reposicionar a peça no fim de agosto.",
         ancoragem=None, formato="Carrossel (5 cards)", persona="Diretor / Sócio / Executivo de Administradora de Condomínios",
         headline="+20 operações de M&A no setor. E em todas elas, a mesma pergunta vinha antes do contrato.",
         subheadline="Crescer organicamente ou adquirir? A resposta errada não é a que você imagina.",
         cta="Comente SESSÃO ESTRATÉGICA.",
         legenda="CARD 2, Título: O dilema real. Corpo: crescer organicamente é seguro, mas pode ser lento para competir com grupos que já têm escala. Adquirir é rápido, mas integração mal preparada destrói valor em meses. CARD 3, Título: Erros mais comuns em aquisições no setor. Corpo: superestimar retenção de clientes, ignorar integração de cultura, due diligence insuficiente sobre passivos. CARD 4, Título: O que o diagnóstico precisa responder antes da decisão. Corpo: situação do mercado local, prontidão operacional para escalar, capital e time para absorver integração. CARD FINAL, HEADLINE: Giuliano Spolavori conduziu +20 operações de M&A em 35 anos de setor. SUBHEADLINE: Nenhuma sem esse diagnóstico estruturado. CTA: Comente SESSÃO ESTRATÉGICA para entender qual caminho faz sentido para a sua empresa.",
         hashtags="#M&A #AdministradoraCondomínios #CrescimentoImobiliário #ElevaGS"),
])

add_day("27/08 (QUI), Semana 4, Fechamento dos 90 dias (Fornecedor + Síndico)", [
    dict(time="18h", channel="INSTAGRAM", tipo="BRANDING + VENDA",
         ancoragem=None, formato="Post Estático", persona="Fornecedor / Síndico",
         headline="90 dias atrás, esse perfil começou a falar de Engenharia da Segurança e Hub de Escala. Hoje fala de Gestor de Ativos e Mentalidade de Alta Performance. O que mudou no meio do caminho?",
         subheadline=None, cta=None,
         legenda="Se você acompanhou os últimos 90 dias, já foi exposto a boa parte do vocabulário que separa quem opera no ecossistema condominial por instinto de quem opera por método, tanto do lado de quem vende para condomínio quanto do lado de quem gere condomínio. Os cursos da Eleva (audiobook + ebook como material complementar) levam esse vocabulário ao método completo. Fornecedor: comente FORNECEDOR. Síndico: comente GESTOR DE ATIVOS. A equipe entra em contato no direct.",
         hashtags="#FornecedoresCondominiais #GestorDeAtivos #ElevaGS"),
])

add_day("LINKEDIN, Semana 4 (Agosto), Mentoria Executiva", [
    dict(time="19h", channel="LINKEDIN", tipo="VENDA (link → Mentoria Executiva)",
         ancoragem=None, formato="Post Estático", persona="Diretor / Sócio / Executivo de Administradora (C-Level)",
         headline="Administradoras que escalam têm um denominador comum. E não tem nada a ver com tamanho de carteira.",
         subheadline="Convite à Mentoria Executiva da Eleva.",
         cta=None,
         legenda="Governança que se descola da figura do fundador: diagnóstico de processos, eficiência operacional, profissionalização da gestão, análise de M&A quando pertinente, plano para maximizar valuation. Atendimento individual, conduzido pelo próprio Giuliano. Ciclos com datas definidas. Acesse: " + MENTORIA_EXEC_LINK,
         hashtags="#MentoriaExecutiva #GovernançaCorporativa #C-Level #ElevaGS"),
])
