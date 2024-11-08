'''
Faça um programa que receba um valor e mostre sua raiz quadrada. 
Para raízes que não são exatas, arredonde para cima ou para baixo. 
Faça a validação para números negativos, avisando ao usuário que 
o resultado será um número complexo.
'''

import math
import os


os.system('cls')

print('-'*70)
print('PROGRAMA PARA CALCULAR A RAIZ QUADRADA')
print('='*70)
print()

resultado = 0

numero = int(input('Entre com um número inteiro: '))

if numero <= 0:
    print('Raiz inválida ou não existe no conjunto dos números Reais!')
else:
    resultado = math.sqrt(numero)
    print(f'A raiz quadrade de {numero} é: {resultado}')

print('Fim do programa!')