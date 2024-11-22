import os

# Limpa a tela do terminal/console
os.system('cls')

# Exibição de cabeçalho formatado
print('-' * 70)
print('SAÍDA COM FOR')
print('=' * 70)

# Criando uma lista vazia para armazenar os nomes dos alunos
lista_alunos = []

# Loop para adicionar nomes à lista
for c in range(0, 5):  # Repetição 5 vezes
    nome = str(input('Entre com o nome do aluno: '))  # Solicita o nome
    lista_alunos.append(nome)  # Adiciona o nome à lista

# Linha em branco para separar as seções
print()

# Exibição dos nomes dos alunos
print('Impressão dos nomes de alunos:')

# Loop para exibir os nomes usando o índice
for aluno in range(len(lista_alunos)):  # Itera sobre o comprimento da lista
    print(lista_alunos[aluno], end=' - ')  # Exibe o nome com separação
    if aluno == 3:  # Condicional para pular linha após o quarto elemento
        print()  # Insere uma quebra de linha

# Finalização do programa
print()
print('-' * 70)
print('Fim do programa!')
print('-' * 70)
