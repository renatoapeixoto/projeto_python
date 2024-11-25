# Faça um programa que preencha uma lista com as notas de 4 alunos, depois 
# imprima a média.
import os


os.system('cls')
notas = []
contador = 0
soma_nota = 0
print('-' * 80)
print('ATIVIDADE 006 - LETRA D')
print('-' * 80)

# Entrada 
for i in range (4):
    nota = input(f'Digite uma Nota {i+1}: ').lower().strip()
    if nota.isnumeric():
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
