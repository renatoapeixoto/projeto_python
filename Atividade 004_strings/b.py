# Faça um programa que receba o nome ‘João da Silva’,
# e em seguida troque o ‘Silva’ para ‘Oliveira’.

# Importando as bibliotecas
import os


os.system('cls')

print('-'*70)
print('PROGRAMA: TROCA DE NOME')
print('='*70)

nome = input('Digite o nome: ')

# usando o replace() para trocar a entrada 'Silva'
novo_nome = nome.replace('Silva', 'Oliveira')

print('-'*70)
print(f'Novo nome: {novo_nome}')
print('='*70)
