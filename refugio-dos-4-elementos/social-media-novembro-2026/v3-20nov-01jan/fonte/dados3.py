"""Calendario Refugio 20/11/2026 a 01/01/2027 (seg, qua, sex). Reaproveita os textos aprovados da v2."""
import copy
from visual import VERDE, LILAS, TERRA
import dados as V2

U = '/mnt/user-data/uploads/'
J = lambda n: f'{U}{n}_Jean_Amorim_27-07-26.jpg'
SITE = '/home/claude/refugio-site/img/'
PERFIL = V2.PERFIL
WHATSAPP_AGENCIA = ''
old = {it['id'][-1]: copy.deepcopy(it) for it in V2.ITENS}

def de(letra, data, dia, **mud):
    it = old[letra]; it.update(data=data, dia=dia, **mud); return it

def novo(data, dia, tipo, tema, objetivo, arte, legenda, cta, foto, nota, **extra):
    return dict(data=data, dia=dia, tipo=tipo, tema=tema, objetivo=objetivo, arte=arte, legenda=legenda,
                cta=cta, foto=foto, nota=nota, **extra)

ciencia = old['E']
cap = list(ciencia['arte'][1]); c0 = cap[0]
cap[0] = ('capa', c0[1], c0[2], c0[3], c0[4], {'fy': 0.5, 'topo': True})
ciencia['arte'] = ('carrossel', cap)

LOUV_DEZ = '[DATA DA LOUVAÇÃO DE DEZEMBRO]'

