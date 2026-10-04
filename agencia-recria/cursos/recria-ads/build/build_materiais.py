from materiais_lib import *
def book(aula, titulo, sub):
    b=Book(f'Material Aula {aula} · Recria Ads', f'Recria Ads · Material da Aula {aula}')
    b.cover(f'Recria Ads · Material da Aula {aula}', titulo, sub); return b

# 0.2
b=book('0.2','Meu <em class="g">compromisso</em>','10 minutos por dia, todos os dias, com o seu negócio.')
b.page('light',f'''<div class="kick">O meu combinado</div><h1>Eu me comprometo com <em class="g">10 minutos por dia</em></h1>
<div class="q">O meu horário do Recria Ads será:</div>{lines(1)}
<div class="q">Onde vou assistir (lugar, aparelho):</div>{lines(1)}
<div class="q">O que eu quero ter aplicado no meu negócio daqui a 1 mês:</div>{lines(4)}
<div class="q">Assinatura e data:</div>{lines(1)}
<div class="box" style="margin-top:22px">Dez minutos por dia valem mais do que cinco horas num domingo que nunca chega.</div>''')
g=''.join(f'<div>Dia {i}</div>' for i in range(1,36))
b.page('light',f'''<div class="kick">Rastreador de 35 dias</div><h1>Marque cada dia em que <em class="g">você cumpriu</em></h1>
<p style="font-size:22px">Uma aula por dia. Um módulo por semana. Em cerca de 5 semanas, tudo aplicado.</p><div class="grid">{g}</div>''')
b.render(OUT+'Aula 0.2 - Meu compromisso.pdf')

# 0.3
b=book('0.3','Ficha <em class="g">Meu cenário</em>','+ o prompt "Meu mês de conteúdo" para gerar 30 ideias hoje.')
qs=['O que você vende e qual o preço médio?','Onde você vende: loja física, online ou os dois? Qual cidade?','Quem é o seu cliente: o que deseja, o que teme, o que o faz desistir de comprar?','Como o seu cliente fala: 3 frases que você mais ouve dele','Por que as pessoas compram de você e não do concorrente?','Quem pode aparecer nos conteúdos: você, equipe, clientes, influenciadores?','Quanto pode investir em anúncios por mês? (nada / até R$ 300 / R$ 300 a R$ 1.000 / mais de R$ 1.000)']
qs2=['Quantas horas por semana você consegue dedicar a criar conteúdo (pensar, escrever, gravar, editar e postar)?','Em quais redes está e com quais formatos se sente à vontade (vídeo, foto, texto, voz)?','O tom de voz da marca em 3 palavras','Datas importantes do seu negócio (sazonalidade, datas comerciais, aniversário da marca)','O seu objetivo principal nos próximos 90 dias','O seu cenário: 1. Eupresa · 2. Negócio local · 3. E-commerce · 4. Empresa média · 5. Empresa grande · 6. Serviços e consultoria · 7. Negócio digital']
b.page('light','<div class="kick">Ficha "Meu cenário" · parte 1</div>'+''.join(f'<div class="q" style="font-size:23px">{i+1}. {q}</div>{lines(2 if i!=2 else 3)}' for i,q in enumerate(qs)))
b.page('light','<div class="kick">Ficha "Meu cenário" · parte 2</div>'+''.join(f'<div class="q" style="font-size:23px">{i+8}. {q}</div>{lines(2)}' for i,q in enumerate(qs2)))
b.page('dark','''<div class="kick">🎁 Bônus · prompt "Meu mês de conteúdo"</div><h1 style="font-size:44px">Copie, cole na IA e <em class="g">complete os colchetes</em></h1>
<div class="mono">Você é um estrategista de conteúdo especializado em negócios reais, que vende sem parecer anúncio.

Com base na ficha do meu negócio abaixo, crie 30 ideias de conteúdo para o mês de [MÊS].

Regras:
- Nada de cara de anúncio. O produto entra como desejo ou solução dentro de uma situação, história ou bastidor.
- Misture: bastidor, história, educativo, prova, entretenimento e oferta indireta.
- Considere as datas comerciais de [MÊS] que fazem sentido para o meu negócio.
- Use a linguagem do meu cliente e o tom de voz da marca.
- Evite clichês como "você sabia?" e "dica do dia".
- Tenho [X] horas por semana para criar conteúdo (pensar, gravar, editar e postar). Marque com ⭐ as prioritárias que cabem nesse tempo.

Entregue em tabela: dia | formato | tema | primeira frase para prender a atenção | o que mostrar | objetivo (atrair, conectar ou vender)

FICHA DO MEU NEGÓCIO:
[cole aqui a sua ficha]</div>''')
b.page('light',f'''<div class="kick">Atividade</div><h1>As minhas <em class="g">5 ideias favoritas</em></h1>
<p>Das 30 ideias que a IA gerou, quais você manteria? Ajuste com a sua realidade.</p>{filltable(['#','Ideia','O que eu ajustaria'],5)}
<div class="box" style="margin-top:20px">A IA não conhece o seu negócio. Quem conhece é você. Guarde tudo: vamos usar no Módulo 6.</div>''')
b.render(OUT+'Aula 0.3 - Ficha Meu cenario e prompt.pdf')

