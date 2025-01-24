# Crie uma função que receba 2 listas: 
# - lista 1: nome, peso, idade 
# - lista 2: John, 40, 1.8
# - Sua função deverá criar um dicionário contendo chave e valor utilizando como base essas duas listas. 
# Depois, seu programa deverá imprimir esse dicionário utilizando uma estrutura de repetição for.

import os
import platform


if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')


def criar_dicionario(lista_chaves, lista_valores):
    
    # Cria o dicionário usando zip para combinar as listas
    dicionario = dict(zip(lista_chaves, lista_valores))
    return dicionario
    
    # dicionario = {}
    # for i in range (0, len(lista1)):
    #     dicionario.update({lista1[i]:lista2[i]})
    # return dicionario

# Listas de exemplo
lista_chaves = ["nome", "peso", "altura"]
lista_valores = ["John", 40, 1.8]

# Cria o dicionário
dicionario_resultado = criar_dicionario(lista_chaves, lista_valores)

# Imprime o dicionário usando um loop for
print("Dicionário gerado:")
print(dicionario_resultado)
for chave, valor in dicionario_resultado.items():
    print(f"{chave}: {valor}")