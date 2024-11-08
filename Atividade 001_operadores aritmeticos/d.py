# Faça um programa que receba e divida 2 números. 
# A saída da divisão precisará ser formatada com 4 casas decimais.

import os

os.system('cls')

print('CÁLCULO DA DIVISÃO')

# Entrada
valor1 = float(input('Insira o 1º valor: '))
valor2 = float(input('Insira o 2º valor: '))

divisao = valor1 / valor2

print(f'O valor {valor1} / {valor2} = {divisao:.4f}')

print('Fim do programa!')