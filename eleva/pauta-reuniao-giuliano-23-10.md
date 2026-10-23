# Pauta — Reunião com Giuliano
**RECRIA Marketing, 23/10/2026**

---

## 1. Campanha Meta Ads — montada e pausada, falta configurar o rastreamento no portal

A campanha já foi montada pelo Claude in Chrome, publicada **pausada** (não gasta nada):

- **Campanha**: AM | Portal do Condomínio | Cadastro | Brasil — objetivo Leads, conversão no site.
- **Evento de otimização**: "Concluir inscrição" (CompleteRegistration) — evento padrão de cadastro da Meta, mas ainda não chega nenhum dado dele.
- **Conjunto**: R$ 25/dia, Brasil, 28 a 65+, com os 16 públicos combinados (sem fornecedor) e expansão de público ligada.
- **Posicionamentos**: só Feed, Stories e Reels do Facebook e Instagram — Audience Network, Messenger, WhatsApp e Threads de fora.
- **Anúncios A2 e A3**: prontos, com as duas versões (4:5 e 9:16), textos e UTMs certos. Ajustes automáticos da Meta AI desligados, pra arte rodar exatamente como foi feita.
- **A1 (carrossel) e A4 (vídeo)**: ficam de fora por enquanto — A1 entra quando o carrossel for publicado, A4 depois do Dia L+9.

**O que falta antes de ativar — e precisa do Claude do Giuliano:**

O Pixel está instalado, mas **não está disparando no portal** — hoje o portal carrega o objeto `fbq`, mas nenhuma requisição sai pro Facebook. Sem isso, a campanha não tem como aprender quem está convertendo.

> **Para colar no Claude do Giuliano:**
>
> Preciso configurar o rastreamento de cadastro do Área Comum para a campanha de Meta Ads da Eleva.
>
> Contexto:
> - Todos os botões "Começar teste grátis" da landing elevags.com.br/area-comum-portal-do-condominio levam para portal.elevags.com.br/entrar. A conta é criada no portal (login com Clerk), não na landing.
> - A campanha da Meta otimiza pelo evento padrão "CompleteRegistration" (no painel aparece como "Concluir inscrição") do Pixel 634359929729484.
> - Hoje o portal tem o objeto fbq carregado, mas nenhuma requisição sai para o Facebook. Na prática o Pixel não está disparando no portal.
>
> O que fazer:
> 1. No portal.elevags.com.br, garantir que o código base do Pixel esteja instalado e inicializado com o ID 634359929729484 (`fbq('init','634359929729484')` + `fbq('track','PageView')`), carregando em todas as páginas.
> 2. Disparar `fbq('track','CompleteRegistration')` UMA vez, só quando uma conta NOVA for criada com sucesso (início do teste grátis). Não disparar em login de quem já tem conta.
> 3. Se possível, enviar o mesmo evento também pela API de Conversões (o Pixel já tem a integração ativa), usando o mesmo event_id do navegador para não contar em dobro.
> 4. Opcional, mas recomendado: levar os parâmetros utm_source, utm_medium, utm_campaign e utm_content da landing para o link do portal, para não perder a origem do cadastro.
> 5. Testar no Gerenciador de Eventos da Meta → Pixel "Pixel - Eleva" → aba "Eventos de teste": criar uma conta de teste e confirmar que "CompleteRegistration" aparece recebido.
>
> Não alterar nada no Gerenciador de Anúncios. Só site, portal e Pixel.

**Checklist antes de ativar (nosso lado):**
1. Configurar o evento de cadastro no portal (acima, com o Claude do Giuliano).
2. Conferir aprovação dos 3 anúncios (estavam "Em processamento" na análise da Meta).
3. Confirmar no Gerenciador de Eventos que "Concluir inscrição" está Ativo.
4. Acompanhar manualmente a frequência (esse objetivo não permite configurar limite de 3x/semana no painel).
5. A4 (vídeo) entra depois do Dia L+9.
6. Ativar campanha e conjunto só com o ok da Amanda, junto com o Google.

---

## 2. Live com Jaime (Instagram)

Jaime (com Y) se convidou para fazer uma live com o Giuliano, e ele já aceitou. Precisamos alinhar com ele:
- Quem é Jaime, qual o alcance/perfil da audiência dele.
- Data e pauta da live.
- Se cabe no calendário de conteúdo atual ou se precisa reorganizar.

## 3. Pagamento ao Hub — evento ElevaCast (novembro)

Está pendente o pagamento ao Hub referente ao próximo evento/podcast do ElevaCast, em novembro. Confirmar valor e prazo com o Giuliano.

## 4. Retorno sobre documento novo do Giuliano

Giuliano enviou um documento novo. Ainda em análise — assim que a Amanda repassar o arquivo, será comparado com os documentos anteriores já revisados, e o retorno com as diferenças entra nesta pauta (ou é enviado separadamente, se a reunião for antes de dar tempo).

## 5. Roteiros dos vídeos

Em revisão — mudança de nomenclatura para "Portal do Condomínio" deve impactar os roteiros já gravados/a gravar. *(Status a confirmar: roteiros ajustados liberados para gravação já, ou entrega prevista até o fim da tarde de hoje.)*
