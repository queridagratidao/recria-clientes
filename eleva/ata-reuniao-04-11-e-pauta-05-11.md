# Ata — Reunião com Giuliano, 04/11/2026
**RECRIA Marketing**

---

## 1 · Teste do evento (cadastro e contratação de teste)

Não deu tempo de rodar o teste ao vivo na reunião de ontem. Ficou combinado para hoje, 05/11, às 10h, junto com o cadastro do chip.

## 2 · Chip para disparos no WhatsApp (Nextags)

Giuliano já comprou o chip e passou um número para cadastro. Falta fazer, junto com ele, o cadastro desse número dentro da Nextags e do Gerenciador de WhatsApp (Meta), para liberar os disparos. Isso também fica para a reunião de hoje, às 10h.

## 3 · Live com o Jayme — cancelada

Não vai acontecer. O Jayme repassou o convite para os parentes dele, porque o assunto não fez sentido para ele participar.

## 4 · Convidados do ElevaCast — confirmados

Já está tudo certo com os convidados do ElevaCast.

## 5 · Episódio 9 do ElevaCast

Giuliano pediu para alinhar com o pessoal do ProHub. Vamos analisar e dar retorno nos próximos dias.

## 6 · Material de tela para o fundo da sala (ElevaCast)

Giuliano quer passar um material na tela ao fundo da sala durante as gravações — possivelmente um slide intercalando os logos da Eleva (Área Comum - portal do condomínio, Eleva Hub de Negócios). Precisamos verificar com a Rafa como funciona esse formato e como enviar o material para eles. Ponto em aberto, nosso.

## 7 · Vídeos do roteiro

Giuliano ficou de enviar até sexta, 06/11, dois vídeos: um para o ElevaCast e outro para divulgação do portal no Instagram, para edição e publicação nas redes já falando do lançamento na segunda-feira.

## 8 · Projeto da Pati — encaminhado

Giuliano pediu para decidirmos direto com ela. Já foi enviado para a Pati um vídeo explicando o calendário de novembro, dezembro e janeiro, mostrando que o processo é mais simples do que parece. Fica aguardando o retorno dela, validando fotos e conteúdos.

---

# Pauta — Reunião com Giuliano, 05/11/2026, 10h
**RECRIA Marketing**

## 1 · Evento de teste (cadastro e contratação de teste)

Giuliano enviou um roteiro próprio (gerado pelo Claude dele) para conduzir esse teste ao vivo. Seguir esse roteiro na reunião:

- **CompleteRegistration**: ele entra pela página do produto com UTM de teste, aceita os cookies, clica em "Teste grátis" e cria a conta. Conferir se aparece `CompleteRegistration`, origem "Servidor", com e-mail (cifrado) e `fbp` nos dados do evento.
- **Purchase**: ele para de compartilhar a tela e paga uma fatura real de teste, no cartão, 1x. Conferir se aparece `Purchase`, origem "Servidor", com `value = 499` e `currency = BRL` (valor da contratação, não o valor pago com juros).
- **Se algum evento não aparecer**: não repetir o cadastro nem o pagamento, só anotar o horário e olhar a aba "Diagnóstico" do pixel (token inválido, falta de permissão ou evento recusado). Se for problema de token, a Recria gera um novo e o Giuliano cola direto no servidor — sem precisar enviar por mensagem.
- **Depois do teste**: Giuliano retira o código de teste do servidor na sexta, 06/11 (não logo após o teste de hoje). A partir daí os eventos contam como reais. As campanhas começam em 09/11.
- **Pendência nossa após a reunião**: enviar para o Giuliano um ok por escrito confirmando que os dois eventos chegaram certos.

## 2 · Cadastro do chip (Nextags + Meta)

Fazer junto com ele o cadastro do número do chip dentro da Nextags e do Gerenciador de WhatsApp, para liberar os disparos.

## 3 · Pendências em aberto (sem necessidade de cobrar hoje, só acompanhar)

- Vídeos do roteiro (ElevaCast + Instagram) — prazo dele: até sexta, 06/11.
- Episódio 9 do ElevaCast — aguardando nosso retorno após falar com o ProHub.
- Material de tela para o fundo da sala — aguardando verificação nossa com a Rafa.
- Projeto da Pati — aguardando retorno dela sobre o calendário enviado.