ITENS = [
 de('A', '2026-11-20', 'Sexta', nota='Saiu de 19/11 para 20/11 (novo cronograma). Louvação no último sábado, 28/11.'),
 dict(ciencia, data='2026-11-23', dia='Segunda', nota=ciencia['nota'] + ' Capa ajustada: texto no alto para não cobrir os rostos.'),
 de('G', '2026-11-25', 'Quarta', legenda=old['G']['legenda'].replace('nos próximos dias você vai conhecer', 'nas próximas semanas você vai conhecer'), arte=('foto', J(283), 'Todo refúgio começa com alguém que decide abrir a porta de casa.', 'Prazer, Daniela e Joelson.', 'Quem cuida de você', {'fy': 0.22, 'nome': True})),
 de('H', '2026-11-27', 'Sexta', tema='Louvação: é amanhã (tema revelado)',
    arte=('foto', J(113), 'Amanhã é dia de Louvação.', 'Sábado, 28/11 · Quintal de Ogum · Tema: [revelar]', 'Louvação de novembro', {'fy': 0.15}),
    legenda=old['H']['legenda'].replace('Faltam 2 dias. 🤍', 'É amanhã. 🤍').replace('Neste sábado, 28/11,', 'Amanhã, sábado, 28/11,'),
    nota='Era o "faltam 2 dias" de 26/11; virou "é amanhã" no novo cronograma. Se o tema não chegar, tirar a frase do tema. Reel de 8 s, colocar música no Instagram.'),
 de('L', '2026-11-30', 'Segunda'),
 de('B', '2026-12-02', 'Quarta', nota=old['B']['nota'].replace(' 20/11 é Dia da Consciência Negra: o tema conversa com a data sem usá-la como gancho.', '')),
 novo('2026-12-04', 'Sexta', 'estatico', 'Louvação de dezembro', 'Regra da 1ª sexta do mês: divulgar a Louvação',
   ('foto', SITE + 'joelson-r.jpg', 'Vamos fechar 2026 em gratidão?', f'{LOUV_DEZ} · Quintal de Ogum, Cuiabá', 'Louvação de dezembro', {'fy': 0.5, 'topo': True}),
   f"""O ano está terminando. E, antes de começar outro, a gente te convida para parar, respirar e agradecer. 🤍

A última Louvação de 2026 vai ser um encontro de oração, cantos, silêncio e gratidão por tudo o que este ano trouxe, inclusive o que foi difícil.

✨ {LOUV_DEZ}
📍 Quintal de Ogum, Cuiabá
🙏 Aberto a qualquer pessoa, de qualquer religião ou crença

O tema do encontro ainda está sendo recebido, no processo de preparo e escuta espiritual que antecede cada Louvação. Assim que ele chegar, a gente conta aqui.

Comenta LOUVAÇÃO que a gente te manda o horário e as orientações no direct.

E se alguém que você ama precisa fechar esse ano com mais leveza, manda esse post pra ela. 💛""",
   'LOUVAÇÃO', 'Joelson em oração na natureza (foto do site)',
   'Falta a data: o último sábado seria 26/12, dia seguinte ao Natal. Confirmar se mantém ou antecipa (19/12).'),
 novo('2026-12-07', 'Segunda', 'carrossel', 'O que dizem quem já passou por aqui (prints reais)',
   'Prova social com prints reais (2º carrossel do mês, liberado pela Amanda)',
   ('carrossel', [
     ('capa', SITE + 'daniela-r.jpg', 'O que dizem as pessoas que já passaram pelo Refúgio.', 'Prints reais de quem confiou a sua história a nós.', 'Quem chegou aqui', {'fy': 0.35}),
     ('print', SITE + 'dep-lucia.png', 'Lúcia · comentário no nosso Instagram', (484, 22, 795, 330)),
     ('card', None, 'Cada processo é único. Todo caminho começa com um primeiro passo.',
       ['Se você sente que é a sua hora, comenta REFÚGIO que a gente te chama no direct.'], LILAS, None),
   ]),
   """A gente poderia passar o mês inteiro explicando o que acontece numa sessão. Mas ninguém conta melhor do que quem viveu. 🤍

Separamos algumas mensagens que recebemos de pessoas que passaram pelo Refúgio. Arrasta para o lado e lê com calma. 👉

A cada uma delas: obrigada por confiar a sua história a nós. 🙏

Cada processo é único, e o tempo de cada pessoa também. Mas todo caminho começa do mesmo jeito: com um primeiro passo.

Se você sente que é a sua hora, comenta REFÚGIO que a gente te chama no direct.

📍 Cuiabá/MT e online""",
   'REFÚGIO', 'Capa: Daniela no bambuzal (foto do site). Cards: prints reais.',
   'Substitui o post do depoimento de 22/11. O print da Lúcia é o comentário real dela no Instagram (o mesmo que está no site). Faltam os outros prints que a Amanda tem: entram um por card, antes do card final. Pedir OK de quem aparece, ou borrar nome e foto.',
   status='pendente'),
 de('C', '2026-12-09', 'Quarta'),
 de('K', '2026-12-11', 'Sexta', arte=('foto', J(329), 'Ele aprendeu a ler o que o corpo diz antes das palavras.', 'Prazer, Jean Carlos.', 'Quem cuida de você', {'fy': 0.12, 'nome': True}),
    legenda=old['K']['legenda'].replace('Há alguns dias você conheceu', 'Há algumas semanas você conheceu')),
 de('F', '2026-12-14', 'Segunda', tema='Mito: preciso ter religião para fazer terapia holística',
    arte=('foto', J(13), 'Preciso ter uma religião para fazer terapia holística?', 'Mito. E a explicação é mais simples do que parece.', 'Mito ou verdade', {'fy': 0.18}),
    legenda="""Mito. 🤍

Essa é uma das dúvidas que mais seguram as pessoas antes do primeiro passo. E faz sentido: muitas terapias holísticas têm origem em tradições antigas, e algumas falam de energia e espiritualidade. Mas isso não quer dizer que você precise seguir uma religião, mudar a sua ou acreditar em algo que não faz sentido pra você.

"Holístico" vem de "inteiro". Uma terapia holística olha para você por inteiro: corpo, mente, emoções e energia, em vez de olhar só para um sintoma. É uma forma de cuidado, não uma religião.

Na prática, funciona assim aqui no Refúgio:
🌿 Nosso trabalho é universalista: católicos, evangélicos, espíritas, umbandistas, pessoas de outras tradições e quem não tem religião nenhuma são recebidos do mesmo jeito.
🌿 Ninguém vai te pedir para rezar de um jeito específico, adotar rituais ou mudar a sua fé.
🌿 Você não precisa "acreditar" para participar. Precisa só estar aberta(o) a olhar para si com carinho e honestidade.
🌿 E muita gente conta que, depois das terapias, se sente até mais conectada com a própria fé.

Aliás, Reiki e Meditação estão entre as práticas integrativas oferecidas pelo SUS desde 2017. Ou seja: são reconhecidas como cuidado, para qualquer pessoa.

A sua fé continua sendo sua. A gente só cuida do caminho.

Tem outra dúvida que te segura? Deixa aqui nos comentários que a gente responde. 👇

📍 Cuiabá/MT e online""",
    nota='Ajuste da Amanda: "terapia holística" no lugar de "terapia espiritual", com explicação melhor. A frase "se sente até mais conectada com a própria fé" vem do relato comum; validar com a Daniela.'),
 de('I', '2026-12-16', 'Quarta', legenda=old['I']['legenda'].replace('O fim do ano vai chegando', 'O fim do ano chegou')),
 de('J', '2026-12-18', 'Sexta', nota='Post de alcance (salvar e comentar o número).'),
 novo('2026-12-21', 'Segunda', 'reels', 'Natal com a família reunida', 'Alcance: tema do momento (encontros de fim de ano)',
   ('foto', J(103), 'O Natal reúne a família. E, com ela, tudo o que ainda não foi resolvido.', '4 jeitos de atravessar as festas mais leve.', 'Constelação Familiar', {'fy': 0.15}),
   """Fim de ano é tempo de mesa cheia, abraço apertado… e, às vezes, daquela tensão que aparece justo quando a família inteira se reúne. 🤍

Se você sente um nó só de pensar na ceia, você não está sozinha(o). Aqui vão 4 cuidados que a gente sempre compartilha por aqui:

1️⃣ Vá com expectativas possíveis
Ninguém muda numa noite. Aceitar as pessoas como elas estão hoje já tira muito peso.

2️⃣ Você não precisa resolver tudo na ceia
Conversas importantes merecem outro momento, com calma. A noite de Natal pode ser só de presença.

3️⃣ Guarde um momento só seu
Uma caminhada, uns minutos de silêncio, uma respiração mais longa. Voltar pra si ajuda a não reagir no automático.

4️⃣ Olhe para o lugar de cada um
Na Constelação Familiar, a gente aprende que cada pessoa da família tem o seu lugar e a sua história. Quando você honra isso, não precisa carregar o que não é seu.

E se algo pesar demais, tudo bem buscar ajuda depois das festas. A gente segue aqui.

Salva esse post pra ler antes da ceia e manda pra quem vai sentar à mesa com você. 💛

📍 Cuiabá/MT e online""",
   'salvar e compartilhar', 'Jean pensativo (103)', 'Reel de 8 s com a foto e música calma do Instagram. Conteúdo de cuidado geral, sem promessa de cura.',
   reel=True),
 novo('2026-12-23', 'Quarta', 'estatico', 'Louvação de dezembro: lembrete', 'Lembrete do evento + revelação do tema',
   ('foto', J(182), 'Falta pouco para a última Louvação do ano.', f'{LOUV_DEZ} · Quintal de Ogum · Tema: [revelar]', 'Louvação de dezembro', {'fy': 0.25, 'fx': 0.45}),
   f"""A última Louvação de 2026 está chegando. 🤍

✨ {LOUV_DEZ}
📍 Quintal de Ogum, Cuiabá

E a mensagem que vai guiar o nosso encontro chegou: [TEMA DE DEZEMBRO]. [1 ou 2 frases da Daniela e do Joelson sobre o tema.]

Uma noite de oração, cantos, silêncio e gratidão para fechar o ano, aberta a qualquer pessoa, de qualquer religião ou crença.

Comenta LOUVAÇÃO que a gente te manda o horário e as orientações no direct.

Vai com alguém? Marca aqui quem você quer levar. 👇""",
   'LOUVAÇÃO', 'Daniela em oração (182)', f'Depende da data. Se a Louvação for em 19/12, este post vira o agradecimento do encontro (como o de 30/11).'),
 novo('2026-12-25', 'Sexta', 'estatico', 'Feliz Natal', 'Data comemorativa (relacionamento, sem venda)',
   ('foto', SITE + 'equipe-r.jpg', 'Que o seu Natal seja casa, abraço e paz.', 'Feliz Natal, do Refúgio dos 4 Elementos para você e sua família.', 'Feliz Natal', {'fy': 0.5, 'topo': True}),
   """Feliz Natal. 🤍

Que a sua noite tenha mesa farta, abraços sinceros e um pouco de silêncio também, para lembrar de tudo o que te trouxe até aqui.

Obrigado por caminhar com a gente em 2026. Cada mensagem, cada sessão e cada Louvação tornaram este ano mais bonito.

Com carinho,
Daniela, Joelson e toda a equipe do Refúgio dos 4 Elementos 🎄""",
   'nenhum', 'Equipe no bambuzal (foto do site)', 'Sem CTA de venda.'),
 novo('2026-12-28', 'Segunda', 'carrossel', 'O Refúgio não é para todo mundo. E tudo bem.', 'Identificação e qualificação (aprovado pela Amanda em 29/10)',
   ('carrossel', [
     ('capa', J(134), 'O Refúgio não é para todo mundo. E tudo bem.', 'Arrasta e veja se ele é pra você.', 'Antes de começar 2027', {'fy': 0.15}),
     ('card', 'É PRA VOCÊ SE...', 'Você carrega um peso que não consegue nomear.', ['Aquele cansaço que não passa com descanso. A sensação de que algo está fora do lugar, mesmo quando tudo parece bem por fora.'], VERDE, None),
     ('card', 'É PRA VOCÊ SE...', 'A mesma história se repete na sua vida.', ['Nos relacionamentos, no trabalho, com dinheiro. Você muda o cenário, mas o roteiro parece sempre o mesmo.'], VERDE, None),
     ('card', 'É PRA VOCÊ SE...', 'Você tem curiosidade, mesmo cheia(o) de dúvidas.', ['Não precisa chegar sabendo o que é Constelação ou Reiki. A gente explica tudo antes, sem pressa e sem julgamento.'], VERDE, None),
     ('card', 'NÃO É PRA VOCÊ SE...', 'Você procura cura milagrosa ou com prazo marcado.', ['Aqui o cuidado é um processo, no seu tempo. E, em crise aguda, o primeiro passo é procurar atendimento médico de urgência.'], TERRA, None),
     ('card', 'NÃO É PRA VOCÊ SE...', 'Você busca o ritual de uma religião específica.', ['Nosso trabalho é universalista. Todas as crenças são bem-vindas, e nenhuma é exigida.'], TERRA, None),
     ('card', None, 'Se reconheceu? Você não precisa estar pronta(o). Só aberta(o).', ['Comenta REFÚGIO que a gente te chama no direct para começar 2027 com uma conversa.'], LILAS, None),
   ]),
   """Antes de começar um ano novo, a gente prefere ser honesto com você. 🤍

O Refúgio é um espaço de acolhimento, sem julgamento e sem pressa. Mas ele não é pra todo mundo, e tá tudo bem.

É pra você que sente um peso que não sabe nomear, que vive repetindo as mesmas histórias ou que simplesmente tem curiosidade e muitas dúvidas.

Não é pra quem procura cura milagrosa, com prazo marcado, nem pra quem busca o ritual de uma religião específica. Aqui o trabalho é universalista e o cuidado acontece em processo, no seu tempo.

E se você está em crise aguda, o primeiro passo é procurar atendimento médico de urgência. A gente segue aqui depois.

Se você se reconheceu, comenta REFÚGIO que a gente te chama no direct para começar 2027 com uma conversa. E salva esse post pra mandar pra quem precisa ler isso. 💛

📍 Cuiabá/MT e online""",
   'REFÚGIO', 'Capa: Daniela sorrindo (134). Cards só texto.', 'Carrossel aprovado em 29/10, enxugado para 7 cards e com gancho de ano novo.'),
 novo('2026-12-30', 'Quarta', 'reels', 'O que você não quer levar para 2027?', 'Engajamento (comentários) + fechamento de ciclo',
   ('foto', J(92), 'O que você não quer levar para 2027?', 'Escreve aqui nos comentários. A gente lê cada um.', 'Fechando ciclos', {'fy': 0.12, 'fx': 0.6}),
   """O que você não quer levar para 2027? 🤍

Um medo, uma mágoa, uma culpa, um padrão que se repetiu o ano inteiro… Às vezes, só dar nome ao que pesa já é o começo de soltar.

Um pequeno ritual para hoje ou amanhã:
1️⃣ Escreva num papel o que você quer deixar em 2026.
2️⃣ Leia em voz alta, agradecendo pelo que aquilo te ensinou.
3️⃣ Rasgue o papel e jogue fora, com a intenção de seguir mais leve.

E, se quiser, escreve aqui nos comentários uma palavra do que você está deixando pra trás. A gente lê cada um. 👇

📍 Cuiabá/MT e online""",
   'comentar', 'Jean olhando para cima (92)', 'Reel de 8 s com música do Instagram.', reel=True),
 novo('2027-01-01', 'Sexta', 'estatico', 'Feliz Ano Novo', 'Data comemorativa (relacionamento, sem venda)',
   ('foto', J(283), 'Que 2027 seja leve, verdadeiro e seu.', 'Feliz Ano Novo, do Refúgio dos 4 Elementos para você.', 'Feliz 2027', {'fy': 0.22}),
   """Feliz 2027. 🤍

Que este ano venha com mais presença, mais leveza e mais coragem para ser quem você é.

Que você honre a sua história, solte o que não é seu e abra espaço para o novo.

E, quando precisar de um refúgio, você já sabe onde nos encontrar.

Com carinho,
Daniela, Joelson e toda a equipe do Refúgio dos 4 Elementos ✨""",
   'nenhum', 'Joelson e Daniela no passe (283)', 'Sem CTA de venda.'),
]

