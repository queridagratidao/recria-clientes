# E-mail Brevo — Leads sem retorno (Strategia)

**Status:** ENVIADO em 23/11/2026 às 10:59 para 29 destinatários (campanha "23.11.26_Strategia_Leads_julho_novembro_recuperação de contato" no Brevo).
**Público:** leads qualificados que preencheram o formulário do site, mas não responderam ligação nem WhatsApp (Marcella/Beto). Excluir leads fora do perfil (ex.: Rio de Janeiro) e quem já recebeu proposta e fez a assembleia sem chamar a Strategia.
**Ferramenta:** Brevo (plano gratuito, 300 envios/dia)
**Variável de nome:** `{{ contact.NOME }}` (confirmar nome do atributo na conta; fallback: `{{ contact.NOME | default : "tudo bem" }}`)

---

**Remetente:** Marcella | Strategia Síndicos (Brevo substitui o Gmail por @brevosend.com; "responder a" = marketingstrategiasindicos@gmail.com, Amanda encaminha respostas para a Marcella)
**Assunto:** A solução para os problemas do seu condomínio
**Pré-cabeçalho:** Descubra como começar a resolver isso ainda em 2026...

---

**Título:** Ainda dá tempo de garantir um próximo ano mais tranquilo para o seu condomínio

Olá, {{ contact.NOME }}, tudo bem?

Aqui é a Marcella, da Strategia Síndicos Profissionais.

Há um tempo você preencheu nosso formulário mostrando interesse em um síndico profissional para o seu condomínio, e queremos retomar essa conversa com você.

Passamos aqui para lembrar que **ainda dá tempo de garantir que o próximo ano do seu condomínio seja mais tranquilo, organizado e bem gerido.**

Sabemos que trocar a gestão é uma decisão importante e que sempre aparecem dúvidas, suas, do conselho ou dos moradores. Para ajudar nessa decisão, oferecemos:

**Antes de decidir, conheça nosso trabalho, sem compromisso**
- Uma **reunião online**, rápida e no horário que for melhor para você, para uma primeira conversa e para tirar as dúvidas iniciais;
- Uma **reunião presencial** no seu condomínio, com o conselho ou direto com os condôminos, para apresentarmos nosso trabalho e esclarecermos todas as dúvidas;
- Se vocês já têm **data de assembleia** marcada, podemos fazer essa conversa antes dela ou, se preferirem, participar da própria assembleia para responder às perguntas ali mesmo.

Há 11 anos, a Strategia cuida de condomínios residenciais e comerciais com atenção à legislação, PPCI, laudos técnicos (marquises, sacadas, medicina do trabalho), controle de consumo de água, revisão de contratos para reduzir custos, acompanhamento da inadimplência e imparcialidade na resolução de conflitos.

Para agendar, é só responder este e-mail dizendo se prefere a reunião online ou presencial e o melhor dia e horário, ou falar comigo direto pelo WhatsApp:

**[BOTÃO com ícone do WhatsApp: Falar com a Marcella no WhatsApp]**
_Clique para abrir o WhatsApp e agendar sua reunião online ou presencial_

Link do botão:
```
https://wa.me/5551994851548?text=Ol%C3%A1%2C%20Marcella!%20Recebi%20o%20e-mail%20da%20Strategia%20e%20quero%20agendar%20uma%20reuni%C3%A3o%20sobre%20o%20meu%20condom%C3%ADnio.
```
Mensagem pronta: "Olá, Marcella! Recebi o e-mail da Strategia e quero agendar uma reunião sobre o meu condomínio."

Vai ser um prazer conversar com você e conhecer o seu condomínio.

Abraço,
**Marcella**
Strategia Síndicos Profissionais

**Rodapé:** ícones Instagram + WhatsApp · @strategiasindicos · (51) 99485-1548 · link de descadastro

---

## Montagem no Brevo (como foi enviado)
1. Imagem: cabeçalho com logo + título
2. Texto: saudação com variável NOME até "...oferecemos:"
3. Imagem: bloco das reuniões
4. Texto: "Há 11 anos..." até "...WhatsApp:"
5. Imagem: botão "Falar com a Marcella no WhatsApp" (link wa.me acima)
6. Texto: "Vai ser um prazer..." + assinatura
7. Bloco Redes sociais (Facebook + Instagram)
8. Imagem: faixa azul com aviso "Você recebeu este e-mail porque preencheu o formulário..."

## Aprendizados para os próximos disparos
- A base foi importada com o nome completo no atributo NOME; nos próximos, subir só o primeiro nome
- Remetente @gmail.com é substituído por @brevosend.com e cai em Promoções; ideal autenticar o domínio strategiasindicos.com.br
- Imagens em 1200 px de largura, sem margem branca lateral, para alinhar com os blocos de texto
- Laranja oficial: #EA2F06; azul do logo: #001F4A

## Pendências antes do disparo (histórico)
- Confirmar número do WhatsApp da Marcella (usado 51 99485-1548 — o informado tinha 8 dígitos)
- Confirmar @ do Instagram (@strategiasindicos)
- Trocar o logo em texto pelo arquivo oficial no Brevo

## Próximos e-mails sugeridos (Marcella)
- Leads antigos (base de anos anteriores): "Você está satisfeito com o seu síndico atual?" + convite para seguir no Instagram e marcar reunião; segmentar por mês de assembleia
- Lembrete ~1 mês antes da assembleia de cada condomínio para quem não fechou este ano
