import os
os.system('cls')

# Descobrir o indice de um elemento da lista 
lista = ['item1',    
         'item2',
         'item3',
        ]
print(lista)
indice = lista.index('item2')

# Cada elemento tem um indice que começa com 0.
print(f'O indice do {lista[indice]} é : {indice}')  

# Descobrir o indice de um elemento da lista 
lista = ['geladeira',    
         'fogao',
         'armario',
        ]

produto = input(f'Digite qual item da lista deseja procurar o indice: {lista} :')
indice = lista.index(produto)

# Cada elemento tem um indice que começa com 0.
print(f'O indice do {produto} é : {indice}')  