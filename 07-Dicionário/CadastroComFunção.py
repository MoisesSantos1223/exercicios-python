def cadastro_produtos():
    dicionario = {}
    
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o valor do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    
    dicionario ["produto"] = produto
    dicionario ["preco"] = preco
    dicionario ["quantidade"] = quantidade
    
    return dicionario

def mostrar_cadastro(dicionario):
    
    print(dicionario)
    
    total = dicionario['preco'] * dicionario['quantidade']
    
    if total > 100:
        print("O valor é alto")
    else:
        print("O valor é baixo")
        
produto = cadastro_produtos()
mostrar_cadastro(produto)