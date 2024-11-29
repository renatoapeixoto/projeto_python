'''
Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
• O intervalo de 1 até 9
• O intervalo de 8 até 13
• Os números pares
• Os números ímpares
• Os múltiplos de 2, 3 e 4
• Lista reversa
• O produto dos intervalos 5-6 por 11-12
'''
import os
os.system('cls')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# O intervalo de 1 até 9
for numero in numeros:
    if numero < 10:
        print(f'{numero}', end='|')
print()
# O intervalo de 8 até 13
for numero in numeros:
    if 8 <= numero <= 13:
        print(f'{numero}', end='|')
print()
# Os números pares
for numero in numeros:
    if (numero % 2) == 0:
        print(f'{numero}', end='|')
print()
# Os números ímpares
for numero in numeros:
    if (numero % 2) != 0:
        print(f'{numero}', end='|')
print()
# Os múltiplos de 2, 3 e 4
for numero in numeros:
    if (numero % 2) == 0 or (numero % 3) == 0 or (numero % 4) == 0: 
        print(f'{numero}', end='|')
print()
# Lista reversa
# aux = reversed(numeros)
aux = numeros[::-1]
for numero in aux:
    print(f'{numero}', end='|')
print()
# O produto dos intervalos 5-6 por 11-12
a = []
b = []
for numero in numeros:
    if 4 < numero < 7:
        a.append(numero)
    if 10 < numero < 13:
        b.append(numero)
for i, numero in enumerate(a):
    print(numero * b[i],end='|')
print()
