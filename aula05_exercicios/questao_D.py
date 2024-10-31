#--------------------------------------------------------------------------------
#Implemente um programa que receba dois números e realize a 
#divisão, formatando o resultado com quatro casas decimais. '''
#--------------------------------------------------------------------------------

# imports
import os

#limpar a tela
os.system('cls')

# Solicita ao usuário dois números
numerador = float(input("Digite o numerador: "))
denominador = float(input("Digite o denominador: "))

# processamento
resultado = numerador / denominador

# saida
print("-" * 70)
print(f"O resultado da divisão é: {resultado:.4f}")
print("-" * 70)
