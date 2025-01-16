# Crie um programa para cadastrar filmes em um cinema. Para cada filme, o programa
# deve armazenar informações como título, gênero, duração e classificação indicativa. 
# O programa deve permitir que o usuário cadastre pelo menos 5 filmes e possibilite
# alterações nas informações, caso necessário. Após o cadastro, o programa deve 
# listar todos os filmes, ordenados por título, e gerar um relatório que indique
# quantos filmes têm duração superior a 2 horas e quantos têm classificação 
# indicativa "Livre".

import os 
os.system('cls')
duracao_maior = {}
filmes = [
            {'Filme': 'avatar', 'Genero': 'aventura', 'Duracao': '2:30', 'Classificacao': 'livre'},
            {'Filme': 'titanic', 'Genero': 'romance', 'Duracao': '3:00', 'Classificacao': '12 anos'},
            {'Filme': 'vingadores', 'Genero': 'ação', 'Duracao': '1:48', 'Classificacao': '12 anos'}
         ]
while True:
    print ('MENU PRINCIPAL')
    print ('Opção 1 -  Incluir Filme')
    print ('Opção 2 -  Altera Filme')
    print ('Opção 3 -  Exibir Filme')
    print ('Opção 4 -  Relatorio')
    print ('Opção 5 -  ❌ Sair')

    escolha = input('Digite sua escolha: ')
    if escolha == '1':
        print('-'*80)
        print('CADASTRANDO FILMES')
        contador = len(filmes)
        while True:
            try:
                # entrada de dados
                filme = input('Digite o nome do Filme: ').strip().lower()
                genero = input('Digite o Genero do filme: ').strip().lower()
                duracao = input('Digite a Duracao do filme, (ex: 2:30): ').strip()
                classificacao = input('Digite a Classificacao do filme: ').strip().lower()
                # validação 
                if filme == '' or genero == '' or duracao == '' or classificacao == '':
                    print('-'*80)
                    print('🚫 Nao pode ter campo vazia, tente novamente.')
                    print('-'*80)
                    continue
                # inclusão dos dados
                filmes.append({'Filme':filme, 'Genero':genero, 'Duracao':duracao, 'Classificacao':classificacao})
                contador += 1
                print('-'*80)
                # continuar cadastrando
                opcao = input('Deseja continuar o cadastrando filmes (S/N) ? ').strip().lower()
                if opcao == 's':
                    continue
                else:
                    print()
                # filmes ordenados
                aux_filmes = []
                for filme in filmes:
                    aux_filmes.append(filme['Filme'])
                aux_filmes = sorted(aux_filmes)
                print('Lista de filmes ordenados:')
                for filme in aux_filmes:
                    print('- ',filme)
                print('-'*80)
                # cadastrar filme em um diconario separado com duração superior a 2 horas 
                for filme in filmes:
                    hora_minuto = filme['Duracao'].split(':') # vira uma lista de 2 itens do tipo string, com a hora e o munito separados. 
                    hora = int(hora_minuto[0]) * 60
                    minuto = int(hora_minuto[1])
                    tempo = hora + minuto
                    if tempo > 120:
                        duracao_maior.update({filme["Filme"]:filme["Duracao"]})
                print('Filmes com duração superior a 2 horas:')
                for chave, valor in duracao_maior.items():
                    print(f'- {chave} -> {valor}')
                print('-'*80)
                # classificação livre
                print('Filme com Classificação Livre:')
                for filme in filmes:
                    if filme['Classificacao'].lower() == "livre":
                        print(f'- {filme["Filme"]}')
                print('-'*80)
            except:
                print(f"Ocorreu um erro, tente novamente") # Mostra a mensagem de erro
                continue
            # continuar cadastrando ou sair
            sair = input('Aperte (S) para sair, ou qualquer tecla para continuar: ').lower()
            if sair == 's':
                print('-'*80)
                break
    elif escolha == '2':
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
    
    
    
    
    elif escolha == '3':
        pass
    elif escolha == '4':
        for filme in filmes:
            hora_minuto = filme['Duracao'].split(':') # vira uma lista de 2 itens do tipo string, com a hora e o munito separados. 
            hora = int(hora_minuto[0]) * 60
            minuto = int(hora_minuto[1])
            tempo = hora + minuto
            if tempo > 120:
                duracao_maior.append({filme["Filme"]:filme["Duracao"]})
        print('Filmes com a duração com mais de 2 horas:')
        print(duracao_maior)
    elif escolha == '5':
        exit()
    else:
        print('\n⚠  Verifique se voçê digitou (1 - 5)\n')