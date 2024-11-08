# Faça um programa que solicite separadamente o nome, o nome do meio e o 
# sobrenome de uma pessoa. Em seguida, imprima o nome completo.
import os

os.system('cls' if os.name == 'nt' else 'clear')


nome = input('Digite o primeiro nome: ').strip()
nome_meio = input('Digite o nome do meio: ').strip()
nome_ultimo = input('Digite o ultimo nome: ').strip()

if nome and nome_meio and nome_ultimo :
    nome_completo = nome.capitalize() + ' ' + nome_meio.capitalize()+ ' ' + nome_ultimo.capitalize()
    print(f'O nome completo é: {nome_completo} ')
else :
    print('Nome está invalido')

