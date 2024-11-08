# Faça um programa que receba o nome completo de uma pessoa e
# depois imprima esse nome separadamente.

# Importando as bibliotecas
import os

# Limpando o terminal
os.system('cls')

print('-'*70)
print('PROGRAMA PARA SEPARAR NOME')
print('-'*70)

nome = str(input('Digite o nome da pessoa: '))

nome_separado = nome.split()

print(f'Nome completo: {nome}')
print(f'Nome separado: {nome_separado}')
print('-'*70)
