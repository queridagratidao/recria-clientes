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