for i, it in enumerate(ITENS):
    it['id'] = f'REF-{it["data"][2:4]}{it["data"][5:7]}{it["data"][8:10]}'
    it.setdefault('status', 'rascunho')
    if '[' in it['legenda'] and it['status'] == 'rascunho': it['status'] = 'pendente'

STORIES = V2.STORIES
FALTA = [
  'Data da Louvação de dezembro (04/12 e 23/12): manter 26/12 ou antecipar para 19/12?',
  'Prints dos depoimentos (07/12): mandar os prints que você tem; cada um vira um card.',
  'Tema da Louvação de novembro (27/11) e de dezembro (23/12), quando forem recebidos.',
  'Foto da Louvação de 28/11 para o post de gratidão (30/11), se a equipe tiver.',
  'Pedir OK da Lúcia e de quem mais aparecer nos prints.',
]

# ---------- ajustes de 19/11 (2ª rodada) ----------
_por_id = {it['id']: it for it in ITENS}
def _set(i, **k): _por_id[i].update(k)

_set('REF-261123', nota='Fontes: Ministério da Saúde, Portaria nº 849/2017 (inclui Reiki e Meditação; definição do Reiki citada) e Portaria nº 702/2018; CONASS, 12/03/2018 (10 novas práticas, total de 29); Goyal et al., JAMA Internal Medicine, 2014 (47 estudos, 3.515 participantes); Guo et al., BMC Palliative Care, 2024 (13 estudos, 824 participantes).')
_set('REF-261125', objetivo='Conexão e confiança: apresentar os cofundadores antes do resto da equipe')
_set('REF-261202', objetivo='Alcance: Reel com frase de identificação')
_set('REF-261209', nota='Abre com a fala de quem chega (gancho) e explica a entrevista prévia.')
_set('REF-261214', nota='Validar com a Daniela a frase "se sente até mais conectada com a própria fé".')
_set('REF-261228', objetivo='Identificação e qualificação antes do ano novo')