# 1.1
b=book('1.1','Sistema 1 × <em class="g">Sistema 2</em>','Descubra com qual parte do cérebro o seu conteúdo está falando.')
b.page('light',f'''<div class="kick">Exercício 1 · diagnóstico</div><h1>Analise 3 posts <em class="g">antigos seus</em></h1>
{filltable(['Post (tema)','Primeira frase','Sistema 1 ou 2?'],3)}
<div class="q">Reescreva a primeira frase de um deles falando com o Sistema 1:</div>{lines(4)}''')
b.page('dark','''<div class="kick">Inspiração</div><h1>10 aberturas que falam com o <em class="g">Sistema 1</em></h1>
<table><tr><th>Negócio</th><th>Abertura</th></tr>
<tr><td>Clínica de estética</td><td>"Eu evitava tirar foto de perfil há 3 anos…"</td></tr>
<tr><td>Doceria</td><td>"A mãe chegou aqui com a foto de um bolo que ela viu aos 7 anos…"</td></tr>
<tr><td>Loja de roupas</td><td>"Ela entrou procurando um vestido e saiu com a autoestima de volta."</td></tr>
<tr><td>Borracharia</td><td>"Eram 11 da noite e a família estava a caminho do casamento da filha."</td></tr>
<tr><td>Nutricionista</td><td>"Ela não jantava com a família havia 2 anos."</td></tr>
<tr><td>Restaurante</td><td>"Esse prato nasceu de um erro na cozinha."</td></tr>
<tr><td>Consultoria</td><td>"Ele trabalhava 14 horas por dia e o lucro não aparecia."</td></tr>
<tr><td>E-commerce</td><td>"A caixa chegou e ela chorou antes de abrir."</td></tr>
<tr><td>Pet shop</td><td>"O Thor tinha medo de banho. Até semana passada."</td></tr>
<tr><td>Academia</td><td>"Ela subiu a escada do prédio sem parar pela primeira vez."</td></tr></table>''')
b.page('light',f'''<div class="kick">Exercício 2 · a sua vez</div><h1>Escreva 5 aberturas para o <em class="g">seu negócio</em></h1>
<p>Personagem + situação + emoção. Nada de ficha técnica no começo.</p>{''.join(f'<div class="q" style="font-size:22px">{i}.</div>{lines(2)}' for i in range(1,6))}''')
b.render(OUT+'Aula 1.1 - Sistema 1 x Sistema 2.pdf')

