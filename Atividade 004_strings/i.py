# Faça um programa que receba o nome completo de uma pessoa, 
# em seguida mostre o primeiro e o último nome.

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

print('-'*70)
print('PROGRAMA QUE BUSCA O PRIMEIRO E O ÚLTIMO NOME')
print('-'*70)

# Entrada
nome = str(input('Digite o seu completo: '))

# processamento
nome_quebrado = nome.split()
primeiro_nome = nome_quebrado[0]
ultimo_nome = nome_quebrado[-1]

print(f'{nome}')
print(f'{nome_quebrado}')
print(f'Primeiro Nome: {primeiro_nome}')
print(f'Último Nome: {ultimo_nome}')

print('-'*70)