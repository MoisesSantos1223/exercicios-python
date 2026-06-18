def cadastro():
    dicionario = {}
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite a sua idade: "))
    gasto = float(input("Digite o valor gasto na loja: "))
    cartao = input("Possui cartão de fidelidade da loja: SIM/NÂO ")
    
    dicionario['nome'] = nome
    dicionario['idade'] = idade
    dicionario['gasto'] = gasto
    dicionario['cartao'] = cartao
    
    return dicionario

def mostrar_cadastro(dicionario):
    
    print("Seus dados")
    print(f"Nome: {dicionario['nome']}")
    print(f"idade: {dicionario['idade']}")
    print(f"Valor gasto na loja: {dicionario['gasto']}")
    print(f"Cartão da loja: {dicionario['cartao']}")
    
    if dicionario['gasto'] > 500.00 or dicionario['cartao'].upper() == "SIM":
        print(f"{dicionario['nome']} você tem direito a desconto")
    else:
        print(f"{dicionario['nome']} você não tem direito a desconto")
        
cadastroo = cadastro()
mostrar_cadastro(cadastroo)
