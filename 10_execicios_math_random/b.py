'''Faça um programa que receba 2 valores, faça a divisão entre eles. Se a divisão 
não for inteira, o programa deverá arredondar o resultado para cima e para 
baixo. Faça a validação para divisão por 0.'''
import os
import math

# limpa a tela
os.system('cls' if os.name == 'nt' else 'clear')

# Entradas
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))


# Verifica se o divisor é zero
if valor2 == 0:
    print("Erro: Divisão por zero não é permitida.")
else:
    # Calcula o resultado da divisão
    resultado = valor1 / valor2
    if resultado.is_integer() :
        print(f'Valor da divisao é : {resultado}')
    else :
        resultado_cima = math.ceil(resultado)
        resultado_baixo = math.floor(resultado)
        print(f'Valor arrendondado para cima: {resultado_cima:.2f}')
        print(f'Valor arrendondado para baixo: {resultado_baixo:.2f}')
