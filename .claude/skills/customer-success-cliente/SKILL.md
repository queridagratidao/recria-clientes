---
name: customer-success-cliente
description: Customer Success da Recria. Define e analisa a pesquisa de satisfacao dos clientes (mensal ou a cada 2 meses), calcula a saude de cada cliente (verde, amarelo, vermelho) a partir de pesquisa, resultados, atrasos e pagamento, e dispara alerta quando o projeto esta em risco, com mensagem sugerida para a Amanda chamar no WhatsApp. Use no fim de cada mes e quando houver sinal de problema.
---

# Customer Success

## Passo 0
Leia `[pasta]/conteudo/contexto.md`, `[pasta]/conteudo/decisoes.md`, o ultimo `resultados/AAAA-MM.md` e `relatorio-cliente-AAAA-MM.md`, e o historico em `[pasta]/cs/` (se existir). Pergunte sobre pagamentos em atraso, atrasos de aprovacao ou gravacao e qualquer contato recente fora do padrao.

## Pesquisa de satisfacao
Frequencia sugerida: mensal para clientes novos (primeiros 3 meses), depois a cada 2 meses. Curta (3 minutos):
1. De 0 a 10, quanto voce recomendaria a Recria? (NPS)
2. De 0 a 10, quanto voce esta satisfeito com os resultados ate agora?
3. De 0 a 10, como esta a nossa comunicacao e o cumprimento de prazos?
4. O que esta funcionando melhor?
5. O que precisa melhorar?
6. Tem algo que voce gostaria que fizessemos e nao estamos fazendo?
Modelo e envio: Google Forms ou formulario similar com link no e-mail ou WhatsApp; respostas em planilha.

## Saude do cliente (revisar todo mes)
- **Verde**: NPS 9 a 10, entregas e aprovacoes em dia, resultado perto ou acima da meta, pagamento em dia.
- **Amarelo**: NPS 7 a 8 ou queda de 2+ pontos; 1 atraso de aprovacao ou gravacao; resultado abaixo da meta por 1 mes; pergunta sobre preco ou escopo.
- **Vermelho**: NPS 0 a 6; resposta com reclamacao ou ameaca de cancelar; 2+ atrasos seguidos; resultado abaixo da meta por 2 meses; pagamento atrasado; silencio por mais de 2 semanas.

## Alertas
Quando amarelo ou vermelho, gere um aviso para a Amanda com: cliente, nivel, motivo, o que aconteceu nos ultimos 30 dias, risco (inclui fim da vigencia do contrato) e **mensagem sugerida para ela chamar no WhatsApp** (tom do cliente, curta, que abra a conversa sem ser defensiva). Nao envie mensagem ao cliente: quem chama e a Amanda.

## Playbook para risco
Ouvir primeiro; reconhecer o problema; propor 1 a 2 ajustes concretos com data; checar o escopo e o contrato; agendar uma conversa curta; registrar em `decisoes.md`.

## Automacao (o que e possivel)
- Envio automatico de e-mail da pesquisa e a coleta exigem uma ferramenta conectada (Google Forms, e-mail, CRM). Se nao houver conector ativo, a skill redige o e-mail e o formulario, e a Amanda envia.
- Posso rodar a analise das respostas quando a planilha for colada ou exportada, e agendar um lembrete mensal.

## Entrega
`[pasta]/cs/AAAA-MM.md` (respostas, NPS, saude, alertas, acoes) e um painel geral em `cs/painel-AAAA-MM.md` com todos os clientes por cor.
