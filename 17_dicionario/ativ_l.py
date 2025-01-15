# Crie um programa para cadastrar filmes em um cinema. Para cada filme, o programa
# deve armazenar informações como título, gênero, duração e classificação indicativa. 
# O programa deve permitir que o usuário cadastre pelo menos 5 filmes e possibilite
# alterações nas informações, caso necessário. Após o cadastro, o programa deve 
# listar todos os filmes, ordenados por título, e gerar um relatório que indique
# quantos filmes têm duração superior a 2 horas e quantos têm classificação 
# indicativa "Livre".


import os 
os.system('cls')

filmes = [
            {'Filme': 'Avatar', 'Gênero': 'Aventura', 'Duração': '2.5', 'Classificação': 'Livre'},
            {'Filme': 'Titanic', 'Gênero': 'Romance', 'Duração': '3.1', 'Classificação': '12 anos'},
            {'Filme': 'Vingadores', 'Gênero': 'Ação', 'Duração': '2.2', 'Classificação': '12 anos'}
         ]

def incluir():
    
    print('CADASTRO DE FILMES')
    print(f'Existe {len(filmes)} Filmes Cadastrados:')
    for filme in filmes:
        print(filme['Filme'])
    
    while True:
        filme = input('Filme: ')
        genero = input('Genero: ')
        duracao = input('Duracao: ')
        classificacao = input('Classificacao: ')
        
        filmes.append({'Filme':filme, 'Genero':genero, 'Duracao':duracao, 'Classificacao':classificacao})
        print(filmes)

        sair = input('Deseja Sair, (S/N): ').lower()
        if sair == 's':
            break

def alterar():
    print('-'*80)
    print('ALTERAÇÃO DE FILMES')
    print(f'Existe {len(filmes)} Filmes Cadastrados:')
    for filme in filmes:
        print(filme['Filme'])
    print('-'*80)
    
    alterar_filme = input('Digite o filme que deseja alterar: ')
    for item in filmes: # loop na lista, cada item da lista é um dicionário 
        if  item['Filme'].lower().strip() == alterar_filme.lower().strip(): # para comparar com letras minúscula e sem espaço evitando erros 
            
            
            print(item['Filme'])
            break
        else:
            print('Filme não encontrado')

def menu():
    print ('MENU PRINCIPAL')
    print ('Opção 1 -  Incluir Ferramentas')
    print ('Opção 2 -  Altera Ferramentas')
    print ('Opção 3 -  Exibir Ferramentas')
    print ('Opção 4 -  Relatorio')
    print ('Opção 5 -  ❌ Sair')


while True:
    menu()
    escolha = input('Digite sua escolha: ')
    if escolha == '1':
        incluir()
    elif escolha == '2':
        alterar()
    elif escolha == '3':
        pass
    elif escolha == '4':
        pass   
    elif escolha == '5':
        exit()
    else:
        print('\n⚠  Verifique se voçê digitou (1 - 5)\n.')