# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números 
# ímpares, ao final do processo exiba na tela quantos números ímpares foram
# encontrados nesse intervalo, assim como a soma dos mesmos.

import os


os.system('cls')

contador = 0

for impar in range (1,101,2):
    contador += impar

print(contador) 