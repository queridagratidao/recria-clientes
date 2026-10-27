# Retorno consolidado — v5 (22/10) e v1 (25/10)
**RECRIA Marketing, 27/10/2026**
**Este documento responde, num lugar só, tanto a "Resposta ao retorno da Recria" (v5, 22/10) quanto a "Medição de conversões na Meta — perguntas à agência" (v1, 25/10).**

---

## 1 · Sobre o Pixel e o Tag Manager (segue do v5)

Você perguntou: *"vocês têm acesso ao Tag Manager da Eleva para fazer isso daí? Se não, fazemos daqui."*

Sim, temos acesso — criamos um container próprio na conta **Eleva Marketing** (e-mail `eleva.gs@gmail.com`), e já usamos ele para instalar o Pixel (detalhes abaixo). Você também pode acessar esse container, entrando em tagmanager.google.com com esse e-mail.

*(O container antigo, de outra agência, não estava mais instalado em nenhuma página do site — por isso optamos por montar um novo do zero, em vez de tentar recuperar acesso ao antigo.)*

**O que já fizemos (27/10):**
1. Criamos o container `GTM-TPTQTWJK`, na conta Eleva Marketing.
2. Instalamos dentro dele duas tags do Pixel da Meta (ID `634359929729484`):
   - Uma tag base, disparando o evento padrão `PageView` em todas as páginas.
   - Uma tag de evento customizado `CliqueTesteGratis`, disparando quando alguém clica em qualquer botão que leva para `portal.elevags.com.br/entrar`.
3. Publicamos o container (versão ativa).
4. Criamos as duas ações de conversão do tipo Importação no Google Ads: **"Área Comum · conta criada"** e **"Área Comum · assinatura"**.

O passo a passo técnico completo do que falta instalar no portal está no documento em anexo, "Instruções para o Claude do Giuliano — Instalação do Tag Manager".

---

## 2 · Respondendo às 3 perguntas do v1

### Pergunta 1 — Vamos usar o envio de conversões do portal para a Meta? Quais eventos?

Sim, os dois eventos — cadastro e assinatura. Mas é importante reforçar um ponto, de novo, porque o documento ainda chama o evento de cadastro de **"Lead"**, e esse não é o nome certo pro nosso caso.

Pensa no exemplo de vocês mesmos, da Eleva Estratégia: lá, "Lead" faz sentido, porque a pessoa preenche um formulário no site e **o Beto responde ela depois, manualmente, pelo WhatsApp** — é um contato que ainda precisa de alguém do outro lado pra avançar.

No Área Comum **não é assim**: a pessoa faz o cadastro sozinha, sem falar com ninguém — ela mesma cria a conta e já começa a usar o teste grátis. Não existe uma etapa de "alguém vai responder essa pessoa depois". Por isso, o nome certo do evento de cadastro é **`CompleteRegistration`**, não `Lead`. Só depois disso — e aí sim, até 30 dias depois — a gente puxa quem, desses cadastros, virou de fato assinante pagante (a "janela de atribuição" que já tínhamos combinado).

Resumindo os três eventos certos:
- Clique no botão "Começar teste grátis" → `CliqueTesteGratis`
- Conta criada (teste grátis iniciado) → `CompleteRegistration`
- Assinatura paga (até 30 dias depois) → `Purchase`

### Pergunta 2 — Em qual portfólio empresarial estão o Pixel, a conta de anúncios e o Instagram? Quem é o dono?

Conferimos agora no Gerenciador de Negócios. O portfólio se chama **"Eleva"**, e dentro dele:

- **Pessoas com acesso total**: Amanda Moraes (`queridagratidao@gmail.com`) e **René Kasper**.
- **Parceiros (empresas com acesso)**: **Considere Feito** (com acesso total à Página do Facebook, à Conta de Anúncios e ao Instagram, todos sob o nome "Eleva Expansão Estratégica" / `eleva.gs`), além de Fator.ag, Giuliano Spolavori, Kommo e Solutions Engineering Team.

René Kasper e a Considere Feito parecem ser da **agência anterior** — a Amanda já está revisando esses acessos (inclusive removendo o acesso de faturamento que a agência antiga ainda tinha). Como você pediu que os ativos fiquem em nome da Eleva, com a Recria como parceira: podemos organizar isso juntos — ou você prefere que a Amanda já remova o acesso da Considere Feito/René Kasper, deixando só Eleva (dono) e Recria (parceira)? Precisamos do seu ok antes de remover o acesso de terceiros.

### Pergunta 3 — A Meta conta a mesma compra só uma vez, se enviada duas vezes com o mesmo identificador?

Sim — esse é exatamente o propósito do `event_id`: quando o mesmo `event_id` chega duas vezes para a Meta, ela reconhece e conta como um evento só, não em dobro. Mesmo assim, concordamos com fazer o teste técnico antes de ligar de vez (como vocês propuseram), pra confirmar isso na prática antes de qualquer coisa valer como conversão real.

---

## 3 · Sobre os pedidos do v1

- **Acesso de administrador para a Eleva**: ver resposta da Pergunta 2 acima — precisamos alinhar com você antes de mexer nos acessos de terceiros (Considere Feito/René Kasper).
- **Teste técnico antes de ligar o envio à Meta**: de acordo, usando a aba "Eventos de teste" do Gerenciador de Eventos, como vocês propuseram.
- **Token da API de Conversões nunca por mensagem, e-mail ou print**: de acordo — ele é gerado e usado só por quem está configurando, direto no servidor/comando de teste, sem circular entre nós em nenhum momento.

---

## 4 · O que falta — do lado do seu Claude

Está tudo detalhado, passo a passo, no documento em anexo ("Instruções para o Claude do Giuliano — Instalação do Tag Manager"). Resumindo:

1. Instalar o snippet do container `GTM-TPTQTWJK` no Webflow (código já pronto no documento).
2. Instalar o mesmo tipo de rastreamento no portal (`portal.elevags.com.br`), subdomínio separado — incluindo a vinculação entre domínios (cross-domain measurement) com `elevags.com.br`.
3. Disparar, no código do portal, os eventos certos: `CompleteRegistration` (não `Lead`) quando a conta é criada, e `Purchase` quando a assinatura é paga — tanto pelo Pixel quanto pela API de Conversões, com o `event_id` compartilhado entre os dois para evitar contagem dupla.
4. Fazer o teste técnico na aba "Eventos de teste" antes de ligar o envio de verdade.
5. Gerar, periodicamente, a lista de conversões (gclid + data + valor) para a Amanda subir no Google Ads.
