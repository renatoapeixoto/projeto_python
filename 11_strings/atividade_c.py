# Faça um programa que leia o nome de uma pessoa e verifique se a palavra 
# 'Oliveira' está presente neste nome, mostrando True ou False.

import os


os.system('cls' if os.name == 'nt' else 'clear')

nome = input('Digite um nome: ')
nome = nome.title()
nome_contido = 'Oliveira' in nome
if nome :
    if nome_contido :
        print(f'Oliveira está contido em: {nome}')
    else :
        print(f'Oliveira não está contido em: {nome}')
else :
    print('Nome inválido')
