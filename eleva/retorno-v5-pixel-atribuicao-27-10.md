# Retorno ao documento v5 — Pixel e Atribuição
**RECRIA Marketing, 27/10/2026**
**Em resposta a "Resposta ao retorno da Recria", v5, 22/10/2026**

---

## Sobre o acesso ao Tag Manager

Você perguntou: *"vocês têm acesso ao Tag Manager da Eleva para fazer isso daí? Se não, fazemos daqui."*

Sim, temos acesso — criamos um container próprio na conta **Eleva Marketing** (e-mail `eleva.gs@gmail.com`), e já usamos ele hoje para instalar o Pixel (detalhes abaixo). Você também pode acessar esse container: basta entrar em tagmanager.google.com com o e-mail Eleva Marketing (ou pedir pra gente adicionar outro e-mail seu como administrador, se preferir usar outro login).

*(Observação: o container antigo, de outra agência, não estava mais instalado em nenhuma página do site — por isso optamos por montar um novo do zero, em vez de tentar recuperar acesso ao antigo.)*

## O que já fizemos hoje (27/10)

1. **Criamos o container `GTM-TPTQTWJK`**, na conta Eleva Marketing.
2. **Instalamos dentro dele duas tags do Pixel da Meta** (ID `634359929729484`):
   - Uma tag base, disparando o evento padrão `PageView` em todas as páginas.
   - Uma tag de evento customizado `CliqueTesteGratis`, disparando quando alguém clica em qualquer botão que leva para `portal.elevags.com.br/entrar` (os botões "Teste grátis" / "Começar teste grátis").
3. **Publicamos o container** (versão 2, ativa).
4. **Criamos as duas ações de conversão do tipo Importação no Google Ads**:
   - **"Área Comum · conta criada"** (categoria Inscrição, sem valor monetário, conta só a primeira interação)
   - **"Área Comum · assinatura"** (categoria Assinatura, com valor, conta só a primeira interação)

## Confirmando os pedidos do seu documento

- **Google Ads**: as duas ações de conversão de importação já estão criadas, com os nomes exatos acima — pode usar esses nomes no sistema do portal, para saber para qual ação cada evento vai.
- **Meta**: confirmado — o Pixel `634359929729484` é o conjunto de dados certo, é o mesmo que usamos nas tags que acabamos de instalar.
- **Chave da API de Conversões**: segue com vocês, como combinado — vocês geram e guardam direto no servidor, sem precisar nos enviar.
- **UTMs**: já estão em todos os anúncios (Google e Meta), desde a configuração das campanhas.

## O que falta — do lado do seu Claude

Está tudo detalhado, passo a passo, no documento em anexo ("Instruções para o Claude do Giuliano — Instalação do Tag Manager"). Resumindo:

1. Instalar o snippet do container `GTM-TPTQTWJK` no Webflow (código já pronto no documento).
2. Instalar o mesmo tipo de rastreamento no portal (`portal.elevags.com.br`), que é um subdomínio separado — incluindo a vinculação entre domínios (cross-domain measurement) com `elevags.com.br`.
3. Disparar, no código do portal, os eventos certos: `CompleteRegistration` (não `Lead`) quando a conta é criada, e `Purchase` quando a assinatura é paga — tanto pelo Pixel quanto pela API de Conversões.
4. Gerar, periodicamente, a lista de conversões (gclid + data + valor) para a Amanda subir no Google Ads.

Qualquer dúvida no documento em anexo, é só perguntar.
