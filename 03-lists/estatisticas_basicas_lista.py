lista = []
soma = 0
contador = 0

while True:
    numero = int(input("Digite um número: "))
    
    if numero == 0:
        break
    
    lista.append(numero)
    contador += 1
    soma += numero

print("Lista:",lista)
print("quantidade:", contador)
print("Soma:",soma)
print("Maior:",max(lista))
print("Menor:",min(lista))