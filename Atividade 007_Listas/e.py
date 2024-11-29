# Faça um programa que receba 7 números inteiros. Depois quebre essa lista em: 
# lista de pares e lista de ímpares. 
# Inicializando as listas
import os


os.system('cls')

numeros = []
pares = []
impares = []

# Recebendo 7 números inteiros
print("Digite 7 números inteiros:")
for i in range(7):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

# Separando os números em pares e ímpares
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Exibindo os resultados
print("\nLista completa:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
