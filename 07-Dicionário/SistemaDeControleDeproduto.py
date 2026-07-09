def cadastro_produtos():
    produto1 = {
        "nome": "Camisa",
        "preco": 29.00,
        "quantidade": 15
    }
    produto2 = {
        "nome": "Calsa",
        "preco": 40,
        "quantidade": 15
    }
    produto3 = {
        "nome": "Meia",
        "preco": 10,
        "quantidade": 20
    }

    lista = [produto1, produto2, produto3]

    return lista

def mostrar_Produtos(lista):
    print("Produtos Castrados\n")
    print("="*100)

    for produto in lista:
        print(f"Nome: {produto['nome']}")
        print(f"Preco: {produto['preco']}")
        print(f"Quantidade: {produto['quantidade']}")
        print("="*100)
def pesquisa_cadastro(lista):
    nome = input("Digite um nome que deseja pesquisar:  ")
    senao = False
    for produto in lista:
        if produto["nome"] == nome:
            print("Produto encontrado:\n")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: {produto['preco']} ")
            print(f"Quantidade: {produto['quantidade']}")
            print("="*50)
            senao = True
            break

            
            

    if senao == False:
        print("\nNenhum nome encontrado")

def adicionar_Produto(lista):
    print("Você escolheu a opção de adicionar produto!\n")

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade de produtos: "))

    produto4 = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    lista.append(produto4)

def valor_total(lista):
    total_estoque = 0
    for produto in lista:
        

        total = produto['preco'] * produto['quantidade']
        total_estoque += total

    mostrar_Produtos(lista)
    print(f"Esse é o valor total do produto: {total_estoque}")

def chamar_funcoes():

    print("Escolha as funções abaixo:\n")

    print("1- Mostrar produtos")
    print("2- Pesquisar produtos")
    print("3- Adicionar produto")
    print("4- Valor total dos produtos")
    print("5- sair")

   
def executar_sistema():
    lista_Produtos = cadastro_produtos()
    while True:
        chamar_funcoes()
        escolha = int(input("Escolha umas das opões: "))

        if escolha == 1:
            mostrar_Produtos(lista_Produtos)
        elif escolha == 2:
            pesquisa_cadastro(lista_Produtos)
        elif escolha == 3:
            adicionar_Produto(lista_Produtos)
        elif escolha == 4:
            valor_total(lista_Produtos)
        elif escolha == 5:
            print("Sistema encerrado.")
            break
        else:
            print("Escolha apenas as opcões acima")

executar_sistema()
