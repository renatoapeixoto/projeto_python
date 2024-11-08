# Faça um programa que peça 4 notas, 
# após a entrada de dados calcular a média das notas digitadas.

import os


os.system('cls')

print('MÉDIA ARITMÉTICA')

# Entrada
nota1 = float(input('Insira o 1º valor: '))
nota2 = float(input('Insira o 2º valor: '))
nota3 = float(input('Insira o 3º valor: '))
nota4 = float(input('Insira o 4º valor: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'notas: {nota1} | {nota2} | {nota3} | {nota4}')
print(f'Média: {media}')

print('Fim do programa!')
