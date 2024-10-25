#--------------------------------------------------------------------------------
#Desenvolva um programa que solicite três valores ao usuário. 
#Em seguida, calcule e exiba a soma e a multiplicação desses valores.
#--------------------------------------------------------------------------------

# imports
import os

#limpar a tela
os.system('cls')

# Entrada de dados
valor1 = int(input("Digite o primeiro valor : "))
valor2 = int(input("Digite o segundo valor..: "))
valor3 = int(input("Digite o terceiro valor.: "))
print("-" * 70)

# Calcula a soma e a multiplicação dos valores
soma = valor1 + valor2 + valor3
multiplicacao = valor1 * valor2 * valor3

# Exibe os resultados
print(f"A soma dos valores {valor1} + {valor2} + {valor3} é............: {soma} ")
print(F"A multiplicação dos valores {valor1} x {valor2} x {valor3} é...: {multiplicacao} ")

