lista = []
contador = 0 
soma = 0

for i in range(5):
    nota = int(input("Digite uma nota: "))
    soma += nota
    lista.append(nota)
    
    if nota > 7: 
        contador += 1

media = soma / 5

print("Maior nota: ", max(lista))
print("Menor nota: ", min(lista))
print(f"Média das notas: {media}")
print(f"Quantas notas foram maior que 7 {contador}")
        