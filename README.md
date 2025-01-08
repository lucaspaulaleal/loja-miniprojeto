# loja-miniprojeto
Mini projeto de Orientação a Objetos de Lucas De Paula Leal

Simulador de Loja Online

Este projeto é um simulador de loja online simples, desenvolvido em Python, que utiliza orientação a objetos. Ele permite que o usuário interaja com uma loja, adicionando produtos ao carrinho, removendo produtos, visualizando o carrinho e salvando os dados da loja e do carrinho em arquivos JSON para persistência.
=============================================================
Funcionalidades:
1. Gerenciamento de Produtos:
-Listar produtos disponíveis na loja.
-Adicionar produtos ao estoque.

2.Carrinho de Compras:
-Adicionar produtos ao carrinho.
-Remover produtos do carrinho.
-Exibir produtos no carrinho com o total da compra.

3.Persistência de Dados:
-Salvar produtos da loja em um arquivo produtos.json.
-Salvar itens do carrinho em um arquivo carrinho.json.
-Carregar dados automaticamente ao iniciar o programa.

4.Interação com o Usuário:
-Interface no terminal para escolha de opções.

=====================================================
Estrutura do Projeto

Classes Principais:

Produto

-Representa os produtos da loja.
-Atributos: nome, preco, estoque.
-Métodos:
--exibir_informacoes: Exibe detalhes do produto.
--atualizar_estoque: Atualiza o estoque ao adicionar/remover produtos.
--to_dict: Converte o objeto em dicionário para salva-lo em JSON.
--from_dict: Converte um dicionário em um objeto Produto.

CarrinhoDeCompras

-Gerencia os itens que o usuário deseja comprar.
-Atributos: itens (dicionário com produtos e quantidades).
-Métodos:
--adicionar_produto: Adiciona um produto ao carrinho, verificando o estoque.
--remover_produto: Remove um produto ou reduz a quantidade.
--exibir_carrinho: Exibe os itens no carrinho e o total da compra.
--calcular_total: Calcula o valor total dos itens no carrinho.
--salvar_carrinho: Salva os dados do carrinho em um arquivo JSON.
--carregar_carrinho: Carrega os dados do carrinho de um arquivo JSON.

Loja

-Representa a loja e seus produtos.
-Atributos: produtos (lista de objetos Produto).
-Métodos:
--adicionar_produto: Adiciona um novo produto ao estoque.
--listar_produtos: Lista os produtos disponíveis na loja.
--buscar_produto: Busca um produto pelo nome.
--salvar_produtos: Salva os produtos da loja em um arquivo JSON.
--carregar_produtos: Carrega os produtos da loja de um arquivo JSON.

======================================================================
Como Executar o Projeto

Pré-requisitos:

-Python instalado (versão 3.6 ou superior).
-Editor de código ou terminal.

Passos:

Clone ou baixe o repositório para o seu computador.

Certifique-se de que os arquivos loja.py, produtos.json e carrinho.json estão na mesma pasta.

Abra o terminal e navegue até a pasta do projeto.

Execute o comando:

python loja.py

Interaja com o menu exibido no terminal.

==============================================================================

Uso

Ao executar o programa, você terá as seguintes opções:

1.Listar Produtos: Exibe os produtos disponíveis na loja, com nome, preço e estoque.

2.Adicionar Produto ao Carrinho: Permite adicionar um produto ao carrinho, especificando a quantidade desejada.

3.Remover Produto do Carrinho: Remove um produto ou reduz sua quantidade no carrinho.

4.Exibir Carrinho: Exibe os itens no carrinho, suas quantidades e o valor total.

5.Salvar e Sair: Salva os dados do carrinho e da loja e encerra o programa.


=============================================================================
Possíveis Expansões:

-Implementar login de usuários.

-Adicionar diferentes formas de pagamento.

-Permitir a edição dos dados dos produtos.

-Criar uma interface gráfica ou web para interação.

