i = 0  
n = 1
soma = 0

while ( n != 0):
    n = int(input("digite um numero:"))
    if n != 0:
        i += 1
        soma += n
        
print("Soma: ", soma)
print("Contador: ", i)