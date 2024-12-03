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
tupla01 = ('renato amaro peixoto')
tupla02 = ('renato', 'amaro', 'peixoto')
lista01 = list(tupla01)
print(lista01)
lista02 = list(tupla02)
print(lista02)

# Alterar tupla você transforma em lista depois transforma em tupla novamente.
tupla02 = ('renato', 'amaro', 'peixoto')
lista = list(tupla02)
print(lista)
lista[1] = 'amaral'
tupla02 = tuple(lista)
print(tupla02)


