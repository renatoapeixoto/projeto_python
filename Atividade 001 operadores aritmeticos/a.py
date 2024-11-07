# Faça um programa que peça 3 valores,
# depois calcule e imprima  a soma e a multiplicação desses valores.

import os

os.system('cls')

print('SOMA E MULTIPLICAÇÃO')

# Entrada
a = float(input('Insira o 1º valor: '))
b = float(input('Insira o 2º valor: '))

soma = a + b
produto = a * b

# Saída
print(f'A soma de {a} + {b} = {soma}')
print(f'O produto de {a} * {b} = {produto}')

print('Fim do programa!')
