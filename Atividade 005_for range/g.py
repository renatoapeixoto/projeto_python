'''
Faça um programa que calcule os números primos em um intervalo pré-determinado 
pelo usuário.
'''

import os
os.system("cls")


inicio = int(input("digite o numero inicial.: "))
final = int(input("digite o numero final.: "))
for i in range(inicio, final):
    divisores = 0
    for j in range(1, i + 1):
        if i % j == 0:
            divisores += 1
    if (divisores== 2):

        print(f"O número {i} é um numero primo.")