# 30/11: sai a gratidão pela Louvação, entra um exercício de respiração conduzido pelo Jean
_set('REF-261130', tema='Respiração de 3 minutos para desacelerar', tipo='estatico', status='rascunho',
     objetivo='Valor prático (salvar e compartilhar) e ponte com o carrossel de ciência sobre meditação',
     arte=('foto', J(126), 'Uma pausa de 3 minutos para quando a cabeça não desliga.', 'Salva para fazer hoje à noite.', 'Meditação guiada pelo Jean', {'fy': 0.15}),
     legenda="""Sabe quando a cabeça não desliga, mesmo com o corpo cansado? 🤍

Esse é um exercício simples que o Jean, condutor de meditação aqui do Refúgio, costuma ensinar. Leva 3 minutos e pode ser feito na cama, no carro (parado) ou no intervalo do trabalho:

1️⃣ Sente ou deite de um jeito confortável e solte os ombros.
2️⃣ Inspire pelo nariz contando até 4.
3️⃣ Solte o ar devagar, pela boca, contando até 6.
4️⃣ Repita por 3 minutos, levando a atenção só para o ar que entra e sai.
5️⃣ Se a mente fugir, tudo bem. Perceba e volte para a respiração, sem brigar com você.

Soltar o ar mais devagar do que puxou ajuda o corpo a sair do modo alerta. E lembra do nosso post sobre a ciência? Programas de meditação já mostraram redução de ansiedade em estudos.

Se sentir tontura ou desconforto, volte a respirar no seu ritmo normal.

Salva esse post para fazer hoje à noite e manda para alguém que anda precisando desacelerar. 💛

📍 Cuiabá/MT e online""",
     cta='salvar e compartilhar', foto='Jean sorrindo (126)',
     nota='Substitui o agradecimento pela Louvação. Técnica de respiração simples (expiração mais longa que a inspiração), sem promessa de tratamento.')

