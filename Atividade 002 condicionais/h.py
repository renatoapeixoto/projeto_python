# Faça um programa que calcule a equação x² - 6x + 5. 
# As raízes são {5, 1}. Esse cálculo deverá ser feito sem ajuda de funções ou métodos. 
# Somente utilizando o que foi aprendido até o momento.

'''
os coeficientes “a”, “b” e “c” devem pertencer aos números reais
e “a” deve ser diferente de 0.
'''

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

print('-'*70)
print('PROGRAMA PARA CALCULAR A EQUAÇÃO x² - 6x + 5  ')
print('='*70)
print()

# Declarção
resposta = ''

#Entrada de dados
a = int(input('Informe o valor de "a": '))
b = int(input('Informe o valor de "b": '))
c = int(input('Informe o valor de "c": '))

# Condicional (só para o a)
if (a == 0):
    resposta = 'Não é uma equação do segundo grau!'

else:

    #Calcular o Delta
    delta = (b ** 2) - (4 * a * c)

    #Calculando as raízes
    x1 = (-b + (delta ** (1/2))) / (2 * a)
    x2 = (-b - (delta ** (1/2))) / (2 * a)

    print(f'As raízes da equação são ({x1}, {x2})')
    print()
    print('-'*70)

# Saída
print('='*70)
print(resposta)
print('-'*70)
