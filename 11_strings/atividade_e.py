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

print(total)
