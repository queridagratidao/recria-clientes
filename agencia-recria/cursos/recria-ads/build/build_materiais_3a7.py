from materiais_lib import *
def book(aula,titulo,sub):
    b=Book(f'Material Aula {aula} · Recria Ads',f'Recria Ads · Material da Aula {aula}'); b.cover(f'Recria Ads · Material da Aula {aula}',titulo,sub); return b
def q(t,n=2): return f'<div class="q" style="font-size:23px">{t}</div>{lines(n)}'

# 3.1
b=book('3.1','Cliente e <em class="g">posicionamento</em>','Quem é o seu cliente de verdade e por que ele deveria escolher você.')
b.page('light','<div class="kick">O seu cliente</div><h1>As 4 <em class="g">perguntas</em></h1>'+q('1. O que ele deseja? (o resultado, não o produto)',3)+q('2. O que ele teme?',3)+q('3. O que faz ele desistir de comprar?',3)+q('4. Quais palavras e frases ele usa?',3))
b.page('dark',f'''<div class="kick">O seu posicionamento</div><h1>Complete a <em class="g">sua frase</em></h1>
<div class="box">"Para [cliente] que [deseja ou sofre com], o [negócio] é [o que você é] que [o que faz de diferente], porque [a sua prova]."</div>
<p style="font-size:22px">Exemplo: "Para mães que querem uma festa linda sem estresse, a Doce Afeto é a doceria de bairro que entrega o bolo exatamente igual à foto, porque cada bolo é aprovado por foto antes da entrega."</p>
<div class="q">O meu porquê (o que me move além do dinheiro):</div>{lines(2)}<div class="q">A minha frase de posicionamento:</div>{lines(4)}''')
b.render(OUT+'Aula 3.1 - Cliente e posicionamento.pdf')
# 3.2
b=book('3.2','Um conteúdo para <em class="g">cada nível</em>','Topo, meio e fundo de funil para o seu negócio.')
b.page('light',f'''<div class="kick">Exemplo · nutricionista</div><h1>Os níveis <em class="g">na prática</em></h1>
<table><tr><th>Funil</th><th>Conteúdo</th></tr><tr><td>Topo</td><td>"Por que você sente sono depois do almoço, mesmo dormindo 8 horas?"</td></tr>
<tr><td>Meio</td><td>"3 trocas simples no almoço que acabam com o sono da tarde" + depoimento</td></tr><tr><td>Fundo</td><td>"Abri 5 horários de consulta este mês. Comente CONSULTA."</td></tr></table>
<h2 style="margin-top:22px">A sua vez</h2>{filltable(['Funil','A minha ideia de conteúdo'],3)}''')
b.render(OUT+'Aula 3.2 - Um conteudo para cada nivel.pdf')
# 3.3
b=book('3.3','Carrossel com o <em class="g">funil completo</em>','Modelo de 7 cards para preencher.')
b.page('light',f'''<div class="kick">Modelo</div><h1>O seu carrossel <em class="g">de 7 cards</em></h1>
<table class="fill"><tr><th>Card</th><th>O que escrever</th></tr>
<tr><td>1 · topo</td><td></td></tr><tr><td>2 · topo (identificação)</td><td></td></tr><tr><td>3 · topo (identificação)</td><td></td></tr>
<tr><td>4 · meio (explicação)</td><td></td></tr><tr><td>5 · meio (prova)</td><td></td></tr><tr><td>6 · meio (cena de desejo)</td><td></td></tr><tr><td>7 · fundo (1 ação)</td><td></td></tr></table>''')
b.render(OUT+'Aula 3.3 - Carrossel com funil completo.pdf')
# 4.1
b=book('4.1','Os 8 tipos <em class="g">de gancho</em>','Escreva um gancho de cada tipo para o seu negócio.')
b.page('light','<div class="kick">Atividade</div><h1>Os meus <em class="g">8 ganchos</em></h1>'+''.join(q(t,1) for t in ['Situação','Quebra de crença','Número específico','Pergunta','Bastidor','Curiosidade (loop aberto)','Identificação','Resultado']))
b.page('dark','''<div class="kick">Checklist do gancho</div><h1>Antes de <em class="g">publicar</em></h1>
<ul><li class="ck">Está na fala, no texto da tela e na imagem?</li><li class="ck">Funciona sem som?</li><li class="ck">Tem movimento ou algo inesperado no primeiro segundo?</li><li class="ck">É concreto (dá para visualizar)?</li><li class="ck">O conteúdo cumpre o que o gancho promete?</li></ul>
<div class="box">Gancho que não cumpre a promessa é clickbait, e clickbait destrói a confiança.</div>''')
b.render(OUT+'Aula 4.1 - Os 8 tipos de gancho.pdf')
# 4.2
b=book('4.2','Modelos <em class="g">de copy</em>','Legenda, carrossel, roteiro de vídeo e a CTA certa.')
b.page('light',f'''<div class="kick">Modelo 1 · legenda</div><h1>Legenda que <em class="g">conduz</em></h1>{q('Primeira linha (gancho, aparece antes do "mais"):',2)}{q('Desenvolvimento (frases e parágrafos curtos):',6)}{q('Uma única CTA:',1)}''')
b.page('light',f'''<div class="kick">Modelo 2 · roteiro de vídeo</div><h1>Os 5 tempos <em class="g">do vídeo</em></h1>
<table class="fill"><tr><th>Tempo</th><th>O que falar e mostrar</th></tr><tr><td>Gancho (0 a 3 s)</td><td></td></tr><tr><td>Contexto</td><td></td></tr><tr><td>Desenvolvimento</td><td></td></tr><tr><td>Virada</td><td></td></tr><tr><td>CTA</td><td></td></tr></table>''')
b.page('dark','''<div class="kick">A CTA certa</div><h1>Para cada objetivo, <em class="g">uma ação</em></h1>
<table><tr><th>CTA</th><th>Quando usar</th></tr><tr><td>Comente [palavra]</td><td>Gerar conversa; com automação, entregar material e ofertar no direct</td></tr>
<tr><td>Salve</td><td>Conteúdo útil, para consultar depois</td></tr><tr><td>Envie para alguém</td><td>Alcançar novas pessoas</td></tr><tr><td>Direct / link na bio</td><td>Levar para a conversa e a venda</td></tr><tr><td>Botão (dark post)</td><td>Anúncio que não aparece no perfil</td></tr></table>
<div class="box" style="margin-top:16px">Uma CTA por conteúdo. E no tom da sua marca.</div>''')
b.render(OUT+'Aula 4.2 - Modelos de copy e CTA.pdf')
# 4.3
b=book('4.3','Prompt e <em class="g">banco de ganchos</em>','Gere 24 ganchos com IA e use os modelos por tipo.')
b.page('dark','''<div class="kick">Prompt de ganchos</div><h1 style="font-size:44px">Copie, cole na IA e <em class="g">complete</em></h1><div class="mono">Você é um especialista em ganchos para redes sociais. Com base no meu negócio abaixo, crie 24 ganchos para os primeiros 2 segundos de um vídeo ou para a capa de um carrossel.

Crie 3 ganchos de cada tipo: situação, quebra de crença, número específico, pergunta, bastidor, curiosidade, identificação e resultado.

Use a linguagem do meu cliente. Nada de clichês como "você sabia" ou "descubra o segredo". Cada gancho com no máximo 12 palavras.

MEU NEGÓCIO:
[cole aqui a sua Ficha "Meu cenário"]</div>''')
BANCO=[('Situação','"Você [situação do dia a dia do cliente] e ainda precisa [problema]."'),('Quebra de crença','"[Crença comum do seu setor] não é para todo mundo."'),('Número específico','"[Número] [clientes/pedidos/anos] depois, aprendi que…"'),('Pergunta','"Você também [comportamento que o cliente tem e não admite]?"'),('Bastidor','"O que acontece aqui antes de [momento que o cliente não vê]."'),('Curiosidade','"O pedido que eu nunca tinha ouvido em [X] anos."'),('Identificação','"Se você é [perfil do cliente] e [situação], isso é para você."'),('Resultado','"De [antes] para [depois] em [tempo]. Olha como."')]
b.page('light','<div class="kick">Banco de ganchos · modelos</div><h1>Complete com o <em class="g">seu negócio</em></h1><table><tr><th>Tipo</th><th>Modelo</th></tr>'+''.join(f'<tr><td>{a}</td><td style="font-weight:400">{c}</td></tr>' for a,c in BANCO)+'</table>')
EX=[('Eupresa','"Eu atendo, produzo e entrego sozinha. E foi isso que me fez parar de vender barato."'),('Negócio local','"A dona Maria vem aqui toda sexta há 8 anos. Hoje eu descobri o porquê."'),('E-commerce','"A caixa chegou e ela chorou antes de abrir."'),('Empresa média','"Perguntei para a nossa equipe o pedido mais difícil do ano."'),('Empresa grande','"O que 200 pessoas fazem aqui antes das 8 da manhã."'),('Serviços e consultoria','"O cliente chegou dizendo que já tinha tentado de tudo."'),('Negócio digital','"Eu quase desisti de gravar esse curso. E ainda bem que não desisti."')]
b.page('dark','<div class="kick">Banco de ganchos · por cenário</div><h1>Um gancho para <em class="g">cada cenário</em></h1><table><tr><th>Cenário</th><th>Gancho</th></tr>'+''.join(f'<tr><td>{a}</td><td>{c}</td></tr>' for a,c in EX)+'</table>')
b.page('light','<div class="kick">Atividade</div><h1>Os meus <em class="g">5 melhores ganchos</em></h1>'+filltable(['#','Gancho da IA','Versão ajustada com uma história real'],5))
b.render(OUT+'Aula 4.3 - Prompt e banco de ganchos.pdf')
# 5.1
b=book('5.1','Roteiro em <em class="g">5 passos</em>','O modelo do conteúdo e anúncio sem cara de anúncio.')
b.page('light','<div class="kick">Modelo</div><h1>O seu roteiro <em class="g">sem cara de anúncio</em></h1><table class="fill"><tr><th>Passo</th><th>O que acontece</th></tr><tr><td>1. Gancho</td><td></td></tr><tr><td>2. Identificação</td><td></td></tr><tr><td>3. Conflito</td><td></td></tr><tr><td>4. Virada (o produto entra)</td><td></td></tr><tr><td>5. Fechamento</td><td></td></tr></table>')
b.page('dark','''<div class="kick">Checklist · Contágio (Jonah Berger)</div><h1>O seu conteúdo <em class="g">tem o que faz compartilhar?</em></h1>
<ul><li class="ck"><b>Moeda social:</b> quem compartilha parece interessante?</li><li class="ck"><b>Gatilho:</b> está ligado a algo do dia a dia do público?</li><li class="ck"><b>Emoção:</b> faz rir, emocionar ou indignar?</li><li class="ck"><b>Público:</b> as pessoas veem outras participando?</li><li class="ck"><b>Valor prático:</b> é útil?</li><li class="ck"><b>História:</b> a mensagem viaja dentro de uma história?</li></ul>''')
b.render(OUT+'Aula 5.1 - Roteiro em 5 passos.pdf')
# 5.2
b=book('5.2','Assuntos que o seu <em class="g">público já vive</em>','A lógica da Toyota × Sarah Fonseca aplicada ao seu negócio.')
b.page('light',f'''<div class="kick">Atividade</div><h1>5 "promessas" ou assuntos <em class="g">que todo o seu público conhece</em></h1>
<p style="font-size:22px">Exemplos: a promessa do carro na faculdade · a volta às aulas · a dieta que começa na segunda · o "dá para fazer mais barato?"</p>{filltable(['#','O assunto','Como o meu produto entra na virada'],5)}''')
b.render(OUT+'Aula 5.2 - Assuntos que o publico ja vive.pdf')
# 5.3
b=book('5.3','A bandeira certa <em class="g">para o seu negócio</em>','Teste a coerência antes de levantar uma causa.')
b.page('light',f'''<div class="kick">As 5 perguntas</div><h1>A causa <em class="g">passa no teste?</em></h1>{q('A causa:',1)}
<ul><li class="ck">O meu público se importa com isso de verdade?</li><li class="ck">Tem a ver com o que eu vendo?</li><li class="ck">Consigo provar com ação, não só com post?</li><li class="ck">Consigo sustentar por meses, não por um dia?</li><li class="ck">Estou preparado(a) para quem discordar?</li></ul>
{q('Se passou nas 5, a ideia de conteúdo:',4)}''')
b.render(OUT+'Aula 5.3 - A bandeira certa.pdf')
# 5.4
b=book('5.4','A sua <em class="g">vaca roxa</em>','O que todo mundo do seu setor faz igual, e como você pode fazer diferente.')
b.page('light','<div class="kick">Atividade</div><h1>Igual a todo mundo × <em class="g">do meu jeito</em></h1>'+filltable(['#','O que todo mundo do setor faz igual','Como eu posso fazer diferente'],5)+'<p style="margin-top:14px;font-size:22px">Pense em: tom de voz, estética, humor, embalagem, atendimento, experiência, nome dos produtos.</p>')
b.render(OUT+'Aula 5.4 - A sua vaca roxa.pdf')
# 5.5
b=book('5.5','Mais capaz <em class="g">do que pensa</em>','Um conteúdo contra a crença limitante do seu cliente.')
b.page('light',f'''<div class="kick">Atividade</div><h1>A crença limitante <em class="g">do seu cliente</em></h1>
<p style="font-size:22px">Exemplos: "não entendo de finanças" · "não levo jeito para cozinhar" · "é tarde demais para aprender" · "isso é só para quem tem dinheiro"</p>
{q('A crença que o meu cliente tem sobre si mesmo:',2)}{q('A pessoa real que prova o contrário (cliente, aluno, equipe):',2)}{q('O roteiro nos 5 passos:',6)}''')
b.render(OUT+'Aula 5.5 - Mais capaz do que pensa.pdf')
# 5.6
b=book('5.6','Mapa de <em class="g">oportunidades</em>','Mapeie 10 oportunidades de marketing para o seu negócio.')
b.page('light','<div class="kick">Atividade</div><h1>10 oportunidades <em class="g">para o meu negócio</em></h1><p style="font-size:21px">Datas comerciais, assuntos recorrentes do setor, situações que o público sempre vive, assuntos do momento.</p>'+filltable(['#','Oportunidade','Quando','Ideia de conteúdo'],10))
b.page('dark','''<div class="kick">Checklist de trend</div><h1>Antes de entrar <em class="g">numa trend</em></h1>
<ul><li class="ck">O meu público entende essa referência?</li><li class="ck">Tem a ver com a minha marca e com o que eu vendo?</li><li class="ck">Ninguém vai se sentir ofendido ou ridicularizado?</li><li class="ck">Consigo fazer em poucos dias?</li><li class="ck">Se eu visse de fora, acharia forçado? (tem que ser "não")</li></ul>
<div class="box">Passou nas 5? Vai com tudo. Não passou? Tudo bem, você não precisa entrar em todas.</div>''')
b.render(OUT+'Aula 5.6 - Mapa de oportunidades.pdf')
# 6.1
b=book('6.1','Os seus <em class="g">dois números</em>','Tempo e verba: o que guia os seus calendários.')
b.page('light',f'''<div class="kick">Atividade</div><h1>Tempo e <em class="g">verba</em></h1>{q('Horas por semana que eu tenho para conteúdo:',1)}{q('Quantos posts no feed por semana cabem nesse tempo:',1)}{q('Verba mensal para anúncios (pode ser zero):',1)}{q('O meu principal objetivo nos próximos 30 dias:',2)}
<div class="box" style="margin-top:18px">Referência: 1 post leva de 1 a 2 horas com prática. 3 h/semana → 2 posts · 5 h/semana → 3 posts.</div>''')
b.render(OUT+'Aula 6.1 - Os seus dois numeros.pdf')
# 6.2 + 6.3
b=book('6.2 e 6.3','O funil <em class="g">no feed</em>','Classifique as suas ideias e escolha as de funil completo.')
b.page('light','<div class="kick">Atividade</div><h1>As minhas ideias <em class="g">por nível</em></h1>'+filltable(['Ideia','Topo, meio, fundo ou funil completo?','Objetivo'],10))
b.render(OUT+'Aula 6.2 e 6.3 - O funil no feed.pdf')
# 6.4 / 6.6 prompts + calendários prontos
b=book('6.4 e 6.6','Prompts-mestres e <em class="g">calendários prontos</em>','Conteúdo e anúncios para os 7 cenários.')
b.page('dark','''<div class="kick">Prompt-mestre · conteúdo</div><h1 style="font-size:40px">Calendário de <em class="g">conteúdo do feed</em></h1><div class="mono">Você é um estrategista de conteúdo. Monte o calendário de conteúdo do feed para o mês de [MÊS], para o negócio da ficha abaixo.

Eu posto [X] vezes por semana. Use a proporção de 3 conteúdos de topo, 2 de meio e 1 de fundo a cada 6. Pelo menos um conteúdo por semana deve ter o funil completo, terminando com a palavra-chave [PALAVRA].

Considere as datas comerciais do mês. Nada de cara de anúncio.

Para cada conteúdo, entregue em tabela: data | formato | nível do funil | objetivo | gancho | resumo | CTA

FICHA + GANCHOS + HISTÓRIAS:
[cole aqui]</div>''')
b.page('dark','''<div class="kick">Prompt-mestre · anúncios</div><h1 style="font-size:40px">Calendário de <em class="g">anúncios</em></h1><div class="mono">Você é um gestor de tráfego. Monte o calendário de anúncios de [MÊS] para o negócio abaixo.

Verba total do mês: [VALOR]. Objetivo principal: [OBJETIVO]. Criativos disponíveis: [LISTA].

Para cada anúncio, diga se ele vai para o feed impulsionado ou se roda como dark post, e escreva a CTA certa: palavra-chave ou link na bio para o feed; botão ("Saiba mais", "Enviar mensagem") para o dark post.

Entregue em tabela: semana | campanha | nível do funil | público | criativo | onde aparece | CTA | verba da semana | quando trocar o criativo

MEU NEGÓCIO + CALENDÁRIO DE CONTEÚDO:
[cole aqui]</div>''')
CEN=[('Eupresa · confeiteira que faz tudo sozinha','BOLO',[('Seg','Reels','Topo','"Eu atendo, faço e entrego sozinha. Olha o meu sábado."','Envie para uma amiga'),('Qua','Carrossel','Meio','"3 erros que fazem o bolo chegar torto na festa"','Salve'),('Sex','Carrossel','Funil completo','"A mãe chegou com a foto de um bolo que viu aos 7 anos"','Comente BOLO'),('Seg','Reels','Topo','"O pedido mais inusitado da semana"','Envie para alguém'),('Qua','Stories + post','Meio','Bastidor da montagem + depoimento','Responda a enquete'),('Sex','Post','Fundo','"Agenda de dezembro aberta: 8 datas"','Comente BOLO')],'Verba zero: só orgânico. Pequena (R$ 100 a 300): impulsionar o carrossel de sexta para engajamento no raio da cidade.'),
('Negócio local · clínica de estética','AVALIAÇÃO',[('Seg','Reels','Topo','"Você evita tirar foto de perfil?"','Envie para alguém'),('Qua','Carrossel','Meio','"Olheira, textura ou flacidez: o que é cada uma"','Salve'),('Sex','Carrossel','Funil completo','"Ela não tirava foto havia 3 anos"','Comente AVALIAÇÃO'),('Seg','Reels','Topo','"O que ninguém te conta antes do primeiro procedimento"','Envie'),('Qua','Post','Meio','Antes e depois autorizado + explicação','Salve'),('Sex','Reels','Fundo','"Abrimos 6 horários de avaliação este mês"','Comente AVALIAÇÃO')],'Pequena: impulsionar o funil completo num raio de 5 a 10 km. Maior: dark post com "Enviar mensagem" + remarketing de quem assistiu 50% dos reels.'),
('E-commerce · loja de roupas online','PROVADOR',[('Seg','Reels','Topo','"Cheguei na festa e dei de cara com o mesmo vestido"','Envie'),('Qua','Carrossel','Meio','"Como acertar o tamanho comprando online"','Salve'),('Sex','Carrossel','Funil completo','"O vestido que foi para a formatura e voltou para o casamento"','Comente PROVADOR'),('Seg','Reels','Topo','"Abrindo as caixas da nova coleção"','Envie'),('Qua','Post','Meio','Clientes reais usando as peças','Salve'),('Sex','Carrossel','Fundo','"Frete grátis até domingo"','Link na bio')],'Pequena: impulsionar os reels com mais salvamentos. Maior: dark post de catálogo com "Comprar agora" + remarketing de carrinho abandonado.'),
('Empresa média · rede de academias','TREINO',[('Seg','Reels','Topo','"Ela subiu a escada do prédio sem parar pela primeira vez"','Envie'),('Qua','Carrossel','Meio','"Treino de 30 minutos para quem não tem tempo"','Salve'),('Sex','Reels','Funil completo','Um dia na vida de uma aluna real + convite','Comente TREINO'),('Seg','Reels','Topo','Bastidor da equipe antes da academia abrir','Envie'),('Qua','Carrossel','Meio','"Mitos da musculação depois dos 40"','Salve'),('Sex','Post','Fundo','"Aula experimental gratuita esta semana"','Comente TREINO')],'Pequena: impulsionar por unidade, no raio de cada academia. Maior: microinfluenciadores locais + dark post "Saiba mais" + remarketing.'),
('Empresa grande · marca de cosméticos','PELE',[('Seg','Reels','Topo','Série com criadora de conteúdo: episódio 1','Envie'),('Qua','Carrossel','Meio','"O que a ciência diz sobre a pele no inverno"','Salve'),('Sex','Reels','Funil completo','Episódio 2 da série, com o produto na virada','Comente PELE'),('Seg','Reels','Topo','Trend com critério (passou nas 5 perguntas)','Envie'),('Qua','Carrossel','Meio','Bastidor do laboratório','Salve'),('Sex','Post','Fundo','Lançamento com condição especial','Link na bio')],'Topo com alcance e vídeos de criadoras (branded content); meio com tráfego para conteúdo; fundo com dark posts "Comprar agora" e remarketing.'),
('Serviços e consultoria · contabilidade para pequenas empresas','CONTADOR',[('Seg','Reels','Topo','"O imposto que você paga sem saber"','Envie para um sócio'),('Qua','Carrossel','Meio','"MEI, Simples ou Presumido: qual é o seu?"','Salve'),('Sex','Carrossel','Funil completo','"O cliente chegou com 3 anos de impostos atrasados"','Comente CONTADOR'),('Seg','Reels','Topo','"O que eu faria se abrisse uma empresa hoje"','Envie'),('Qua','Post','Meio','Depoimento de cliente','Salve'),('Sex','Post','Fundo','"Diagnóstico fiscal gratuito para 5 empresas"','Comente CONTADOR')],'Pequena: impulsionar o funil completo para donos de negócio da região. Maior: dark post com "Enviar mensagem" + remarketing de quem salvou os carrosséis.'),
('Negócio digital · mentora de finanças','MENTORIA',[('Seg','Reels','Topo','"O erro de dinheiro que eu cometi aos 25 anos"','Envie'),('Qua','Carrossel','Meio','"3 planilhas que eu uso todo mês"','Salve'),('Sex','Carrossel','Funil completo','"Ela achava que não entendia de finanças"','Comente MENTORIA'),('Seg','Reels','Topo','Bastidor da gravação de uma aula','Envie'),('Qua','Stories + post','Meio','Resultado de aluna + caixinha de dúvidas','Responda a caixinha'),('Sex','Post','Fundo','"Turma aberta até domingo"','Comente MENTORIA')],'Pequena: impulsionar o funil completo com automação. Maior: dark post com "Saiba mais" para a página + remarketing de quem assistiu 50% dos vídeos.')]
for nome,pal,rows,ads in CEN:
    tb='<table><tr><th>Dia</th><th>Formato · funil</th><th>Gancho / tema</th><th>CTA</th></tr>'+''.join(f'<tr><td>{d}</td><td style="font-weight:400">{f} · {n}</td><td style="font-weight:400">{g}</td><td style="font-weight:400">{c}</td></tr>' for d,f,n,g,c in rows)+'</table>'
    b.page('light',f'<div class="kick">Calendário pronto · 2 semanas</div><h1 style="font-size:40px">{nome}</h1><p style="font-size:20px">Palavra-chave da automação: <b>{pal}</b> · 3 posts por semana</p>{tb.replace("font-size:21px","")}<div class="box" style="font-size:22px;margin-top:14px">Anúncios · {ads}</div>')