# 07/12: comentário (singular), sem "print"
_d = _por_id['REF-261207']
_cap = list(_d['arte'][1])
_cap[0] = ('capa', SITE + 'daniela-r.jpg', 'O que falam sobre o nosso trabalho.', 'Comentários de quem confiou a sua experiência a nós.', 'Quem chegou aqui', {'fy': 0.35})
_d.update(tema='O que falam sobre o nosso trabalho', objetivo='Prova social: comentário de quem já passou pelo Refúgio (2º carrossel de dezembro)',
     arte=('carrossel', _cap), status='rascunho',
     foto='Capa: Daniela no bambuzal (foto do site). Card 2: comentário da Lúcia no Instagram.',
     legenda="""A gente poderia passar o mês inteiro explicando o que acontece numa sessão. Mas ninguém conta melhor do que quem viveu. 🤍

Arrasta para o lado e lê o que a Lúcia escreveu aqui no nosso Instagram sobre o processo dela. 👉

Lúcia, obrigada por confiar a sua experiência a nós. 🙏

Cada processo é único, e o tempo de cada pessoa também. Mas todo caminho começa do mesmo jeito: com um primeiro passo.

Se você sente que é a sua hora, comenta REFÚGIO que a gente te chama no direct.

📍 Cuiabá/MT e online""",
     nota='Comentário da @luciarruda_01 no Instagram do Refúgio (o mesmo do site). Se chegarem mais comentários, cada um vira um card antes do card final. Pedir OK da Lúcia.')

# 16/12 <-> 18/12 (para não ficar Joelson em 14 e 16)
_a, _b = _por_id['REF-261216'], _por_id['REF-261218']
_a['data'], _a['dia'], _b['data'], _b['dia'] = '2026-12-18', 'Sexta', '2026-12-16', 'Quarta'
_a['id'], _b['id'] = 'REF-261218', 'REF-261216'
ITENS.sort(key=lambda it: it['data'])

# 01/01: equipe de mãos unidas (foto do post de 23/10, usada sem ampliar)
_set('REF-270101', arte=('foto', '/home/claude/w/refugio-dos-4-elementos/social-media-outubro-2026/post07_23-10_primeira-sessao.jpg',
     'Que 2027 seja leve, verdadeiro e seu.', 'Feliz Ano Novo, do Refúgio dos 4 Elementos para você.', 'Feliz 2027',
     {'encaixe': (0, 0, 1080, 876), 'sem_icone': True}),
     foto='Equipe de mãos unidas (a mesma foto do post de 23/10)', nota='Se tiver o arquivo original dessa foto, trocar para ganhar nitidez.')

FALTA = [
  'Data da Louvação de dezembro (04/12 e 23/12): fica o último sábado (26/12) até eles confirmarem.',
  'Tema da Louvação de novembro (27/11) e de dezembro (23/12), quando forem recebidos.',
  'Reels de 27/11, 02/12, 21/12 e 30/12: a Amanda coloca a música e devolve.',
  'Pedir OK da Lúcia para usar o comentário dela (07/12).',
]

# ---------- ajustes de 19/11 (3ª rodada) ----------
_por_id = {it['id']: it for it in ITENS}
_set = lambda i, **k: _por_id[i].update(k)
_set('REF-261127', foco=(0.5, 0.3))            # zoom no rosto e nas maos
_por_id['REF-261127']['arte'][5]['reel_base'] = 560
_set('REF-261202', foco=(0.5, 0.3))
_a = _por_id['REF-261202']['arte']; _a[5]['reel_base'] = 640
_a = _por_id['REF-261230']['arte']; _a[5]['reel_base'] = 700
_set('REF-261230', foco=(0.55, 0.3))
_set('REF-261204', arte=('foto', SITE + 'joelson-r.jpg', 'Vamos fechar 2026 em gratidão?', f'{LOUV_DEZ} · Quintal de Ogum, Cuiabá',
     'Louvação de dezembro', {'encaixe': (0, 0, 1728, 1300)}))
