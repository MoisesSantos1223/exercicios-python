"""
Faça um programa que leia um ângolo qualquer e mostre na tela o valor do seno,
consseno e tangente desse ângulo.
"""
import math

an = float(input("Digite um número"))
seno = math.sin(math.radians(an))

print(f"O ângulo de {an} tem o SENO de {seno :.2f}")

