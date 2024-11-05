# Faça um programa que receba o nome 'João da Silva' e, em seguida, substitua 
# 'Silva' por 'Oliveira'.

import os


os.system('cls' if os.name == 'nt' else 'clear')

nome = 'João da Silva'
print(f'Nome orignal: {nome} \n')
novo_nome = nome.replace('Silva', 'Oliveira')
print(f'O novo nome: {novo_nome} \n')
