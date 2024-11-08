'''
Faça um programa que receba um ângulo qualquer. 
Em seguida, calcule o seno, cosseno e tangente do ângulo, 
limitando a saída a 2 casas decimais.
'''

import math
import os


os.system('cls')

print('-'*70)
print('PROGRAMA PARA CALCULAR RAZÃO TRIGONOMÉTRICA')
print('='*70)
print()

resultado = 0.0

angulo = float(input('Informe o ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O Seno de {angulo}° é {seno:.2f}')
print(f'O Cosseno de {angulo}° é {cosseno:.2f}')
print(f'A tangente de {angulo}° é {tangente:.2f}')

print('Fim do programa!')
