lista = []
soma = 0

while True:
    numero = int(input("Digite um número:"))
    if numero == 0:
        break
    if numero % 2 == 1:
        lista.append(numero)
        soma += numero
        
print("Ímpares: ", lista)
print("Soma dos ímpares: ", soma)