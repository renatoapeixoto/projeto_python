import os

# Limpa a tela do terminal/console
os.system('cls')

print('-' * 70)
print('SAÍDA COM IN E NOT IN')
print('-' * 70)

# EXEMPLO COM IN
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if 3 in lista_numeros:  # Verifica se o número 3 está na lista
    print(lista_numeros)  # Exibe a lista
    posicao = lista_numeros.index(3)  # Obtém a posição do número 3 na lista
    print(f'O número 3 está na posição {posicao}')
else:
    print('O elemento não consta na listagem')

print()

# EXEMPLO COM NOT IN
lista_nomes = ['John', 'Jane', 'Carol']

if 'Maria' not in lista_nomes:  # Verifica se 'Maria' não está na lista
    # Exibe a lista antes de modificar
    print(lista_nomes)
    
    # Não está na lista, acrescentar
    lista_nomes.append('Maria')  # Adiciona 'Maria' à lista
    print('\nO nome Maria foi acrescentado')
    print(lista_nomes)  # Exibe a lista após a modificação

print()
print('-' * 70)
print('Fim do programa!')
print('-' * 70)

'''
Explicação do Código:
Uso do in:
O operador in verifica se um elemento está presente em uma lista.
if 3 in lista_numeros: Confirma se o número 3 existe em lista_numeros.
lista_numeros.index(3): Obtém a posição do número 3 na lista.

Uso do not in:
O operador not in verifica se um elemento não está presente em uma lista.
if 'Maria' not in lista_nomes: Confirma que 'Maria' não está presente em lista_nomes.
lista_nomes.append('Maria'): Adiciona 'Maria' à lista caso esteja ausente.
Organização e Exibição:

Cabeçalhos e divisores ('-' * 70) são usados para melhorar a clareza do programa e separar seções.
Mensagens informativas explicam o que está acontecendo no código.
Função append():
Adiciona um elemento ao final de uma lista, útil para modificar a lista dinamicamente.
'''