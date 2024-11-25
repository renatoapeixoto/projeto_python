'''
Faça um programa que leia um número indeterminado de notas (pressione "s" ou "0" para sair). 
Após esta entrada de dados, faça o seguinte:
• Mostre a quantidade de notas que foram lidas.
• Exiba todas as notas na ordem em que foram informadas.
• Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
• Calcule e mostre a soma das notas.
• Calcule e mostre a média das notas.
'''

import os


os.system('cls')
notas = []
contador = 0
soma_nota = 0
print('-' * 80)
print('ATIVIDADE 007 - LETRA A')
print('-' * 80)

# Entrada 
while True:
    nota = input('Digite uma Nota, ou digite "S" ou "0" para sair: ').lower().strip()
    if nota == 's' or nota == '0':
        break
    elif nota.isnumeric():
        notas.append(nota)
        contador += 1 
        continue    
    elif not nota:
        print('Você precisa digitar uma nota, , ou digite "S" ou "0" para sair !')
        print('-' * 80)
        continue
    else:
        print('opação inválida')
        print('-' * 80)

if len(notas) > 0:
    # Converter para numero    
    for i in range (len(notas)):
        notas[i] = float(notas[i])
        soma_nota += notas[i] 
    # Mostre a quantidade de notas que foram lidas.
    print('-' * 80)
    print(f'Foram lidas {contador} notas')
    print('-' * 80)

    #Exiba todas as notas na ordem em que foram informadas.        
    for i, nota in enumerate(notas):
        print(f'Notas {i+1}: {nota} ')
    print('-' * 80)

    # Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
    # Opção 1 - muito rapiso
    # notas.reverse()
    # print(notas)

    # Opção 2 - rapido
    # notas_revertida = notas.__reversed__()        
    # for nota in notas_revertida:
    #     print(nota)

    # Opção 3 - rapido
    notas_revertida = notas[::-1]
    for nota in notas_revertida:
        print(nota)
    print('-' * 80)
            
    # Calcule e mostre a soma das notas.
    print(f'A soma das notas: {soma_nota}')
    print('-' * 80)

    # Calcule e mostre a média das notas.
    media_nota = soma_nota / contador
    print(f'A media das notas: {media_nota}')
    print('-' * 80)
