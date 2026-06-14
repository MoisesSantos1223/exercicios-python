def cadastrar_livros():
    lista = []
    
    print("Para sair do programa digite: fim")
    
    while True:
        livros = input("Digite um livro para cadastrar:")
        
        if livros.lower() == "fim":
            print("Você saiu do programa")
            break
        else:
            lista.append(livros)
    return lista

def mostrar_livros(lista):
    if len(lista) == 0:
        print("Nenhuma livro foi encontrado")
    else:
        print(f"Quantidade de livros cadastrado: {len(lista)}")
        print(f"Primeiro livro cadastrado: {lista[0]}")
        print(f"Utimo livro cadastrado: {lista[-1]}")
        
        pesquisa = input("Digite o livro que dejesa pesquisar: ")
        
        if pesquisa in lista:
            print("Esse livro está cadastrado")
        else:
            print("Esse livro não está cadastrado")
            
livors = cadastrar_livros()
mostrar_livros(livors)

        