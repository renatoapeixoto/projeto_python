import os

# Limpa a tela do terminal/console
os.system('cls')

# Lista original
lista = [1, 2, 3, 4]

# Mostrando a lista original
print("Lista original:", lista)

# Pedindo ao usuário o elemento a ser removido
elemento = input("Elemento a ser removido: ")

# Tentando remover o elemento da lista
if elemento.isdigit():  # Se for um número, a entrada é convertida para um inteiro.
    elemento = int(elemento)  # Converte para inteiro se for um número
    if elemento in lista:  # Verifica se o elemento está na lista
        lista.remove(elemento)  # Remove o elemento da lista
        print("Lista após a remoção:", lista)
    else:
        print("Elemento não encontrado na lista.")
else:
    print("Entrada inválida. Insira um número.")
