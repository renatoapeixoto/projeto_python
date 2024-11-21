import os

os.system('cls')

lista = [1,2,2,2,3,4]
lista2 = [5,6,7,7,7,7,8]
print(lista)
print(lista2)

lista.append(10)
print(lista)

lista.extend(lista2)
print(lista)

lista.pop(0)
print(lista)

lista.insert(0,100)
print(lista)

print('o numero 2 aparece: ', lista.count(2))

indice = lista.index()
print('o indice do numero 8: ', lista.)