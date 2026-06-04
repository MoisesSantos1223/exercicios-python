"""
lista = []

while True:
    numero = int(input("Digite um número: "))
    
    if numero <= 5:
        lista.append(numero)
        break
    
        if numero in lista:
            numero1 = int(input("Escolha um número que pode está na lista: "))
            
print(lista)
print("O número que está na lista é", numero1)
"""

#Codigo corrigido
""""
lista = []
contador = 0

while contador < 0:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    contador += 1
    
numero_busca = int(input("Digite um número para encontrar o número dentro da lista:"))

if numero_busca in lista:
    print("Você encontrou o número dentro da lista", numero_busca)
else:
    print("Você não encoutrou o número")
    
print("Lista: ", lista)
"""
#Codigo correto!

lista = []
contador = 0

while contador < 5:
    numero = int(input("Digite um número:"))
    lista.append(numero)
    contador += 1
    
numero_buscar = int(input("Digite um número para encontrar o número: "))

if numero_buscar in lista:
    print("Vocé encontrou o número", numero_buscar)
else:
    print("Você não encontrou o numero")
    
    
print("Lista: ", lista)