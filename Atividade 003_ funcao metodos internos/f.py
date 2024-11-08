# Faça um programa onde o usuário tenta adivinhar o número que o computador está ‘pensando’.

import os
import random


os.system('cls')

print('-'*70)
print('JOGO DA ADVINHAÇÃO')
print('='*70)

resposta = ''

# computador pensando
npc = random.randint(1, 20)

# usuário adivinhando
jogador = int(input('Estou pensando em um número entre 1-20: '))

if (jogador == npc):
    resposta = 'Você acertou!!!'
else:
    resposta = 'Você Errou!!!'

print(resposta)

print('Fim do programa!')
