#--------------------------------------------------------------------------------
#Faça um programa que receba um número inteiro e exiba seu sucessor e antecessor.
#--------------------------------------------------------------------------------

# imports
import os

#limpar a tela
os.system('cls')

# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Calcula o antecessor e o sucessor
antecessor = numero - 1
sucessor = numero + 1

# Exibe o antecessor e o sucessor
print("-" * 70)
print(f"O antecessor de {numero} é..: {antecessor}")
print(f"O sucessor de {numero} é....: {sucessor}")
print("-" * 70)