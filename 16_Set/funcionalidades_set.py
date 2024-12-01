import os


os.system('cls')

# Lista com elementos duplicados
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
print("Lista original:", lista_com_duplicatas)

# Usando set removendo duplicatas
set_sem_duplicatas = set(lista_com_duplicatas)
print("Set removendo duplicatas:", set_sem_duplicatas)

# Revomendo com set e tranformando em lista novamente.
lista_sem_duplicatas = list(set(lista_com_duplicatas))
print("Lista sem duplicatas:", lista_sem_duplicatas)
