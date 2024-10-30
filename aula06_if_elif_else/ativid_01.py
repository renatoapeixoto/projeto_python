# A)  A empresa "TechSolutions" contratou você para desenvolver um programa em
# Python que irá automatizar uma parte do seu sistema de processamento de dados.
# Eles precisam de um programa que solicite ao usuário a entrada de um número
# inteiro e, em seguida, verifique se esse número é par ou ímpar.
# Essa funcionalidade é essencial para o sistema deles, pois eles processam
# grandes conjuntos de dados e precisam classificar os números de forma
# eficiente para realizar cálculos específicos em cada tipo de número.

#imports
import os


# limpa a tela
os.system('cls')

# Entradas e declarações
resultado = ''
numero = int(input('Digte um numero: '))

# processamento
if numero % 2 == 0:
    resultado = f'O numero {numero} é par'
else:
    resultado = f'O numero {numero} é impar'

# saida
print(resultado)