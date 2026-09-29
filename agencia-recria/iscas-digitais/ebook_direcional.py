from ebook_lib import Book, DIAG, SERV, fechamento

UTM = 'direcional_mkt'
b = Book('Direcional de Marketing e Negócios · Agência Recria', 'Direcional de Marketing e Negócios · Agência Recria')

b.cover('Presente Agência Recria', 'Direcional de<br><em class="g">Marketing e Negócios</em>',
        'O básico bem feito que separa os negócios que crescem dos que ficam pelo caminho. Um guia prático para você olhar para o seu negócio com outros olhos.')

b.page('light', '''<div class="kick">Por que isso importa</div><h1>Muitos negócios param <em class="g">no meio do caminho</em></h1>
<div class="stat"><div><strong>6 em 10</strong><span>empresas fecham as portas em até 5 anos de atividade</span></div><div><strong>29%</strong><span>dos MEIs encerram as atividades em até 5 anos</span></div></div>
<p class="src">Fontes: IBGE, Demografia das Empresas; Sebrae, Sobrevivência de Empresas (2020).</p>
<p>Quase nunca é por falta de esforço. Na maioria das vezes, o negócio cresce no improviso: sem saber quem é o cliente ideal, sem canal próprio de comunicação, vendendo sempre para clientes novos e esquecendo quem já comprou.</p>
<div class="box">A boa notícia: o básico bem feito já coloca você à frente da maior parte do mercado.</div>''')

b.page('dark', '''<div class="kick">Pilar 1</div><h1>Presença digital: <em class="g">ser encontrado</em></h1>
<p>Antes de qualquer anúncio, o seu cliente precisa conseguir te achar e confiar no que vê.</p>
<ul>
<li class="ck"><b>Google Meu Negócio</b> (Perfil da Empresa) completo: endereço, horário, fotos, telefone e avaliações respondidas</li>
<li class="ck"><b>Instagram</b> com bio clara: o que você faz, para quem, e como comprar</li>
<li class="ck"><b>Site ou página de vendas</b>: um endereço que é seu, não do algoritmo</li>
<li class="ck"><b>WhatsApp Business</b> com catálogo, mensagem de boas-vindas e respostas rápidas</li>
<li class="ck">Mesmas informações em todos os canais (nome, horário, preço, link)</li>
</ul>
<div class="box">Rede social é terreno alugado. Site, lista de clientes e WhatsApp são terreno próprio.</div>''')

b.page('light', '''<div class="kick">Pilar 2</div><h1>Quem é o seu <em class="g">cliente de verdade?</em></h1>
<p>Quem tenta falar com todo mundo não conversa com ninguém. Responda por escrito:</p>
<ul>
<li class="ck">Quem mais compra de você (idade, momento de vida, região, renda)?</li>
<li class="ck">Qual problema ou desejo faz essa pessoa procurar você?</li>
<li class="ck">O que ela pesquisa, pergunta ou teme antes de comprar?</li>
<li class="ck">Por que ela escolhe você e não o concorrente?</li>
<li class="ck">Quem são os seus clientes mais lucrativos (não só os que mais compram)?</li>
</ul>
<div class="box">Dica: pergunte aos seus 10 melhores clientes por que compram de você. As respostas viram conteúdo, anúncio e posicionamento.</div>''')

b.page('dark', '''<div class="kick">Pilar 3</div><h1>Posicionamento: <em class="g">por que você?</em></h1>
<p>Se o seu cliente não sabe dizer em uma frase por que escolher você, ele vai escolher pelo preço.</p>
<h2>Complete a frase:</h2>
<div class="box">"Ajudamos [quem] a [resultado] por meio de [como], diferente de [alternativa comum] porque [diferencial]."</div>
<ul>
<li>Um diferencial precisa ser <b>importante para o cliente</b>, e não só para você</li>
<li>Precisa ser <b>provável</b>: com dados, depoimentos, antes e depois</li>
<li>E precisa ser <b>sustentável</b>: algo que você consegue entregar sempre</li>
</ul>
<p>Foi assim que o Grupo Boticário se diferenciou com pesquisa sobre o corpo feminino, e que a Liquid Death transformou água em uma marca bilionária.</p>''')

