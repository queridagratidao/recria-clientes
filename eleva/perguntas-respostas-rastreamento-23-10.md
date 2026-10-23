# Perguntas e respostas — rastreamento Meta/Google (23/10)
**RECRIA Marketing, 23/10/2026**
**Resumo de apoio para a Amanda**

---

**P: Onde ele tirou que dá para instalar Pixel via Google Tag Manager? É possível isso? Porque o Google é uma coisa, Pixel é da Meta.**

R: É possível, sim. O GTM é um "container" neutro que dispara scripts de qualquer empresa, não só do Google — inclusive tem modelo pronto de "Facebook Pixel" na galeria do GTM. A vantagem de instalar por lá é poder usar o mesmo gatilho de consentimento de cookies que já existe para as tags do Google, em vez de configurar separado em cada ferramenta (como o campo nativo do Webflow faz, disparando sem esperar o "Aceitar todos").

---

**P: Na prática, quando a pessoa aceitar os cookies, ela está aceitando tanto o rastreio do Pixel quanto das tags do Google/GA4?**

R: Sim. Com um gatilho de consentimento único no GTM, todas as tags amarradas a ele — Google Ads, GA4 e o Pixel da Meta — só disparam depois desse "Aceitar todos". Um aceite libera tudo de uma vez.

---

**P: O Claude do Giuliano consegue fazer sozinho, só com o código do Pixel que a gente já passou?**

R: Sim, tecnicamente só precisa do ID do Pixel (634359929729484) e acesso de edição ao GTM da Eleva, que ele já tem (confirmado pelos prints anteriores do Tag Assistant, mostrando o container GTM-WX4W4NBX ativo).

---

**P: Não vai ter lógica a ideia dele de evento de clique (teste grátis)? Qual a diferença entre clique, Lead e CompleteRegistration?**

R: Faz sentido, sim — são três momentos diferentes:
1. **Clique em "Começar teste grátis"** → evento `CliqueTesteGratis`. A pessoa só clicou, ainda sem dar nenhum dado; pode desistir no meio. Serve só para ver o funil, não entra na otimização da campanha.
2. **Conta criada no portal** → evento `CompleteRegistration`. A pessoa deu os dados e o cadastro foi concluído de verdade — é esse evento que a campanha usa para aprender e otimizar.
3. **Assinatura paga (até 30 dias depois)** → evento `Purchase`.

"Lead" não encaixa no momento 2 porque, na Meta, "Lead" é reservado para quando alguém só demonstra interesse sem completar nada (tipo um formulário "me liga depois"). Aqui não existe meio-termo: ou a conta é criada, ou não é — por isso o nome certo é `CompleteRegistration`.

---

**P: Isso também não funcionaria como "Lead" no Google, né? Ou no Google é tudo a mesma coisa?**

R: No Google é diferente — lá as ações de conversão não têm nome padrão fixo, você cria com o nome que quiser (é o que o próprio documento do Giuliano já propõe: "Área Comum · conta criada" e "Área Comum · assinatura"). O problema de "Lead" x "CompleteRegistration" existe só do lado da Meta, que usa eventos padronizados com nome fixo.

---

**P: O Claude dele vai instalar o gclid/fbclid (atribuição de 30 dias) e passar pra gente, ou a gente tem que fazer isso daqui?**

R: É com o lado dele — o próprio documento do Giuliano diz "a parte do portal e da página fica com a Eleva". Do nosso lado, só entra: criar as duas ações de conversão de importação no Google Ads, confirmar o Pixel certo, não circular chave de API, e manter as UTMs nos anúncios (isso já está feito).

---

**P: O que é uma "ação de conversão do tipo importação" no Google Ads?**

R: É o tipo de conversão usado quando a venda não acontece na hora do clique (como é o nosso caso, até 30 dias depois). Em vez da tag do Google captar sozinha em tempo real, alguém "importa" depois os dados de quem converteu, usando o gclid salvo de cada clique como chave. Cria-se em Ferramentas e Configurações → Conversões → Nova ação de conversão → origem "Importação" → sub-tipo "Dados de rastreamento de cliques".

---

**P: O Pixel 634359929729484 é o certo, é o da Eleva mesmo?**

R: Sim, confirmado — é o ID que veio direto da conta de anúncios da Eleva.

---

**P: Onde eu pego a chave da API de Conversões dentro do Gerenciador?**

R: Fica em Gerenciador de Eventos → selecionar o conjunto de dados (Pixel 634359929729484) → aba "Configurações" → seção "API de Conversões" → botão "Gerar token de acesso". Mas, pelo próprio pedido do Giuliano no documento, essa chave não deve ser pega por nós — ele gera e guarda direto no servidor dele, sem circular por e-mail/mensagem.
