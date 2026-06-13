def cadastro_participantes():
    lista = []
    
    print("Pra sair do cadastro digite: sair")
    
    while True:
        participantes = input("Digite os nome do participantes: ")
        
        if participantes.lower() == "sair":
            print("Você saiu do programa!")
            break
        else:
            lista.append(participantes)
            
    return lista

def mostrar_participantes(lista):
    if len(lista) == 0:
        print("Nenhum nome encontrado")
    else:
        print(f"Quantidade de participantes cadastrado: {len(lista)}")
        print(f"O primeiro cadastro: {lista[0]}")
        print(f"O utimo cadastrado: {lista[-1]}")
        
    if "Moises" in lista:
        print("Moises está cadastrado")
    else:
        print("Moises não está cadastrado")
        
participantes = cadastro_participantes()
mostrar_participantes(participantes)