''' 4. Exercício de Nível Muito Difícil: Sequência Alternada
Escreva um programa que receba uma lista de números inteiros e verifique se os
números alternam entre positivos e negativos. Por exemplo, [1, -2, 3, -4, 5] é 
alternado, mas [1, -2, -3, 4] não é. O programa deve dizer se a lista é
alternada ou não. '''
import os


os.system('cls' if os.name == 'nt' else 'clear')

################################################################################
################################################################################
# numeros = input('Digite uma lista na mesma linha: ')

# # Converter uma lista string para inteiro
# numeros = numeros.split()
# numeros = [int(numero) for numero in numeros]
# print(numeros)

# tamanho = len(numeros)
# sinal = ''

# if numeros[0] > 0 :
#     sinal = 'positivo'
# else :
#     sinal = 'negativo'
    
# if sinal == 'positivo' :
#     for i in range(0, tamanho, 2) :
#             if numeros[i] > 0 and numeros[i+1] < 0 :
#                 resultado = 'lista alternada'
#             else :
#                 resultado = 'lista não alternada'
# else :
#     for i in range(0, tamanho, 2) :
#             if numeros[i] < 0 and numeros[i+1] > 0 :
#                 resultado = 'lista alternada'
#             else :
#                 resultado = 'lista não alternada'

# print(resultado)
################################################################################
################################################################################
numeros = list(map(int, input("Digite uma lista de números inteiros separados \
por espaço: ").split()))

alternada = True

for i in range(len(numeros) - 1):
    if (numeros[i] > 0 and numeros[i + 1] > 0) or (numeros[i] < 0 and numeros[i + 1] < 0):
        alternada = False
        break

if alternada:
    print("A lista é alternada.")
else:
    print("A lista não é alternada.")

