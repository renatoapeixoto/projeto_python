# Faça um programa que preencha uma lista com 50 números aleatórios. Depois 
# fatie essa lista em 5 listas de 10 elementos.
import random
import os


# os.system('cls')

# numeros = []
# aux = []
# listas_fatiadas = []
# for i in range (50):
#     numeros.append(random.randint(1,50))
# print(numeros)
# print()
# for numero in numeros:
#     aux.append(numero)
#     tamanho = len(aux)
#     if tamanho % 10 == 0:
#         listas_fatiadas.append(aux.copy())
#         print(aux)
#         aux.clear()
# print()
# print(listas_fatiadas)

# ################################################################################
# import random

# # Gerar 50 números aleatórios entre 1 e 50
# numeros = [random.randint(1, 50) for _ in range(50)]

# # Dividir a lista em 5 sublistas de 10 elementos
# listas_fatiadas = [numeros[i:i + 10] for i in range(0, len(numeros), 10)]

# # Exibir resultados
# print("Lista completa:")
# print(numeros)
# print("\nListas fatiadas:")
# for lista in listas_fatiadas:
#     print(lista)
# ################################################################################
# import random

# # Gerar 50 números aleatórios entre 1 e 50
# numeros = [random.randint(1, 50) for _ in range(50)]

# # Dividir a lista em 5 sublistas de 10 elementos
# listas_fatiadas = []
# for i in range(0, len(numeros), 10):
#     listas_fatiadas.append(numeros[i:i + 10])

# # Exibir resultados
# print("Lista completa:")
# print(numeros)
# print("\nListas fatiadas:")
# for lista in listas_fatiadas:
#     print(lista)
################################################################################
lista4 = []
lista4_fatiada = []
lista4 = [random.randint(1,50) for i in range(1,51)]
lista4_fatiada = [lista4[i:i+10] for i in range(0, len(lista4),10)]
print(lista4_fatiada)