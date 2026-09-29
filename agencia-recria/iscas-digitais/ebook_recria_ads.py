from ebook_lib import Book, DIAG, SERV, fechamento

UTM = 'checklist_recria_ads'
LINK_RECRIA_ADS = 'https://www.agenciarecria.com.br/'  # TROCAR pelo link do Recria Ads quando a página estiver no ar
b = Book('Checklist: conteúdos e anúncios sem cara de anúncio · Agência Recria', 'Venda sem parecer chato · Agência Recria')

b.cover('Presente Agência Recria', 'Venda sem<br><em class="g">parecer chato</em>',
        'O checklist para criar conteúdos e anúncios sem cara de anúncio, mesmo sem a verba de uma grande marca.')

b.page('light', '''<div class="kick">Por que isso funciona</div><h1>Todo mundo pula anúncio. <em class="g">Inclusive você.</em></h1>
<p>O anúncio com cara de anúncio é ignorado, e o custo para comprar atenção só sobe. As marcas que mais vendem hoje trocaram a interrupção pela história.</p>
<p><b>O cérebro odeia história sem final.</b> Quando uma história começa e desperta interesse, a mente só sossega quando sabe como ela termina. É por isso que a novela acaba no ápice, e é por isso que assistimos até o fim um vídeo que parece conteúdo.</p>
<div class="box">A lógica: a situação chama atenção, a história prende e gera identificação, e o produto entra como desejo ou solução.</div>''')

b.page('dark', '''<div class="kick">A estrutura</div><h1>Os 5 passos de um anúncio <em class="g">sem cara de anúncio</em></h1>
<table><tr><th>Passo</th><th>O que fazer</th></tr>
<tr><td>1. Gancho</td><td>Uma situação que o seu público reconhece em 2 segundos</td></tr>
<tr><td>2. Identificação</td><td>Um detalhe real que faz a pessoa pensar "isso é comigo"</td></tr>
<tr><td>3. Conflito</td><td>A tensão, a dúvida, o problema que prende até o fim</td></tr>
<tr><td>4. Virada</td><td>O produto entra como desejo ou solução, sem quebrar a história</td></tr>
<tr><td>5. Fechamento</td><td>Um bordão, um final marcante ou um convite para o próximo episódio</td></tr></table>
<div class="box" style="margin-top:16px">Exemplo: a Toyota com @sarahafonseca. "Passou na faculdade, ganhou um carro?" O pai se safa com uma resposta genial, e o Yaris Cross entra como o desejo da história.</div>
<p style="font-size:23px;margin-top:4px">Fizemos uma análise completa, passo a passo, dessa collab. Veja no perfil da Agência Recria no Instagram: <b style="color:#E4C988">@agencia.recria</b></p>''')

b.page('light', '''<div class="kick">Quem vai aparecer?</div><h1>3 caminhos, <em class="g">qualquer orçamento</em></h1>
<h2>1. Você, dono(a) do negócio</h2>
<p>Ninguém conta a história do seu negócio melhor do que você. Bastidores, rotina, decisões, erros e acertos geram confiança.</p>
<h2>2. A sua equipe</h2>
<p>Funcionárias que topam aparecer humanizam a marca. Como a loja que mostrou cada colaboradora "aquecendo para a maior Black da história".</p>
<h2>3. Microinfluenciadores locais</h2>
<p>Pessoas da sua cidade ou do seu nicho, com público menor e mais próximo, e que muitas vezes vendem mais do que um perfil gigante.</p>''')

b.page('dark', '''<div class="kick">Microinfluenciadores</div><h1>Seguidor não paga boleto: <em class="g">engajamento, sim</em></h1>
<p>Não escolha pelo número de seguidores. Um perfil pequeno, mas engajado, costuma converter mais do que um perfil grande e frio.</p>
<h2>Como calcular a taxa de engajamento</h2>
<div class="box">(curtidas + comentários) ÷ número de seguidores × 100</div>
<h2>O que observar antes de fechar</h2>
<ul>
<li class="ck">Os comentários são de pessoas reais, com conversa, ou só emojis?</li>
<li class="ck">O público desse perfil é o seu público (região, idade, interesse)?</li>
<li class="ck">O perfil já indicou outros produtos? Como o público reagiu?</li>
<li class="ck">Os valores desse perfil combinam com os da sua marca?</li>
<li class="ck">Os stories têm visualizações consistentes?</li>
</ul>''')

b.page('light', '''<div class="kick">Como remunerar</div><h1>Formatos de parceria <em class="g">que cabem no bolso</em></h1>
<table><tr><th>Formato</th><th>Como funciona</th></tr>
<tr><td>Permuta</td><td>Produto ou serviço em troca de conteúdo. Ideal para começar</td></tr>
<tr><td>Cachê fixo</td><td>Valor combinado por entrega (ex.: 1 reels + 3 stories)</td></tr>
<tr><td>Comissão</td><td>Cupom ou link exclusivo com uma porcentagem sobre as vendas</td></tr>
<tr><td>Híbrido</td><td>Um cachê menor + produto + comissão. Divide o risco dos dois lados</td></tr>
<tr><td>Recorrente</td><td>Parceria mensal: o público vê a marca várias vezes e passa a confiar</td></tr></table>
<div class="box" style="margin-top:16px">Exemplo: R$ X de cachê + produtos do mês + 10% de comissão com cupom próprio. Combine tudo por escrito, com datas, entregas e direitos de uso do conteúdo.</div>''')

