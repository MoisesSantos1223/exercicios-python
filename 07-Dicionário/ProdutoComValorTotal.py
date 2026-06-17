produto = {
    "nome": "Planta",
    "preco": 29.99,
    "Quantidade": 5,
}

print(f"Nome: {produto['nome']}")
print(f"Preço {produto['preco']}")
print(f"Quantidade: {produto['Quantidade']}")

total = produto['preco'] * produto['Quantidade']

if total > 100:
    print("Esse produto possui ")
else:
    print("Esse produto possui baixo valor")