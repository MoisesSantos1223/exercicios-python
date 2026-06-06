# Esse é um exercicio de sistema de notas, dps do cadastro e com aprovado, vai fazer outro cadastro

def cadastro_Notas():
    contador = 0
    soma = 0
    
    while contador < 3:
        nota = int(input("Digite a sua nota: "))
        soma += nota
        contador += 1
        
    media = soma / 3
    return media    

def Aprovado_Reprovado(media):
    
    if media >= 7:
        return "Aprovado" 
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
    
def sistema():
    continuar = "s"
    
    while continuar != "n":
        
        nome = input("Digite o nome do aluno: ")
        
        media = cadastro_Notas()
        situacao = Aprovado_Reprovado(media)
        
        print(f"Olá {nome}, sua média ficou: {media}")
        print(f"Situação: {situacao}")
        continuar = input("Deseja cadastrar outro aluno? s/n: ")
        
        
sistema()