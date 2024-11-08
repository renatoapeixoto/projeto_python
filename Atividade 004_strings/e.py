# Faça um programa que receba uma frase,
# depois mostre quantas vezes as vogais foram utilizadas.

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

print('-'*70)
print('PROGRAMA PARA CONTAR VOGAIS')
print('-'*70)

frase = str(input('Digite uma frase: ')).lower()
qtd_vogais = 0
vogal = ['a', 'e', 'i', 'o', 'u']

for i in vogal :
    quant = frase.count(i)
    print(f'A vogal: {i} aparece: {quant} vezes')
    qtd_vogais = qtd_vogais + quant

print(f'Quantidade de vogais: {qtd_vogais}')

# # guardando as ocorrências das vogais
# a = frase.count('a')
# e = frase.count('e')
# i = frase.count('i')
# o = frase.count('o')
# u = frase.count('u')

# quantidade_vogais = a + e + i + o + u

# print(f'A vogal "a" aparece {a} vezes')
# print(f'A vogal "e" aparece {e} vezes')
# print(f'A vogal "i" aparece {i} vezes')
# print(f'A vogal "o" aparece {o} vezes')
# print(f'A vogal "u" aparece {u} vezes')
# print('-'*70)
# print(f'Quantidade de vogais na frase: {quantidade_vogais} vogais')
# print('-'*70)
