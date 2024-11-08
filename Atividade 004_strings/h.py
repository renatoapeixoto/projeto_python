# Faça um programa que leia o nome de um aluno e 
# mostre quantas vezes aparece a letra ‘o’ e em que 
# posição ela aparece a 1ª e pela última vez.

# Importando as bibliotecas
import os


os.system('cls')

print('-'*70)
print('Programa que calcula a quantidade de "o" e posição na String')
print('-'*70)

nome = str(input('Entre com o nome do aluno: ')).lower()

quant_o = nome.count('o')

# +1: indica a posição na frase, não no índice
primeiro_o = nome.find('o') + 1
ultimo_o = nome.rfind('o') + 1

# Saída
print(f'O caracter "o" aparece {quant_o} vezes')
print(f'O caracter "o" aparece a primeira vez na posição {primeiro_o}')
print(f'O caracter "o" aparece a pela última vez na posição {ultimo_o}')
print('-'*70)