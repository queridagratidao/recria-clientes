# VSL "Aula Gratuita que Vende" · Camila Sartori
**Teste do modelo do playbook (`playbooks/vsl-aula-gratuita/PLAYBOOK.md`) para a Comunidade AME-SE · nov/2026**

## O que tem aqui

| Arquivo | O que é |
|---|---|
| `01-conceito-mecanismo-resultado-metodo.md` | Mecanismo, resultado e método (2 opções de cada, recomendada primeiro), vilão duplo, metáforas e fontes |
| `02-anuncio-aula-padrao.md` | Anúncio-aula frio (~90s), 2 ganchos, CTA PADRÃO, automação Youze, 2 palavras alternativas |
| `03-roteiro-vsl.md` | Roteiro completo da VSL (~18 a 19 min), 26 blocos, B-roll, marca do botão a ~70% |
| `../site-vsl/index.html` | Página nova da VSL (a página atual em `../site/` não foi alterada) |
| `05-anuncio-remarketing.md` | 2º anúncio-aula para quem saiu sem comprar (insight: a culpa depois do não), CTA CASA |
| `06-anuncios-4-ganchos.md` | **v2:** 4 anúncios-aula (amor, família, amigas, trabalho), gravados numa sessão só (4 aberturas + 1 corpo) |
| `07-roteiro-vsl-v2.md` | **v2:** VSL que passa pelas 4 áreas, com TCC, mais autoridade, encontros em grupo em formato de mentoria e bônus real para as 10 primeiras. Usar esta com os anúncios do `06` |

**Conceito escolhido (recomendado):** mecanismo **O Padrão de Casa** · resultado **Voz Adulta** · método **Perceber, Nomear, Pausar, Escolher**.
**Frase-centro da aula:** *o seu cérebro confunde o que é familiar com o que é seguro.*

## Nome do produto (conferido no repositório)
O curso é **Comunidade AME-SE** (site atual, automações e materiais de novembro). "Donas de Si" aparece só nos materiais do **grupo gratuito de WhatsApp** ("Comunidade Donas de Si"). Nos materiais da VSL usamos só **Comunidade AME-SE** e não citamos o grupo, para não repetir a confusão entre grupo e curso. ⚠️ Vale alinhar o nome do grupo: os PDFs de novembro/dezembro chamam de "Comunidade Donas de Si", e a orientação anterior era "Grupo VIP".

---

## Página: onde trocar o vídeo, o checkout e o tempo de revelação

Abra `camila-sartori/site-vsl/index.html` e vá até o bloco **CONFIGURAÇÃO** (no `<script>` do final do arquivo). Só isso precisa ser mexido:

```js
var CONFIG = {
  TEMPO_REVELACAO_SEGUNDOS: 790,   // ← segundo em que a oferta aparece
  DURACAO_VIDEO_SEGUNDOS: 1140,    // ← duração total do vídeo (para os eventos de 25/50/70%)
  VIDEO_TIPO: "placeholder",       // ← "youtube", "vimeo", "mp4" ou "iframe" (Panda e outros)
  VIDEO_ID: "",                    // ← ID do YouTube/Vimeo, URL do mp4 ou URL do embed
  LINK_CHECKOUT: "COLE_AQUI_O_LINK_DO_CHECKOUT_HOTMART"
};
```

**Como achar o tempo certo:** depois de editar a VSL, anote o segundo em que a Camila diz **"Por isso eu criei a Comunidade AME-SE"** (bloco 14). Converta para segundos (ex.: 13:10 = 13×60+10 = **790**) e coloque em `TEMPO_REVELACAO_SEGUNDOS`. A estimativa pelo roteiro é ~13:10, mas o tempo real muda com o ritmo da fala e com o trecho pessoal do bloco 7.

