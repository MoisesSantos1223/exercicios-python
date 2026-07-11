"""
Um professor quer sortear um dos seus quatro alunos para
apagar o quadro. faça um programa que ajude ele, lendo o
nome deles e escrevendo o nome escolhido.
"""
import random

def cadastro():
    lista = []
    contador = 1 

    print("Digite 4 nomes")

    while contador <= 4:
        nome1 = input("Digite um nome: ")

        lista.append(nome1)
        contador += 1
    
    return lista

def sorteo(lista):
    
    escolhido = random.choice(lista)
    
    print(f" Esses são os nomes cadastrados {lista} \nO nome escolhido vai ser: {escolhido}")

    

cadastroo = cadastro()
sorteo(cadastroo)
    
   

