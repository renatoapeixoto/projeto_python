''' Faça um programa que receba uma frase e, em seguida, mostre quantas 
vezes as vogais foram utilizadas. '''

import os
os.system('cls')

frase = input('Digite uma frase: ')
frase = frase.lower()

a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o')
u = frase.count('u')

total = a + e + i + o + u

print(f'A vogal "a" foi utilizada: {a} vezes.')
print(f'A vogal "e" foi utilizada: {e} vezes.')
print(f'A vogal "i" foi utilizada: {i} vezes.')
print(f'A vogal "o" foi utilizada: {o} vezes.')
print(f'A vogal "u" foi utilizada: {u} vezes.')
print(f'Total utilizada: {total} vezes.')