b.page('light', '''<div class="kick">Pilar 4</div><h1>Os 5 níveis de <em class="g">consciência</em></h1>
<p>Nem todo mundo que vê o seu conteúdo está pronto para comprar. Cada nível pede uma mensagem diferente:</p>
<table><tr><th>Nível</th><th>O que a pessoa pensa</th><th>O que comunicar</th></tr>
<tr><td>Inconsciente</td><td>"Não tenho problema nenhum."</td><td>Histórias e situações que geram identificação</td></tr>
<tr><td>Consciente do problema</td><td>"Tenho um problema, mas não sei resolver."</td><td>Nomear a dor e mostrar que tem saída</td></tr>
<tr><td>Consciente da solução</td><td>"Sei que existe solução."</td><td>Explicar por que o seu jeito funciona</td></tr>
<tr><td>Consciente do produto</td><td>"Conheço você, mas estou em dúvida."</td><td>Provas, depoimentos, quebra de objeções</td></tr>
<tr><td>Totalmente consciente</td><td>"Quero, só falta um motivo."</td><td>Oferta clara, bônus, prazo</td></tr></table>
<p class="src">Modelo de níveis de consciência de Eugene Schwartz, "Breakthrough Advertising" (1966).</p>''')

b.page('dark', '''<div class="kick">Pilar 5</div><h1>Tenha um canal <em class="g">que é seu</em></h1>
<p>O algoritmo muda. A sua lista de clientes, não. Monte ao menos um canal direto:</p>
<ul>
<li><b>Grupo ou comunidade no WhatsApp</b> para clientes e interessados: novidades, bastidores e ofertas exclusivas</li>
<li><b>Lista de transmissão</b> segmentada por interesse ou último produto comprado</li>
<li><b>E-mail</b> para conteúdos mais longos e para quem prefere não receber mensagem</li>
</ul>
<h2>A régua de comunicação</h2>
<p>Intercale: <b>atrair → engajar → nutrir → aumentar a consciência → vender</b>. Quem só recebe oferta para de ler.</p>
<div class="box">Foi uma régua assim que fez um e-commerce que atendemos faturar R$ 1,2 milhão em 3 meses, sem tráfego pago, só com a base que ele já tinha.</div>''')

b.page('light', '''<div class="kick">Pilar 6</div><h1>Venda de novo para <em class="g">quem já comprou</em></h1>
<p>Conquistar um cliente novo costuma custar de <b>5 a 25 vezes mais</b> do que manter um cliente atual. E aumentar a retenção em 5% pode elevar o lucro entre 25% e 95%.</p>
<p class="src">Fontes: Harvard Business Review ("The Value of Keeping the Right Customers", 2014); Frederick Reichheld, Bain & Company.</p>
<h2>Duas contas que todo negócio precisa saber</h2>
<ul>
<li><b>CAC</b> (custo de aquisição): quanto você gasta em marketing e vendas ÷ número de clientes novos</li>
<li><b>LTV</b> (valor do cliente no tempo): ticket médio × compras por ano × anos que o cliente fica</li>
</ul>
<div class="box">Regra de bolso: o LTV precisa ser bem maior que o CAC, idealmente 3 vezes ou mais. Se não for, você está pagando para vender.</div>''')

b.page('dark', '''<div class="kick">Pilar 7</div><h1>Recorrência: <em class="g">a assinatura</em></h1>
<p>Um dos jeitos mais eficientes de aumentar o LTV é transformar a compra avulsa em compra recorrente:</p>
<table><tr><th>Negócio</th><th>Ideia de assinatura</th></tr>
<tr><td>Salão de beleza</td><td>Plano mensal com preço fixo: 2 ou 3 procedimentos por mês (escova, manicure, hidratação)</td></tr>
<tr><td>Suplementos</td><td>Envio automático todo mês, com desconto para assinantes</td></tr>
<tr><td>Pet shop</td><td>Ração entregue antes de acabar + banho mensal incluso</td></tr>
<tr><td>Livraria / café</td><td>Clube do livro ou do café, com curadoria mensal</td></tr>
<tr><td>Clínica / estética</td><td>Pacote de manutenção com sessões programadas</td></tr>
<tr><td>Serviços / B2B</td><td>Plano anual com acompanhamento, em vez de projeto avulso</td></tr></table>
<p style="margin-top:12px">Receita previsível, cliente que volta sempre e mais tempo para cuidar de quem já confia em você.</p>''')

