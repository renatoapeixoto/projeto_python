''' Faça um programa que receba um número inteiro e mostre na tela:
A quantidade de unidades, a quantidade de dezenas, a quantidade de centenas 
e a quantidade de milhares. '''

import os

# Limpa a tela (compatível com Windows e Unix)
os.system('cls' if os.name == 'nt' else 'clear')

# Recebe um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Calcula cada parte do número
unidades = numero % 10
dezenas = (numero // 10) % 10
centenas = (numero // 100) % 10
milhares = (numero // 1000) % 10

# Mostra os resultados
print(f"Unidades: {unidades}")
print(f"Dezenas: {dezenas}")
print(f"Centenas: {centenas}")
print(f"Milhares: {milhares}")