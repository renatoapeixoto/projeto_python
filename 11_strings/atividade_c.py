# Faça um programa que leia o nome de uma pessoa e verifique se a palavra 
# 'Oliveira' está presente neste nome, mostrando True ou False.

import os


os.system('cls' if os.name == 'nt' else 'clear')

nome = input('Digite um nome: ')
verificar = nome in 'oliveira'
input(verificar)