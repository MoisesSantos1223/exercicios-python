def cadastro():
    dicionario = {}
    
    nome = input("Digite o seu nome: ")
    nomeProduto = input("Digite o nome do produto: ")
    preco = float(input("Digite o valor do produto escolhido: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    cupom = input(f"{nome} vc tem cupom de desconto? ")
    
    dicionario['nome'] = nome
    dicionario['produto'] = nomeProduto
    dicionario['preco'] = preco
    dicionario['quantidade'] = quantidade
    dicionario['cupom'] = cupom
    
    return dicionario

def mostrar(dicionario):
    print("======= Dados cadastrado =========")
    print(f"Nome: {dicionario['nome']}")
    print(f"Produto: {dicionario['produto']}\nPreço: {dicionario['preco']} \nQuantidade: {dicionario['quantidade']} \nCupom: {dicionario['cupom']}")
    
    total = dicionario['preco'] * dicionario['quantidade']
    
    print(f"o valor total: {total}")
    
    if total > 200 or dicionario['cupom'].upper() == "SIM":
        print(f"{dicionario['nome']}, você tem direito a desconto!")
    else:
        print("Você não tem direito a desconto\n=============================")
        
cliente = cadastro()
mostrar(cliente)