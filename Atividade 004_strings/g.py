# Faça um programa que receba um número milhar e mostre na tela:
# - Quantidade de unidades
# - quantidade de dezenas
# - quantidade de centenas
# - quantidade de milhar.

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

print('-'*70)
print('PROGRAMA PARA MOSTRAR A MILHAR SEPARADA ')
print('-'*70)

numero = str(input('Digite um número: '))

# casting
numero_int = int(numero)

# Processamento/Cálculo
unidade = str(numero_int // 1 % 10)
dezena = str(numero_int // 10 % 10)
centena = str(numero_int // 100 % 10)
milhar = str(numero_int // 1000 % 10)

# dezena_milhar = numero_int // 10000 % 10
# centena_milhar = numero_int // 100000 % 10

# Saída
print(f'O número {numero_int} tem {unidade} unidade(s)')
print(f'O número {numero_int} tem {dezena} dezena(s)')
print(f'O número {numero_int} tem {centena} centena(s)')
print(f'O número {numero_int} tem {milhar} unidade(s) de milhar')
print('-'*70)
