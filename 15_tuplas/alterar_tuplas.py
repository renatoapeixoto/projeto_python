import os
os.system('cls')

# list com string
texto = 'renato amaro peixoto'
texto2 = 'renato', 'amaro', 'peixoto'
lista = list(texto)
print(lista)
lista = list(texto2)
print(lista)

# transformando tupla em lista
texto = ('renato amaro peixoto')
texto2 = ('renato', 'amaro', 'peixoto')
lista = list(texto)
print(lista)
lista = list(texto2)
print(lista)

# Alterar tupla você transforma em lista depois transforma em tupla novamente.
texto2 = ('renato', 'amaro', 'peixoto')
lista = list(texto2)
print(lista)
lista[1] = 'amaral'
texto2 = tuple(lista)
print(texto2)


