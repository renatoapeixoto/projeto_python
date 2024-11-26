# Faça um programa que leia as vogais, depois mostre-as em ordem inversa.
import os


os.system('cls')
vogais = []
contador = 1
print('-' * 80)
print('ATIVIDADE 006 - LETRA E')
print('-' * 80)
# Entrada 
while contador <= (5):
    vogal = input(f'Digite "S" par sair, ou Digte as vogais, {contador}º vogal: ').lower().strip()
    # validacao
    if vogal == 's':
        break
    elif vogal.isalpha() and vogal in ['a', 'e', 'i', 'o', 'u']:
        if not vogal in vogais: 
            # incluir na lista
            vogais.append(vogal)
            # contar notas
            contador += 1 
            # somar notas
            continue
        else:
            print('Vogal repetida !')
            continue    
    # se entrada vazia
    elif not vogal:
        print('Você precisa digitar uma vogal !')
        print('-' * 80)
        continue
    # se entrada diferente de numero e vazio
    else:
        print('opação inválida !')
        print('-' * 80)
    # fim do loop
# Converter para numero se lista não estiver vazio   
if len(vogais) == 5: 
    vogais.sort()
    print(vogais)
    vogais.reverse()
    #vogais = vogais[::-1]
    print(vogais)
elif contador > 0:
    print('Não foram digitados todas vogais')
    print('-' * 80)
else:
    print('Não foram digitada nenhuma nota')
    print('-' * 80)