def Analise_numeros(x):
    if len(x) == 0:
        print("Nenhum número cadastrado")
    else:
        print(f"Quantidade {len(x)}")
        print(f"O primeiro número cadastrado: {x[0]}")
        print(f"O utimo número cadastrado: {x[-1]}")
        print(f"O maior número cadastrado: {max(x)}")
        print(f"O menor número cadastrado: {min(x)}")
        
numeros = [1, 20, 700]
Analise_numeros(numeros)