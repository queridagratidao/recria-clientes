# Verificar e instalar o Pixel da Meta — passo a passo
**RECRIA Marketing, 20/10/2026**
**Cliente:** Eleva — Área Comum, Portal do Condomínio

---

## Antes de instalar: confirmar se é mesmo pra instalar

O documento "Mídia paga v11" que o Giuliano mandou diz, no §8 e no §9.2: **"O portal não tem pixel"**, por causa da Política de Privacidade v9 (§9.3), que proíbe. Ou seja, pelas regras atuais do projeto, instalar o Pixel não é permitido — a campanha de Meta foi desenhada de propósito sem ele (objetivo Tráfego, não Cadastro).

**Antes de qualquer passo abaixo, confirmar com o Giuliano**: a regra de não ter Pixel continua valendo, ou ele quer reconsiderar para a Meta poder otimizar por cadastro de verdade (o que normalmente melhora muito o resultado da verba)?

---

## Como verificar se já existe algum Pixel instalado (sem precisar do Claude dele)

Qualquer pessoa com acesso ao navegador consegue checar isso sozinha, em 2 minutos, sem mexer em nada:

1. Abrir a página **https://www.elevags.com.br/area-comum-portal-do-condominio** no Chrome.
2. Instalar a extensão gratuita **"Meta Pixel Helper"** (da própria Meta, na Chrome Web Store).
3. Com a página aberta, clicar no ícone da extensão. Se houver um Pixel instalado, ela mostra o ID dele e os eventos disparados (PageView, Lead, etc.). Se não houver nada, a extensão fica cinza/sem detecção.
4. Alternativa sem instalar nada: abrir o DevTools (F12) → aba "Rede"/"Network" → recarregar a página → filtrar por "facebook" ou "fbevents". Se aparecer uma chamada para `connect.facebook.net/.../fbevents.js`, há Pixel.
5. Para conferir a tag do Google (Tag Manager), mesmo processo com a extensão **"Tag Assistant Legacy"** ou **"Google Tag Manager"**, também da própria Google.

Com isso dá pra confirmar, sem depender do Giuliano, se o Pixel existe e qual é o ID — e aí sim confrontar se é um Pixel da conta de anúncios da Eleva ou de outra coisa.

---

## Se não houver Pixel e a decisão for instalar: passo a passo para o Giuliano passar ao Claude dele

1. **Criar (ou localizar) o Pixel na conta de anúncios da Meta** (Gerenciador de Eventos, business.facebook.com/events_manager2). Se já existir um Pixel da Eleva (de outras campanhas), reaproveitar o mesmo, não criar um novo.
2. **Copiar o código-base do Pixel** (snippet com o Pixel ID), disponível no Gerenciador de Eventos em "Adicionar Eventos" → "Instalar código manualmente".
3. **Inserir o código-base no `<head>` de todas as páginas do site**, incluindo a página do Área Comum.
4. **Criar um evento de conversão personalizado** no clique do botão "Começar teste grátis" (o mesmo botão que já dispara a conversão do Google) — via Gerenciador de Eventos, como "Evento Personalizado" ou configurando um "Lead"/"CompleteRegistration" nesse clique específico.
5. **Respeitar o consentimento de cookies**: o Pixel só pode disparar depois que a pessoa aceitar "Aceitar todos" no banner de cookies (mesma regra já aplicada à tag do Google, conforme a Política de Privacidade v9, §9).
6. **Testar** com o Meta Pixel Helper (ver seção acima) ou pelo próprio Gerenciador de Eventos, em "Testar Eventos" — confirmar que o PageView e o evento de conversão disparam corretamente.
7. **Avisar a Amanda** assim que estiver no ar, com um print do Gerenciador de Eventos mostrando o evento "Recebendo dados" ou "Ativo", para ela então mudar a campanha de Meta de objetivo Tráfego para objetivo Cadastro/Conversão.
