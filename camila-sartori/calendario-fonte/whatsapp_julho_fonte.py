# -*- coding: utf-8 -*-
# JULHO 2026 - GRUPO DE WHATSAPP - Jornada AME-SE
# 3 conteúdos/semana: 2 reposts do Instagram (mesmo dia do post) + 1 exclusivo (segunda/terça).
# Grupo começa a ser alimentado via automação a partir dos posts de 22/07 e 24/07 do Instagram.
#
# PENDENTE PARA AGOSTO: definir com a Camila um termo específico para chamar as pessoas do
# grupo (testadas e recusadas: "Jornadeiras", "Tribo AME-SE", "Time AME-SE", "Amêsianas").
# Por enquanto, usar apenas "mulheres" / "mulher".

add_month("Grupo de WhatsApp - Julho 2026 (últimas 2 semanas)")

add_week("SEMANA 3 · 20 a 26/07")

add_day("24/07 (SEX), Boas-vindas ao grupo (roteiro para a Camila gravar)", [
    dict(time="18h", channel="WHATSAPP", tipo="EXCLUSIVO (vídeo de boas-vindas)",
         formato="Vídeo curto gravado pela Camila",
         cenario="Sentada, tom acolhedor, boa luz e áudio.",
         headline=None, subheadline=None, cta=None,
         label_legenda="ROTEIRO DE VÍDEO:",
         legenda="Oi, que bom ter você aqui. Meu nome é Camila, sou psicóloga há quase dez anos, mestre em Psicologia Clínica e atualmente doutoranda. Criei esse espaço, esse grupo VIP, para compartilhar com vocês de maneira mais próxima, alguns conteúdos exclusivos, sobre autoconhecimento, autoestima e relacionamentos. Do mesmo jeito que eu trabalho na minha prática individual, como psicóloga, só que aqui em um contexto de grupo. Por isso, vou trazer sempre percepções mais gerais, já que aqui temos várias pessoas, em vários momentos, com várias trajetórias diferentes. Deixando claro que esse grupo não substitui um atendimento psicológico individual e personalizado. Aqui eu vou trazer reflexões, técnicas, bastidores, materiais de estudo que eu não posto em nenhum outro lugar. Fico muito feliz que você tenha se permitido começar, ou se aprofundar na sua jornada de autoconhecimento. Contem comigo! Nos próximos dias vocês já vão ver alguns conteúdos bem interessantes por aqui, um ótimo dia!",
         observacao="Primeiro conteúdo do grupo. Postar depois que os posts de 22/07 e 24/07 do Instagram já tiverem tido tempo de trazer gente para o grupo via automação."),
])

add_week("SEMANA 4 · 27/07 a 02/08")

add_day("27/07 (SEG), Reflexão + enquete — texto pronto para copiar e colar no grupo", [
    dict(time="09h", channel="WHATSAPP", tipo="EXCLUSIVO (reflexão + enquete)",
         formato="Mensagem de texto + Enquete do WhatsApp (3 ações, enviar nessa ordem)",
         headline=None, subheadline=None, cta=None,
         acoes=[
             dict(label="Mensagem de reflexão",
                  texto="Bom dia / Boa tarde / Boa noite! Uma pergunta simples para começar a semana: quando foi a última vez que você fez alguma coisa só porque queria, sem pensar primeiro no que os outros iam achar?"),
             dict(label="Pergunta de transição",
                  texto="Além disso, para eu conhecê-las melhor e assim, direcionar conteúdos que façam mais sentido para vocês, responde a essa enquete:"),
             dict(label="Enquete",
                  texto='"Você entrou nesse grupo por qual motivo?"\nOpções: Quero trabalhar minha autoestima / Quero entender melhor meus relacionamentos / Quero aprender mais sobre autoconhecimento / Tenho curiosidade sobre terapia do esquema e TCC / Só quero acompanhar o conteúdo.'),
         ]),
])

add_day("29/07 (QUA), Repost — texto pronto para copiar e colar no grupo", [
    dict(time="09h", channel="WHATSAPP", tipo="REPOST (Instagram 29/07, mesmo dia)",
         formato="Texto de chamada + Repost (2 ações, enviar nessa ordem)",
         headline=None, subheadline=None, cta=None,
         acoes=[
             dict(label="Texto de chamada (enviar antes do repost)",
                  texto="Mulheres, vocês já se pegaram respondendo sim quando na verdade queriam dizer não? Pois é, quanto mais a gente faz isso, mais acaba se anulando, se invalidando. Eu me aprofundo nessa temática no post de hoje, no link abaixo 👇🏻"),
             dict(label="Repost do Instagram",
                  texto='Repostar o post estático de 29/07, com a mesma arte e legenda do Instagram: "Toda vez que você diz sim para todo mundo, talvez esteja dizendo não para você mesma..."'),
         ]),
])

add_day("31/07 (SEX), Repost — texto pronto para copiar e colar no grupo", [
    dict(time="09h", channel="WHATSAPP", tipo="REPOST (Instagram 31/07, mesmo dia)",
         formato="Texto de chamada + Repost (2 ações, enviar nessa ordem)",
         headline=None, subheadline=None, cta=None,
         acoes=[
             dict(label="Texto de chamada (enviar antes do repost)",
                  texto="Mulheres, vocês já repararam que, quando um relacionamento começa a dar certo de verdade, uma parte de vocês fica desconfiada? Pois é, isso também pode ser uma crença limitante. Eu me aprofundo nessa temática no post de hoje, no link abaixo 👇🏻"),
             dict(label="Repost do Instagram",
                  texto='Repostar o reel de 31/07, com o mesmo vídeo e legenda do Instagram: "Você já reparou que, quando um relacionamento começa a dar certo de verdade..."'),
         ],
         observacao='PENDENTE PARA AGOSTO: definir com a Camila um termo específico para chamar as pessoas do grupo (testadas e recusadas: Jornadeiras, Tribo AME-SE, Time AME-SE, Amêsianas). Por enquanto, usar apenas "mulheres"/"mulher".'),
])
