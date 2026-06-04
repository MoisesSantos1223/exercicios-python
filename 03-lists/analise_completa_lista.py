""""
lista = []
soma = 0
quantidade = 0

while True:
    numero = int(input("Digite um número: "))
    
    if numero == 0:
        print("Você acertou!!")
        break
    if numero != 0:
        lista.append(numero)
        quantidade += 1
        soma += numero
        pares = numero % 2
        impares = numero % 1
        
print("Listas: ", lista)
print("Quantidade: ", quantidade)
print("Soma: ", soma)
print("Número maior: ", max(lista))
print("Número menor: ", min(lista))
print("Números pares: ", pares)
print("Números impares: ", impares)
"""

#Codigo corrigido

lista = []
soma = 0  
quantidade = 0  
pares = 0
impares = 0 

while True: 
    numero = int(input("Digite um número: "))
    
    if numero == 0: 
        break 
    
    lista.append(numero) 
    quantidade += 1
    soma += numero
    
    if numero % 2 == 0: 
        pares +1
    else: 
        impares += 1
        
media = soma / quantidade

print("Lista", lista)
print("Quantidade:", quantidade)
print("Soma:", soma)
print("Média:", media)
print("Número maior:", max(lista)) 
print("Número menor:", min(lista)) 
print("Números pares:", pares)
print("Números ímpares:", impares)
