# Fluxo Automático de Recepção no WhatsApp — Nextags
**RECRIA Marketing, 27/11/2026**

---

## Resumo: sim, dá para fazer

Dá para criar um fluxo automático sem IA na Nextags, que responde quem chama a Eleva primeiro, com botões, sem custo extra por mensagem. Veja como funciona a cobrança e o prazo:

- **Quando a pessoa chama a Eleva primeiro** (mensagem espontânea, de forma natural dela): a gente consegue responder automaticamente, com botões e tudo, **sem pagar nada a mais**. É um fluxo de recepção, não precisa de aprovação da Meta.
- **Quando é a Eleva quem inicia o contato** (um disparo, como o Nextags de 1000 contatos): aí sim precisa de um modelo de mensagem aprovado pela Meta, e tem custo por mensagem enviada.
- **Janela de 24 horas**: assim que a pessoa toca num botão ou responde qualquer coisa, abre uma janela de 24 horas onde a conversa fica livre (seja com o fluxo automático, seja com uma pessoa). Se passar 24 horas sem a pessoa responder, a conversa trava, e só reabre com um novo disparo aprovado pela Meta.

## Onde aprender a montar, passo a passo

A própria Nextags tem um tutorial oficial, com vídeo e texto, explicando exatamente como montar esse fluxo de recepção sem IA:

**https://ajuda.nextags.com.br/fluxos-de-conversa/como-criar-um-fluxo-de-boas-vindas-e-recepcao-de-clientes-sem-ia**

## Quem monta o fluxo

Pode ser a Amanda, pode ser o Giuliano, ou o Giuliano pode montar do jeito que achar melhor e mandar pra Amanda revisar e ajustar. O importante é ter esse fluxo pronto e publicado antes das pessoas começarem a responder os disparos do Nextags, pra já cair automaticamente nele.

## Sugestão de fluxo ideal

**Mensagem inicial** (bloco "Lista de Opções", até 4 botões):

1. Achei legal o Área Comum, mas tenho uma dúvida
2. Quero saber mais sobre os outros serviços da Eleva
3. Quero testar grátis agora
4. Falar direto com alguém da Eleva

### Rota 1 — "Tenho uma dúvida sobre o Área Comum"

Envia uma mensagem padrão com as principais dúvidas resumidas (ex: como funciona o teste grátis, o que o sistema entrega, se precisa de cartão de crédito). Se a dúvida da pessoa não for resolvida com isso, o fluxo transfere a conversa para o Giuliano (ação de "Atribuir conversa a um administrador" + "Transferir conversa para humano").

### Rota 2 — "Quero saber mais sobre os outros serviços da Eleva"

Envia uma mensagem explicando o ecossistema:

> "A Eleva é um ecossistema com 4 frentes: **Eleva Sistemas** (o Área Comum, portal do condomínio), **Eleva Expansão Estratégica** (cursos, treinamentos, sessão estratégica, diagnóstico e mentoria), **Eleva Corretora de Seguros** (serviço de seguros para condomínio), e **Eleva Hub de Negócios** (rede de parceiros do ramo condominial). Digite qual dessas opções você quer saber mais."

Conforme a pessoa escolher, o fluxo manda mais detalhes daquela frente específica. Se a dúvida não for resolvida pelo fluxo, direciona para o comercial (a Geórgia, se ela ficar responsável por isso) ou para o Giuliano.

### Rota 3 — "Quero testar grátis agora"

Manda direto o link de cadastro do Área Comum.

### Rota 4 — "Falar direto com alguém da Eleva"

Transfere direto para o Giuliano (ou pra Geórgia, dependendo de quem for responsável pelo atendimento comercial).

---

Em todas as rotas, sempre deixar um botão de "Voltar ao menu principal", pra pessoa não ficar presa num caminho sem saída.
