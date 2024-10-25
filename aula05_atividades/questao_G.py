#--------------------------------------------------------------------------------
#Crie um programa que converta uma medida em metros para centímetros e milímetros.
#--------------------------------------------------------------------------------

# imports
import os

#limpar a tela
os.system('cls')

# Solicita ao usuário uma medida em metros
metros = float(input("Digite uma medida em metros: "))

# Converte para centímetros e milímetros
centimetros = metros * 100
milimetros = metros * 1000

# Exibe os resultados
print("-" * 80)
print(f"{metros} metros equivalem a {centimetros} centímetros.")
print(f"{metros} metros equivalem a {milimetros} milímetros.")
print("-" * 80)