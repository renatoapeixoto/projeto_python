# a) Faça um programa para criar um dicionário com pelo menos 4 elementos. O 
# programa deve permitir que o usuário insira as chaves e valores. As chaves 
# devem ser únicas, e o programa deve garantir isso. Após inserir todos os 
# elementos, o programa deve exibir o dicionário ordenado pelas chaves.

import os
os.system('cls')

print('-'*80)
print('Digite pelo menos com 4 elementos para incluir no dicionario')
print('Digite chave e valor ou "S" para sair')

print('-'*80)

dicionario = dict()
dicionario_ordenado01 = dict()
contador = 1
    
while contador <= 4: # Para garantir que o dicionario tenha pelo menos 4 elementos
    chave = input(f'Digite a {contador}º chave: ').strip().upper()
    if chave == '': # Caso vazio, retornar para digitar 
        print('Você não digitou a chave, tente novamente.')
        continue
    elif chave in dicionario: # Verificar se chave está dentro do dicionario
        print('chave já existe, digite outra chave.')
        continue
    elif chave == 's':
        exit()
    valor = input('Digite o Valor: ').strip().upper()
    dicionario[chave] = valor
    contador += 1
    print('-'*80)
print(f'Dicionario...........: {dicionario}')

# Ordenando e imprimindo o dicionário
dicionario_ordenado01 = {chave:dicionario[chave] for chave in sorted(dicionario.keys())}
print(f'Dicionário_ordenado01: {dicionario_ordenado01}')








# dicionario_ordenado02 = {}
# dicionario_ordenado03 = []
## Opção 1 - Ordenando o dicionário e criando um novo
# dicionario_ordenado01 = {chave:dicionario[chave] for chave in sorted(dicionario)}

# # Opção 2 - Ordenando o dicionário e criando um novo
# for chave in sorted(dicionario):
#     dicionario_ordenado02[chave] = dicionario[chave]

# # Opção 3 - Ordenando o dicionário e criando um novo
# for chave in sorted(dicionario):
#     dicionario_ordenado03.append({chave:dicionario[chave]})

# print(f'dicionario_ordenado01: {dicionario_ordenado01}')
# print(f'dicionario_ordenado02: {dicionario_ordenado02}')
# print(f'dicionario_ordenado03: {dicionario_ordenado03}')

# print(dicionario_ordenado03[0])



