# Missao 11 

#Minha tentativa 

"""
while True:
    numeros = int(input("Digite um número: "))
    if numeros == 0:
        print("Você acertou o numero")
        break
    else:
        numeros = [numeros]
        
print("Numeros digitados: ", numeros)
"""

#Exemplo corrigido

lista = []

while True:
    numero = int(input("Digite um número: "))
    
    if numero == 0: 
        break
    
    lista.append(numero)
    
print("Números digitados: ", lista)