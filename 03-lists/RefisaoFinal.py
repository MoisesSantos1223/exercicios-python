def cadastrar_aluno():
    lista = []
    
    print("Pra sair desse programa digite: sair")
    while True:
        aluno = input("Digite o nome do aluno: ")
        
        if aluno.lower() == "sair":
            print("Você saiu do programa")
            break
        else:
            lista.append(aluno)
            
    return lista

def mostrar_aluno(lista):
    if len(lista) == 0:
        print("Nenhum aluno cadastrado")
    else:
        print(f"Quantidades de alunos: {len(lista)}")
        print(f"O primeiro aluno cadastrado: {lista[0]}")
        print(f"A ultima pessoa cadastrada: {lista[-1]}")
        print(f"Todos os alunos cadastrados: {lista}")
        
        aluno = input("Digite o aluno que deseja pesquisar: ")
        
        if aluno in lista:
            print(f"O aluno {aluno}, está cadastrado")
        else:
            print(f"O {aluno} não está cadastrado")
            
            
aluno = cadastrar_aluno()
mostrar_aluno(aluno)
        
            