import os
os.system('cls')

# Lista
produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']

# Declaração -  adicionando - metodo .append()
produtos.append('computador')
print(produtos)
print()

# Entrada de dados -  adicionando - metodo .append()
produto = input('Adicione um produto na lista: ').lower()
produtos.append(produto)
print(produtos)
print()

# Mover da lista - metodo .pop()
# OBS: Para mover tem que usar o indice do produto na lista  
produto = input('Mover um produto na lista: ').lower()
indice = produtos.index(produto)
aux = produtos.pop(indice)
#aux = produtos.pop(-1)
print(produtos)
print(f'Movida para dentro de uma variavél: {aux}')
print()

# remover da lista - metodo .pop() 
produto = input('Remover um produto na lista: ').lower()
produtos.remove(produto)
print(produtos)
print()