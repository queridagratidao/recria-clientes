# Prompt para Claude Chat/Claude in Chrome — Investigar o Google Analytics da Eleva
**Para colar no Claude Chat, 23/11/2026**

---

> Preciso que você entre no Google Analytics (analytics.google.com), na conta "Considere Feito" > propriedade "Eleva", e investigue os pontos abaixo. Não altere nada, é só pra conferir informações.
>
> **1. Conta e propriedade**
> Confirme em qual conta do Google Analytics a propriedade "Eleva" está (nome da conta, não da propriedade), e quem são os administradores/usuários com acesso a essa conta (Administrador → Gerenciamento de acesso à conta).
>
> **2. Fluxos de dados**
> Vá em Administrador → Coleta e modificação de dados → Fluxos de dados. Liste todos os fluxos existentes (nome do site, URL, ID de medição). Confirme se existe mais de um fluxo, e se algum deles aponta pra um domínio diferente de `elevags.com.br`.
>
> **3. Relatório de aquisição (últimos 28 dias)**
> Vá em Relatórios → Aquisição → Aquisição de tráfego (ou "Visão geral de aquisição"). Me diga:
> - O total de sessões/usuários no período.
> - A divisão por canal (Orgânico, Pago/CPC, Direto, Social, Referência, etc.).
> - Se aparece tráfego vindo especificamente do Google Ads e da Meta/Facebook Ads (procure por "cpc", "paid", "google / cpc", "facebook / paid" ou similar nos canais/origens).
>
> **4. Checagem de mistura de dados**
> Dentro do relatório de aquisição, veja se existe alguma página, evento ou nome de conteúdo que não pareça pertencer ao site da Eleva/Área Comum (por exemplo, nomes de página de outro negócio, como "Confiança Administradora de Condomínios" ou qualquer outro nome estranho). Relate exatamente o que encontrar, com prints se possível.
>
> **Importante**: o nome "Confiança Administradora de Condomínios" (ou "Administração de imóveis") já apareceu em telas do Google Analytics e também do Google Ads (sugestão de público "semelhante a: Administração de imóveis"). Investigue especificamente de onde vem essa referência: é um nome de página/evento dentro do próprio Analytics (indicando mistura de dados de outro site), é uma sugestão de público do Google Ads baseada em alguma lista de clientes carregada, ou é outra coisa? Explique a causa exata, porque isso pode estar enviesando a análise.
>
> **5. Tempo real**
> Abra Relatórios → Tempo real, e enquanto isso, me diga se os usuários ativos mostrados batem com o que seria esperado (tráfego do site da Eleva).
>
> **6. Vínculo com o Google Ads**
> Vá em Administrador → Vínculos de produtos → Vínculos do Google Ads. Confirme se essa propriedade já está vinculada a alguma conta do Google Ads, e qual.
>
> Ao final, monte um resumo dizendo: (a) se a propriedade realmente está fora de uma conta própria da Eleva, (b) se existe ou não mistura de dados de outro site, com evidência concreta pra cada afirmação, e (c) se o tráfego de anúncios (Google e Meta) está sendo capturado corretamente ou não.
