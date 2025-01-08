import json

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibir_informacoes(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque}")

    def atualizar_estoque(self, quantidade):
        self.estoque -= quantidade

    def to_dict(self):
        return {"nome": self.nome, "preco": self.preco, "estoque": self.estoque}

    @staticmethod
    def from_dict(dados):
        return Produto(dados['nome'], dados['preco'], dados['estoque'])


class CarrinhoDeCompras:
    def __init__(self):
        self.itens = {}

    def adicionar_produto(self, produto, quantidade):
        if produto.estoque >= quantidade:
            if produto.nome in self.itens:
                self.itens[produto.nome]['quantidade'] += quantidade
            else:
                self.itens[produto.nome] = {'produto': produto, 'quantidade': quantidade}
            produto.atualizar_estoque(quantidade)
            print(f"{quantidade}x {produto.nome} adicionado ao carrinho.")
        else:
            print(f"Estoque insuficiente para {produto.nome}.")

    def remover_produto(self, produto, quantidade):
        if produto.nome in self.itens:
            if self.itens[produto.nome]['quantidade'] > quantidade:
                self.itens[produto.nome]['quantidade'] -= quantidade
                produto.estoque += quantidade
                print(f"{quantidade}x {produto.nome} removido do carrinho.")
            else:
                del self.itens[produto.nome]
                produto.estoque += quantidade
                print(f"{produto.nome} removido completamente do carrinho.")
        else:
            print(f"{produto.nome} não está no carrinho.")

    def exibir_carrinho(self):
        print("\nCarrinho de Compras:")
        for item in self.itens.values():
            produto = item['produto']
            quantidade = item['quantidade']
            print(f"{produto.nome} - {quantidade}x - R${produto.preco * quantidade:.2f}")
        print(f"Total: R${self.calcular_total():.2f}\n")

    def calcular_total(self):
        return sum(item['produto'].preco * item['quantidade'] for item in self.itens.values())

    def salvar_carrinho(self):
        with open("carrinho.json", "w") as arquivo:
            dados = {
                produto: {"quantidade": item["quantidade"], "preco": item["produto"].preco}
                for produto, item in self.itens.items()
            }
            json.dump(dados, arquivo, indent=4)
        print("Carrinho salvo com sucesso!")

    def carregar_carrinho(self, loja):
        try:
            with open("carrinho.json", "r") as arquivo:
                dados = json.load(arquivo)
                for nome, item in dados.items():
                    produto = loja.buscar_produto(nome)
                    if produto:
                        self.adicionar_produto(produto, item["quantidade"])
            print("Carrinho carregado com sucesso!")
        except FileNotFoundError:
            print("Nenhum carrinho salvo encontrado.")


class Loja:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        print("\nProdutos Disponíveis:")
        for produto in self.produtos:
            produto.exibir_informacoes()

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return produto
        return None

    def salvar_produtos(self):
        with open("produtos.json", "w") as arquivo:
            dados = [produto.to_dict() for produto in self.produtos]
            json.dump(dados, arquivo, indent=4)
        print("Produtos salvos com sucesso!")

    def carregar_produtos(self):
        try:
            with open("produtos.json", "r") as arquivo:
                dados = json.load(arquivo)
                self.produtos = [Produto.from_dict(prod) for prod in dados]
            print("Produtos carregados com sucesso!")
        except FileNotFoundError:
            print("Nenhuma lista de produtos salva encontrada.")


# Simulação
loja = Loja()
loja.carregar_produtos()

if not loja.produtos:
    loja.adicionar_produto(Produto("Celular", 1500.00, 10))
    loja.adicionar_produto(Produto("Notebook", 2500.00, 5))
    loja.adicionar_produto(Produto("Fone de Ouvido", 200.00, 15))
    loja.salvar_produtos()

carrinho = CarrinhoDeCompras()
carrinho.carregar_carrinho(loja)

while True:
    print("1. Listar Produtos")
    print("2. Adicionar Produto ao Carrinho")
    print("3. Remover Produto do Carrinho")
    print("4. Exibir Carrinho")
    print("5. Salvar e Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        loja.listar_produtos()
    elif opcao == "2":
        nome_produto = input("Digite o nome do produto: ")
        produto = loja.buscar_produto(nome_produto)
        if produto:
            quantidade = int(input("Digite a quantidade: "))
            carrinho.adicionar_produto(produto, quantidade)
    elif opcao == "3":
        nome_produto = input("Digite o nome do produto: ")
        produto = loja.buscar_produto(nome_produto)
        if produto:
            quantidade = int(input("Digite a quantidade: "))
            carrinho.remover_produto(produto, quantidade)
    elif opcao == "4":
        carrinho.exibir_carrinho()
    elif opcao == "5":
        carrinho.salvar_carrinho()
        loja.salvar_produtos()
        print("Até mais!")
        break
    else:
        print("Opção inválida!")
