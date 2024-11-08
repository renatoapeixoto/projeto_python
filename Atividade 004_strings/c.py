# Faça um programa que leia o nome de uma pessoa e
# verifique se há a palavra ‘Oliveira’ neste nome, mostrando True ou False.

# Importando as bibliotecas
import os


os.system('cls')

print('-'*70)
print('ENCONTRAR NOME')
print('-'*70)

nome_completo = str(input('Digite o nome: '))

busca = 'Oliveira' in nome_completo

if busca == True:
    print(f'{busca}! "Oliveira" EXISTE neste nome!')
else:
    print(f'{busca}! "Oliveira" NÃO EXISTE neste nome!')

print('-'*70)