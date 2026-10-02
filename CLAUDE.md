# Preferências de trabalho (Agência Recria)

## Documentos para clientes (propostas, relatórios, resumos)

Quando for preparar um documento explicativo, proposta, relatório ou resumo para a Amanda revisar
(e eventualmente enviar a um cliente), usar o fluxo de **Claude Docs** (artifact de documento),
abrindo-o lateralmente para edição colaborativa, em vez de só escrever o conteúdo no chat ou gerar
um arquivo direto.

Por quê: a Amanda gosta de acompanhar o documento sendo preenchido em tempo real e poder
comentar/editar diretamente nele, em vez de só ler texto corrido no chat. Isso agiliza a
comunicação e as rodadas de ajuste.

Fluxo:
1. Criar o doc já com o esqueleto (título, seções) e abri-lo (`open`) assim que nascer.
2. Preencher seção por seção enquanto ela acompanha.
3. Aplicar os ajustes pedidos diretamente no doc (não reescrever do zero em texto no chat).
4. Quando o conteúdo estiver pronto e ela confirmar, exportar para PDF (`export`, format `pdf`)
   e salvar no repositório do cliente correspondente dentro de `recria-clientes/`
   (ex.: `strategia-sindicos/comercial/` para material comercial da Strategia Síndicos),
   com nome de arquivo descritivo (`<Cliente>-<Assunto>-<Período>.pdf`).
5. Enviar o PDF pelo chat quando ela pedir para baixar.

Aplicar essa mesma dinâmica para todos os clientes da agência, não só a Strategia Síndicos.
