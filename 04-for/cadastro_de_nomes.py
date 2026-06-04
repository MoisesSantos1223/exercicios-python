lista = []

for i in range(5):
    nome = input("Dígite um nome: ")
    
    lista.append(nome)
    
print(lista)

EscolhaNome = input("Dígite um nome dentro da lista: ")

if EscolhaNome in lista:
    print("Você encontrou", EscolhaNome)
else:
    print("Dígite apenas nomes que estão na lista")