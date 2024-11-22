'''Crie uma lista com 5 números inteiros. Depois imprima a soma desses 
valores.'''

import os

os.system('cls')

lista = [1, 2, 3, 4, 5]
print(lista)

soma = 0
for item in lista:
    soma += item
print(f'soma: {soma}')