_d = _por_id['REF-261207']; _cap = list(_d['arte'][1])
_cap[0] = ('capa', SITE + 'daniela-r.jpg', 'Comentário de quem confia no nosso trabalho.', 'Arrasta para o lado e leia.', 'O que falam do Refúgio', {'fy': 0.35})
_d['arte'] = ('carrossel', _cap); _d['tema'] = 'Comentário de quem confia no nosso trabalho'
_set('REF-261221', tipo='estatico', reel=False,
     arte=('foto', '/home/claude/nov2/natal_provisorio.jpg', 'O Natal reúne a família. E, com ela, tudo o que ainda não foi resolvido.', '4 jeitos de atravessar as festas mais leve.', 'Fim de ano em família', {'fy': 0.5}),
     foto='Imagem gerada por IA (árvore de Natal ao fundo, duas pessoas conversando). Por enquanto, imagem provisória.',
     nota='A Amanda vai gerar a imagem com o prompt combinado. Trocar a imagem provisória quando chegar.')
_set('REF-270101', arte=('foto', '/home/claude/nov/out/post01_04-11_mito-verdade-constelacao.jpg',
     'Que 2027 seja leve, verdadeiro e seu.', 'Feliz Ano Novo, do Refúgio dos 4 Elementos para você.', 'Feliz 2027',
     {'encaixe': (0, 0, 1080, 998), 'sem_icone': True}),
     foto='Equipe de mãos dadas (a mesma foto do post de 04/11)')
FALTA = [
  'Data da Louvação de dezembro (04/12 e 23/12): fica o último sábado (26/12) até eles confirmarem.',
  'Tema da Louvação de novembro (27/11) e de dezembro (23/12), quando forem recebidos.',
  'Imagem de Natal gerada por IA para o post de 21/12 (prompt enviado).',
  'Reels de 27/11, 02/12 e 30/12: a Amanda coloca a música e devolve.',
  'Pedir OK da Lúcia para usar o comentário dela (07/12).',
]

# ---------- ajustes de 19/11 (4ª rodada) ----------
_por_id = {it['id']: it for it in ITENS}
_set = lambda i, **k: _por_id[i].update(k)
# capa da ciencia: titulo mais curto para o texto acabar antes dos rostos
_c = _por_id['REF-261123']; _cap = list(_c['arte'][1])
_cap[0] = ('capa', SITE + 'equipe-r.jpg', 'Terapia holística é "só crença"?', 'A ciência já tem algumas respostas. Arrasta para o lado.', 'O que a ciência diz', {'fy': 0.5, 'topo': True})
_c['arte'] = ('carrossel', _cap)
_n = _por_id['REF-261225']; _n['arte'] = ('foto', SITE + 'equipe-r.jpg', 'Feliz Natal.', 'Que o seu Natal seja casa, abraço e paz.', 'Do Refúgio para você', {'fy': 0.5, 'topo': True})
# intercalar o Jean: depoimentos vai para 30/11 e a respiracao para 07/12
_dep, _resp = _por_id['REF-261207'], _por_id['REF-261130']
_dep.update(data='2026-11-30', dia='Segunda', id='REF-261130')
_resp.update(data='2026-12-07', dia='Segunda', id='REF-261207')
_set('REF-261204', arte=('foto', J(134), 'Vamos fechar 2026 em gratidão?', f'{LOUV_DEZ} · Quintal de Ogum, Cuiabá', 'Louvação de dezembro', {'fy': 0.15}),
     foto='Daniela sorrindo, mãos unidas (134)')
_por_id['REF-261223']['arte'] = ('foto', J(283), 'Falta pouco para a última Louvação do ano.', f'{LOUV_DEZ} · Quintal de Ogum · Tema: [revelar]', 'Louvação de dezembro', {'fy': 0.22})
_por_id['REF-261223']['foto'] = 'Joelson e Daniela no passe (283)'
_p = _por_id['REF-261228']; _cap = list(_p['arte'][1]); _c0 = _cap[0]
_cap[0] = ('capa', J(182), _c0[2], _c0[3], _c0[4], {'fy': 0.25, 'fx': 0.45}); _p['arte'] = ('carrossel', _cap); _p['foto'] = 'Capa: Daniela em oração (182). Cards só texto.'
ITENS.sort(key=lambda it: it['data'])
_por_id = {it['id']: it for it in ITENS}
_por_id['REF-261130']['objetivo'] = 'Prova social: comentário de quem já passou pelo Refúgio (2º carrossel de novembro)'

# 21/12: imagem de Natal gerada pela Amanda
_por_id = {it['id']: it for it in ITENS}
_a = _por_id['REF-261221']['arte']
_por_id['REF-261221'].update(arte=('foto', '/home/claude/nov2/natal_ia.jpg', _a[2], _a[3], _a[4], {'fy': 0.0}),
    foto='Família celebrando o Natal (imagem gerada por IA)', nota='Imagem gerada por IA pela agência.')

# ---------- ajustes de 19/11 (5ª rodada): card branco x degradê ----------
from visual import AZUL
ESCURO = (40, 26, 18)   # marrom bem escuro
PRETO = (14, 11, 10)
_por_id = {it['id']: it for it in ITENS}
def _kw(i, capa=False):
    a = _por_id[i]['arte']
    return a[1][0][5] if capa else a[5]
