# Faça um programa que receba um valor em reais, 
# depois calcule quantos dólares daria para 
# comprar com esse valor.

import os


os.system('cls')

print('COMPRAR DÓLAR COM REAL')

valor_dolar = 5.5

real = float(input('Entre com um valor em real: '))

compra = real / valor_dolar

print(f'Com R${real} dá para comprar {compra:.2f} dólares')

print('Fim do programa!')