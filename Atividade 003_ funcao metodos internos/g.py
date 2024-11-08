'''Faça um programa que peça os valores de a, b e c de uma equação do 2º grau. 
Calcule as raízes da equação do 2º grau seguindo a 
fórmula: Δ = b² - 4ac, x = (-b ± raiz(Δ)) / (2a).'''

import os
import math


os.system('cls')

print('-'*70)
print('EQUAÇÃO DO 2º GRAU')
print('='*70)

a = int(input('Qual o valor de a: '))
b = int(input('Qual o valor de b: '))
c = int(input('Qual o valor de c: '))

delta = math.pow(b, 2) - (4 * a * c)

x1 = (-b + math.sqrt(delta)) / (2 * a)

x2 = (-b - math.sqrt(delta)) / (2 * a)

print(f'Equação do 2º com valores de a={a} b={b} c={c} tem:')
print(f'Delta = {delta}')
print(f"X' = {x1}")
print(f"X'' = {x2}")
