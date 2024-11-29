# Crie uma lista com 6 nomes, depois verifique se o nome ‘Pedro’ está nessa lista.
import os


os.system('cls')
nomes = []
for i in range (6):
    nomes.append(input(f'Digite o {i+1} nome: ').lower().strip())
nome = input('Digite um nome para verificar se está dentro da lista:')
if nome in nomes:
    print('nome está dentro da lista')
else:
    print('nome não está dentro da lista')    