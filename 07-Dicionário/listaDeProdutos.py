produtos = []

dicionario = {
    "produto": "TV",
    "preco": 299.99,
    "quantidade": 2
}

produtos.append(dicionario)

dicionario1 = {
    'produto': "Mesa",
    'preco': 100,
    'quantidade': 1
}

produtos.append(dicionario1)

dicionario2 = {
    'produto': 'sofá',
    'preco': 500,
    'quantidade': 1
}

produtos.append(dicionario2)

for produto in produtos:
    print("======================")
    print(f"Produto: {produto['produto']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")