b.page('dark', '''<div class="kick">O briefing</div><h1>O que combinar <em class="g">antes de gravar</em></h1>
<ul>
<li class="ck">Objetivo: gerar desejo, apresentar um produto, levar para a loja?</li>
<li class="ck">A mensagem principal, em uma frase</li>
<li class="ck">O que <b>não</b> pode faltar (produto, benefício, cupom, CTA)</li>
<li class="ck">O que pode ser feito do jeito do(a) criador(a): o tom e a história precisam ser dele(a)</li>
<li class="ck">Formato, duração e datas de postagem</li>
<li class="ck">Uso do conteúdo em anúncios (e por quanto tempo)</li>
<li class="ck">Marcação da marca e a sinalização de publicidade (#publi)</li>
</ul>
<div class="box">Roteiro engessado mata a naturalidade. Dê a direção e deixe o(a) criador(a) contar do jeito dele(a).</div>''')

b.page('light', '''<div class="kick">Inspiração</div><h1>Ganchos para <em class="g">adaptar ao seu negócio</em></h1>
<table><tr><th>Negócio</th><th>Gancho</th></tr>
<tr><td>Restaurante</td><td>"Tudo começou num almoço de domingo na casa da minha avó…"</td></tr>
<tr><td>Loja de roupa</td><td>"Cheguei na festa e dei de cara com uma mulher usando o mesmo vestido que eu…"</td></tr>
<tr><td>Clínica</td><td>"Nunca cuidei da pele. Até o dia em que vi uma foto minha que eu não esperava…"</td></tr>
<tr><td>E-commerce</td><td>"Eu jurei que não ia comprar mais nada este mês. Até que…"</td></tr>
<tr><td>Serviço / consultoria</td><td>"O cliente chegou dizendo que já tinha tentado de tudo…"</td></tr>
<tr><td>Doceria</td><td>"Minha mãe sempre dizia que bolo de verdade tem que ter…"</td></tr></table>
<p style="margin-top:12px">Repare: nenhum começa falando do produto. Todos começam por uma situação.</p>''')

b.page('dark', f'''<div class="kick">Quer ir além?</div><h1>Aprofundamos tudo isso <em class="g">no Recria Ads</em></h1>
<p>Neste checklist você viu o caminho. No <b>Recria Ads</b>, ensinamos passo a passo a criar conteúdos e anúncios sem cara de anúncio, com você, com a sua equipe ou com microinfluenciadores, utilizando <b>neuromarketing, neurociência e comportamento do consumidor aplicados às vendas</b>.</p>
<p>Um método construído em mais de 10 anos de experiência em marketing, atendendo de pequenas a grandes empresas, inclusive marcas conhecidas dos nichos de banheiras e de moda.</p>
<div class="cta"><div class="t">Recria Ads</div><p>Vender todo dia, com leveza e naturalidade, sem parecer aquele vendedor chato.</p><a class="l" href="{LINK_RECRIA_ADS}?utm_source={UTM}">Quero conhecer o Recria Ads</a></div>''')

b.page('light', '''<div class="kick">Antes de publicar</div><h1>Checklist <em class="g">final</em></h1>
<ul>
<li class="ck">Os 2 primeiros segundos prendem a atenção sem falar do produto?</li>
<li class="ck">Existe uma situação que o público reconhece?</li>
<li class="ck">Tem conflito ou curiosidade que faz assistir até o fim?</li>
<li class="ck">O produto entra como desejo ou solução, sem quebrar a história?</li>
<li class="ck">O final é marcante (bordão, virada, gancho para o próximo)?</li>
<li class="ck">Tem legenda na tela para quem assiste sem som?</li>
<li class="ck">O CTA está claro (comentar, clicar, ir até a loja)?</li>
<li class="ck">A parceria está sinalizada como publicidade?</li>
</ul>''')

b.page('dark', f'''<div class="kick">Para concluir</div><h1>A melhor venda é a que <em class="g">não parece venda</em></h1>
<p>Não é sobre ter a verba de uma grande marca. É sobre contar uma história que o seu público quer ouvir, com o seu produto no lugar certo dela.</p>
<p style="font-size:23px">Quer um direcional para o seu negócio? Conheça o <a style="color:#E4C988;font-weight:600" href="{DIAG}?utm_source={UTM}">Diagnóstico Recria</a>. E veja todos os nossos serviços em <a style="color:#E4C988;font-weight:600" href="{SERV}?utm_source={UTM}">agenciarecria.com.br</a>.</p>
''' + fechamento(UTM).replace('color:#9a7424', 'color:#E4C988').replace('color:#5a4412', 'color:#d9d3c7'))

b.render('/home/user/recria-clientes/agencia-recria/iscas-digitais/Checklist Venda sem Parecer Chato - Agencia Recria.pdf')
