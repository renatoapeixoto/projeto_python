''' CONCEITO
| b - c | < a < b + c, seja a < b + c
| a - c | < b < a + c, ou seja b < a + c
| a - b | < c < a + b, ou seja c < a + b
'''
# não forma triângulo
# 20, 15 e 5 para testar
# 5, 1 e 2 para testar

import os


os.system('cls')

print(' TRIANGULO')
print('-'*70)

a = float(input('Entre com o 1º segmento: '))
b = float(input('Entre com o 2º segmento: '))
c = float(input('Entre com o 13 segmento: '))

if (a <= 0 or b <= 0 or c <= 0):
    resposta = 'Valor de segmento inválido!'

elif ((a < (b + c)) and (b < (a + c)) and (c < (a + c))):
    resposta = f'{a} + {b} + {c}, formam um triângulo!'

else:
    resposta = f'{a} + {b} + {c}, não formam um triângulo!'

print()
print('='*70)
print(resposta)
print('-'*70)



