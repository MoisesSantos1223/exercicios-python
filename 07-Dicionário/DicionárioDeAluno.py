aluno = {
    "nome": "Moisés",
    "idade": 18,
    "nota": 6,
    "curso": "ADS"
}

print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']}")
print(f"Nota: {aluno['nota']}")
print(f"Curso: {aluno['curso']}")

if aluno['nota'] >= 7:
    print("Aluno foi aprovado")
elif aluno['nota'] >= 5:
    print("O aluno está de recuperação")
else:
    print("O aluno está reprovado")