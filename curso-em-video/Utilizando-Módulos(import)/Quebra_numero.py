"Crie uma programa que leia um número Real qualquer pelo teclado e mostre  na tela a sua porção inteira"

from math import trunc

numero = float(input("Digite um número: "))

print(f" o número {numero} tempo a parte inteira {trunc(numero)}")

