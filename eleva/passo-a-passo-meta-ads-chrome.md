# Passo a passo — Subir campanha Meta Ads (Área Comum)
**RECRIA Marketing, 22/10/2026**
**Para colar no chat do Claude no Chrome**

Instrução: acessar o Gerenciador de Anúncios da Meta (Business Manager) da Eleva e montar a campanha abaixo. **Deixar tudo PAUSADO ao final — não ativar nada.**

Pré-requisito: confirmar que o Pixel da Meta (ID `634359929729484`) já está instalado e disparando no site, com o evento de "Começar teste grátis" configurado como conversão personalizada. Se ainda não estiver, avisar antes de continuar — sem isso a campanha não consegue otimizar por Cadastro.

---

## 1. Criar a campanha

- **Nome**: `AM | Área Comum | Cadastro | Brasil`
- **Objetivo**: **Cadastro** (otimizar diretamente pela conversão de início do teste grátis, via Pixel)
- **Otimização**: conversões (evento "Começar teste grátis")

## 2. Conjunto de anúncios

- **Nome**: `AM | Área Comum | Conjunto 1`
- **Orçamento**: R$ 25,00/dia (no conjunto)
- **Público**:
  - Local: Brasil (sem restrição de região/cidade por enquanto)
  - Idade: 28 a 65 anos
  - **Públicos personalizados já existentes na conta** (adicionar todos juntos, no mesmo conjunto — não separar em conjuntos diferentes, por causa do orçamento baixo):
    - Listas diretas: `Lista_3_Meta_Ads_30.05.26_Relação de Síndicos`, `Lista_02.07.26_sindicos-profissionais-autonomos.xl`, `Lista_02.07.26_entidades-associacoes-sindicos.xlsx`
    - Engajamento/remarketing: `RMKT-ADS-365D`, `RMKT-365D-ENG.IG`, `Rmkt 365D - Interagiu perfil`, `Eng. FB - 365D`, `RMKT Page view`, `ThruPlay -365D`, `VideoView - 50 e 75% - 365D`
    - Semelhantes (lookalike): `Semelhante (1%) - Lista_3_Meta_Ads_30.05.26_Relação de Síndicos`, `Semelhante (1%) - Lista_02.07.26_sindicos-profissionais-autonomos.xl`, `Semelhante (1%) - Lista_02.07.26_entidades-associacoes-sindicos.xlsx`, `Semelhante (1%) - RMKT-ADS-365D`, `Semelhante (1%) - LAL 1% - Eng IG`, `Semelhante (1%) - Pixel - Eleva - Website using Purchase`
  - **Não usar** nenhum público com "Fornecedor" no nome (ex.: `Lista_2_30.05.26_Meta_Ads_Fornecedores_Gerais_27.0`, `16.05.26_Lista_de_fornecedores_Eleva - Fornecedor`, e seus respectivos "Semelhante")
  - Expansão de público da Meta: **ligada**
- **Posicionamentos**: manuais — Feed, Stories e Reels do Instagram e do Facebook. **Desligar** Audience Network e Messenger
- **URL de destino** (variar o `utm_content` por anúncio — a1, a2, a3, a4):
  `https://www.elevags.com.br/area-comum-portal-do-condominio?utm_source=meta&utm_medium=paid&utm_campaign=area-comum&utm_content=a1` (trocar "a1" por a2/a3/a4 em cada anúncio correspondente)
- **Pixel**: vincular o Pixel `634359929729484` e selecionar o evento "Começar teste grátis" como o evento de conversão que o conjunto vai otimizar
- **Frequência**: se for configurável no painel, marcar para revisar/trocar o criativo se a mesma pessoa ver o anúncio mais de 3x por semana

## 3. Os anúncios (criar os 3 primeiros agora; o A4 só entra depois, com o vídeo)

### Anúncio A1 — Carrossel do produto
Usar as imagens 01 a 07 da pasta "Instagram_Carrossel" (v10), nessa ordem, como cartões do carrossel.

- **Texto principal**: "O prazo que passa despercebido é sempre o que custa mais caro. O Área Comum - portal do condomínio reúne as obrigações do condomínio, com aviso antes de vencer, e as ocorrências do dia a dia, tudo documentado. 30 dias grátis, sem cartão de crédito."
- **Título**: "Área Comum - portal do condomínio"
- **Botão (CTA)**: Saiba mais
- Link de cada cartão: o mesmo link de destino acima, com `utm_content=a1`

### Anúncio A2 — Relatório e Informativo
Usar os dois arquivos da pasta "4_Meta_Anuncios": `A2_relatorio_e_inf...` (versão 4:5) e `A2_relatorio_e_inf...` (versão 9:16/quadrada) — subir os dois juntos nesse mesmo anúncio, para a Meta escolher o formato certo por posicionamento.

- **Texto principal**: "Ei, síndico morador, síndico profissional ou administradora: gerir condomínio já é tarefa grande, não precisa também virar refém de planilha e prazo perdido. Com o Área Comum - portal do condomínio, cada obrigação chega com aviso antes de vencer, e toda ocorrência fica documentada do início ao fim. Relatório de Conformidade para o conselho e a assembleia, Informativo Mensal para os moradores — os dois já saem com a sua logo. Teste grátis por 30 dias, sem cartão de crédito."
- **Título**: "Relatório e Informativo com a sua logo"
- **Botão (CTA)**: Saiba mais
- Link: `utm_content=a2`

### Anúncio A3 — Painel
Usar os dois arquivos da pasta "4_Meta_Anuncios": `A3_painel_4x5_108...` e `A3_painel_9x16_10...` — subir os dois juntos nesse mesmo anúncio.

- **Texto principal**: "Ei, síndico morador, síndico profissional ou administradora: tudo o que precisa da sua atenção devia estar num só lugar, não espalhado entre grupo de WhatsApp, papel e memória. O Área Comum - portal do condomínio reúne o que venceu, o que está perto de vencer e o que está em andamento, em cada condomínio da sua carteira. Teste grátis por 30 dias, sem cartão de crédito."
- **Título**: "Teste grátis por 30 dias"
- **Botão (CTA)**: Saiba mais
- Link: `utm_content=a3`

### Anúncio A4 — Vídeo de tela (não criar agora)
Fica pendente: só entra depois do Dia L+9, quando o vídeo de 30s do Relatório de Conformidade estiver gravado (depende do acesso de demonstração com a marca nova no portal).

---

## 4. Antes de terminar

- Conferir que a **campanha e o conjunto de anúncios estão PAUSADOS**.
- Conferir que Audience Network e Messenger estão desligados.
- Conferir que nenhuma lista de contatos (Hotmart, Sessão Estratégica, Comunidade) foi usada como público.
- Tirar um print final da campanha pausada, com os 3 anúncios, para a Amanda revisar.

**Não ativar a campanha em nenhuma hipótese — isso só acontece com o ok da Amanda, junto com a ativação do Google, perto do Dia L.**

---

## Observação sobre o Pixel

Essa campanha pressupõe que o Pixel (`634359929729484`) já está instalado e o evento "Começar teste grátis" configurado. Se ao configurar você notar que o Pixel não está disparando, ou que o evento de conversão não aparece como opção, **pare e avise a Amanda** antes de prosseguir — não dá para montar a campanha com objetivo Cadastro sem isso funcionando.
