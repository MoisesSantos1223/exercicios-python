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

lista = [] # criar uma lista vazia para guardar todos os números digitados
soma = 0  # Guardar a soma total dos números
quantidade = 0  
pares = 0 # Contar quantos números pares foram digitados
impares = 0 # Conta quantos números ímpares foram digitados

while True: #Cria um loop infinito, que só para qaundo usar break
    numero = int(input("Digite um número: "))
    
    if numero == 0: # Se o usario digitar 0 
        break # Para o loop
    
    lista.append(numero) # Adicionar o número digitado na lista
    quantidade += 1 #Soma +1 na quantidade de números digitados
    soma += numero # Soma o número digitado na soma total
    
    if numero % 2 == 0: #Verifica se o número é par
        pares +1 # Soma +1 na quantidade de pares
    else: # se não for par
        impares += 1 # Soma +1 na quantidade de ímpares
        
media = soma / quantidade

print("Lista", lista)
print("Quantidade:", quantidade)
print("Soma:", soma)
print("Média:", media)
print("Número maior:", max(lista)) # mostra o número maior
print("Número menor:", min(lista)) # mostra o número menor
print("Números pares:", pares)
print("Números ímpares:", impares)