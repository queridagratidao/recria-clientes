# Página de obrigado por e-book (venda extra pós-compra)

Em cada e-book, na Hotmart, coloque como **página de obrigado** o endereço abaixo (o `?p=` diz qual e-book a pessoa comprou, e a página mostra 3 sugestões relevantes, depois do aviso de acesso, do convite para a comunidade Recriadores e antes do botão para a página de links com tudo o que a Recria oferece).

| E-book | Página de obrigado (cole na Hotmart) | Sugestões mostradas |
|---|---|---|
| Calendário de Conteúdos | https://www.agenciarecria.com.br/obrigado-ebook/?p=calendario-de-conteudos | Post, Reels, MIV |
| Calendário com IA | https://www.agenciarecria.com.br/obrigado-ebook/?p=calendario-com-ia | Reels, MIV, Esteira |
| MIV | https://www.agenciarecria.com.br/obrigado-ebook/?p=miv | Reels, Calendário com IA, Esteira |
| Post | https://www.agenciarecria.com.br/obrigado-ebook/?p=post | MIV, Calendário com IA, Esteira |
| Reels | https://www.agenciarecria.com.br/obrigado-ebook/?p=reels | MIV, Calendário com IA, Esteira |
| Negócio Local no Digital | https://www.agenciarecria.com.br/obrigado-ebook/?p=negocio-local | Low Ticket, Medium Ticket, High Ticket + Consultoria |
| Esteira de Produtos | https://www.agenciarecria.com.br/obrigado-ebook/?p=esteira-de-produtos | Medium Ticket, High Ticket, Estrutura + Consultoria |
| Mais de 100 Ideias de Low Ticket | https://www.agenciarecria.com.br/obrigado-ebook/?p=100-ideias-low-ticket | Esteira, High Ticket, Estrutura + Consultoria |
| Medium Ticket | https://www.agenciarecria.com.br/obrigado-ebook/?p=medium-ticket | Esteira, Estrutura, Low Ticket + Consultoria e Mentoria |
| High Ticket | https://www.agenciarecria.com.br/obrigado-ebook/?p=high-ticket | Estrutura, Medium Ticket, Low Ticket + Consultoria e Mentoria |
| Manual de Estrutura de Negócio | https://www.agenciarecria.com.br/obrigado-ebook/?p=estrutura-de-negocio | Medium Ticket, High Ticket, Low Ticket + Consultoria e Mentoria |

Sem `?p=` (ou com um valor desconhecido), a página mostra 3 sugestões padrão (Calendário de Conteúdos, Post e Esteira de Produtos).

Os links dos cartões levam `utm_source=obrigado&utm_medium=pagina&utm_campaign=cross_<e-book>`, e o clique dispara o evento `CliqueVendaExtra` no Pixel, para você medir quanto a página de obrigado gera.

## Order bump (na tela de pagamento)
Na Hotmart: **Produtos > Meus produtos > (e-book) > Ferramentas > Order Bump**. Adicione o produto complementar, o preço e o texto do convite (sugestões no guia `hotmart-cadastro-ebooks.md`). Depois, copie o **link da oferta com o bump** e me envie, para eu trocar o botão da página de vendas.

| Manual de Narrativas | https://www.agenciarecria.com.br/obrigado-ebook/?p=manual | 3 padrão (Calendário de Conteúdos, Post, Esteira) |
| Curso Express | https://www.agenciarecria.com.br/obrigado-ebook/?p=express | 3 padrão (Calendário de Conteúdos, Post, Esteira) |

**Evento de compra no Pixel:** com o `?p=` correto, a página dispara **Purchase** (valor do preço de tabela, BRL) uma vez por visita. Atenção: se você também ativar o Pixel na Hotmart com o evento de Compra, o Meta pode contar a mesma venda **duas vezes**. Use apenas um dos dois (o da Hotmart é mais preciso, porque considera bump, cupom e parcelamento).

A página também mostra um bloco **"Se você quiser que eu pegue na sua mão"** (Consultoria R$ 67 e/ou Mentoria) a partir do Negócio Local, nos e-books de negócio (ver coluna acima). Nos e-books de conteúdo (Calendários, Post, Reels e MIV), não aparece.
