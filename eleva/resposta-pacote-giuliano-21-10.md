# Retorno da Recria — Área Comum, portal do condomínio
**RECRIA Marketing, 21/10/2026**
**Cliente:** Eleva

Retorno sobre os pontos abordados na última reunião e no material que você passou.

---

## 1. Peças (carrosséis e estáticos)

Também faz muito sentido o reposicionamento para a Área Comum - portal do condomínio, e vamos seguir usando os carrosséis da forma que você fez atualmente.

## 2. Estratégia de Google Ads

Concordamos com a estrutura de 4 grupos de anúncios (síndico profissional, administradoras/gestores, obrigações, marca). A verba diária não é dividida entre os grupos — fica num só "bolo", e o próprio Google decide quanto investir em cada grupo conforme o desempenho. Os 4 grupos servem para casar o anúncio certo com cada busca, o que melhora a relevância em vez de pulverizar a verba.

## 3. Estratégia de Meta Ads

Concordamos com o objetivo Tráfego para a campanha de Instagram/Facebook. Mas aqui tem um ponto importante:

### Instalar o Pixel da Meta no Webflow

Sem o Pixel instalado na página, não conseguimos rastrear nenhum dos eventos relacionados às campanhas de Instagram/Meta — é o equivalente, na Meta, à tag do Google que já está configurada. Precisamos capturar **todos os eventos relevantes**: o cadastro (início do teste grátis) e também o evento de compra, já que às vezes a pessoa assina na hora do cadastro.

Pedimos para o seu Claude, que já está conectado ao Webflow, instalar o Pixel em todas as páginas do site. Segue o passo a passo para colar diretamente no chat dele:

> **Passo a passo para o Claude do Giuliano (Webflow):**
>
> 1. No painel do Webflow, ir em **Site Settings → Integrations**.
> 2. Procurar o campo **Facebook Pixel ID** (ou "Meta Pixel ID").
> 3. Colar o ID: `634359929729484`
> 4. Publicar o site.
> 5. Confirmar que o Pixel está disparando em todas as páginas, inclusive a do Área Comum - portal do condomínio.
> 6. Criar os eventos de conversão personalizados: um no clique de "Começar teste grátis" (cadastro), e outro (se houver um botão/fluxo de assinatura imediata) para o evento de compra.
> 7. Respeitar o consentimento de cookies: o Pixel só dispara depois do "Aceitar todos", igual já é feito com a tag do Google.
> 8. Testar com a extensão Meta Pixel Helper (Chrome) ou pela aba "Testar Eventos" do Gerenciador de Eventos da Meta, para confirmar que os eventos aparecem como "Recebendo dados".

Se o Claude dele não conseguir fazer essa instalação, nos avise que fazemos daqui.

**Também pedimos para confirmar se a tag do Google (GTM) já está puxando corretamente o evento de cadastro e, se existir, o evento de compra** — o mesmo cuidado de capturar todos os eventos vale para o lado do Google também.

### Ritmo de investimento

Entendemos que o teto máximo é R$ 3.700, conforme definido por você. Vamos começar com um investimento mínimo nos primeiros dias, para forçar as campanhas a entregarem o máximo de cadastro pelo menor custo possível, e ir aumentando a verba aos poucos, de acordo com o resultado de cadastros.

## 4. Calendário dos carrosséis

Gostamos muito dos carrosséis, ficaram muito bons. Nossa sugestão: postar um carrossel por semana, intercalado com os outros conteúdos que já estão no feed, a partir da semana em que o Área Comum - portal do condomínio for ao ar — sem dinâmica de lançamento, como você pediu. Entram nessa fila o carrossel de Produto, a Série Recursos e a Série Relatórios.

## 5. Linktree

Em vez do Linktree, nossa sugestão é o seu Claude criar uma página própria, no mesmo estilo, direto no domínio da Eleva (por exemplo, elevags.com.br/links). A vantagem: dá para ter um pop-up quando a pessoa clicar em "Síndico", "Fornecedor" ou "Executivo", abrindo os botões certos para cada público — recurso que o Linktree gratuito não tem.

**Como ficaria:**
- Botão **Síndico** → abre pop-up com: Curso de Formação de Síndico, Curso Avançado (Síndico Profissional), Sessão Estratégica, Diagnóstico, Mentoria.
- Botão **Fornecedor** → abre pop-up com: Curso para Fornecedor, Sessão Estratégica, Diagnóstico, Mentoria.
- Botão **Executivo** → abre pop-up com: Sessão Estratégica, Diagnóstico, Mentoria.
- Os demais itens (Área Comum, Comunidade de Síndicos, Corretora de Seguros, Hub de Negócios, YouTube, Spotify, Blog) ficam como botão único, levando direto para a página certa.

Segue um esboço de como ficaria:

![Esboço da página de links](esboco-linktree.png)

## 6. Fornecedor de WhatsApp

Recomendamos o **Nextags** em vez do SocialHub:

| | Nextags | SocialHub |
|---|---|---|
| Mensalidade (até 2.500 contatos) | R$ 147,00 | A partir de R$ 299,00 |
| Tarifa de disparo da Meta | À parte, ~R$ 384/mês | A confirmar |
| **Total estimado** | **~R$ 531/mês** | **~R$ 483 a 683/mês** |

Você já conhece a ferramenta, e o custo fica menor para o tamanho da sua base (~450 contatos). Vamos te enviar um documento separado, só com o comparativo completo entre Nextags e SocialHub.

## 7. Próximos passos

Já estamos na etapa de configurar as campanhas de Google e Meta, deixando tudo programado e pausado, pronto para ir ao ar quando você confirmar a data certa em novembro. Da sua parte, fica só a instalação do Pixel pelo seu Claude (ou nos avise se precisar que a gente faça daqui).
