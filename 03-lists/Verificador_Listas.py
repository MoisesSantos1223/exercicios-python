def Cadastro_alunos(x):
    if len(x) == 0:
        print("Nenhum aluno cadastrado")
    else:
        print(f"Quantidade de alunos cadastrado {len(x)} utima pessao cadastrada {x[-1]} e o primeiro {x[0]}")
    
alunos = ["pedro", "lucas", "moises"]
Cadastro_alunos(alunos)
