'''
Faça um programa que receba 2 valores, faça a divisão entre eles. 
Se a divisão não for inteira, o programa deverá arredondar o resultado 
para cima e para baixo. Faça a validação para divisão por 0.
'''

import math
import os


os.system('cls')

print('-'*70)
print('PROGRAMA PARA CALCULAR A DIVISÃO')
print('='*70)
print()

resultado = 0

numero1 = int(input('Entre com um número: '))
numero2 = int(input('Entre com outro número: '))

if numero2 == 0:
    print('Divisão inválida!')
else:
    divisao = numero1 / numero2
    
    arredondar_cima = math.ceil(divisao)
    arredondar_baixo = math.floor(divisao)
    print(f'A divisão de {numero1} / {numero2} = {divisao}')
    print(f'Arredondando para cima: {arredondar_cima}')
    print(f'Arredondando para baixo: {arredondar_baixo}')

print('Fim do programa!')