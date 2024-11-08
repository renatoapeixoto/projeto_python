# Faça um programa que peça o ano do seu
# nascimento e calcule a sua idade.

import os


os.system('cls')

print('CÁLCULO DA IDADE')

# Declarações
ano_atual = 2024

# Entrada
ano_nasc = int(input('Digite o ano de nascimento: '))

 # processamento
idade = ano_atual - ano_nasc

# Saída
print(f'Você tem {idade} anos!')
print('Fim do programa!')
