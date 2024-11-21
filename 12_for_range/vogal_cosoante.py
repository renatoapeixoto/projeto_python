# 2. Exercício de Nível Médio : Contagem de Consoantes
# Crie um programa que receba uma frase e conte quantas consoantes ela possui.
# Considere que a frase é composta apenas por letras do alfabeto e ignore 
# secretas e minúsculas.

import os
os.system("cls")

################################################################################
################################################################################
frase = input("Digite uma frase: ").lower()
consoante = 0
vogal = 0
if frase.isalpha :
    
    ''' Tirei os espaços com o .replace() porque depois que contar as consoantes 
    tudo que sobrar na lista vai ser vogal, por isso que tem que tirar os espaços '''
    frase = frase.replace(' ', '')
   
   # Criei uma lista de cada caracter
    frase = list(frase)
    print(frase)

    tamanho = len(frase)
    for i in range (tamanho) :
        # Escrever na linha de baixo use : \ ou envolva entre parenteses ( ) .
        if frase[i] != 'a' and  frase[i] != 'e' and  frase[i] != 'i' and \
           frase[i] != 'o' and frase[i] != 'u':
            consoante = consoante + 1 
        else :
            vogal = vogal +1
    print(f'A frase tem {consoante} consoantes e {vogal} vogais.')        

else : 
    print ('Digite somente letras')

################################################################################
################################################################################
# frase = input("Digite uma frase: ").lower()
# consoantes = "bcdfghjklmnpqrstvwxyz"
# vogal = "aeiou"
# contador_consoantes = 0
# contador_vogal = 0
# for letra in frase:
#     if letra in consoantes:
#         contador_consoantes += 1
#     if letra in vogal : 
#         contador_vogal += 1
# print(f"A frase possui {contador_consoantes} consoantes ")
# print(f"A frase possui {contador_vogal} vogais ")
################################################################################
################################################################################