def _card(i, cor, pos='baixo', capa=False):
    k = _kw(i, capa); k.pop('topo', None); k.pop('encaixe', None); k.pop('sem_icone', None); k.pop('nome', None)
    k.update(estilo='card', cor=cor, pos=pos)
# card branco embaixo
for _i, _c in [('REF-261204', TERRA), ('REF-261207', VERDE), ('REF-261209', VERDE), ('REF-261214', LILAS),
               ('REF-261216', TERRA), ('REF-261218', AZUL), ('REF-261221', TERRA), ('REF-261223', TERRA)]:
    _card(_i, _c)
# card branco em cima (fotos com rostos embaixo)
_card('REF-261123', VERDE, 'topo', capa=True); _kw('REF-261123', True)['fy'] = 0.75
_card('REF-261225', VERDE, 'topo'); _kw('REF-261225')['fy'] = 0.75
# degradê mais escuro
for _i, _capa in [('REF-261125', False), ('REF-261130', True), ('REF-261211', False), ('REF-261228', True), ('REF-270101', False)]:
    _kw(_i, _capa)['fade'] = ESCURO
_kw('REF-261202')['fade'] = PRETO
_kw('REF-261230')['fade'] = ESCURO

# ---------- ajustes de 19/11 (6ª rodada): card branco em todos os posts que não são vídeo ----------
_por_id = {it['id']: it for it in ITENS}
def _card2(i, cor, pos='baixo', capa=False, manter=()):
    k = _kw(i, capa)
    for x in ('topo', 'fade'): k.pop(x, None)
    k.update(estilo='card', cor=cor, pos=pos)
_card2('REF-261120', TERRA)
_card2('REF-261125', LILAS)                 # mantem nome=True (nome em destaque)
_card2('REF-261130', LILAS, capa=True)
_card2('REF-261211', LILAS)                 # mantem nome=True
_card2('REF-261228', VERDE, capa=True)
_card2('REF-270101', LILAS); _kw('REF-270101')['fy'] = 0.0   # mantem encaixe e sem_icone (icone ja esta na foto)

# 11/12: Jean mais afastado (aparece até a cintura)
_por_id = {it['id']: it for it in ITENS}
_kw('REF-261211').update(zoom=0.68, fy=0.05)

# ---------- ajustes da Daniela (26/11) ----------
_por_id = {it['id']: it for it in ITENS}
GRUPO = '/home/claude/nov/out/post01_04-11_mito-verdade-constelacao.jpg'   # equipe sem o Breno (provisória até chegar a foto original)
GRUPO_CROP = (0, 0, 1080, 998)
TEMA_NOV = 'Louvação ao Seu Zé Pilintra'
TEMA_DEZ = 'Encerramento do Ciclo 2026'
# 27/11: tema de novembro
_i = _por_id['REF-261127']; _a = _i['arte']
_i['arte'] = ('foto', _a[1], _a[2], f'Sábado, 28/11 · Quintal de Ogum · {TEMA_NOV}', _a[4], _a[5])
_i['legenda'] = _i['legenda'].replace('E a mensagem que vai guiar o nosso encontro chegou: [TEMA DE NOVEMBRO]. [1 ou 2 frases da Daniela e do Joelson sobre o tema.]',
    f'E a mensagem que vai guiar o nosso encontro chegou: este mês, a nossa é uma {TEMA_NOV}.')
_i['status'] = 'rascunho'; _i['tema'] = f'Louvação: é amanhã ({TEMA_NOV})'
# 04/12 e 23/12: tema de dezembro
_i = _por_id['REF-261204']
_i['legenda'] = _i['legenda'].replace('O tema do encontro ainda está sendo recebido, no processo de preparo e escuta espiritual que antecede cada Louvação. Assim que ele chegar, a gente conta aqui.',
    f'O tema deste encontro: {TEMA_DEZ}.')
_i = _por_id['REF-261223']; _a = _i['arte']
_i['arte'] = ('foto', _a[1], _a[2], f'{LOUV_DEZ} · Quintal de Ogum · {TEMA_DEZ}', _a[4], _a[5])
_i['legenda'] = _i['legenda'].replace('E a mensagem que vai guiar o nosso encontro chegou: [TEMA DE DEZEMBRO]. [1 ou 2 frases da Daniela e do Joelson sobre o tema.]',
    f'E o tema do nosso encontro já chegou: {TEMA_DEZ}.')
# 30/11: Luciana Arruda
_i = _por_id['REF-261130']; _cap = list(_i['arte'][1])
_cap[1] = ('print', _cap[1][1], 'Luciana Arruda · comentário no nosso Instagram', _cap[1][3])
_i['arte'] = ('carrossel', _cap)
_i['legenda'] = _i['legenda'].replace('o que a Lúcia escreveu', 'o que a Luciana Arruda escreveu').replace('Lúcia, obrigada', 'Luciana, obrigada')
_i['foto'] = _i['foto'].replace('Lúcia', 'Luciana Arruda')
# sem o Breno: capa da ciência (23/11) e Natal (25/12) com a foto de estúdio da equipe
for _id, _capa in [('REF-261123', True), ('REF-261225', False)]:
    _k = _kw(_id, _capa); _k.update(encaixe=GRUPO_CROP, sem_icone=True, fy=0.0)
    if _capa:
        _cap = list(_por_id[_id]['arte'][1]); _c0 = _cap[0]; _cap[0] = ('capa', GRUPO, _c0[2], _c0[3], _c0[4], _k); _por_id[_id]['arte'] = ('carrossel', _cap)
    else:
        _a = _por_id[_id]['arte']; _por_id[_id]['arte'] = ('foto', GRUPO, _a[2], _a[3], _a[4], _k)
