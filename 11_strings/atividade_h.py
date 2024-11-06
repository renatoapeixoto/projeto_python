''' Faça um programa que leia o nome de um aluno e mostre quantas vezes a letra 
'o' aparece e em que posição ela aparece pela primeira e última vez. '''

import os 


os.system('cls' if os.name == 'nt' else 'clear')

nome_aluno = input('Digite o nome do aluno: ')
nome_aluno = nome_aluno.lower()
alfanumerico = nome_aluno.isalpha()
primeira_pos = nome_aluno.find('o')
ultima_pos = nome_aluno.rfind('o')

if nome_aluno :
    if  alfanumerico == True:
        contador_o = nome_aluno.count('o')
        
        if contador_o > 0 and  contador_o <= 1:
            print(f'A letra "o" apareceu : {contador_o} vezes. Na primeira posição: {primeira_pos}')
        elif contador_o > 1 :
            print(f'A letra "o" apareceu : {contador_o} vezes.')
            print(f'Na primeira posição: {primeira_pos} e na ultima posição: {ultima_pos}')
        else :
            print('Não tem nenhum letra "o" nesse nome.')
    
    else :
        print('Nome inválido, verifique se digitou algum numero.')

else :
    print('Campo vazio, preencha o seu nome.')