# 1.2
b=book('1.2','Mapa dos <em class="g">7 princípios</em>','Os gatilhos de Cialdini aplicados ao seu negócio, sem manipulação.')
b.page('light',f'''<div class="kick">Exercício · o seu mapa</div><h1>Como cada princípio aparece <em class="g">no seu negócio</em></h1>
<table class="fill"><tr><th>Princípio</th><th>Como vou usar esta semana</th></tr>
{''.join(f'<tr><td>{p}</td><td></td></tr>' for p in ['Reciprocidade','Compromisso e coerência','Prova social','Afeição','Autoridade','Escassez (real)','Unidade'])}</table>''')
b.page('dark','''<div class="kick">Exemplos por cenário</div><h1>Ideias para <em class="g">começar</em></h1>
<table><tr><th>Princípio</th><th>Exemplos</th></tr>
<tr><td>Reciprocidade</td><td>Dica gratuita em story · amostra · checklist de presente · aula ao vivo</td></tr>
<tr><td>Compromisso</td><td>"Comente EU QUERO" · enquete · caixinha · quiz nos stories</td></tr>
<tr><td>Prova social</td><td>Print de mensagem de cliente (com autorização) · antes e depois · fila na porta</td></tr>
<tr><td>Afeição</td><td>Bastidor · sua história · equipe · bloopers</td></tr>
<tr><td>Autoridade</td><td>Explicar o porquê · análise de erro comum · certificações mostradas na prática</td></tr>
<tr><td>Escassez</td><td>Agenda com vagas reais · lote limitado de verdade · data de fim real</td></tr>
<tr><td>Unidade</td><td>"Nós, mães empreendedoras" · linguagem do grupo · causa em comum</td></tr></table>''')
b.page('light','''<div class="kick">A linha vermelha</div><h1>Checklist de <em class="g">ética</em></h1>
<p>Antes de publicar, confira:</p>
<ul><li class="ck">A prova social é real e autorizada?</li><li class="ck">A escassez é verdadeira (a vaga, o estoque ou o prazo existem mesmo)?</li>
<li class="ck">O depoimento não foi inventado nem editado para mudar o sentido?</li><li class="ck">Os números são reais e verificáveis?</li>
<li class="ck">Eu teria orgulho se o meu cliente soubesse exatamente como fiz esse post?</li></ul>
<div class="box">Gatilho não é truque. É entender como as pessoas já decidem, e respeitar isso.</div>''')
b.render(OUT+'Aula 1.2 - Mapa dos 7 principios.pdf')

# 1.3
b=book('1.3','Da oferta direta à <em class="g">oferta indireta</em>','Gere desejo antes de pedir a compra.')
b.page('light',f'''<div class="kick">Exemplo</div><h1>Antes e <em class="g">depois</em></h1>
<table><tr><th>Oferta direta</th><th>Oferta indireta</th></tr>
<tr><td style="font-weight:400">"Bolo de ninho com morango, R$ 90. Encomende!"</td><td>A criança de olho arregalado no parabéns, a mãe emocionada, o bolo igual ao que ela imaginou.</td></tr>
<tr><td style="font-weight:400">"Contrate a nossa consultoria."</td><td>Como o cliente estava antes (14 horas por dia) e como está agora.</td></tr></table>
<div class="q">A sua oferta direta:</div>{lines(2)}<div class="q">A sua oferta indireta (a cena, a história ou o resultado):</div>{lines(5)}''')
b.page('dark',f'''<div class="kick">As 4 alavancas do desejo (Alex Hormozi)</div><h1>Como mostrar cada uma <em class="g">sem dizer "compre"</em></h1>
<table class="fill"><tr><th>Alavanca</th><th>Como mostrar no meu conteúdo</th></tr>
<tr><td>Resultado grande</td><td></td></tr><tr><td>Alta chance de dar certo</td><td></td></tr><tr><td>Pouco tempo</td><td></td></tr><tr><td>Pouco esforço</td><td></td></tr></table>
<div class="box" style="margin-top:18px">Dica: resultado de cliente, passo a passo visível, prazo real, "você faz isso, nós fazemos o resto".</div>''')
b.page('light',f'''<div class="kick">Exercício · impressão de aumento</div><h1>O que cada post <em class="g">deixa para quem vê?</em></h1>
<p>Liste 5 conteúdos que entregam valor mesmo para quem nunca vai comprar (dica, reflexão, informação útil, sorriso).</p>
{''.join(f'<div class="q" style="font-size:22px">{i}.</div>{lines(1)}' for i in range(1,6))}
<div class="q">Os meus "palcos" (pontos de contato) que preciso cuidar melhor:</div>{lines(3)}''')
b.render(OUT+'Aula 1.3 - Da oferta direta a indireta.pdf')

