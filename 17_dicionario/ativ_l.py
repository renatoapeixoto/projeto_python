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
            {'Filme': 'vingadores', 'Genero': 'ação', 'Duracao': '1:48', 'Classificacao': '12 anos'},
            {'Filme': 'rei leão', 'Genero': 'infantil', 'Duracao': '2:48', 'Classificacao': 'livre'},
            {'Filme': 'avatar 2', 'Genero': 'aventura', 'Duracao': '2:45', 'Classificacao': 'livre'},
         ]
while True:
    print ('MENU PRINCIPAL')
    print ('Opção 1 -  ✅ Incluir Filme')
    print ('Opção 2 -  🖋  Alterar Filme')
    print ('Opção 3 -  💻 Relatórios')
    print ('Opção 4 -  ❌ Sair')

    escolha = input('Digite sua escolha: ')
    if escolha == '1':
        print('-'*80)
        print('CADASTRANDO FILMES')
        contador = len(filmes)
        while True:
            # ENTRADA DE DADOS COM VALIDAÇÃO
            while True:
                filme = input('Digite o nome do Filme: ').strip().lower() 
                if filme == '':
                    print('-'*80)
                    print('🚫 O título do filme não pode está em branco, tente novamente.')
                    print('-'*80)
                    continue
                else:
                    break    
            while True:
                genero = input('Digite o Genero do filme: ').strip().lower()
                if genero == '' or genero.isnumeric():
                    print('-'*80)
                    print('🚫 Erro, não pode está em branco ou ter somente número, tente novamente.')
                    print('-'*80)
                    continue
                else:
                    break
            while True:
                try:
                    duracao = input('Digite a Duracao do filme, (ex: 2:30): ').strip()
                    aux_duracao = duracao.split(':')
                    if duracao == '' or len(aux_duracao[0]) > 2 or len(aux_duracao[1]) > 2 or int(aux_duracao[0]) > 23 or int(aux_duracao[1]) > 59 : # quantidade de digitos da hora e dos minutos
                        print('-'*80)
                        print('🚫 Algo deu errado, possíveis erros:')
                        print('- horas e minutos só pode ter 2 dígitos')
                        print('- horas: 1 à 23, minutos: 1 à 59.')
                        print('- Escrever letras no lugar de números')
                        print('- Deixar em branco, etc...')
                        print('▶ Tente novamente')
                        print('-'*80)
                        continue
                    else:
                        break   
                except: # quando o programa tenta converter o valor da duração de string para inteiro , caso dar algum erro , vem para essa parte do programa.
                    print('-'*80)
                    print('🚫 Algo deu errado, possíveis erros:')
                    print('- horas e minutos só podem ter 2 dígitos')
                    print('- horas: 1 à 23, minutos: 1 à 59.')
                    print('- Escrever letras no lugar de números')
                    print('- Deixar em branco,  etc...')
                    print('▶ Tente novamente')
                    print('-'*80)
                    continue
            while True:
                classificacao = input('Digite a Classificacao do filme: ').strip().lower()
                if classificacao == '':
                    print('-'*80)
                    print('🚫 A classificação do filme não pode está em branco, tente novamente.')
                    print('-'*80)
                    continue
                else:
                    break    
            # inclusão dos dados no cadastro
            filmes.append({'Filme':filme, 'Genero':genero, 'Duracao':duracao, 'Classificacao':classificacao})
            print('-'*80)
            opcao = input('Deseja continuar o cadastrando filmes (S/N) ? ').strip().lower()  # continuar cadastrando
            if opcao == 's':
                continue
            else:
                break
        # Quantidade de filmes 
        print('-'*80)
        print('RESUMO:')
        print(f'O cadastro possui {len(filmes)} filmes:')
        # filme com duração superior a 2 horas 
        for filme in filmes:
            hora_minuto = filme['Duracao'].split(':') # vira uma lista de 2 itens do tipo string, com a hora e o munito separados. 
            hora = int(hora_minuto[0]) * 60
            minuto = int(hora_minuto[1])
            tempo = hora + minuto
            if tempo > 120:
                duracao_maior.update({filme["Filme"]:filme["Duracao"]})
        print(f'{len(duracao_maior)} filmes com duração superior a 2 horas:')
        # classificação livre
        aux_classificacao = {}
        for filme in filmes:
            if filme['Classificacao'].lower() == "livre":
                aux_classificacao.update({filme['Filme']:filme['Classificacao']})
        print(f'{len(aux_classificacao)} filmes com Classificação Livre:')
        print('OBS: Para maiores detalhes consulte em relatórios')
        print('-'*80)
    elif escolha == '2':
        resultado = 0
        print('-'*80)
        print('ALTERAÇÃO DE FILMES')
        print(f'{len(filmes)} Filmes Cadastrados:')
        for item in filmes:
            print(f'• Filme: {item["Filme"].title()} - Gênero: {item["Genero"].title()} - Duração: {item["Duracao"]} - Classificação: {item["Classificacao"].title()}')
        print('-'*80)
        alterar_filme = input('Digite o filme que deseja alterar: ')
        for item in filmes: # loop na lista, cada item da lista é um dicionário 
            if  item['Filme'].lower().strip() == alterar_filme.lower().strip(): # para comparar com letras minúscula e sem espaço evitando erros 
                while True:
                    filme = input('Altere o nome do Filme: ').strip().lower() 
                    if filme == '':
                        print('-'*80)
                        print('🚫 O título do filme não pode está em branco, tente novamente.')
                        print('-'*80)
                        continue
                    else:
                        item['Filme'] = filme
                        break    
                while True:
                    genero = input('Altere o Genero do filme: ').strip().lower()
                    if genero == '' or genero.isnumeric():
                        print('-'*80)
                        print('🚫 Erro, não pode está em branco ou ter somente número, tente novamente.')
                        print('-'*80)
                        continue
                    else:
                        item['Genero'] = genero
                        break
                while True:
                    try:
                        duracao = input('Altere a Duracao do filme, (ex: 2:30): ').strip()
                        aux_duracao = duracao.split(':')
                        if duracao == '' or len(aux_duracao[0]) > 2 or len(aux_duracao[1]) > 2 or int(aux_duracao[0]) > 23 or int(aux_duracao[1]) > 59 : # quantidade de digitos da hora e dos minutos
                            print('-'*80)
                            print('🚫 Algo deu errado, possíveis erros:')
                            print('- horas e minutos só pode ter 2 dígitos')
                            print('- horas: 1 à 23, minutos: 1 à 59.')
                            print('- Escrever letras no lugar de números')
                            print('- Deixar em branco, etc...')
                            print('▶ Tente novamente')
                            print('-'*80)
                            continue
                        else:
                            item['Duracao'] = duracao
                            break   
                    except: # quando o programa tenta converter o valor da duração de string para inteiro , caso dar algum erro , vem para essa parte do programa.
                        print('-'*80)
                        print('🚫 Algo deu errado, possíveis erros:')
                        print('- horas e minutos só podem ter 2 dígitos')
                        print('- horas: 1 à 23, minutos: 1 à 59.')
                        print('- Escrever letras no lugar de números')
                        print('- Deixar em branco,  etc...')
                        print('▶ Tente novamente')
                        print('-'*80)
                        continue
                while True:
                    classificacao = input('Altere a Classificacao do filme: ').strip().lower()
                    if classificacao == '':
                        print('-'*80)
                        print('🚫 A classificação do filme não pode está em branco, tente novamente.')
                        print('-'*80)
                        continue
                    else:
                        item['Classificacao'] = classificacao
                        print('-'*80)
                        break    
                print('Filme alterado com sucesso')        
                for item in filmes:
                    print(f'• Filme: {item["Filme"].title()} - Gênero: {item["Genero"].title()} - Duração: {item["Duracao"]} - Classificação: {item["Classificacao"].title()}')
                print('-'*80)
            else:
                resultado += 1
        if resultado == len(filmes):
            print('Filme não cadastrado')
            print('-'*80)       
    elif escolha == '3':
        os.system('cls')
        while True:
            print('-'*80)
            print ('MENU RELATÓRIOS')
            print ('Opção 1 -  Cadastro detalhado')
            print ('Opção 2 -  Filmes em ordem crescente')
            print ('Opção 3 -  Filmes em ordem decrescente')
            print ('Opção 4 -  Consutar filmes pelo Titulo')
            print ('Opção 5 -  Filmes com a classificao livre')
            print ('Opção 6 -  Filmes superior a 2 horas de duração')
            print ('Opção 7 -  ❌ Sair')
            print('-'*80)
            escolha = input('Digite sua escolha: ')
            if escolha == '1':
                print('-'*80)
                print(f'Esse cadastrado possui {len(filmes)} Filmes:')
                for item in filmes:
                    print(f'• Filme: {item["Filme"].title()} - Gênero: {item["Genero"].title()} - Duração: {item["Duracao"]} - Classificação: {item["Classificacao"].title()}')
            elif escolha == '2':
                # filmes ordem crescente
                print('-'*80)
                aux_filmes = []
                for filme in filmes:
                    aux_filmes.append(filme['Filme'].title())
                aux_filmes = sorted(aux_filmes)
                print(f'O Relatório possui {len(aux_filmes)} filmes:')
                for filme in aux_filmes:
                    print('• ',filme)
            elif escolha == '3':
                # filmes decrescente
                print('-'*80)
                aux_filmes = []
                for filme in filmes:
                    aux_filmes.append(filme['Filme'].title())
                aux_filmes = sorted(aux_filmes, reverse= True)
                print(f'O Relatório possui {len(aux_filmes)} filmes ordenados:')
                for filme in aux_filmes:
                    print('• ',filme)
            elif escolha == '4':
                print('-'*80)
                lista_consulta = []
                consultar = input('Digite o nome do título do filme: ').lower()
                for filme in filmes:
                    if consultar in filme['Filme']:
                        lista_consulta.append(filme['Filme'])
                if len(lista_consulta) < 1:
                    print('Filme não encontrado')
                else:
                    lista_consulta = sorted(lista_consulta)
                    print(f'O Relatório possui {len(lista_consulta)} filmes:')
                    for item in lista_consulta:
                        print(f'• Filme: {item.title()}')
            elif escolha == '5':
                # classificação livre
                print('-'*80)
                aux_classificacao = {}
                for filme in filmes:
                    if filme['Classificacao'].lower() == "livre":
                        aux_classificacao.update({filme['Filme']:filme['Classificacao']})
                print(f'O Relatório possui {len(aux_classificacao)} filmes:')
                for chave in aux_classificacao.keys():
                    print(f'• {chave.title()}')
            elif escolha == '6':
                # cadastrar filme em um diconario separado com duração superior a 2 horas 
                print('-'*80)
                for filme in filmes:
                    hora_minuto = filme['Duracao'].split(':') # vira uma lista de 2 itens do tipo string, com a hora e o munito separados. 
                    hora = int(hora_minuto[0]) * 60
                    minuto = int(hora_minuto[1])
                    tempo = hora + minuto
                    if tempo > 120:
                        duracao_maior.update({filme["Filme"]:filme["Duracao"]})
                print('Filmes com duração superior a 2 horas:')
                print(f'O Relatório possui {len(duracao_maior)} filmes:')
                for chave, valor in duracao_maior.items():
                    print(f'• {chave.title()} -> {valor.title()}')
            elif escolha == '7':
                os.system('cls')
                break    
            else:
                print('\n⛔  Verifique se voçê digitou (1 - 5)\n')    
    elif escolha == '4':
        exit()
    else:
        print('\n⛔  Verifique se voçê digitou (1 - 5)\n')
