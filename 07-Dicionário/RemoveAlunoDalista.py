def alunos_cadastrado():
    alunos = [
        {"nome": "Pedro", "idade": 17, "nota": 7},
        {"nome": "Lucas", "idade": 17, "nota": 9},
        {"nome": "Ana", "idade": 18, "nota": 10}
    ]
    
    return alunos

def mostrar_alunos(alunos):
    print("\n Lista de alunos atualizados:")
    for aluno in alunos:
        
        print("="*100)
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Nota: {aluno['nota']}")
    
def remova_aluno(alunos):
    remover = input("Digite um nome pra remover: ")
    found = False
    
    for procurar in alunos:
        if remover == procurar['nome']:
            alunos.remove(procurar)
            found = True
            print("Removido com sucesso")
            mostrar_alunos(alunos)
            break
        
   
            
    
    if found == False:
        print("não encontrado!")
        
ligacao = alunos_cadastrado()
remova_aluno(ligacao)