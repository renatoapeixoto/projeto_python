# Utilizando o exercício anterior, coloque todas as listas em ordem crescente de valor
import random
import os


os.system('cls')
numeros = []
aux = []
listas_fatiadas = []
for i in range (50):
    numeros.append(random.randint(1,50))
print(numeros)
print()
for numero in numeros:
    aux.append(numero)
    tamanho = len(aux)
    if tamanho % 10 == 0:
        listas_fatiadas.append(aux.copy())
        print(aux)
        aux.clear()
print()
for item in listas_fatiadas:
    item.sort()
    print(item)

print()
