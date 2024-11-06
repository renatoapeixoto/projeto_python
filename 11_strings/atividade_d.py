'''  Faça um programa que leia uma frase e depois exiba na tela:
• A frase em minúsculas, a frase em maiúsculas, a quantidade de caracteres na 
frase e quantas letras tem a 2ª palavra na frase.   '''

import os 


os.system('cls' if os.name == 'nt' else 'clear')
frase = input('Digite uma frase: ')

print('-' * 70)
frase =  frase.lower()
print(frase)
print('-' * 70)

frase =  frase.upper()
print(frase)
print('-' * 70)

tamanho_frase = len(frase)
print(tamanho_frase)
print('-' * 70)

lista = frase.split() # cria uma lista com indice com as palavras da frase
lista = len(lista[1]) # pego o tamanho do 2 elemento da lista 
print(lista)