**Como a revelação funciona**
- **YouTube (não listado), Vimeo e mp4:** a página lê o tempo real do player. A oferta aparece quando a pessoa **chega** naquele ponto do vídeo (se pular para frente, também aparece).
- **`iframe` (ex.: Panda Video) ou placeholder:** o player não informa o tempo, então a página usa um **cronômetro** do tempo em que a página ficou aberta e visível. É aproximado; se for usar Panda, prefira o YouTube/Vimeo para o teste ou aceite essa margem.
- Quem já chegou no pitch uma vez vê a página completa quando voltar (fica salvo no navegador).
- `?oferta=1` no fim do link abre a página **já com a oferta** (use no remarketing do público que chegou a 70%).
- `?teste=1` revela em 5 segundos, para testar no celular antes de subir.

**Pixel (mesmo ID do site atual):** `PageView`, `ViewContent`, eventos personalizados `VSL_25`, `VSL_50`, `VSL_70` e `VSL_Pitch_Revelado`, e `InitiateCheckout` no clique dos botões. Os UTMs que chegam na página são repassados para o link do checkout. `Purchase` continua vindo da Hotmart (conferir se a integração do pixel na Hotmart está ativa).

**Publicar:** a página tem `noindex` (não aparece no Google). Subir como página separada, por exemplo `curso-ame-se.camilasartori.com.br/aula` ⚠️ (confirmar com quem hospeda o site atual). Testar no celular com `?teste=1` antes de ligar o anúncio.

---

## Públicos de remarketing (Meta)
1. Quem assistiu 50%+ do anúncio-aula + quem comentou/enviou DM → anúncio de remarketing (CTA **CASA**).
2. Visitantes da página sem `InitiateCheckout` → mesmo anúncio de remarketing.
3. Evento `VSL_70` ou `VSL_Pitch_Revelado` sem compra (o mais quente) → mesmo vídeo com botão direto para a página com `?oferta=1`.

**Com verba curta:** rodar 1 anúncio frio (testar gancho A × gancho B) + o remarketing só depois de juntar público (algumas centenas de pessoas no público 1). Não rodar mais de 2 criativos ao mesmo tempo. **O que medir:** custo por comentário, % que toca no link da mensagem 2, % que chega a 70% da VSL, conversão de quem chegou a 70%, custo por venda.

---

## ⚠️ Lista consolidada do que a Camila precisa validar

**Antes de gravar**
- [ ] Conceito: nomes **Padrão de Casa**, **Voz Adulta** e os 4 passos (ou escolher as opções B) — `01`
- [ ] Tom sobre a família ("inclusive em famílias que amavam muito"), para não soar como culpar os pais — `03` bloco 9
- [ ] Citações: Jeffrey Young; Kelly Paim e Bruno Cardoso (química); estudo de nomear emoções (Lieberman et al., 2007) — `01` e `03` blocos 9 e 12
- [ ] "Pergunta que eu escuto no consultório com frequência" é verdadeira (sem caso real) — `02` e `03` bloco 1
- [ ] Trecho pessoal da história (bloco 7) e a observação "chegam sabendo e repetem" — `03`
- [ ] Trecho "objeção = sintoma" (bloco 21) e a saída livre que acompanha — `03`
- [ ] Pergunta do remarketing ("machucou alguém ou só fez diferente?") — `05`

**Sobre a oferta (fatos que precisam bater com a Hotmart)**
- [ ] Valor exato da parcela: usamos **12x de R$ 16,24** (é o que está nos materiais do Grupo VIP de novembro). Conferir no checkout.
- [ ] Se quer citar que o curso já custou R$ 297 (é real, mas opcional) — `03` bloco 19
- [ ] Como funciona hoje a **mentoria em grupo** (frequência, formato). O diagnóstico de julho fala em "mentoria individual"; o site atual fala em "em grupo". Usamos "em grupo".
- [ ] Bônus atuais. Não usamos os valores "de R$ 200 / R$ 97 / R$ 47" do site atual; só entram se forem preços reais pelos quais esses itens já foram vendidos.
- [ ] Formas de pagamento (cartão, Pix, boleto) e acesso de 1 ano + certificado.
- [ ] Número do **CRP** para o rodapé da página e a tela final da VSL.

