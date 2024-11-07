'''
Faça um programa que receba as informações de base e expoente. Calcule a potência.
'''

import math
import os


os.system('cls')

print('-'*70)
print('PROGRAMA PARA CALCULAR A POTÊNCIA')
print('='*70)
print()

resultado = 0

base = int(input('Entre com a base: '))
expoente = int(input('Entre com o expoente: '))

potencia = math.pow(base, expoente)

print(f'O número {base} elevado a {expoente} é igual a {potencia}')

print('Fim do programa!')