# foto de estúdio já sem o ícone antigo gravado
GRUPO = '/home/claude/nov2/grupo_limpo.jpg'
for _id, _capa in [('REF-261123', True), ('REF-261225', False), ('REF-270101', False)]:
    _k = _kw(_id, _capa); _k['sem_icone'] = False; _k['encaixe'] = GRUPO_CROP
    if _capa:
        _cap = list(_por_id[_id]['arte'][1]); _c0 = _cap[0]; _cap[0] = ('capa', GRUPO, _c0[2], _c0[3], _c0[4], _k); _por_id[_id]['arte'] = ('carrossel', _cap)
    else:
        _a = _por_id[_id]['arte']; _por_id[_id]['arte'] = ('foto', GRUPO, _a[2], _a[3], _a[4], _k)

# fotos originais enviadas pela Daniela (26/11)
EQUIPE_V = '/home/claude/nov2/equipe_estudio_vertical.jpg'
GATO = '/home/claude/nov2/daniela_gato.jpg'
for _id, _capa in [('REF-261123', True), ('REF-261225', False)]:
    _k = _kw(_id, _capa)
    for _x in ('encaixe', 'sem_icone'): _k.pop(_x, None)
    _k['fy'] = 0.0
    if _capa:
        _cap = list(_por_id[_id]['arte'][1]); _c0 = _cap[0]; _cap[0] = ('capa', EQUIPE_V, _c0[2], _c0[3], _c0[4], _k); _por_id[_id]['arte'] = ('carrossel', _cap)
    else:
        _a = _por_id[_id]['arte']; _por_id[_id]['arte'] = ('foto', EQUIPE_V, _a[2], _a[3], _a[4], _k)
for _id in ('REF-261125', 'REF-261223'):
    _a = _por_id[_id]['arte']; _k = dict(_a[5]); _k['fy'] = 0.12
    _por_id[_id]['arte'] = ('foto', GATO, _a[2], _a[3], _a[4], _k); _por_id[_id]['foto'] = 'Daniela com o gato no jardim (foto enviada pela Daniela)'
_por_id['REF-261123']['foto'] = 'Capa: equipe no estúdio (foto enviada pela Daniela). Demais cards só texto.'
_por_id['REF-261225']['foto'] = 'Equipe no estúdio (foto enviada pela Daniela)'

# Louvação de dezembro: sábado, 19/12 (arte enviada pela Daniela)
DATA_DEZ = 'Sábado, 19/12'
FRASE = 'Louvar é agradecer, é honrar e é fortalecer nossa caminhada espiritual.'
def _troca_data(it):
    a = it['arte']
    it['arte'] = ('foto', a[1], a[2].replace(LOUV_DEZ, DATA_DEZ), a[3].replace(LOUV_DEZ, DATA_DEZ), a[4], a[5])
    it['legenda'] = it['legenda'].replace(LOUV_DEZ, DATA_DEZ); it['status'] = 'rascunho'
_troca_data(_por_id['REF-261204'])
_por_id['REF-261204']['legenda'] = _por_id['REF-261204']['legenda'].replace(f'O tema deste encontro: {TEMA_DEZ}.', f'O tema deste encontro: {TEMA_DEZ}.\n\n{FRASE}')
_l = _por_id['REF-261223']; _troca_data(_l)
_a = _l['arte']; _l['arte'] = ('foto', _a[1], 'Amanhã é a última Louvação do ano.', _a[3].replace(DATA_DEZ, 'Sábado, 19/12'), _a[4], _a[5])
_l['legenda'] = _l['legenda'].replace('A última Louvação de 2026 está chegando. 🤍', 'É amanhã: a última Louvação de 2026. 🤍').replace(
    f'E o tema do nosso encontro já chegou: {TEMA_DEZ}.', f'O tema do nosso encontro: {TEMA_DEZ}.\n\n{FRASE}')
_l.update(data='2026-12-18', dia='Sexta', tema='Louvação de dezembro: é amanhã', id='REF-261218')
_x = _por_id['REF-261218']; _x.update(data='2026-12-23', dia='Quarta', id='REF-261223')
_n = _por_id['REF-261127']
_n['legenda'] = _n['legenda'].replace(f'este mês, a nossa é uma {TEMA_NOV}.', f'este mês, a nossa é uma {TEMA_NOV}.\n\n{FRASE}')
ITENS.sort(key=lambda it: it['data'])
_por_id = {it['id']: it for it in ITENS}
FALTA = ['Reels de 27/11, 02/12 e 30/12: a Amanda coloca a música e devolve.',
         'Foto do Jean e a do perfil: Jean pediu para manter como está.']