b.page('light', '''<div class="kick">Pilar 8</div><h1>O comercial que <em class="g">não perde venda</em></h1>
<p>Marketing traz a pessoa até a porta. Quem fecha é o atendimento.</p>
<ul>
<li class="ck">Responder rápido: quanto mais o cliente espera, mais ele esfria</li>
<li class="ck">Ter um roteiro de atendimento com as perguntas e objeções mais comuns</li>
<li class="ck">Fazer <b>follow-up</b>: a maioria das vendas não fecha no primeiro contato</li>
<li class="ck">Registrar os contatos (planilha ou CRM) para não esquecer ninguém</li>
<li class="ck">Pedir indicação e depoimento para quem ficou satisfeito</li>
</ul>
<div class="box">Não adianta investir em anúncio se o WhatsApp demora horas para responder.</div>''')

b.page('dark', '''<div class="kick">Pilar 9</div><h1>Os números que você <em class="g">precisa acompanhar</em></h1>
<table><tr><th>Indicador</th><th>O que mostra</th></tr>
<tr><td>Faturamento e margem</td><td>Se você está vendendo com lucro, não só vendendo</td></tr>
<tr><td>Ticket médio</td><td>Quanto cada cliente gasta por compra</td></tr>
<tr><td>Taxa de conversão</td><td>Quantos contatos viram vendas</td></tr>
<tr><td>Taxa de recompra</td><td>Quantos clientes voltam a comprar</td></tr>
<tr><td>CAC e LTV</td><td>Quanto custa conquistar e quanto cada cliente deixa</td></tr>
<tr><td>Origem das vendas</td><td>De onde vêm os clientes: indicação, Instagram, Google, anúncio</td></tr></table>
<p style="margin-top:12px">O que não é medido não é melhorado. Escolha poucos números e acompanhe todo mês.</p>''')

b.page('light', '''<div class="kick">Autodiagnóstico</div><h1>Onde o seu negócio <em class="g">está hoje?</em></h1>
<p>Marque o que já está funcionando:</p>
<ul>
<li class="ck">Sei exatamente quem é o meu cliente ideal</li>
<li class="ck">Consigo explicar em uma frase por que escolher o meu negócio</li>
<li class="ck">Tenho Google Meu Negócio, Instagram e site ou página atualizados</li>
<li class="ck">Tenho um canal próprio com os meus clientes (WhatsApp, e-mail)</li>
<li class="ck">Falo com a minha base com frequência, e não só para vender</li>
<li class="ck">Tenho alguma forma de recompra ou recorrência</li>
<li class="ck">Sei o meu CAC, o meu LTV e a minha margem</li>
<li class="ck">Tenho um processo de atendimento e follow-up</li>
</ul>
<div class="box">Marcou menos de 5? Existe dinheiro na mesa, e provavelmente dentro da sua própria base.</div>''')

b.page('dark', f'''<div class="kick">Um olhar para o seu negócio</div><h1>Quer que olhemos <em class="g">o seu caso de perto?</em></h1>
<p>Cada negócio pede um diagnóstico específico. Às vezes o caminho é nutrir a base, às vezes é atrair novos clientes, às vezes é reposicionar a marca, às vezes é tudo isso junto.</p>
<div class="cta"><div class="t">Diagnóstico Recria</div><p>Em uma reunião online, entendemos o seu negócio e os seus objetivos, mapeamos os gargalos, mostramos as alavancas de crescimento e <b>entregamos tudo documentado</b> depois da reunião.</p><p>No momento, com condição especial: <b>R$ 67 por sessão</b>. Esse valor pode mudar a qualquer momento.</p><a class="l" href="{DIAG}?utm_source={UTM}">Quero o meu Diagnóstico Recria</a></div>''')

b.page('light', f'''<div class="kick">Para concluir</div><h1>O básico bem feito <em class="g">vende todo dia</em></h1>
<p>Presença digital, cliente bem definido, posicionamento claro, canal próprio, recorrência, atendimento e números acompanhados. Nada disso é mágica, mas é o que sustenta quem cresce de verdade.</p>
<p>Comece por um pilar. Depois vá para o próximo.</p>
<p style="font-size:23px">E se quiser a ajuda da Agência Recria, conheça todos os nossos serviços em <a style="color:#9a7424;font-weight:600" href="{SERV}?utm_source={UTM}">agenciarecria.com.br</a></p>
{fechamento(UTM)}''')

b.render('/home/user/recria-clientes/agencia-recria/iscas-digitais/Direcional de Marketing e Negocios - Agencia Recria.pdf')
