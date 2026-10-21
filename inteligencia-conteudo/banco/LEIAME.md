# Painel do banco de referencias

Pagina interna (uso da agencia) com filtros por etapa do funil, nivel de consciencia, objetivo, anuncio, formato, tags e encaixe por nicho, mais botoes para copiar o texto das referencias filtradas e um prompt pronto para outra IA.

- **Endereco** (nao divulgar): https://www.agenciarecria.com.br/banco-consulta-interna-fd4760c6/ (depois que a branch for mesclada na principal do repositorio do site).
- **Fonte dos dados**: `dados.json` (esta pasta). **Modelo da pagina**: `template.html`. **Gerador**: `gerar.py`.
- **Imagens**: no repositorio do site, em `banco-consulta-interna-fd4760c6/img/REF-NNNN/`.

## Como atualizar
1. Acrescentar a referencia em `dados.json` (a skill `pesquisador-ganchos` faz isso).
2. Salvar as imagens recortadas no repositorio do site.
3. Rodar `python3 gerar.py [pasta-do-site]/banco-consulta-interna-fd4760c6/index.html`.
4. Mesclar na principal do site para publicar.

## Privacidade
A pagina tem `noindex` e nao esta no sitemap, mas **quem tiver o link consegue abrir**: qualquer pessoa. Nao e senha. Nao colocar dados de cliente, valores nem informacoes pessoais. Prints devem ser recortados (so o conteudo). Imagens de terceiros sao de uso interno, para estudo.
