import os

os.system('cls')

print('-' * 70)
print('COMANDO WHILE')
print('-' * 70)

contador = 1

while contador <= 10:
    print(f'Contando... {contador}')
    
    # contador += 1 é o mesmo que contador = contador + 1
    contador += 1

print('Fim do programa!\n')
