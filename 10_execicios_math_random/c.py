''' Faça um programa que receba as informações de base e expoente. 
Calcule a potência. '''

import math
import os

os.system('cls' if os.name == 'nt' else 'clear')

base =  float(input('Digite a base: '))
expoente =  float(input('Digite o expoente: '))

resultado = math.pow(base, expoente)
                  
print(f'O Resultado é : {resultado}')                  