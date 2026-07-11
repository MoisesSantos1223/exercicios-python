"""
O mesmo professor do desafio anterio quer sortear a ordem de apresentação 
de trabalho dos alunos. Faça um programa que leia a nome dos quatro alunos 
e mostre a ordem sorteada.
"""

import random

def cadastro():
    lista = []
    contador = 1

    print("Escolha 4 nomes:")

    while contador <= 4:
        nome = input("Digite um nome: ")

        lista.append(nome)
        contador += 1

    return lista

def sorteo(lista):
    
    random.shuffle(lista)

    print(f"Os nomes sorteados são {lista}")

alunos = cadastro()
sorteo(alunos)