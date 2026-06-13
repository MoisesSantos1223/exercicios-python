"""
Faça um comprimento do  cateto oposto e do cateto adjacente de um triângulo, calcule
e mostre o comprimento da hipotenusa.
"""
from math import hypot

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adiacente"))
hi = hypot(ca, co)

print(f"A hipotenusa vai medir {hi}")