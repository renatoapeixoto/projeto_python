#  Ler uma lista com 10 números, depois apresente o maior e o menor número da lista
import os


os.system('cls')
numeros = []
for i in range (10,):   
    numero = input(f'Digite numeros {i+1}: ')
    numeros.append(float(numero))
print(numeros)
maior = max(numeros)
menor = min(numeros)
print(f'numero maior: {maior} numero mennor: {menor}')