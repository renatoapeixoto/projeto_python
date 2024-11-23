import os

os.system('cls')

lista = [1,2,2,2,3,4]
lista02 = [5,6,7,7,7,7,8]

def escolher_lista ():
    while True:
        op = input('Digite "1" p/ Lista01, ou "2" para Lista02: ').lower()
        if op == '1':
            return lista
        elif op == '2':
            return lista02
        elif op == 'sair':
            continue
        else:
            print('opção inválida')
            exit()
escolha = escolher_lista()

tamanho = len(escolha)

print(tamanho)





exit()

l
print(lista)
print(lista2)

entrada = input('Aperte enter: ')
print(entrada)
if entrada == "":
    print('deu certo')

lista.append(10)
print(lista)

lista.extend(lista2)
print(lista)

lista.pop(0)
print(lista)

lista.insert(0,100)
print(lista)

print('o numero 2 aparece: ', lista.count(2))

indice = lista.index(3)
print('o indice do numero 8: ', lista)