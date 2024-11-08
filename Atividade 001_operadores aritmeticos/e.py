# Faça um programa que receba um
# número inteiro e mostre o sucessor e antecessor.

import os


os.system('cls')

print('CÁLCULO DO SUCESSOR E ANTECESSOR')

# Entrada
numero = int(input('Insira um valor inteiro: '))

antecessor = numero - 1
sucessor = numero + 1

# saída
print(f'O Antecessor de {numero} é {antecessor} ')
print(f'O sucessor de {numero} é {sucessor} ')

print('Fim do programa!')