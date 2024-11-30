# OBS : Notei que numeros no set é impresso na ordem. 

import os

# add(elemento): Adiciona um elemento ao set.
os.system('cls')

print('METODOS SETs')
print('-' * 80)

print('Escolha "s" para sair, ou "p" para imprimir os SETs')
print('Escolha "1" para Metodo .add()')
print('Escolha "2" para Metodo .remove()')
print('Escolha "3" para Metodo .discard() ')
print('Escolha "4" para Metodo .clear() ')
print('Escolha "5" para Metodo .union(set_2) ')
print('Escolha "6" para Metodo .intersection() ')
print('Escolha "7" para Metodo .difference(set_2) ')
print('Escolha "8" para Metodo .symmetric_difference ')
print('Escolha "9" para Metodo . ')

print('-' * 80)

set_1 = {'1', '2', '3', '4'}
set_2 = {'1', '2', '3', '4'}

while True:
    escolha = input('Digite o número do Metodo SETs: ').lower().strip()
    if escolha == 's':
        break
    # add(elemento): Adiciona um elemento ao set.
    elif escolha == 'p':
        print(set_1)
        print(set_2)
        print('-' * 80)
    elif escolha == '1':
        nome = input('Digite um elemento: ').strip().lower()
        set_1.add(nome)
        print(set_1)
        print('add(elemento) : Adiciona um elemento ao set.')
        print('-' * 80)
    # remove(elemento): Remove um elemento do set. Lança um erro se o elemento 
    # não estiver presente.
    elif escolha == '2':
        nome = input('Digite um elemento: ').strip().lower()
        set_1.remove(nome)
        print(set_1)
        print('remove(elemento) : Remove um elemento do set. Lança um erro' 
              'se o elemento não estiver presente.')
        print('-' * 80)
    # discard(elemento): Remove um elemento do set se ele estiver presente. 
    # Não faz nada se o elemento não estiver presente.
    elif escolha == '3':
        nome = input('Digite um elemento: ').strip().lower()
        set_1.discard(nome)
        print(set_1)
        print('discard(elemento) : Remove um elemento do set se ele estiver presente.' 
              ' Não faz nada se o elemento não estiver presente.')
        print('-' * 80)
    # clear(): Remove todos os elementos do set.
    elif escolha == '4':
        set_1.clear()
        print(set_1)
        print('clear() : Remove todos os elementos do set.')
        print('-' * 80)
    # union(set2) ou |: Retorna um novo set que é a união de dois sets.
    elif escolha == '5':
        set_uniao = set_1.union(set_2)
        print('set_1', set_1)
        print('set_2', set_2)
        print('set_união', set_uniao)
        print('union(set2) ou | : Retorna um novo set que é a união de dois sets, observação, não repete elemento.')
        print('-' * 80)
    # intersection(set2) ou &: Retorna um novo set que é a interseção de dois sets.
    elif escolha == '6':
            set_interseção = set_1.intersection(set_2)
            print('set_1', set_1)
            print('set_2', set_2)
            print('set_intercessão', set_uniao)
            print('intersection(set2) ou & : Retorna um novo set que é a interseção de dois sets.')
            print('-' * 80)
    # difference(set2) ou -: Retorna um novo set com os elementos do primeiro
    # set que não estão no segundo set.
    elif escolha == '7':
        set_diferença = set_1.difference(set_2)
        print('set_1', set_1)
        print('set_2', set_2)
        print('set_diferença', set_diferença)
        print('difference(set2) ou - : Retorna um novo set com os elementos do primeiro'
              ' set que não estão no segundo set.')
        print('-' * 80)
    # symmetric_difference(set2) ou ^: Retorna um novo set com elementos que 
    # estão em um dos sets, mas não em ambos.
    elif escolha == '8':
        set_symmetric_difference = set_1.symmetric_difference(set_2)
        print('set_1', set_1)
        print('set_2', set_2)
        print('set_symmetric_difference', set_symmetric_difference)
        print('symmetric_difference(set2) ou ^: Retorna um novo set com elementos que '
                ' estão em um dos sets, mas não em ambos.')
        print('-' * 80)