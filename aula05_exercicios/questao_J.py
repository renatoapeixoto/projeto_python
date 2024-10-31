#--------------------------------------------------------------------------------
#Elabore um programa que peça as dimensões de um retângulo e calcule seu perímetro.
#--------------------------------------------------------------------------------

# imports
import os

#limpar a tela
os.system('cls')

# Solicita ao usuário as dimensões do retângulo
largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo.: "))

# Calcula o perímetro do retângulo
perimetro = 2 * (largura + altura)

# Exibe o resultado
print("-" * 80)
print(f"O perímetro do retângulo é: {perimetro:.2f}")
print("-" * 80)
