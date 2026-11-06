# Ata reunião Recria/Eleva — Amanda e Giuliano
**Ata geral, reuniões/trocas de 04/11, 05/11 e 06/11/2026**

---

## 1 · Teste do evento de conversões

**Em 04/11**: não deu tempo de fazer o teste.

**Em 05/11**: teste realizado. `CompleteRegistration` chegou certinho na Meta, origem "Servidor". `Purchase` não apareceu, mesmo com pagamento aprovado e nota fiscal emitida. Giuliano identificou a causa (a etapa que avisa a Meta não tinha tempo de terminar, logo depois do portal responder à confirmação do Asaas) e já publicou uma correção no portal.

**Em 06/11**: reteste feito, pelo WhatsApp (sem necessidade de call). Giuliano pagou uma nova compra de teste, e o `Purchase` apareceu certinho na aba "Eventos de teste", com a Meta confirmando o recebimento. **Teste concluído com sucesso.** Giuliano já removeu o `test_event_code` do servidor — a partir de agora, cadastros e compras do portal vão direto para a campanha.

Conferido também na "Visão geral" do Gerenciador de Eventos (filtro 05/11 a 06/11): `Compra` com 2 eventos, `Concluir inscrição` com 1 evento, todos via API de Conversões. Qualidade de correspondência atual: 3.2/10 — fica como melhoria futura (hash de telefone, nome, external_id e dados do navegador), já combinada para depois do lançamento.

**Sem pendência** — teste concluído.

## 2 · Chip para disparos no WhatsApp (Nextags)

**Em 04/11**: Giuliano já tinha comprado o chip e passado o número, mas não deu tempo de fazer o cadastro.

**Em 05/11**: cadastro concluído. Número **+55 51 9375-0621** cadastrado na Nextags e vinculado à Plataforma API do WhatsApp Business. Também foi cadastrado o cartão de cobrança (Mastercard final **6454**) no Gerenciador do WhatsApp, cobrindo os custos dos disparos.

> ⚠️ Esse número não pode, em hipótese alguma, ser vinculado a nenhum WhatsApp comum (nem pessoal, nem Business via app de celular) — senão a API cai e o número perde a conexão com a Nextags.

A Nextags não tem aplicativo de celular — o acesso é só pelo navegador (celular ou computador), com login no Gmail do Eleva Marketing (`eleva.gs@gmail.com`), pelo link https://nextags.com.br/. É por essa tela que o Giuliano deve responder as pessoas que receberem o disparo.

**Sem pendência** — cadastro completo.

## 3 · Live com o Jayme

**Em 04/11**: Giuliano e Jayme se reuniram para alinhar a parceria.

**Em 05/11**: live cancelada. Giuliano passou o contato do Jayme para os próprios parentes, para que eles façam a parceria com ele — o assunto que o Jayme quer abordar não fez sentido para o Giuliano no momento.

## 4 · ElevaCast — episódios 8 e 9 e material de tela

**Em 04/11**: convidados do ElevaCast confirmados. Episódio 9 ainda pendente de alinhamento com o ProHub e o Rene.

**Em 05/11**: o Rene respondeu e já subiu os episódios 8 e 9 no YouTube. Amanda programou o episódio 8 para sair hoje, 05/11, às 19h, no YouTube, com divulgação no Instagram; e o episódio 9 para sair em 07/12, às 19h, também no YouTube com divulgação no Instagram. O ProHub também respondeu hoje sobre o material de tela de fundo das gravações: Amanda vai providenciar um vídeo em MP4, rodando em loop os logos da Eleva, cada logo ficando pelo menos 10 segundos antes de trocar para o próximo — vai aprovar com o Giuliano antes de enviar ao ProHub.

**Sem pendência** — só falta aprovar o vídeo com o Giuliano e enviar ao ProHub.

## 5 · Vídeos do roteiro

**Em 04/11 e 05/11**: Giuliano ficou de enviar até sexta, 06/11, os vídeos para o ElevaCast e para divulgação do portal no Instagram.

**Falta para 06/11**: receber os vídeos.

## 6 · Lista de síndicos e administradoras para disparo

**Em 05/11**: Giuliano enviou a lista atualizada de síndicos (nome, telefone, e-mail) para subir na Nextags, com disparos previstos para a semana que vem. Ele também está avaliando uma possível lista de administradoras de condomínio para entrar nos disparos.

## 7 · Mensagens de disparo

**Em 05/11**: a Amanda vai configurar as mensagens na Nextags e tentar validar com o Giuliano até amanhã, para aprovação.

## 8 · Segmentação da campanha Meta

**Em 05/11**: Giuliano pediu que a Recria envie a segmentação usada na campanha da Meta (ele havia passado uma lista de regiões prioritárias anteriormente). Pendência da Recria.

---

## Resumo do que ainda está em aberto

- Receber os vídeos do roteiro (Giuliano, prazo 06/11).
- Finalizar e compartilhar as mensagens de disparo na Nextags (Amanda).
- Enviar a segmentação da campanha Meta para o Giuliano (Recria).

## Pedido de apoio ao Giuliano

Conversar com a Pati sobre a continuidade do projeto dela e trazer um retorno ainda essa semana. Já temos material pronto para novembro, dezembro e janeiro — precisamos saber o que fazer com esse material, principalmente o de novembro, para programar sem perder tempo.