# 1.4
b=book('1.4','Mapa de <em class="g">memórias afetivas</em>','Mapeie 10 memórias do seu público e transforme em conteúdo.')
b.page('dark','''<div class="kick">Para puxar a memória</div><h1>Perguntas para descobrir a <em class="g">infância do seu cliente</em></h1>
<ul><li>Em que ano ele nasceu? O que passava na TV quando ele tinha 8 a 12 anos?</li><li>Que músicas, desenhos, novelas e brinquedos marcaram essa época?</li>
<li>Que doces, lanches e marcas ele comia na escola?</li><li>Que objetos, cheiros e rituais de família são dessa geração?</li>
<li>Que moda, gírias e jogos eram febre?</li></ul>
<div class="box">Pesquise "o que era sucesso em [ano]" ou pergunte na caixinha: "qual desenho marcou a sua infância?"</div>''')
b.page('light',f'''<div class="kick">Atividade</div><h1>10 memórias, <em class="g">10 ideias</em></h1>
{filltable(['#','Memória afetiva do meu público','Ideia de conteúdo ou ação'],10)}''')
b.page('dark','''<div class="kick">Inspiração por cenário</div><h1>Como usar <em class="g">na prática</em></h1>
<table><tr><th>Cenário</th><th>Ideias</th></tr>
<tr><td>Eupresa</td><td>"O que eu queria ser quando era criança" ligado ao que você faz hoje</td></tr>
<tr><td>Negócio local</td><td>O doce da porta da escola · o prato da casa da vó · a loja "como antigamente"</td></tr>
<tr><td>E-commerce</td><td>Coleção com estética dos anos 90/2000 · embalagem nostálgica · edição colecionável</td></tr>
<tr><td>Empresa média</td><td>Cartão fidelidade com carimbos temáticos · série de embalagens</td></tr>
<tr><td>Empresa grande</td><td>Parceria com uma marca ou personagem querido do público</td></tr>
<tr><td>Serviços</td><td>Explicar conceitos com cenas de filmes, séries ou desenhos da época</td></tr>
<tr><td>Negócio digital</td><td>Aula ou e-book com referências da época · live temática · bônus nostálgico</td></tr></table>''')
b.render(OUT+'Aula 1.4 - Mapa de memorias afetivas.pdf')

# 2.1
b=book('2.1','As minhas <em class="g">3 histórias</em>','Personagem, conflito e transformação.')
pg=''.join(f'<div class="q">História {i}</div><table class="fill"><tr><th>Personagem</th><th>Conflito</th><th>Transformação</th></tr><tr><td></td><td></td><td></td></tr></table><div class="q" style="font-size:21px">Em uma frase:</div>{lines(1)}' for i in range(1,4))
b.page('light','<div class="kick">Atividade</div><h1>Escreva 3 histórias <em class="g">reais</em></h1>'+pg)
b.page('dark','''<div class="kick">Exemplo</div><h1>Relato × <em class="g">história</em></h1>
<table><tr><th>Só relato</th><th>História</th></tr>
<tr><td style="font-weight:400;color:#e9e4da">"Fui à padaria e comprei pão."</td><td>"Fui à padaria e a única pessoa na fila era o meu ex."</td></tr>
<tr><td style="font-weight:400;color:#e9e4da">"Atendemos uma cliente hoje."</td><td>"A cliente chegou dizendo que já tinha tentado de tudo, e saiu daqui chorando de alegria."</td></tr></table>
<div class="box" style="margin-top:20px">Sem conflito, não tem história. Só tem relato.</div>''')
b.render(OUT+'Aula 2.1 - As minhas 3 historias.pdf')

