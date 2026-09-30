from materiais_lib import *
def R(n,titulo,sub,pages,fname):
    b=Book(f'Resumão Módulo {n} · Recria Ads',f'Recria Ads · Resumão do Módulo {n}')
    b.cover(f'Recria Ads · Resumão do Módulo {n}',titulo,sub)
    for cls,body in pages: b.page(cls,body)
    b.render(OUT+fname)
R(3,'Estratégia antes <em class="g">do conteúdo</em>','Para quem você fala, por que te escolhem e em que momento cada pessoa está.',[
('light','''<div class="kick">Aula 3.1 · Cliente e posicionamento</div><h1>Cliente não é faixa etária. <em class="g">É desejo, medo e objeção.</em></h1>
<ul><li><b>Desejo:</b> o resultado, não o produto</li><li><b>Medo:</b> o que ele teme perder ou errar</li><li><b>Objeção:</b> o que o faz desistir</li><li><b>Linguagem:</b> as palavras que ele usa</li></ul>
<p><b>Simon Sinek, <i>Comece pelo Porquê</i>:</b> as pessoas compram por que você faz.<br><b>Al Ries e Jack Trout, <i>Posicionamento</i>:</b> é o lugar que você ocupa na cabeça do cliente.<br><b>Seth Godin, <i>A Vaca Roxa</i>:</b> numa estrada cheia de vacas, só a roxa faz parar.</p>
<div class="box">"Para [cliente] que [deseja/sofre], o [negócio] é [o que é] que [diferença], porque [prova]."</div>'''),
('dark','''<div class="kick">Aula 3.2 · Níveis de consciência e funil</div><h1>Nem todo mundo está <em class="g">pronto para comprar</em></h1>
<p style="font-size:22px">Os 5 níveis de consciência (Eugene Schwartz)</p>
<table><tr><th>Funil</th><th>Nível</th></tr>
<tr><td>Topo: atrair</td><td>1. Inconsciente · 2. Consciente do problema</td></tr>
<tr><td>Meio: educar e gerar desejo</td><td>3. Consciente da solução · 4. Consciente do produto</td></tr>
<tr><td>Fundo: converter</td><td>5. Totalmente consciente</td></tr></table>
<div class="box" style="margin-top:18px">Só fundo = catálogo que ninguém engaja. Só topo = seguidores sem clientes.</div>'''),
('light','''<div class="kick">Aula 3.3 · Os três níveis num só carrossel</div><h1>Um conteúdo, <em class="g">o funil inteiro</em></h1>
<table><tr><th>Cards</th><th>O que fazem</th></tr><tr><td>1 a 3 · topo</td><td>Situação e identificação ("Você evita tirar foto de perfil?")</td></tr>
<tr><td>4 a 6 · meio</td><td>Explicação, prova e a cena de desejo</td></tr><tr><td>7 · fundo</td><td>Um convite claro ("Comente AVALIAÇÃO")</td></tr></table>
<h2>As 3 regras</h2><ul><li>Cada card, uma ideia</li><li>Cada card dá vontade de ver o próximo</li><li>Uma única ação no final</li></ul>'''),
('dark','''<div class="kick">Checklist do Módulo 3</div><h1>Você aplicou <em class="g">tudo?</em></h1>
<ul><li class="ck">Respondi as 4 perguntas sobre o meu cliente</li><li class="ck">Escrevi a minha frase de posicionamento</li><li class="ck">Criei uma ideia de conteúdo para cada nível do funil</li><li class="ck">Montei o roteiro de um carrossel de 7 cards com o funil completo</li></ul>
<h2>Para ir além (leituras)</h2><p style="font-size:22px"><i>Comece pelo Porquê</i> (Simon Sinek) · <i>Posicionamento</i> (Al Ries e Jack Trout) · <i>A Vaca Roxa</i> (Seth Godin) · <i>A Estratégia do Oceano Azul</i> (W. Chan Kim e Renée Mauborgne)</p>''')],
'Resumao Modulo 3 - Estrategia.pdf')
R(4,'Ganchos <em class="g">e copy</em>','Os 2 primeiros segundos e o texto que conduz até a ação.',[
('light','''<div class="kick">Aula 4.1 · Os 2 primeiros segundos</div><h1>Você tem <em class="g">2 segundos</em></h1>
<p>O gancho funciona em 3 camadas: <b>fala + texto na tela + imagem</b>. Muita gente assiste sem som.</p>
<p><b>Chip e Dan Heath, <i>Ideias que Colam</i>:</b> ideias que ficam são inesperadas e concretas.</p>
<table><tr><th>Tipo</th><th>Exemplo</th></tr><tr><td>Situação</td><td>"Você chega em casa às 8 da noite e ainda precisa pensar no jantar."</td></tr>
<tr><td>Quebra de crença</td><td>"Beber 2 litros de água por dia não é para todo mundo."</td></tr><tr><td>Número específico</td><td>"137 noivas atendidas este ano."</td></tr>
<tr><td>Pergunta</td><td>"Você também pede desculpa quando cobra o seu preço?"</td></tr><tr><td>Bastidor</td><td>"O que acontece aqui antes das 7 da manhã."</td></tr>
<tr><td>Curiosidade</td><td>"O pedido que eu nunca tinha ouvido em 10 anos."</td></tr><tr><td>Identificação</td><td>"Se você responde cliente às 11 da noite…"</td></tr>
<tr><td>Resultado</td><td>"De 3 para 30 encomendas por semana."</td></tr></table>'''),
('dark','''<div class="kick">Aula 4.2 · Copy e CTA</div><h1>Copy não é texto bonito. <em class="g">É texto que conduz.</em></h1>
<ul><li><b>Legenda:</b> gancho na primeira linha · desenvolvimento em frases curtas · CTA</li><li><b>Carrossel:</b> capa = promessa · 1 ideia por card · o último entrega e convida</li>
<li><b>Vídeo:</b> gancho (0 a 3 s) · contexto · desenvolvimento · virada · CTA</li></ul>
<h2>A CTA certa para cada objetivo</h2><ul><li>Comente [palavra]: conversa + automação</li><li>Salve: conteúdo útil</li><li>Envie para alguém: alcance</li><li>Direct / link na bio: venda</li><li>Dark post: o botão ("Saiba mais")</li></ul>
<div class="box">Uma CTA por conteúdo.</div>'''),
('light','''<div class="kick">Aula 4.3 · Ganchos com IA</div><h1>A IA gera quantidade. <em class="g">Você escolhe a qualidade.</em></h1>
<ul><li>Peça 24 ganchos: 3 de cada um dos 8 tipos</li><li>Corte os genéricos (se serve para todo mundo, não diferencia ninguém)</li><li>Ajuste com histórias e detalhes reais do seu negócio</li><li>Converse com a IA para refinar</li></ul>
<div class="box">Nada de "descubra o segredo" ou "você sabia?". Troque por uma situação real.</div>'''),
('dark','''<div class="kick">Checklist do Módulo 4</div><h1>Você aplicou <em class="g">tudo?</em></h1>
<ul><li class="ck">Escrevi um gancho de cada um dos 8 tipos</li><li class="ck">Escrevi uma legenda completa com uma única CTA</li><li class="ck">Gerei 24 ganchos com a IA e escolhi os 5 melhores</li><li class="ck">Ajustei os ganchos com histórias reais</li></ul>
<h2>Para ir além (leituras)</h2><p style="font-size:22px"><i>Ideias que Colam</i> (Chip e Dan Heath) · <i>O Guia da Escrita Criativa</i> (Rock Content)</p>''')],
'Resumao Modulo 4 - Ganchos e copy.pdf')
R(5,'Sem cara <em class="g">de anúncio</em>','A estrutura e os casos reais de marcas que vendem sem parecer que estão vendendo.',[
('light','''<div class="kick">Aula 5.1 · A estrutura</div><h1>Os 5 passos do anúncio <em class="g">sem cara de anúncio</em></h1>
<table><tr><th>Passo</th><th>O que fazer</th></tr><tr><td>1. Gancho</td><td>Uma situação reconhecível em 2 segundos</td></tr><tr><td>2. Identificação</td><td>Um detalhe real: "isso é comigo"</td></tr>
<tr><td>3. Conflito</td><td>A tensão que prende até o fim</td></tr><tr><td>4. Virada</td><td>O produto entra como desejo ou solução</td></tr><tr><td>5. Fechamento</td><td>Bordão, virada ou próximo episódio</td></tr></table>
<p style="margin-top:14px"><b>Jonah Berger, <i>Contágio</i>:</b> compartilhamos o que dá moeda social, está ligado a gatilhos do dia a dia, gera emoção, é visível, é útil e vem numa história.</p>'''),
('dark','''<div class="kick">Aulas 5.2 a 5.5 · Os casos</div><h1>O que cada caso <em class="g">ensina</em></h1>
<table><tr><th>Caso</th><th>A lição</th></tr>
<tr><td>Toyota × Sarah Fonseca</td><td>Marketing de oportunidade: entrar num assunto que o público já vive (a promessa do carro)</td></tr>
<tr><td>Boticário × Mari Krüger</td><td>Causa com coerência: público, produto e prova. Bud Light (2023): sem coerência, vendas caíram cerca de 25%</td></tr>
<tr><td>Liquid Death</td><td>Produto comum vira desejo com posicionamento diferente (avaliada em US$ 1,4 bi em 2024)</td></tr>
<tr><td>Dove, Retratos da Real Beleza (2013)</td><td>A história carrega a mensagem; a marca aparece só no fim</td></tr></table>'''),
('light','''<div class="kick">Aula 5.6 · Trend e oportunidade</div><h1>Nem toda trend <em class="g">é para você</em></h1>
<p><b>Funcionou:</b> Burger King × Fiuk, o "ex-herdeiro" do BK Shake a R$ 10 (AlmapBBDO, 2026). Assunto do momento, rir com e não de, tom da marca, oferta simples.</p>
<h2>As 5 perguntas antes de entrar numa trend</h2><ul><li class="ck">O meu público entende a referência?</li><li class="ck">Tem a ver com a minha marca?</li><li class="ck">Ninguém vai se sentir ofendido?</li><li class="ck">Consigo fazer rápido?</li><li class="ck">De fora, não parece forçado?</li></ul>
<div class="box">Oportunidades previsíveis do seu público quase nunca queimam o filme.</div>'''),
('dark','''<div class="kick">Checklist do Módulo 5</div><h1>Você aplicou <em class="g">tudo?</em></h1>
<ul><li class="ck">Escrevi um roteiro com os 5 passos</li><li class="ck">Listei 5 assuntos que o meu público já conhece</li><li class="ck">Testei uma causa nas 5 perguntas de coerência</li><li class="ck">Listei 5 coisas que o meu setor faz igual, e como fazer diferente</li><li class="ck">Escrevi um conteúdo contra uma crença limitante do meu cliente</li><li class="ck">Mapeei 10 oportunidades para o meu negócio</li></ul>
<h2>Para ir além</h2><p style="font-size:22px"><i>Contágio</i> (Jonah Berger) · <i>Alquimia</i> (Rory Sutherland)</p>''')],
'Resumao Modulo 5 - Sem cara de anuncio.pdf')
R(6,'Os dois <em class="g">calendários</em>','Conteúdo e anúncios: objetivos, funil, CTA e IA.',[
('light','''<div class="kick">Aulas 6.1 a 6.3 · Calendário de conteúdo</div><h1>Dois calendários, <em class="g">dois objetivos</em></h1>
<table><tr><th>Calendário</th><th>Para quê</th></tr><tr><td>Conteúdo</td><td>Engajar, atrair seguidores, gerar desejo e, em alguns momentos, vender. Muda toda semana.</td></tr>
<tr><td>Anúncios</td><td>Alcançar quem não te conhece ou lembrar quem já demonstrou interesse. Roda enquanto dá resultado.</td></tr></table>
<h2>A proporção inicial no feed</h2><div class="stat"><div><strong>3</strong><span>de topo (atrair)</span></div><div><strong>2</strong><span>de meio (educar e gerar desejo)</span></div><div><strong>1</strong><span>de fundo (converter)</span></div></div>
<p>Pelo menos 1 conteúdo por semana com o funil completo + "comente [palavra]" + automação.</p>'''),
('dark','''<div class="kick">Aula 6.5 · A CTA certa</div><h1>Onde aparece <em class="g">decide a CTA</em></h1>
<table><tr><th>Onde</th><th>CTA</th></tr><tr><td>Post do feed (impulsionado ou não)</td><td>"Comente [PALAVRA]" com automação, ou "link na bio"</td></tr>
<tr><td>Dark post</td><td>O botão: "Saiba mais", "Comprar agora", "Enviar mensagem"</td></tr><tr><td>Remarketing</td><td>Fundo de funil: garantia, objeção, lembrete</td></tr></table>
<div class="box" style="margin-top:18px">Nunca escreva "link na bio" num dark post: a pessoa não está no seu perfil.</div>
<p><b>Pouca verba:</b> impulsione os posts que já engajaram, com palavra-chave e automação. Dark posts de venda e remarketing vêm depois.</p>'''),
('light','''<div class="kick">Aulas 6.4 e 6.6 · Com IA</div><h1>Os prompts-mestres <em class="g">fazem o rascunho</em></h1>
<ul><li>Conteúdo: frequência, proporção 3·2·1, funil completo semanal, datas do mês</li><li>Anúncios: verba, objetivo, criativos, onde cada um aparece e a CTA certa</li></ul>
<h2>Revise sempre</h2><ul><li class="ck">Está equilibrado entre topo, meio e fundo?</li><li class="ck">Cabe no meu tempo e na minha verba?</li><li class="ck">A CTA combina com onde o conteúdo aparece?</li><li class="ck">Tem a cara do meu negócio?</li></ul>'''),
('dark','''<div class="kick">Checklist do Módulo 6</div><h1>Você aplicou <em class="g">tudo?</em></h1>
<ul><li class="ck">Anotei o meu tempo semanal e a minha verba mensal</li><li class="ck">Classifiquei as minhas ideias em topo, meio e fundo</li><li class="ck">Escolhi os conteúdos com funil completo</li><li class="ck">Montei o meu calendário de conteúdo do mês</li><li class="ck">Decidi quais conteúdos vão para o feed e quais viram dark post</li><li class="ck">Montei o meu calendário de anúncios</li></ul>''')],
'Resumao Modulo 6 - Os dois calendarios.pdf')
R(7,'Rotina <em class="g">e plano</em>','Constância, a semana de criação e o seu Plano de 30 dias.',[
('light','''<div class="kick">Aula 7.1 · A rotina</div><h1>Constância vale mais <em class="g">do que volume</em></h1>
<p><b>Michael Gerber, <i>O Mito do Empreendedor</i>:</b> conteúdo é trabalhar <b>para</b> o negócio, não só <b>no</b> negócio.<br><b>James Clear, <i>Hábitos Atômicos</i>:</b> pequenas ações repetidas geram resultados enormes.</p>
<table><tr><th>Dia</th><th>Etapa</th></tr><tr><td>Segunda</td><td>Curadoria de referências e ideias</td></tr><tr><td>Terça</td><td>Roteiros, ganchos e legendas</td></tr><tr><td>Quarta</td><td>Gravação (em lote)</td></tr><tr><td>Quinta</td><td>Edição e artes</td></tr><tr><td>Sexta</td><td>Programação</td></tr></table>
<div class="box" style="margin-top:16px">Sem dias livres? 1 hora por dia, de segunda a sábado, sustenta 2 a 3 posts por semana.</div>'''),
('dark','''<div class="kick">Aula 7.2 · O Plano de 30 dias</div><h1>Tudo o que você construiu, <em class="g">num só lugar</em></h1>
<ul><li><b>A base:</b> ficha, cliente, posicionamento</li><li><b>O estoque:</b> histórias, ganchos, memórias afetivas, oportunidades</li><li><b>Os calendários:</b> conteúdo e anúncios</li><li><b>O plano de ação (5W2H):</b> o quê, por quê, onde, quando, quem, como, quanto</li><li><b>Os números da semana:</b> alcance, salvamentos, comentários, direct e vendas</li></ul>
<div class="box">Toda sexta: o que funcionou? O que eu repito? O que eu troco?</div>'''),
('light','''<div class="kick">Checklist final</div><h1>Você <em class="g">concluiu o Recria Ads!</em></h1>
<ul><li class="ck">Defini quantos posts cabem na minha vida pelos próximos 3 meses</li><li class="ck">Coloquei a semana de criação na agenda</li><li class="ck">Montei o meu Plano de 30 dias completo</li><li class="ck">Postei o meu primeiro conteúdo com tudo o que aprendi</li></ul>
<p>Você tem 1 ano de acesso: volte às aulas sempre que precisar.</p>
<p style="font-family:'Playfair Display';font-style:italic;font-size:28px;color:#9a7424">Parabéns!<br>Amanda, CEO da Agência Recria</p>''')],
'Resumao Modulo 7 - Rotina e plano.pdf')
