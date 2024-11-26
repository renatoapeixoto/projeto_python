# Faça um programa que preencha uma lista com 50 números aleatórios. Depois 
# fatie essa lista em 5 listas de 10 elementos.
import random
import os


os.system('cls')

numeros = []
aux = []
listas_fatiadas = []
for i in range (50):
    numeros.append(random.randint(1,50))
print(numeros)
for numero in numeros:
    aux.append(numero)
    tamanho = len(aux)
    if tamanho % 10 == 0:
        listas_fatiadas.append(aux.copy())
        aux.clear()

print(listas_fatiadas)