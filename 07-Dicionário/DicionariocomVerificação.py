produto = {
    "Produto": "Ovo",
    "Preco": 10.99,
    "Quantidade": 10
}

print(f"Produto: {produto['Produto']}")
print(f"Preço: {produto['Preco']:.2f}")
print(f"Quantidade: {produto['Quantidade']}")

if produto['Quantidade'] > 0:
    print("Produto está disponível")
else:
    print("Produto não está disponível")