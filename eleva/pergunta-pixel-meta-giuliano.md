# Pergunta ao Giuliano — Pixel da Meta
**RECRIA Marketing, 20/10/2026**
**Cliente:** Eleva — Área Comum, Portal do Condomínio

---

## O que a gente analisou

A gente revisou todo o material que você passou, incluindo a Política de Privacidade (v9, §9.3), e ela diz que o portal não tem Pixel instalado.

O problema: **o Pixel da Meta é o equivalente, na Meta, à tag do Google que vocês já configuraram.** Sem ele, a gente não consegue rastrear nada dentro da própria Meta — a campanha do Instagram/Facebook fica "cega": sabe quantos cliques teve, mas não sabe quantos desses cliques viraram cadastro de verdade, nem consegue otimizar o anúncio pra buscar mais gente parecida com quem se cadastrou. Isso derruba bastante o desempenho possível da verba de Meta.

A gente queria confirmar se isso foi uma decisão consciente (por exemplo, para não captar dados do visitante antes do consentimento de cookies, ou por outro motivo de privacidade específico), ou se passou despercebido quando a política foi escrita — porque pelo que vimos no restante do material, o rastreamento é levado a sério em tudo (UTM em todos os links, tag do Google configurada com cuidado), e o Pixel ficar de fora destoa um pouco disso.

---

## O que fazer sem o Pixel (caminho atual)

Se a decisão for mantida, a campanha de Meta roda com objetivo **Tráfego** (otimizada por clique, não por cadastro), e o rastreio de quem virou cliente de fato é manual: cada anúncio tem um link com UTM próprio (`utm_source=meta&utm_content=a1/a2/a3/a4`), e a Eleva confere toda segunda-feira quantos cadastros vieram com essa origem. Funciona, só que é mais trabalhoso e menos preciso do que o Pixel faria.

---

## Se você decidir instalar o Pixel

Você já tem um Pixel configurado na conta de anúncios — segue o ID:

**Pixel ID: 634359929729484**

Como o site é feito no Webflow, a instalação é simples — o Webflow tem um campo nativo pra isso, não precisa nem mexer em código:

### Passo a passo para o Claude dele (ou qualquer um com acesso ao Webflow) instalar

**Opção 1 — campo nativo do Webflow (mais simples, recomendado):**
1. No painel do Webflow, ir em **Site Settings** (Configurações do site).
2. Ir na aba **Integrations** (Integrações).
3. Procurar o campo **Facebook Pixel ID** (ou "Meta Pixel ID").
4. Colar o ID: `634359929729484`.
5. Publicar o site.

O Webflow já injeta o código do Pixel automaticamente em todas as páginas do site quando esse campo é preenchido — inclusive respeitando a ferramenta de consentimento de cookies, se o site já tiver uma configurada.

**Opção 2 — código manual (só se a opção 1 não estiver disponível no plano do Webflow):**
1. No painel do Webflow, ir em **Site Settings → Custom Code**.
2. Colar o código-base do Pixel no campo **Head Code** (código do `<head>`), disponível no Gerenciador de Eventos da Meta (business.facebook.com/events_manager2), usando o Pixel ID `634359929729484`.
3. Publicar o site.
4. Se o site tiver banner de cookies, condicionar o disparo do Pixel ao "Aceitar todos", igual já é feito com a tag do Google.

### Depois de instalado

5. Testar com a extensão gratuita **Meta Pixel Helper** (Chrome) ou pela aba "Testar Eventos" do Gerenciador de Eventos da Meta, pra confirmar que o PageView dispara.
6. Criar o evento de conversão no clique do botão "Começar teste grátis" (mesmo botão que já dispara a conversão do Google).
7. Avisar a Amanda quando estiver ativo, com um print do Gerenciador de Eventos mostrando "Recebendo dados" — aí a campanha de Meta pode mudar de objetivo Tráfego para objetivo Cadastro/Conversão, que tende a performar melhor.

---

## Outra pergunta que segue em aberto

Já tínhamos perguntado antes (e segue valendo, com ou sem Pixel): **o que está sendo considerado em cada parâmetro de UTM** — utm_source, utm_medium, utm_campaign, utm_content, utm_term — usados nos links de anúncio. Isso ajuda a confirmar que a classificação de canal (Google x Meta x WhatsApp x orgânico) nos cadastros está vindo certa, e não misturada.
