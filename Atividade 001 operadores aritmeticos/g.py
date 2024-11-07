#Faça um programa que converta metros 
# em centímetros e milímetros.

import os


os.system('cls')

print('CÁLCULO CONVERSÃO: CENTÍMETRO E MILÍMETRO')

metro = float(input('Digite o valor do metro: '))

centimetro = metro * 100
milimetro = metro * 1000

print(f'O valor de {metro}m equivale a {centimetro}cm')
print(f'O valor de {metro}m equivale a {milimetro}mm')

print('Fim doa programa!')