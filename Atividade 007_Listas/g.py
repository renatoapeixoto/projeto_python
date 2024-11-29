# Faça um programa que sorteia os números da Mega Sena e da Lotofácil
import os
import random

os.system('cls')
aleatorio_inteiro = random.randint(1, 20)

numeros_mega_sena = []
numeros_lotofacil = []

for i in range (6):
    mega_sena = random.randint(1,60)
    numeros_mega_sena.append(mega_sena)
print(f'Numeros mega_sena: {numeros_mega_sena}')

for i in range (15):
    lotofacil = random.randint(1,25)
    numeros_lotofacil.append(lotofacil)
print(f'Numeros lotofacil: {numeros_lotofacil}')