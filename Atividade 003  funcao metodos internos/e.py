# Faça um programa para sortear um número de 1 a 20.

# Importando as bibliotecas
import os
import random


os.system('cls')

print('-'*70)
print('SORTEIO DE NÚMERO')
print('='*70)

resultado = 0

resultado = random.randint(1, 20)

print(f'O número sorteado foi: {resultado}')

print('Fim do programa!')
