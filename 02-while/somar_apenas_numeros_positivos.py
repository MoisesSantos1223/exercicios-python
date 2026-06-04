contador = 0 # vai definir a quantas vezes o usario digitou o número\
total = 0 # Seria a soma 

while True: # True é faz repitir finitamente até o break 
    numero =  int(input("Digite um número: "))
    
    if numero == 0:
        break
    
    if numero < 0:
        continue
    
    contador += 1 
    total += numero
    
print(f"quantidade: {contador}\n")
print(f"Soma: {total}")