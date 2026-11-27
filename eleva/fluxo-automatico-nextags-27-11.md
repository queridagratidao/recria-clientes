# Fluxo Automático Nextags — Eleva

Sim, o plano atual da Nextags já permite criar esse fluxo automático, com ou sem IA. Importante: não é um fluxo "dentro do WhatsApp" em si, é montado na ferramenta Nextags, e a pessoa recebe a resposta no WhatsApp dela do outro lado.

- **Quando a pessoa chama a Eleva primeiro** (mensagem espontânea): dá para responder automaticamente, com botões, sem custo além da mensalidade da ferramenta. É um fluxo de recepção, não precisa de aprovação da Meta.
- **Imagem junto com o botão, no fluxo de resposta**: mensagem com botão funciona confirmado (direciona para a opção A, B etc). Ainda falta confirmar se dá para mandar imagem junto nesse tipo de resposta automática — segue em verificação.
- **Quando é a Eleva quem inicia o contato** (um disparo, como o Nextags de 1000 contatos): aí sim precisa de modelo aprovado pela Meta, com imagem e texto juntos, e tem custo por mensagem enviada.
- **Janela de 24 horas**: assim que a pessoa toca num botão ou manda mensagem, abre uma janela de 24h de conversa livre, sem custo além da mensalidade. Passando 24h sem resposta, a caixa fecha, e só reabre com um novo disparo aprovado pela Meta, ou quando a própria pessoa manda mensagem de novo.
- **Número vinculado à Nextags** (+55 51 93750621): é esse que recebe tudo. Não pode abrir o WhatsApp comum (app ou Web) nesse número, porque derruba toda a automação. Tudo deve ser acompanhado pela caixa de entrada dentro do site da Nextags (não tem aplicativo próprio, só navegador, pelo computador ou celular).

## Como montar, e quem monta

A Nextags tem um tutorial oficial, com vídeo e texto, mostrando passo a passo como montar um fluxo de recepção sem IA, veja no link:

[Como criar um fluxo de boas-vindas e recepção de clientes sem IA](https://ajuda.nextags.com.br/fluxos-de-conversa/como-criar-um-fluxo-de-boas-vindas-e-recepcao-de-clientes-sem-ia).

O fluxo pode ser automático com a ajuda de uma IA conectada (ChatGPT, Gemini, Claude), ou montado manualmente por nós, cadastrando cada mensagem e botão. Para esse caso (respostas fixas, sem risco de a IA inventar informação que o portal não tem), o ideal é montar manualmente.

Quem monta pode ser a Amanda, o Giuliano, ou o Giuliano monta do jeito que achar melhor e manda para a Amanda revisar. O importante é publicar esse fluxo antes das pessoas começarem a responder aos disparos do Nextags, para já caírem nele automaticamente.

## Quando a pessoa aperta "Falar com o Giuliano"

Depois que o chatbot responder todas as perguntas, se a pessoa ainda disser que quer falar com o Giuliano, há duas opções:

1. **Deixar a conversa em aberto dentro da Nextags**: o fluxo avisa que o Giuliano vai responder em seguida, e a conversa continua ali mesmo. Exige que o Giuliano esteja com a Nextags aberta (no navegador, computador ou celular) em horário comercial, acompanhando a fila.
2. **Botão com mensagem pronta para o WhatsApp pessoal do Giuliano (ou da Eleva)**: a pessoa clica num botão tipo "Gostaria de ser atendido por humano", que a leva direto pro WhatsApp comum do Giuliano ou da Eleva (outro número, não o da Nextags), já com uma mensagem pronta. Aí o atendimento sai da Nextags e vai para esse número normal.

**Atenção**: o número vinculado à Nextags (+55 51 93750621) nunca deve ser aberto no WhatsApp comum (app ou Web) para responder por lá — isso derruba toda a automação. Esse número só deve ser respondido dentro da ferramenta Nextags. Se a opção 2 for escolhida, o atendimento humano precisa ser por outro número (pessoal do Giuliano ou da Eleva), nunca o mesmo do disparo.

## Pendência: e-mail de contato

O fluxo usaria `hub@elevags.com.br` como contato público. Confirmar com o Giuliano se esse é um e-mail novo, já que o que a Eleva usa hoje é ligado ao "Eleva Marketing".

## Sugestão de fluxo ideal

**Mensagem inicial** (bloco "Lista de Opções", até 4 botões):

1. Achei legal o Área Comum, mas tenho uma dúvida
2. Quero saber mais sobre os outros serviços da Eleva
3. Quero testar grátis agora
4. Falar direto com alguém da Eleva

### Rota 1 — "Tenho uma dúvida sobre o Área Comum"

Envia uma mensagem padrão com as principais dúvidas resumidas (ex: como funciona o teste grátis, o que o sistema entrega, se precisa de cartão de crédito). Se a dúvida da pessoa não for resolvida com isso, o fluxo transfere a conversa para o Giuliano.

### Rota 2 — "Quero saber mais sobre os outros serviços da Eleva"

Envia uma mensagem explicando o ecossistema:

> "A Eleva é um ecossistema com 4 frentes: **Eleva Sistemas** (o Área Comum, portal do condomínio), **Eleva Expansão Estratégica** (cursos, treinamentos, sessão estratégica, diagnóstico e mentoria), **Eleva Corretora de Seguros** (serviço de seguros para condomínio), e **Eleva Hub de Negócios** (rede de parceiros do ramo condominial). Digite qual dessas opções você quer saber mais."

Conforme a pessoa escolher, o fluxo manda mais detalhes daquela frente específica. Se a dúvida não for resolvida pelo fluxo, direciona para o comercial (a Geórgia, se ela ficar responsável por isso) ou para o Giuliano.

### Rota 3 — "Quero testar grátis agora"

Manda direto o link de cadastro do Área Comum.

### Rota 4 — "Falar direto com alguém da Eleva"

Transfere direto para o Giuliano (ou pra Geórgia, dependendo de quem for responsável pelo atendimento comercial).

Em todas as rotas, sempre deixar um botão de "Voltar ao menu principal", para a pessoa não ficar presa num caminho sem saída.

## Opções que o Giuliano já havia pedido

Além das 4 rotas sugeridas acima, o Giuliano também havia pedido estas opções no fluxo original, que podem ser incorporadas junto ou no lugar das nossas:

1. Como funciona
2. Quanto custa
3. Criar minha conta
4. Falar com o Giuliano

Dá para combinar as duas listas num menu só, ou manter como rotas adicionais dentro de cada opção.
