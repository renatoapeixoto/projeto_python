#Faça um programa que receba o nome completo de uma pessoa e, posteriormente,
#imprima esse nome separadamente.

import os
os.system('cls')

nome = input('Digite um Nome: ')
nome = nome.title()

nome = nome.split()

for i in range(len(nome)) :
    print(nome[i])