# 2.2
b=book('2.2','Herói, guia e <em class="g">loop aberto</em>','Reescreva a sua história com o cliente no centro.')
b.page('light',f'''<div class="kick">Exercício 1 · o herói</div><h1>O cliente é o herói, <em class="g">você é o guia</em></h1>
<div class="q">Quem é o herói (o cliente) e o que ele quer?</div>{lines(2)}<div class="q">Qual problema ele enfrenta?</div>{lines(2)}
<div class="q">Como você entra como guia (o plano, a ajuda)?</div>{lines(2)}<div class="q">Como ele termina transformado?</div>{lines(2)}
<div class="q">A sua primeira frase, abrindo um loop:</div>{lines(2)}''')
b.page('dark','''<div class="kick">15 modelos de frases que abrem loop</div><h1>Complete com o <em class="g">seu negócio</em></h1>
<ul style="columns:1"><li>"O cliente chegou com um pedido que eu nunca tinha ouvido em [X] anos…"</li><li>"Eu quase desisti do negócio no dia em que…"</li>
<li>"Ninguém te conta isso sobre [seu nicho]…"</li><li>"O erro que me custou [algo] e que você pode evitar…"</li><li>"Ela entrou aqui por um motivo e saiu por outro completamente diferente."</li>
<li>"Parte 1: o dia em que tudo deu errado."</li><li>"Eu achava que [crença]. Até que…"</li><li>"O que acontece aqui antes das 7 da manhã…"</li>
<li>"A pergunta que eu mais recebo, e a resposta que ninguém espera."</li><li>"Esse [produto] quase não existiu."</li><li>"O que o [cliente] me disse no fim do atendimento me fez parar tudo."</li>
<li>"3 coisas que eu faria diferente se começasse hoje. A terceira é a mais importante."</li><li>"Todo mundo faz [X]. Nós decidimos fazer o contrário."</li>
<li>"Eu não ia postar isso, mas…"</li><li>"No fim deste vídeo, você vai entender por que…"</li></ul>''')
b.render(OUT+'Aula 2.2 - Heroi guia e loop aberto.pdf')

# 2.3
b=book('2.3','O meu <em class="g">Banco de Histórias</em>','8 tipos de história que todo negócio tem.')
tipos=[('Origem','Como tudo começou? Qual foi o primeiro cliente?'),('O porquê','O que te move além do dinheiro?'),('Bastidor','Como o produto ou serviço é feito?'),('O erro','O que deu errado e o que você aprendeu?'),('O cliente','Qual foi o antes e o depois de alguém que comprou?'),('A equipe','Quem está por trás? Qual a história de cada um?'),('O dia a dia','Que rotina o cliente nunca vê?'),('O inimigo','O que o seu negócio combate?')]
for part in (tipos[:4],tipos[4:]):
    b.page('light','<div class="kick">Banco de Histórias</div>'+''.join(f'<div class="q">{t}</div><p style="font-size:21px;margin:0">{p}</p>{lines(3)}' for t,p in part))
b.render(OUT+'Aula 2.3 - Banco de Historias.pdf')

# 2.4
b=book('2.4','Diário de <em class="g">7 dias</em>','Documente o seu negócio e nunca mais fique sem conteúdo.')
b.page('dark','''<div class="kick">O método</div><h1>Capturar sem <em class="g">parar a rotina</em></h1>
<ul><li class="ck">Criei o álbum "Conteúdo" no celular</li><li class="ck">Criei a nota "Banco de ideias"</li></ul>
<h2>As 3 tomadas (15 segundos)</h2><ul><li>Plano aberto: o ambiente</li><li>Detalhe: mãos, produto, objeto</li><li>Rosto: a sua reação ou a de alguém da equipe</li></ul>
<h2>As 4 perguntas</h2><ul><li>O que deu errado?</li><li>O que me surpreendeu?</li><li>O que o cliente me perguntou?</li><li>O que ninguém vê?</li></ul>''')
b.page('light',f'''<div class="kick">Diário de 7 dias</div><h1>Um momento <em class="g">por dia</em></h1>{filltable(['Dia','O momento','Qual pergunta ele responde?'],7)}''')
b.page('light',f'''<div class="kick">1 momento → 3 conteúdos</div><h1>Escolha o melhor momento <em class="g">da semana</em></h1>
<div class="q">O momento:</div>{lines(2)}<div class="q">📱 Story (o que mostrar e o texto):</div>{lines(3)}<div class="q">🎬 Reels (a primeira frase e a sequência):</div>{lines(3)}<div class="q">🗂️ Carrossel (capa + ideia de cada card):</div>{lines(3)}''')
b.render(OUT+'Aula 2.4 - Diario de 7 dias.pdf')
