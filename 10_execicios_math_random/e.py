''' Faça um programa para sortear um número de 1 a 20. '''
# Sorteando um nome em uma lista
import os
import random


# Limpando o terminal
os.system('cls' if os.name == 'nt' else 'clear') # windonws cls, outros clear.

print('Sorteando um numero de 1 a 20')
lista = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numero_sorteado = random.choice(lista)
print(f'Lista: {lista}')
print(f'O nome escolhido foi: {numero_sorteado}')
print('-' * 70)
