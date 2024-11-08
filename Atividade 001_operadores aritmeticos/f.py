# Faça um programa que receba um número qualquer e 
# calcule o dobro e o triplo desse número.

import os


os.system('cls')

print('CÁLCULO DO DOBRO E O TRIPLO')

numero = int(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3

print(f'O dobro de {numero} é {dobro}')
print(f'O triplo de {numero} é {triplo}')

print('Fim do programa!')