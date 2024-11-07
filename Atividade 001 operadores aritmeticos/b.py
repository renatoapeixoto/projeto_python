# Faça um programa que peça o ano do seu
# nascimento e calcule a sua idade.

import os


os.system('cls')

print('CÁLCULO DA IDADE')

# Declarações
ano_atual = 2024

# Entrada
ano = int(input('Digite o ano de nascimento: '))

idade = ano_atual - ano

# Saída
print(f'Você tem {idade} anos!')
print('Fim do programa!')
