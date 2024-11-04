''' Faça um programa que receba um ângulo qualquer. Em seguida, calcule o seno, 
cosseno e tangente do ângulo, limitando a saída a 2 casas decimais.  '''

import os
import math


# Limpando o terminal
os.system('cls' if os.name == 'nt' else 'clear') # windonws cls, outros clear.

angulo = int(input('Digite o angulo: '))

# Para achar o sin, con e tan, precisa achar também o radiando do angulo
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O seno de {angulo} é: {seno:.2f}')
print(f'O cosseno de {angulo} é: {cosseno:.2f}')
print(f'A tangente de {angulo} é: {tangente:.2f}')