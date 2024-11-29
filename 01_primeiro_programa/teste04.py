# #### 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma 
# mensagem caso o valor seja inválido e continue pedindo até que o usuário 
# informe um valor válido.

import os
os.system('cls')

nota =  float(input('Digite una nota de 0 à 10: ').strip())
while not (0 <= nota < 11):
    print('Nota invalida, digite novamente! ')
    nota =  float(input('Digite una nota de 0 à 10: ').strip())

# nota =  float(input('Digite una nota de 0 à 10: ').strip())
# while True:
#     if 0 <= nota < 11:
#         break
#     else:
#         input('Nota invalida, digite novamente: ')



