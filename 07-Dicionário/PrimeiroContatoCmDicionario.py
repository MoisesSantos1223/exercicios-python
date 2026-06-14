dicionario = {}

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
curso = input("Digite o seu curso: ")

dicionario["nome"] = nome
dicionario["idade"] = idade
dicionario["curso"] = curso

print(dicionario)

print(f'nome: {dicionario['nome']}')
print(f"Idade: {dicionario['idade']}")
print(f"Curso: {dicionario['curso']}")