# Ajuste do Google Analytics da Eleva
**Para o Claude do Giuliano, 23/11/2026 — logado como giuliano@elevags.com.br**

---

## Resumo do problema e o que já foi resolvido

O Analytics que a Eleva vinha usando (`G-PZ63FC1V16`) está numa conta "Eleva" dentro da organização "Considere Feito" (ex-agência), e **99% dos dados dele vinham de outro site**, `www.confiancacondo.com.br` (Confiança Administradora de Condomínios), que usa o mesmo ID por engano. Por isso o tráfego dos anúncios quase não aparecia: em 28 dias, só 1 sessão de "google / cpc" e nenhuma da Meta.

Hoje (23/11) o site já foi trocado para um Analytics novo (`G-B3F2ZB845M`), numa conta própria da Eleva. Falta: dar acesso à Amanda, vincular o Google Ads à conta nova, tirar da antiga, e limpar uma sobra de código no site.

---

## Decisões do Giuliano (escolher antes de executar)

### 1 · Quando desvincular o Google Ads da propriedade antiga

- **Desvincular já, no mesmo dia que vincular a nova**: a conta de anúncios para de compartilhar dados com a base misturada imediatamente. Risco: se a propriedade nova ainda não estiver recebendo dados corretamente por algum motivo, fica um intervalo sem nenhum vínculo até corrigir.
- **Esperar alguns dias com os dois vínculos em paralelo**: dá tempo de confirmar que a propriedade nova está funcionando direito antes de cortar a antiga. Risco: durante esse período, o Google Ads continua puxando sinais (públicos, otimização) da base misturada, o que pode seguir distorcendo a entrega dos anúncios.

### 2 · Conversar com a Considere Feito

- **Sim, conversar com a Considere Feito (rene@considerefeito.com)**: pedir pra sair da organização deles e avisar que o site da Confiança está usando o ID de Analytics da Eleva por engano. Resolve a situação de vez, mas exige esse contato.
- **Não conversar agora**: como a Eleva já não vai mais usar essa propriedade, dá pra simplesmente deixar quieto e seguir só com a conta nova, sem precisar desse desgaste com a ex-agência.

### 3 · Quais eventos marcar como principais no Analytics novo

- **Só o clique para o portal** (`portal.elevags.com.br`): mais simples, já que o cadastro e a assinatura de verdade são medidos pelo próprio portal, não pelo site.
- **Outros eventos além desse**: se quiser acompanhar mais coisas pelo Analytics (por exemplo, tempo na página, rolagem, cliques em botões específicos), é só listar quais.

---

## Passo a passo (depois das decisões acima)

**Regras**: não apagar nenhuma propriedade do Analytics (a antiga fica parada, só histórico). Não mexer em campanhas, orçamentos ou anúncios do Google Ads nem da Meta. Não colocar Google Analytics dentro do Tag Manager (o GA novo já está direto no código do site; uma segunda tag duplicaria as visitas). Nunca pedir nem usar a senha da Amanda.

1. **Confirmar a propriedade nova**: em Administrador → Fluxos de dados, confirmar que o ID é `G-B3F2ZB845M` e a URL é `https://www.elevags.com.br`, e que essa conta não está dentro da organização "Considere Feito".

2. **Dar acesso à Amanda**: Administrador → Gerenciamento de acesso à CONTA (nível da conta, não só da propriedade) → Adicionar usuários. E-mail: `queridagratidao@gmail.com`. Função: Administrador. Marcar "Notificar novos usuários por e-mail". **[CONFIRMAR antes de salvar]**

3. **Configurações básicas**: Administrador → Coleta e modificação de dados → Retenção de dados: 14 meses. **[CONFIRMAR]** Conferir se a métrica otimizada do fluxo está ligada.

4. **Vincular o Google Ads à propriedade nova**: Administrador → Vínculos de produtos → Contas vinculadas do Google Ads → Vincular. Conta `455-373-9886`, publicidade personalizada ativada, codificação automática ativada. **[CONFIRMAR]**

5. **Desvincular da propriedade antiga**: conforme a decisão 1 acima, no mesmo dia ou depois de alguns dias. **[CONFIRMAR]** Não apagar a propriedade antiga.

6. **Conferir o Tag Manager `GTM-TPTQTWJK` (só leitura)**: confirmar que tem a tag do Pixel `634359929729484` com PageView em todas as páginas e o evento no clique dos links para `portal.elevags.com.br`, e que não existe nenhuma tag de Google Analytics dentro. Não publicar nada.

7. **Remover a sobra do `GTM-WX4W4NBX`**: na página `/curso-formacao-de-sindico-profissional` do Webflow, localizar e remover esse bloco de código (contém o GA antigo `G-PZ63FC1V16` e um Pixel extra `2782378458628105`). **[CONFIRMAR antes de remover e antes de publicar]** Depois de publicar, conferir no código-fonte da página que não aparece mais.

8. **Testar**: abrir `www.elevags.com.br/area-comum-portal-do-condominio` numa janela anônima, aceitar os cookies, e no Analytics novo (Tempo real) confirmar que a visita aparece. Com o Meta Pixel Helper (ou Testar eventos no Gerenciador de Eventos), confirmar que o Pixel dispara PageView uma vez só. Numa segunda janela anônima, recusar os cookies e confirmar que nada do Google ou da Meta carrega.

9. **Relatório final**, pra devolver pra Recria conferir:
   - ID e nome da conta e da propriedade novas.
   - Lista de usuários com acesso, confirmando `queridagratidao@gmail.com` como Administrador.
   - Vínculo com o Google Ads na propriedade nova, e confirmação de que saiu da antiga.
   - Tags do `GTM-TPTQTWJK`.
   - Confirmação de que o `GTM-WX4W4NBX` saiu do site.
   - Resultado dos testes do passo 8, com prints.
