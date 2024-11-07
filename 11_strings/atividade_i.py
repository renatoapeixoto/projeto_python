# Faça um programa que receba o nome completo de uma pessoa e, em seguida, 
# mostre o primeiro e o último nome.


import os
os.system('cls')

nome = input('Digite o nome completo: ')

nome = nome.split()
tamanho = len(nome)
print(f'O primeiro nome: {nome[0]} ')
print(f'O segundo nome: {nome[tamanho - 1]} ')

