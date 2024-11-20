# Num frigorifico existem 90 bois. cada boi traz em seu pescoço um cartão 
# cotendo um numero de identificação e seu peso. Faça um algoritmo que escreva 
# o número e o peso do boi mais gordo e do boi mais magro.

import os
os.system('cls')

# Entrada
boi_gordo = 0.0
boi_magro = 0.0
maior_peso = 0.0
menor_peso = 99999999999999999.0
contador = 0
# Processamento
while True :
    identificacao = int(input('Digite a identificação do boi ou < -1 > para sair: '))
    # Sair do loop
    if contador >= 90 or identificacao == -1 :
        break
    peso = int(input('Digte o peso do boi: '))
    print('-'*80)
    # identificacao boi mais gordo
    if peso > maior_peso :
        boi_gordo = identificacao
        maior_peso = peso
    # identificacao boi mais magro 
    if peso < menor_peso :
        boi_magro = identificacao
        menor_peso = peso
    # contagem de boi
    contador += 1
# saida de dados
if contador >= 1 :
    print('-'*80)
    print(f'Identificacao boi gordo : {boi_gordo}')
    print(f'Peso do boi gordo       : {maior_peso}')
    print(f'Identificacao boi magro : {boi_magro}')
    print(f'Peso do boi magro       : {menor_peso}')
    print(f'Quantidade de bois      : {contador}')
    print('-'*80)