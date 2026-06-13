def mostrar_listas(lista):
    if len(lista) == 0:
        print("Nenhuma nome na lista")
    else:
        print(f"Quantidade de nomes cadastrado: {len(lista)}")
        
nomes = ["Moises", "Henrique", "José"]
mostrar_listas(nomes)