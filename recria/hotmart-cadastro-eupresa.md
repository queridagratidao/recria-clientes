# Hotmart · cadastro do Recria EUpresa

O Recria EUpresa é um serviço (não um e-book). A pessoa paga a gestão pela Hotmart, cai na página de obrigado, preenche os dados e você recebe o alerta por e-mail.

## 1. Criar o produto
- Produto novo → tipo **Curso online** (ou "Serviço", se aparecer), pagamento **único**.
- **Nome:** Recria EUpresa
- **Descrição curta:** Gestão de anúncios no Instagram para microempresas e pequenos negócios, por semana, sem contrato.
- **Categoria:** Negócios e carreira. **Idioma:** Português.
- **Capa 600x600:** usar a mesma identidade dos outros produtos (peça 19 dos criativos serve de base).
- **Página de vendas:** https://www.agenciarecria.com.br/recria-eupresa/
- **Página de obrigado:** https://www.agenciarecria.com.br/eupresa-obrigado/
- **Garantia:** 7 dias é obrigatória na Hotmart para produto digital. Se o serviço já foi iniciado, explique no regulamento. Confirme as regras vigentes na Hotmart.
- Entrega: como não há área de membros, publique um conteúdo simples (um PDF "Como funciona o Recria EUpresa", ou o link da página de obrigado).

## 2. Ofertas (uma por período)
| Oferta | Nome | Preço |
|---|---|---|
| 1 | Recria EUpresa · 1 semana | R$ 100 |
| 2 | Recria EUpresa · 2 semanas | R$ 200 |
| 3 | Recria EUpresa · 3 semanas | R$ 300 |
| 4 | Recria EUpresa · 4 semanas (1 mês) | R$ 400 |

- Formas de pagamento: Pix, cartão e boleto. Parcelamento: à vista (valores pequenos).
- Cada oferta gera um link de checkout.

## 3. Colocar os links na página
Me envie os 4 links de checkout. Eu coloco em `CHECKOUT_1` a `CHECKOUT_4` da página `/recria-eupresa/`. Enquanto estiverem vazios, os botões abrem o WhatsApp.

## 4. Alerta de venda
1. Instalar o script `apps-script-eupresa.gs` (mesmo processo do checklist) e me enviar a URL do app da Web. Vou colocar na página de obrigado (`window.EUPRESA.API`).
2. Resultado: a pessoa paga → preenche o formulário → você recebe o e-mail "Você acabou de vender: Recria EUpresa (período) · negócio", com nome, negócio, Instagram, WhatsApp, e-mail, período, verba e destino. Também fica salvo na aba "EUpresa - contratações" da planilha.
3. Observação: quem paga e não preenche o formulário não gera o alerta do script. Nesse caso a própria Hotmart te avisa da venda (e-mail), e você chama a pessoa.

## 4b. Pix direto (sem Hotmart)?
Com a chave Pix fixa, não há como confirmar o pagamento automaticamente. Só com um gateway (Mercado Pago, Asaas, etc.), que avisa o sistema quando o Pix cai. Dá para fazer depois, mas exige conta no gateway. Por enquanto, tudo pela Hotmart.

## 5. Teste
Compre o próprio produto (ou use o link de teste da Hotmart), confira a página de obrigado e o e-mail de alerta.
