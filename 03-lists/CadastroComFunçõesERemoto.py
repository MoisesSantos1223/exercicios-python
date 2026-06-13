def cadastrar_nomes():
    lista = []
    
    print("Para sair do programa, digite SAIR")
    
    while True:
        nome = input("Digite um nome para guardar na lista: ")
        
        if nome == "SAIR":
            print("Você saiu do programa")
            break
        
        lista.append(nome)
    return lista

def mostrar_resumo(lista):
    if len(lista) == 0:
        print("Nenhum cadastro encontrado")
    else:
        print(f"Qauntidade de cadastro: {len(lista)}")
        print(f"O primeiro cadastro: {lista[0]}")
        print(f"O útimo cadastro: {lista[-1]}")
        print(lista)
        
nomes = cadastrar_nomes()
mostrar_resumo(nomes)