b.render(OUT+'Aula 6.4 e 6.6 - Prompts e calendarios prontos.pdf')
# 6.5
b=book('6.5','Feed ou <em class="g">dark post?</em>','Escolha o caminho de cada anúncio e a CTA certa.')
b.page('dark','''<div class="kick">A regra</div><h1>Onde aparece <em class="g">decide a CTA</em></h1><table><tr><th>Onde</th><th>CTA</th></tr><tr><td>Post do feed</td><td>"Comente [PALAVRA]" com automação, ou "link na bio"</td></tr><tr><td>Dark post</td><td>O botão: "Saiba mais", "Comprar agora", "Enviar mensagem"</td></tr><tr><td>Remarketing</td><td>Garantia, quebra de objeção, lembrete</td></tr></table>
<div class="box" style="margin-top:18px">Nunca "link na bio" num dark post.</div>''')
b.page('light','<div class="kick">Atividade</div><h1>3 conteúdos que <em class="g">viram anúncio</em></h1>'+filltable(['Conteúdo','Feed impulsionado ou dark post?','A CTA'],3))
b.render(OUT+'Aula 6.5 - Feed ou dark post.pdf')
# 7.1
b=book('7.1','A minha <em class="g">rotina de criação</em>','A semana de criação e a versão de 1 hora por dia.')
b.page('light',f'''<div class="kick">Modelo · semana de criação</div><h1>A minha semana</h1><table class="fill"><tr><th>Dia</th><th>Etapa</th><th>Horário</th></tr>
<tr><td>Segunda</td><td>Curadoria</td><td></td></tr><tr><td>Terça</td><td>Roteiros</td><td></td></tr><tr><td>Quarta</td><td>Gravação em lote</td><td></td></tr><tr><td>Quinta</td><td>Edição</td><td></td></tr><tr><td>Sexta</td><td>Programação</td><td></td></tr></table>
{q('Quantos posts por semana vou sustentar pelos próximos 3 meses:',1)}''')
b.page('dark','''<div class="kick">Versão de 1 hora por dia</div><h1>Segunda a <em class="g">sábado</em></h1><table><tr><th>Dia</th><th>A sua hora</th></tr><tr><td>Segunda</td><td>Curadoria e ideias</td></tr><tr><td>Terça</td><td>Roteiros</td></tr><tr><td>Quarta</td><td>Gravação</td></tr><tr><td>Quinta</td><td>Edição</td></tr><tr><td>Sexta</td><td>Programação</td></tr><tr><td>Sábado</td><td>Stories, respostas e números da semana</td></tr></table>''')
b.render(OUT+'Aula 7.1 - Minha rotina de criacao.pdf')
# 7.2
b=book('7.2','O meu Plano <em class="g">de 30 dias</em>','Tudo o que você construiu no curso, num só lugar.')
b.page('light',f'''<div class="kick">Parte 1 · a base</div><h1>A base do <em class="g">meu plano</em></h1>{q('O meu cenário:',1)}{q('O meu cliente (desejo, medo, objeção):',3)}{q('A minha frase de posicionamento:',3)}{q('A palavra-chave da minha automação:',1)}''')
b.page('light',f'''<div class="kick">Parte 2 · o estoque</div><h1>O meu <em class="g">estoque de conteúdo</em></h1>{q('As 3 melhores histórias do meu banco:',3)}{q('Os 5 melhores ganchos:',3)}{q('As oportunidades do mês:',2)}''')
b.page('light','<div class="kick">Parte 3 · plano de ação (5W2H)</div><h1>A minha <em class="g">primeira semana</em></h1>'+filltable(['O quê','Por quê','Onde','Quando','Quem','Como','Quanto'],6))
b.page('light','<div class="kick">Parte 4 · os números da semana</div><h1>Toda sexta, <em class="g">olhe os números</em></h1>'+filltable(['Semana','Alcance','Salvamentos','Comentários','Direct','Vendas'],4)+q('O que funcionou? O que eu repito? O que eu troco?',4))
b.render(OUT+'Aula 7.2 - Meu Plano de 30 dias.pdf')
# 7.3 Acervo Recria
b=book('7.3','Acervo <em class="g">Recria</em>','Os livros e as referências por trás da metodologia.')
LIV=[('1','<i>Rápido e Devagar</i>','Daniel Kahneman','Como o cérebro decide: a emoção vem antes da razão'),('2','<i>As Armas da Persuasão</i>','Robert Cialdini','Os 7 princípios da influência, sem manipulação'),('3','<i>StoryBrand</i>','Donald Miller','O cliente é o herói; a marca é o guia'),('4','<i>Comece pelo Porquê</i>','Simon Sinek','As pessoas compram o porquê'),('5','<i>A Vaca Roxa</i>','Seth Godin','Seja notável ou seja invisível'),('6','<i>Ideias que Colam</i>','Chip e Dan Heath','Por que algumas ideias ficam na cabeça'),('7','<i>Contágio</i>','Jonah Berger','Por que as pessoas compartilham'),('8','<i>Mostre seu Trabalho!</i>','Austin Kleon','Documentar é mais fácil do que criar'),('9','<i>Hábitos Atômicos</i>','James Clear','Constância em pequenas doses'),('10','<i>O Mito do Empreendedor</i>','Michael Gerber','Trabalhar para o negócio, não só no negócio'),('11','<i>Sapiens</i>','Yuval Noah Harari','O poder das histórias compartilhadas'),('12','<i>Ofertas de US$ 100 milhões</i>','Alex Hormozi','A equação de valor de uma oferta')]
b.page('light','<div class="kick">Os livros · na ordem de leitura sugerida</div><h1>A estante <em class="g">do Recria Ads</em></h1><table><tr><th>#</th><th>Livro · autor</th><th>A ideia central</th></tr>'+''.join(f'<tr><td>{n}</td><td style="font-weight:400">{t} · {a}</td><td style="font-weight:400">{i}</td></tr>' for n,t,a,i in LIV)+'</table>')
REF=[('Toyota × Sarah Fonseca','Marketing de oportunidade em formato de episódio'),('Boticário × Mari Krüger','Causa coerente com público, produto e prova'),('Liquid Death','Posicionamento que transforma um produto comum em desejo'),('Dove · Retratos da Real Beleza','A história carrega a mensagem; a marca aparece no fim'),('Burger King × Dragon Ball','Memória afetiva e colecionáveis'),('Burger King × Fiuk','Assunto do momento com humor e coerência de marca'),('Case CRM (Agência Recria)','Funil completo num carrossel, com palavra-chave'),('Duolingo no TikTok','Um personagem de marca com humor e constância'),('Old Spice (campanhas com humor)','Humor absurdo como assinatura de marca'),('Heineken "Worlds Apart"','Conversa real entre pessoas que discordam')]
b.page('dark','<div class="kick">10 referências de criativos para modelar</div><h1>Pesquise, observe <em class="g">e adapte</em></h1><table><tr><th>Referência</th><th>O que observar</th></tr>'+''.join(f'<tr><td>{r}</td><td>{o}</td></tr>' for r,o in REF)+'</table><p style="font-size:20px;margin-top:12px">Modelar não é copiar: observe a estrutura, a emoção e o gancho, e adapte ao seu negócio.</p>')
b.page('light','''<div class="kick">O Acervo completo</div><h1>Quer ir <em class="g">mais fundo?</em></h1><p>O Acervo Recria completo, com livros, materiais, insights e referências de criativos sempre atualizados, está na <b>Comunidade Recria</b>.</p><div class="box">Como aluno(a) do Recria Ads, você tem uma condição exclusiva para entrar.</div><p style="font-family:'Playfair Display';font-style:italic;font-size:28px;color:#9a7424">Amanda, CEO da Agência Recria</p>''')
b.render(OUT+'Aula 7.3 - Acervo Recria.pdf')
