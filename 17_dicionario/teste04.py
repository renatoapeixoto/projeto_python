import os
os.system('cls')

# Lista para armazenar vários filmes (cada filme será um dicionário)
filmes = []

# Cadastro inicial de 3 filmes para exemplo
for i in range(3):
    print(f"\nCadastro do {i + 1}º filme:")
    filme = input('Filme: ')
    genero = input('Gênero: ')
    duracao = input('Duração: ')
    classificacao = input('Classificação: ')
    
    # Criando o dicionário do filme e adicionando à lista
    filmes.append({
        'Filme': filme,
        'Gênero': genero,
        'Duração': duracao,
        'Classificação': classificacao
    })

# Exibir a lista de filmes cadastrados
print("\nFilmes cadastrados:")
for filme in filmes:
    print(filme)

# Alterar informações de um filme
filme_alterar = input('\nDigite o título do filme que deseja alterar: ')

# Buscar e alterar o filme
encontrado = False
for filme in filmes:
    if filme['Filme'].lower() == filme_alterar.lower():
        print("\nFilme encontrado. Insira as novas informações:")
        filme['Filme'] = input('Novo título: ')
        filme['Gênero'] = input('Novo gênero: ')
        filme['Duração'] = input('Nova duração: ')
        filme['Classificação'] = input('Nova classificação: ')
        print("\nFilme alterado com sucesso!")
        encontrado = True
        break

if not encontrado:
    print("\nFilme não encontrado.")

# Exibir a lista de filmes atualizada
print("\nFilmes atualizados:")
for filme in filmes:
    print(filme)
