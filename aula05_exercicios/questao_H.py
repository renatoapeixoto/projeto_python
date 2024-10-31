#--------------------------------------------------------------------------------
#Implemente um programa que receba um número inteiro e imprima sua tabuada de 
# multiplicação.
#--------------------------------------------------------------------------------

# imports
import os

#limpar a tela
os.system('cls')

# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Imprime a tabuada de multiplicação
print("-" * 80)
print(f"Tabuada de {numero}:")
print("-" * 80)


for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
print("-" * 80)