#Meu codigo
"""""
lista = []
cont = 0 
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    numero = numero % 2 == 0
    cont += numero
    lista.append(numero)
    
print("Os números pares da lista digitado foram: ", lista)
print("Os números pares digitados: ", cont)
"""
#Correção do codigo

lista = []
cont = 0

while True:
    numero = int(input("Digite um número: "))
    
    if numero == 0:
        break
    
    if numero % 2 == 0:
        lista.append(numero)
        cont += 1
        
print("Os números pares: ", lista)
print("Quantidade de pares: ", cont)