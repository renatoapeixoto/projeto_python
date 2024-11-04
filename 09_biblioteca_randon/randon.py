# Importando as bibliotecas necessárias
import random
import os

# Limpando o terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Exibindo título
print('-' * 70)
print('BIBLIOTECA RANDOM')
print('=' * 70)

# Gerando um número aleatório entre 0 e 1
print('\nNúmero aleatório')
numero_aleatorio = random.random()
print(f'O número gerado foi: {numero_aleatorio}')
print('-' * 70)

# Gerando um número inteiro aleatório entre 1 e 20
print('\nNúmero aleatório inteiro')
aleatorio_inteiro = random.randint(1, 20)
print(f'O número inteiro gerado foi: {aleatorio_inteiro}')
print('-' * 70)

# Gerando um número decimal aleatório no intervalo de 1 a 10
print('\nNúmero aleatório decimal no intervalo')
aleatorio_decimal = random.uniform(1, 10)
print(f'O número decimal gerado foi: {aleatorio_decimal}')
print('-' * 70)

# Sorteando um nome em uma lista
print('\nSorteio em uma lista')
lista = ['Ágata', 'Coly', 'Isis', 'Bia']
nome_sorteado = random.choice(lista)
print(f'Lista: {lista}')
print(f'O nome escolhido foi: {nome_sorteado}')
print('-' * 70)

# Embaralhando uma lista de forma aleatória
print('\nEmbaralhar sequência')
lista2 = ['Ágata', 'Coly', 'Isis', 'Bia']
print(f'Lista original: {lista2}')

# Embaralhando a lista in-place
random.shuffle(lista2)
print(f'Lista embaralhada: {lista2}')
print('-' * 70)

# Selecionando uma amostra aleatória de elementos únicos de uma população
print('\nRetorno de elementos únicos de uma população')
numeros = [1, 2, 3, 4, 5, 6, 7]
amostra_aleatoria = random.sample(numeros, 5)
print(f'Lista original: {numeros}')
print(f'Retorno da amostragem: {amostra_aleatoria}')
print('-' * 70)
