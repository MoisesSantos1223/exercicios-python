print("=======Adivinha um numero=======")

i = 0
nume = 1

while (nume != 0):
    nume = int(input("Digite um numero: "))
    if nume != 0:
        i += 1
    else:
        print(f"Você acertou o numero {nume}")
        
        
print("O contador é ", i) 