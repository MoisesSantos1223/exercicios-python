nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))

media = (nota1 + nota2 + nota3) /3

if media > 6:
    print(f"Aprovado, sua média é: {media}")
else:
    print(f"Reprovado, sua média é: {media}")