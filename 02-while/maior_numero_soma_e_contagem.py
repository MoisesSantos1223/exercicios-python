n = 1
i = 0
soma = 0
maior = 0

while n != 0:
    n = int(input("Digite um numero:"))
    if n != 0:
        i += 1
        soma += n
        
    if n > maior:
        maior = n

print(f"A quantidade foi {i}")
print(f"A soma foi {soma}")
print(f"O numero maio digitado foi {maior}")
        