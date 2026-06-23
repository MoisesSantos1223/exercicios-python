lista = []

produto1 = {
    "produto": "Pão",
    "preco": 00.50,
    "quantidade": 3
}

lista.append(produto1)

produto2 = {
    "produto": "Leite",
    "preco": 5,
    "quantidade": 2
    
}

lista.append(produto2)

produto3 = {
    "produto": "Pó de café",
    "preco": 30,
    "quantidade": 2
    
}
lista.append(produto3)

for produto in lista:
    total = produto['preco'] * produto['quantidade']

print("=" *100)
print(f"Produto: {produto['produto']}")
print(f"Proço: {produto['preco']}")
print(f"Quantidade: {produto['quantidade']}")
print(f"Valor total em estoque: {total:.2f}")
print('=' * 100)