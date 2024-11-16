import os
os.system('cls')


# Criar listas
lista = []  # lista vazia
print(f'lista: {lista} tipo: {type(lista)}')

lista = [1, 2, 3, 4, 5, 6]
print(f'lista: {lista} tipo: {type(lista)}')

lista = ['renato', 10 , [1,2,3], 2.5, True] # pode conter varios tipos 
print(f'lista: {lista} tipo: {type(lista)}')

lista = ['item1',
         'item2',
         'item3',
        ]
print(f'lista: {lista} tipo: {type(lista)}')

# Pode imprimir um item especifico da lista
lista = ['item1',    
        'item2',
        'item3',
        ]
print(lista[1])  # Cada elemento tem um indice que começa com 0.