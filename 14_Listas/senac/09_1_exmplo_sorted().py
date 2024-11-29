
'''Como funciona?: Ele retorna uma nova lista ordenada com base no objeto passado
(que pode ser qualquer iterável, como listas, tuplas ou até strings).'''

import os

# Limpa a tela do terminal/console
os.system('cls')

lista = [3, 1, 4, 1, 5, 9]
nova_lista = sorted(lista)
print(lista)       # Saída: [3, 1, 4, 1, 5, 9] (original permanece igual)
print(nova_lista)  # Saída: [1, 1, 3, 4, 5, 9]


lista = [3, 1, 4, 1, 5, 9]
nova_lista = sorted(lista, reverse=True)
print(nova_lista)  # Saída: [9, 5, 4, 3, 1, 1]
