
import os
os.system('cls')

print('-'*80)
a = int(input('Digite 1º numero:'))
b = int(input('Digite 2º numero:'))
c = int(input('Digite 3º numero:'))
aux = 0

if a > b or a > b:
    if b < c:
        aux = a
        a = b
        b = aux
    else:
        aux = a
        a = c
        c = aux
if b > c:
    aux = b
    b = c
    c = aux

print('-'*80)
print(f'O 1º numero é: {a}')
print(f'O 2º numero é: {b}')
print(f'O 3º numero é: {c}')
print('-'*80)
