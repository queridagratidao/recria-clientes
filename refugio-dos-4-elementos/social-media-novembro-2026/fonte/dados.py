"""Dados do calendario de novembro/2026, Refugio dos 4 Elementos. Fonte unica para o .md e o feed simulado."""

WHATSAPP_AGENCIA = ''  # numero da Recria para receber aprovacoes (ex.: 5551999999999). Vazio = so copia o texto.

PERFIL = {
    'usuario': 'refugiodos4elementos',
    'nome': 'Refúgio dos 4 Elementos | Terapias',
    'categoria': 'Terapeuta',
    'bio': 'Terapias Integrativas & Espirituais\nConstelação Familiar | Reiki | Aromaterapia\nImersão na Cachoeira com os 4 Elementos...',
    'posts': 210, 'seguidores': 163, 'seguindo': 205,
}

ITENS = [
  {
    'id': 'REF-2611-01', 'data': '2026-11-04', 'dia': 'Quarta', 'tipo': 'estatico', 'status': 'agendado',
    'tema': 'Mito e Verdade · Constelação Familiar',
    'objetivo': 'Engajamento (comentário de dúvida)',
    'imagens': ['post01_04-11_mito-verdade-constelacao.jpg'],
    'legenda': """Mito. Constelação Familiar é basicamente uma conversa guiada, parecida com uma terapia de aconselhamento comum.

Não é bem assim. A Constelação usa representações, outras pessoas (ou objetos, em sessões individuais) ocupam o lugar de membros da sua família, e o que se revela através desse movimento vai muito além do que qualquer conversa alcançaria.

Muita gente descreve a sensação de ver fisicamente uma dinâmica que só sentia por dentro, sem nunca ter conseguido explicar em palavras.

Não é terapia de conversa. É um método próprio, com técnica e lógica bem definidas.

Tem outra dúvida sobre como funciona a Constelação? Comenta aqui embaixo que a gente responde.

📍 Cuiabá/MT e online""",
    'automacao': 'nenhuma (post de engajamento)',
    'nota': 'Sobra de outubro, já agendado pela Amanda. Confirmar se é este o post (suposição: o de 16/10 não aparece no feed).',
  },
  {
    'id': 'REF-2611-02', 'data': '2026-11-06', 'dia': 'Sexta', 'tipo': 'estatico', 'status': 'pendente',
    'tema': 'Louvação · Novembro',
    'objetivo': 'Evento do mês (oferta)',
    'imagens': ['post02_06-11_louvacao-novembro.jpg'],
    'foto': 'Daniela em oração (foto 182)',
    'legenda': """Uma vez por mês, abrimos as portas para um encontro coletivo de oração, gratidão e cura espiritual, aberto a qualquer pessoa, independente de religião ou crença.

É uma noite de cantos, reflexões, momentos de silêncio e oração coletiva, pensada para cuidar do ser de forma integral: corpo, mente e espírito.

[DATA E DIA DA SEMANA A CONFIRMAR], no Quintal de Ogum, em Cuiabá.

Quer saber o horário e como participar? Comenta LOUVAÇÃO aqui embaixo que a gente te manda tudo no direct.

📍 Cuiabá/MT""",
    'automacao': 'LOUVAÇÃO',
    'nota': 'Regra fixa: 1ª sexta do mês = Louvação. Falta a data/tema de novembro (pedido à Amanda). Arte e legenda têm o campo [DATA A CONFIRMAR]. Mantém o padrão de outubro: sem citar a medicina no feed.',
  },
  {
    'id': 'REF-2611-03', 'data': '2026-11-11', 'dia': 'Quarta', 'tipo': 'carrossel', 'status': 'rascunho',
    'tema': 'Para quem é (e para quem não é) o Refúgio',
    'objetivo': 'Alcance (salvar e compartilhar) + qualificação de lead',
    'imagens': ['post03_11-11_carrossel-capa.jpg'] + [f'post03_11-11_carrossel-card{i}.jpg' for i in range(2, 9)],
    'foto': 'Capa: Daniela de braços cruzados (foto 211). Demais cards só texto.',
    'legenda': """Antes de qualquer coisa, a gente prefere ser honesto com você.

O Refúgio é um espaço de acolhimento, sem julgamento e sem pressa. Mas ele não é pra todo mundo, e tá tudo bem.

É pra você que sente um peso que não sabe nomear, que vive repetindo as mesmas histórias, que está atravessando um momento difícil ou que simplesmente tem curiosidade e muitas dúvidas.

Não é pra quem procura cura milagrosa, com prazo marcado, nem pra quem busca o ritual de uma religião específica. Aqui o trabalho é universalista e o cuidado acontece em processo, no seu tempo.

E se você está em crise aguda, o primeiro passo é procurar atendimento médico de urgência. A gente segue aqui depois.

Se você se reconheceu, salva esse post e manda pra alguém que precisa ler isso hoje. E se quiser conversar, comenta REFÚGIO que a gente te chama no direct.

📍 Cuiabá/MT e online""",
    'automacao': 'REFÚGIO',
    'nota': 'Único carrossel do mês. Conteúdo vem da seção "Para quem é / não é" do site, ainda não usada no feed. Molde: identificação + qualificação.',
  },
  {
    'id': 'REF-2611-04', 'data': '2026-11-13', 'dia': 'Sexta', 'tipo': 'estatico', 'status': 'rascunho',
    'tema': 'Quem cuida de você · Jean Carlos',
    'objetivo': 'Conexão e autoridade da equipe',
    'imagens': ['post04_13-11_prazer-jean.jpg'],
    'foto': 'Jean no jardim, sorrindo (foto 329)',
    'legenda': """O Refúgio não é uma pessoa só. É uma equipe, e a gente quer que você conheça quem vai te receber.

Esse é o Jean Carlos Amorim.

✦ Constelador Sistêmico Familiar (Curso Avançado, ALMT)
✦ Analista Visual, Sistêmico e Comportamental
✦ Mestre em Reiki
✦ Condutor de Meditação
✦ Cromoterapeuta

No Refúgio, o Jean conduz sessões de Constelação Familiar e Reiki, sempre com o mesmo cuidado: escutar antes de indicar qualquer caminho.

Quer conversar com ele sobre o que você está vivendo? Comenta REFÚGIO que a gente te chama no direct.

📍 Cuiabá/MT e online""",
    'automacao': 'REFÚGIO',
    'nota': 'Série "Quem cuida de você" (manual de marca: reconhecer a equipe). Credenciais copiadas do site. Validar com o Jean o parágrafo do que ele conduz.',
  },
  {
    'id': 'REF-2611-05', 'data': '2026-11-18', 'dia': 'Quarta', 'tipo': 'estatico', 'status': 'rascunho',
    'tema': 'Como funciona · a conversa antes da sessão',
    'objetivo': 'Valor + quebra de objeção (oferta leve)',
    'imagens': ['post05_18-11_antes-da-sessao.jpg'],
    'foto': 'Joelson pensativo, P&B (foto 59)',
    'legenda': """Aqui ninguém marca uma sessão no escuro.

Antes de qualquer terapia, existe uma conversa. É assim que funciona por aqui:

1. Você chega, do jeito que está, sem precisar ter tudo claro.
2. A gente fala com você pelo WhatsApp pra entender o momento.
3. Um terapeuta da equipe faz uma entrevista prévia com você.
4. Ele indica a terapia que faz mais sentido e vocês combinam o melhor horário.
5. Sua jornada começa, com acompanhamento e no seu ritmo.

Não existe terapia certa pra todo mundo. Existe a terapia certa pro seu momento, e é nessa conversa que a gente descobre qual é.

Comenta REFÚGIO que a gente começa por ela.

📍 Cuiabá/MT e online""",
    'automacao': 'REFÚGIO',
    'nota': 'Os 5 passos são da seção "Como funciona" do site, ainda não usada no feed.',
  },
  {
    'id': 'REF-2611-06', 'data': '2026-11-20', 'dia': 'Sexta', 'tipo': 'estatico', 'status': 'rascunho',
    'tema': 'Ancestralidade · Constelação Familiar',
    'objetivo': 'Alcance (identificação, compartilhamento)',
    'imagens': ['post06_20-11_ancestralidade.jpg'],
    'foto': 'Jean meditando, P&B (foto 237)',
    'legenda': """Antes de você, vieram seus pais. Antes deles, seus avós. E antes ainda, muita gente que você nunca conheceu, mas que de algum jeito continua em você.

No jeito de amar, de reagir, de lidar com dinheiro, de se proteger. Muito do que a gente carrega não começou na gente.

A Constelação Familiar olha pra isso com respeito. Não pra encontrar culpados, mas pra reconhecer o lugar de cada um e devolver o que não é seu.

Honrar quem veio antes também é uma forma de cuidar de si, e de abrir caminho pra quem vem depois.

Qual história da sua família você sente que ainda carrega? Se quiser conversar sobre isso, comenta CONSTELAÇÃO.

📍 Cuiabá/MT e online""",
    'automacao': 'CONSTELAÇÃO (palavra nova, criar na automação) ou trocar por REFÚGIO',
    'nota': '20/11 é feriado nacional (Dia da Consciência Negra). O tema de ancestralidade conversa com a data sem usar a data como gancho. Se a cliente quiser citar o dia, incluir uma linha na legenda, com cuidado para não soar oportunista.',
  },
  {
    'id': 'REF-2611-07', 'data': '2026-11-25', 'dia': 'Quarta', 'tipo': 'estatico', 'status': 'rascunho',
    'tema': 'Quem cuida de você · Daniela e Joelson',
    'objetivo': 'Conexão, confiança e história da marca',
    'imagens': ['post07_25-11_cofundadores.jpg'],
    'foto': 'Joelson aplicando passe em Daniela (foto 283)',
    'legenda': """Todo refúgio começa com alguém que decidiu abrir a porta.

O nosso começou com a Daniela e o Joelson, que há 3 anos recebem pessoas carregando histórias, medos e padrões que já não fazem mais sentido.

Daniela Sampaio
✦ Consteladora Sistêmica Familiar (Curso Avançado, ALMT)
✦ Aromaterapeuta e Cristaloterapeuta
✦ Reikiana e Passe Energético

Joelson Sampaio
✦ Constelador Sistêmico Familiar (Curso Avançado, ALMT)
✦ Aromaterapeuta e Cristaloterapeuta
✦ Reikiano Fitoterápico e Passe Energético
✦ Terapeuta em Cachoeira

Hoje o Refúgio é uma equipe, mas a essência continua a mesma do primeiro dia: acolher sem julgamento, com técnica e no tempo de cada pessoa.

Comenta REFÚGIO se quiser conversar com a gente.

📍 Cuiabá/MT e online""",
    'automacao': 'REFÚGIO',
    'nota': 'Credenciais do site. Ficaram de fora "Guardiã(o) da Medicina Ayahuasca" e "Quintal de Ogum" para manter o cuidado do feed com o tema (contexto do cliente). Validar com eles.',
  },
  {
    'id': 'REF-2611-08', 'data': '2026-11-27', 'dia': 'Sexta', 'tipo': 'estatico', 'status': 'rascunho',
    'tema': 'Processo e pacotes (dia da Black Friday)',
    'objetivo': 'Oferta direta, sem urgência agressiva',
    'imagens': ['post08_27-11_processo.jpg'],
    'foto': 'Joelson com as mãos em passe (foto 219)',
    'legenda': """Hoje o mundo inteiro está correndo atrás de desconto relâmpago. A gente vai no sentido contrário.

Transformação de verdade não acontece numa sessão só, nem cabe numa contagem regressiva. Ela acontece em processo, com constância e acompanhamento.

Por isso, no Refúgio, o desconto não é de um dia: quanto maior o pacote de sessões, maior o desconto. E dá pra pagar no Pix, no cartão ou parcelado.

Quer entender qual pacote faz sentido pro seu momento? Comenta REFÚGIO que a gente te explica tudo no direct, sem pressão.

📍 Cuiabá/MT e online""",
    'automacao': 'REFÚGIO',
    'nota': 'Black Friday cai em 27/11. Postura anti-urgência combina com o manual de marca. Não citar percentual sem a cliente confirmar os valores dos pacotes. Respeitar a capacidade da agenda: se lotar, trocar CTA por lista de espera.',
  },
]

STORIES = [
  {'id': 'REF-2611-S1', 'titulo': 'Bastidores do ensaio', 'telas': [
      'Foto do ensaio + "Fizemos fotos novas pra você conhecer quem cuida de você"',
      'Enquete: "Qual terapia você quer conhecer melhor?" (Constelação / Reiki)',
      'Sticker de link para o WhatsApp: "Quer conversar? Chama aqui"'],
   'nota': 'Usar na semana do post do Jean (13/11).'},
  {'id': 'REF-2611-S2', 'titulo': 'Caixinha de dúvidas', 'telas': [
      '"Manda sua dúvida sobre Constelação Familiar"',
      'Respostas em vídeo curto da Daniela ou do Jean (gravar no celular)'],
   'nota': 'Alimenta o destaque "Dúvidas" e gera pauta para Reels.'},
  {'id': 'REF-2611-S3', 'titulo': 'Lembrete da Louvação', 'telas': [
      'Arte da Louvação + contagem regressiva do Instagram',
      '"Comenta LOUVAÇÃO no post ou chama no direct"'],
   'nota': 'Repostar 2 dias antes da data.'},
]
