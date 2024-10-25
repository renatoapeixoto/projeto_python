#--------------------------------------------------------------------------------
#Desenvolva um programa que solicite um valor em reais e calcule quantos dólares 
#podem ser comprados com esse valor.
#--------------------------------------------------------------------------------

# imports
import os

#limpar a tela
os.system('cls')

# Solicita ao usuário o valor em reais
valor_reais = float(input("Digite o valor em reais (R$): "))

# Define uma taxa de câmbio atual ou permite que o usuário insira a taxa
taxa_cambio = float(input("Digite a taxa de câmbio atual (1 dólar em reais): "))

# Calcula quantos dólares podem ser comprados
valor_dolares = valor_reais / taxa_cambio

# Exibe o resultado
print("-" * 80)
print(f"Com R${valor_reais:.2f}, você pode comprar aproximadamente US${valor_dolares:.2f}.")
print("-" * 80)
