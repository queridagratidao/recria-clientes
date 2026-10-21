# Passo a passo — Subir campanha Meta Ads (Área Comum)
**RECRIA Marketing, 21/10/2026**
**Para colar no chat do Claude no Chrome**

Instrução: acessar o Gerenciador de Anúncios da Meta (Business Manager) da Eleva e montar a campanha abaixo. **Deixar tudo PAUSADO ao final — não ativar nada.**

---

## 1. Criar a campanha

- **Nome**: `Área Comum | Tráfego | Brasil`
- **Objetivo**: **Tráfego** (não "Cadastro"/"Conversão" — o site não tem Pixel configurado para decidir lance por conversão, só um evento de leitura; ver observação no fim)
- **Otimização**: cliques no link

## 2. Conjunto de anúncios

- **Nome**: `Área Comum | Conjunto 1`
- **Orçamento**: R$ 25,00/dia (no conjunto)
- **Público**:
  - Local: Brasil
  - Idade: 28 a 65 anos
  - Público personalizado de base: quem segue e interage com a página/perfil da Eleva no Instagram e no Facebook, últimos 365 dias
  - Sugestões de interesse (não como filtro obrigatório, deixar a Meta ampliar a partir daqui): administração de condomínios, síndico
  - Expansão de público da Meta: **ligada**
  - **Não subir nenhuma lista de contatos** (Hotmart, Sessão Estratégica, Comunidade) — não usar públicos personalizados a partir de listas enviadas
- **Posicionamentos**: manuais — Feed, Stories e Reels do Instagram e do Facebook. **Desligar** Audience Network e Messenger
- **URL de destino** (variar o `utm_content` por anúncio — a1, a2, a3, a4):
  `https://www.elevags.com.br/area-comum-portal-do-condominio?utm_source=meta&utm_medium=paid&utm_campaign=area-comum&utm_content=a1` (trocar "a1" por a2/a3/a4 em cada anúncio correspondente)
- **Pixel**: se houver um Pixel configurado na conta (ver observação no fim), vincular só para leitura do evento de clique em "Começar teste grátis" como conversão personalizada — **isso não decide o lance**, a otimização continua sendo por clique no link
- **Frequência**: se for configurável no painel, marcar para revisar/trocar o criativo se a mesma pessoa ver o anúncio mais de 3x por semana

## 3. Os anúncios (criar os 3 primeiros agora; o A4 só entra depois, com o vídeo)

### Anúncio A1 — Carrossel do produto
Usar as imagens 01 a 07 da pasta "Instagram_Carrossel" (v10), nessa ordem, como cartões do carrossel.

- **Texto principal**: "O prazo que passa despercebido é sempre o que custa mais caro. O Área Comum - portal do condomínio reúne as obrigações do condomínio, com aviso antes de vencer, e as ocorrências do dia a dia, tudo documentado. 30 dias grátis, sem cartão de crédito."
- **Título**: "Área Comum - portal do condomínio"
- **Botão (CTA)**: Saiba mais
- Link de cada cartão: o mesmo link de destino acima, com `utm_content=a1`

### Anúncio A2 — Relatório e Informativo
Usar a imagem do card 06 (Relatório de Conformidade / Informativo Mensal) da pasta "Instagram_Serie_Relatorios" ou "Meta_Anuncios" (A2, formato 4:5 ou 9:16 conforme o posicionamento).

- **Texto principal**: "Trabalho que aparece é trabalho valorizado. Relatório de Conformidade para o conselho e a assembleia, Informativo Mensal para os moradores, os dois com a sua logo."
- **Título**: "Relatório e Informativo com a sua logo"
- **Botão (CTA)**: Saiba mais
- Link: `utm_content=a2`

### Anúncio A3 — Painel
Usar a imagem do card 03 (Painel) da pasta "Meta_Anuncios" (A3, 4:5 ou 9:16).

- **Texto principal**: "Tudo o que precisa da sua atenção, num só lugar: o que venceu, o que está perto de vencer e o que está em andamento, em cada condomínio."
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

Essa campanha foi desenhada pressupondo que **não há Pixel configurado** no site (conforme a Política de Privacidade atual) — por isso o objetivo é Tráfego, não Cadastro. Já mandamos uma pergunta ao Giuliano sobre isso, com o passo a passo para instalar se ele decidir mudar. Se, ao configurar, você notar que já existe um Pixel ativo na conta de anúncios, avise antes de prosseguir — pode valer a pena reconsiderar o objetivo da campanha.
