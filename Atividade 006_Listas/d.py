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
while contador <= (3):
    nota = input(f'Digite "S" par sair, ou digte a {contador+1}º nota: ').lower().strip()
    # validacao
    if nota == 's':
        break
    elif nota.isnumeric():
        # incluir na lista
        notas.append(nota)
        # contar notas
        contador += 1 
        # somar notas
        continue    
    # se entrada vazia
    elif not nota:
        print('Você precisa digitar uma nota !')
        print('-' * 80)
        continue
    # se entrada diferente de numero e vazio
    else:
        print('opação inválida')
        print('-' * 80)
    # fim do loop
# Converter para numero se lista não estiver vazio   
if len(notas) == 4: 
    for i in range (len(notas)):
        notas[i] = float(notas[i])
        soma_nota += notas[i] 
    # imprimir media
    media = soma_nota / contador
    print(f'Media das notas: {media}')
elif len(notas) > 0:
    print('Não foram digitados as 4 notas')
else:
    print('Não foram digitada nenhuma nota')