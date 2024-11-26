import os


os.system('cls')

# Unindo uma lista de palavras em uma string com separador
lista = ['Olá', 'mundo']
print(len(lista)) # 2
juncao = "_".join(lista)  # Junta a lista em uma string com "_" como separador
print(len(juncao)) # 9
juncao1 = ' '.join(lista)
print(len(juncao1)) # 9
print(f"Lista original: {lista}")
print(f"Lista unida em string: {juncao}")
print(f"Lista unida em string: {juncao1}")
print('-' * 70)
# 2
# 9
# 9
# Lista original: ['Olá', 'mundo']
# Lista unida em string: Olá_mundo
# Lista unida em string: Olá mundo

# Para remover todos os espaços em branco da entrada de dados em Python, você 
# pode usar o método .replace()para substituir todos os espaços por uma string 
# vazia. 
# Solicitando a entrada do usuário
entrada = input("Digite algo: ")
# Removendo todos os espaços em branco
entrada_sem_espacos = entrada.replace(" ", "")
# Exibindo o resultado
print("Entrada sem espaços:", entrada_sem_espacos)
# Explicação
# input(): Coleta a entrada do usuário como uma string.
# .replace(" ", ""): Substitui todos os espaços em branco por uma string vazia, eliminando-os.

# Se você quiser remover todos os tipos de espaços (incluindo quebras de linha 
# e tabulações), use o método .join()combinado com .split():
# Entrada do usuário
entrada = input("Digite algo: ")
# Removendo todos os espaços em branco, incluindo tabulações e quebras de linha
entrada_sem_espacos = "".join(entrada.split())
# Exibindo o resultado
print("Entrada sem espaços:", entrada_sem_espacos)
# Diferença entre as abordagens
# .replace(" ", ""): Remover apenas os espaços simples.
# "".join(entrada.split()): Remove todos os espaços, incluindo tabulações ( \t) 
# e quebras de linha ( \n).
# Use a segunda abordagem se quiser garantir que absolutamente todos os espaços
# e caracteres invisíveis sejam removidos.