def cadastro():
    dicionario = {}
    print("==========CADASTRO=========")
    
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    curso = input("Digite o nome do curso: ")
    nota = float(input("Digite a sua nota final: "))
    
    dicionario["nome"] = nome
    dicionario["idade"] = idade
    dicionario["curso"] = curso
    dicionario["nota"] = nota
    
    return dicionario

def mostra_cadastro(dicionario):
    print(f"Olá {dicionario['nome']} \n Vamos mostra se vc passou de ano")
    
    print(f"Nome: {dicionario['nome']}")
    print(f"Idade: {dicionario['idade']}")
    print(f"Curso: {dicionario['curso']}")
    print(f"Nota Final: {dicionario['nota']}")
    
    if dicionario['nota'] >= 7:
        print("Passou de ano")
    elif dicionario['nota'] >= 5:
        print("Recuperação")
    else:
        print("Reprovado")
        
aluno = cadastro()
mostra_cadastro(aluno)