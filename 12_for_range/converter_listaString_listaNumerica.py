import os


os.system('cls' if os.name == 'nt' else 'clear')

# Digite uma lista na mesma linha com espaço de separador 
numeros = input("Digite uma lista de números inteiros \
separados por espaço: ")

# Convertendo string para lista, separador de espaço  
numeros = numeros.split()

# 01 solução - Convertendo list_string para lista_inteira 
numeros = list(map(int, numeros))
print(numeros)
numeros = list(map(float, numeros))
print(numeros)

# 02 solução - Convertendo list_string para lista_inteira 
numeros =  [float(numero) for numero in numeros]
print(numeros)
numeros = [int(numero) for numero in numeros]
print(numeros)