"""
Escreva um programa que pergunte a quantidade de km percorrida por um carro alugado e a quantidade
de dias pelos quais ele foi alugado. Calcule o preço pra pagar, sabendo que o carro custa 60 por dia e 0,15 por km rodado
"""

km = float(input("Digite a quantidade percorrida pelo carro: KM: "))
dias = int(input("Digite a quantidades de dias que foram alugados: "))
pago = (dias * 60) + (km * 0.15)

print(f"A quantidade pra pagar é: {pago}")