**Inconsistências encontradas nos materiais atuais (não alteramos nada fora desta pasta)**
- O site atual promete "Atualizações **vitalícias**" e, no FAQ, "acesso por **1 ano**". Na VSL e na página nova usamos só "1 ano de acesso".
- O anúncio de venda direta de agosto (Roteiro 2 de `roteiros-anuncios-video-curto.md`) fala em "sete dias **grátis**". O correto é **7 dias de garantia** (a pessoa paga e pode pedir reembolso).
- O site atual ainda tem a seção de contato para terapia ("Quero fazer terapia"). A página nova não tem.

**Black Friday (09 a 15/11, R$ 97)**
Se a VSL entrar no ar durante essa janela, há duas saídas honestas: (a) só subir a VSL depois de 15/11, com R$ 157; ou (b) usar a condição real de Black Friday no bloco 20 ("Urgência real") e na página, **com as datas verdadeiras**, e voltar para R$ 157 no dia 16. O que não pode é a página mostrar R$ 157 enquanto o grupo recebe R$ 97, sem explicação. ⚠️ Decidir antes de publicar.

---

## Limites aplicados (seção 7 do playbook)
Sem promessa de resultado, cura ou prazo (a VSL diz explicitamente que "não é de um dia pro outro" e "não vou te prometer que o padrão vai desaparecer"). Sem depoimento, sem número de alunas, sem escassez, sem sorteio, sem ancoragem inventada. Garantia de reembolso de 7 dias, sim; garantia de resultado, não. "Não substitui terapia" aparece no anúncio, na VSL, na página e no FAQ, e a página indica o CVV (188) para quem está em sofrimento intenso.

---

## v2 · Bônus das 10 primeiras (encontro individual)

**Como ficou:** as 10 primeiras compras até uma **data real** ganham um **encontro individual de mentoria** de ~30 min com a Camila (não é sessão de terapia). Ela chama no privado depois da compra.

**Por que não do jeito "se o botão está aparecendo, você ainda tem chance":** o botão aparece para todo mundo, sempre, então a frase seria escassez falsa (seção 7 do playbook). A versão honesta usa um **aviso separado na página**, que só aparece enquanto a condição vale de verdade:
- no bloco `CONFIG` da página: `BONUS_ATIVO`, `BONUS_VAGAS_RESTANTES`, `BONUS_DATA_LIMITE`, `BONUS_DATA_TEXTO`, `BONUS_DURACAO_MIN`;
- o aviso **some sozinho** quando a data passa ou quando as vagas chegam a 0;
- **as vagas precisam ser atualizadas à mão** conforme as vendas confirmadas na Hotmart (uma vez por dia basta). Se ninguém for atualizar, melhor não mostrar o número de vagas;
- na VSL a Camila fala "se você ainda está vendo o aviso do encontro individual aqui embaixo, ele ainda está valendo", o que é verdade enquanto a página for mantida.
- Vem desligado (`BONUS_ATIVO: false`) até a Camila aprovar.

**Sorteio:** fica fora. No Brasil, sorteio em promoção comercial precisa de autorização prévia do governo; "as 10 primeiras" resolve sem isso.

**⚠️ Pontos para a Camila validar antes de ligar o bônus**
- [ ] Se ela tem agenda real para 10 encontros de ~30 min nas semanas seguintes.
- [ ] O enquadramento como **mentoria do curso** (por onde começar), e não atendimento psicológico. Oferecer sessão de psicoterapia como brinde de venda pode esbarrar no Código de Ética (publicidade de serviços psicológicos); vale ela conferir com o CRP.
- [ ] Data limite real e se coincide com a Black Friday (09 a 15/11). Se coincidir, decidir se o bônus é parte da Black Friday ou vem depois.
- [ ] Como funcionam hoje os **encontros em grupo** (frequência e formato), já que agora eles estão no centro da oferta.
