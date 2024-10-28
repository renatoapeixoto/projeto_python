import os

os.system('cls')

print('-'*70)
print('Estudo de Condicional: Parte 1')
print('-'*70)

# Entrada
numero = float(input('Digite um número: '))
resposta = ''

# Condicional
# operedores relacionais -  > , < , == , != , >= , <=
#  operadores logicos - and , or , not

if numero % 2 == 0:
    resposta = f'O número {numero} é par'
else:
    resposta = f'O número {numero} é ímpar'

# Saída
print('-'*70)
print(resposta)
print('Fim do programa!\n')  # \n salta uma linha
