#--------------------------------------------------------------------------------
# Desenvolva um programa que peça um número qualquer e calcule o dobro e o triplo 
# desse número.
#--------------------------------------------------------------------------------

# imports
import os

#limpar a tela
os.system('cls')

# Solicita ao usuário um número
numero = float(input("Digite um número: "))

# Calcula o dobro e o triplo
dobro = numero * 2
triplo = numero * 3

# Exibe o dobro e o triplo usando f-strings para formatação
print("-" * 70)
print(f"O dobro de {numero} é..: {dobro}")
print(f"O triplo de {numero} é.: {triplo}")
print("-" * 70)