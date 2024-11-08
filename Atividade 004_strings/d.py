# Faça um programa que leia uma frase e depois mostre na tela:
# - A frase em minúsculo
# - a frase em maiúscula
# - quantidade de caracteres na frase
# - quantas letras tem a 2ª palavra na frase.

# Importando as bibliotecas
import os


os.system('cls')

print('-'*50)
print('CONVERSÕES EM FRASE')
print('-'*70)

frase = str(input('Entre com uma frase: '))

minusculo = frase.lower()
maiusculo = frase.upper()
quant_caractere = len(frase)
frase_quebrada = frase.split()
quantidade_palavra2 = len(frase_quebrada[1])

print(f'A frase minúscula: {minusculo}')
print(f'A frase maiúscula: {maiusculo}')
print(f'A frase tem {quant_caractere} caracteres')
print(f'A segunda palavra é: {frase_quebrada[1]}')
print(f'A segunda palavra tem {quantidade_palavra2} caracteres')
print('-'*70)