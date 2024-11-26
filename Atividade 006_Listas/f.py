# Faça um programa que leia 5 nomes, depois imprima estes nomes com seus 
# respectivos índices.

import os


os.system('cls')
nomes = []
contador = 1
print('-' * 80)
print('ATIVIDADE 006 - LETRA F')
print('-' * 80)
# Entrada 
while contador <= (5):
    nome = input(f'Digite "S" par sair, ou Digte 5 nomes, {contador}º nome: ').lower().strip()
    # validacao
    if nome == 's':
        break
    # se entrada vazia
    elif not nome:
        print('Você precisa digitar uma nome !')
        print('-' * 80)
        continue
    elif nome.isalpha():
        if not nome in nomes: 
            # incluir na lista
            nomes.append(nome)
            # contar notas
            contador += 1 
            # somar notas
            continue
        else:
            print('nome repetida !')
            continue    
    # se entrada diferente de numero e vazio
    else:
        print('opação inválida !')
        print('-' * 80)
    # fim do loop

print('-' * 80)
# Converter para numero se lista não estiver vazio   
if len(nomes) == 5: 
    for i, item in enumerate(nomes):
        print(f'Indice: {i}, Nome: {item} ')
elif not nomes:
    print('Não foram digitada nenhuma nota')
    print('-' * 80)
elif 0 < len(nomes) < 5:
    print('Não foram digitados todas nomes')
    print('-' * 80)
