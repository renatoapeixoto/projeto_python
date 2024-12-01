# OBS : Notei que numeros no set é impresso na ordem. 

import os

# add(elemento): Adiciona um elemento ao set.
os.system('cls')

# Criação de 2 Set´s.
set_1 = {'3', '4'}
set_2 = {'3', '4', '5', '6'}

# Tela
def tela ():
    os.system("cls")
    print('METODOS SETs')
    print('-' * 80)
    print(f'Set_1: {set_1} Set_2: {set_2}')
    print('-' * 80)
    print('Escolha "1" para Metodo .add(elemento)')
    print('Escolha "2" para Metodo .remove(elemento)')
    print('Escolha "3" para Metodo .discard(elemento) ')
    print('Escolha "4" para Metodo .clear() ')
    print('Escolha "5" para Metodo .union(set_2) ')
    print('Escolha "6" para Metodo .intersection(set_2) ')
    print('Escolha "7" para Metodo .difference(set_2) ')
    print('Escolha "8" para Metodo .symmetric_difference(set_2) ')
    print('Escolha "9" para Metodo .issubset(set2) ')
    print('Escolha "S" para sair, ou "V" para visualizar Menu novamente')
    print('-' * 80)

tela()
while True:
    escolha = input('Digite o número do Metodo SETs: ').lower().strip()
    if escolha == '':
        continue
    elif escolha == 's':
        # aperta S para sair do loop e do programa
        confirma = input('Confirma "S" p/ sair,  ou "N" para voltar: ').lower().strip()
        if confirma == 'n':
            continue
        elif confirma == 's':
            os.system("cls")
            print('Fim do programa!!!')
            break
    elif escolha == 'v':
        # imprime os Set´s novamente
        tela()
    elif escolha == '1':
        # add(elemento): Adiciona um elemento ao set.
        while True:
            elemento = input('Digite um elemento: ').strip().lower()
            if elemento == "":
                print('Você precisa digitar um elemento')
                continue
            else:
                break 
        confirma = input('Confirma adicionar "S" ou "N": ').lower().strip()
        if confirma == 'n':
            continue
        else:
            escolhe_set = input('Digite "1" para adicionar no Set_1, ou "2" para Set_2: ').lower().strip()
            if escolhe_set == '1':
                set_1.add(elemento)
            elif escolhe_set == '2':
                set_2.add(elemento)
            else:
                print('opção inválida')    
                continue
        print(F'set_1: {set_1}')
        print(F'set_2: {set_2}')
        print('OBS: set_1.add(elemento) : Adiciona um elemento ao set.')
        print('-' * 80)
    elif escolha == '2':
        # remove(elemento): Remove um elemento do set. Lança um erro se o elemento 
        # não estiver presente.
        while True:
            elemento = input('Digite um elemento: ').strip().lower()
            if elemento == "":
                print('Você precisa digitar um elemento')
                continue
            else:
                break
        confirma = input('Confirma remover "S" ou "N": ').lower().strip()
        if confirma == 'n':
            continue
        elif confirma == 's':
            escolhe_set = input('Digite "1" para Set_1, ou "2" para Set_2: ').lower().strip()
            if escolhe_set == '1':
                set_1.remove(elemento)
            elif escolhe_set =='2':
                set_2.remove(elemento)
            else:
                print('opção inválida')
                continue    
        else:
            print('opção inválida')
        print(F'set_1: {set_1}')
        print(F'set_2: {set_2}')
        print('OBS: set_1.remove(elemento) : Remove um elemento do set. Lança um erro\n' 
              'se o elemento não estiver presente.')
        print('-' * 80)
    elif escolha == '3':
        # discard(elemento): Remove um elemento do set se ele estiver presente. 
        # Não faz nada se o elemento não estiver presente.
        while True:
            elemento = input('Digite um elemento: ').strip().lower()
            if elemento == "":
                print('Você precisa digitar um elemento')
                continue
            else:
                break
        confirma = input('Confirma o descartar "S" ou "N": ').lower().strip()
        if confirma == 'n':
            continue
        elif confirma == 's':
            escolhe_set = input('Digite "1" para Set_1, ou "2" para Set_2: ').lower().strip()
            if escolhe_set == '1':
                set_1.discard(elemento)
            else:
                set_2.discard(elemento)
        else:
            print('opção inválida')
        print(F'set_1: {set_1}')
        print(F'set_2: {set_2}')
        print('OBS: set_1.discard(elemento) : Remove um elemento do set se ele estiver presente.\n' 
              'Não faz nada se o elemento não estiver presente.')
        print('-' * 80)
    elif escolha == '4':
        # clear(): Remove todos os elementos do set.
        confirma = input('Confirma Limpar "S" ou "N": ').lower().strip()
        if confirma == 'n':
            continue
        elif confirma == 's':
            escolhe_set = input('Digite "1" para Set_1, ou "2" para Set_2: ').lower().strip()
            if escolhe_set == '1':
                set_1.clear()
            else:
                set_2.clear()
        else:
            print('opção inválida')
        print(F'set_1: {set_1}')
        print(F'set_2: {set_2}')
        print('OBS: set_1.clear() : Limpa todos os elementos de um Set.')
        print('-' * 80)
    elif escolha == '5':
        # union(set2) ou |: Retorna um novo set que é a união de dois sets.
        confirma = input('Confirma unir Set_1 e Set_2, "S" ou "N": ').lower().strip()
        if confirma == 'n':
            continue
        elif confirma == 's':
            set_uniao = set_1.union(set_2)
            print(F'set_1: {set_1}')
            print(F'set_2: {set_2}')
            print('Set_união: ', set_uniao)
            print('OBS: set_uniao = set_1.union(set_2) : Retorna um novo set que é a\n' 
            'união de dois sets. Observação, não repete elemento.')
            print('-' * 80)
        else:
            print('opção inválida')
    elif escolha == '6':
        # intersection(set2) ou & : Retorna um novo set que é a interseção de dois sets.
        confirma = input('Confirma intercessão Set_1 e Set_2, "S" ou "N": ').lower().strip()
        if confirma == 'n':
            continue
        elif confirma == 's':
            set_interseção = set_1.intersection(set_2)
            print(F'set_1: {set_1}')
            print(F'set_2: {set_2}')
            print('Set_intercessão: ', set_interseção)
            print('OBS: set_interseção = set_1.intersection(set_2): Retorna um novo set\n'
            'que é a interseção de dois sets.')
            print('-' * 80)
        else:
            print('opção inválida')    
    elif escolha == '7':
        # difference(set2) ou -: Retorna um novo set com os elementos do primeiro
        # set que não estão no segundo set.
        confirma = input('Confirma diferença Set_1 e Set_2, "S" ou "N": ').lower().strip()
        if confirma == 'n':
            continue
        elif confirma == 's':
            set_diferença = set_1.difference(set_2)
            print(F'set_1: {set_1}')
            print(F'set_2: {set_2}')
            print('Set_diferença: ', set_diferença)
            print('OBS: set_diferença = set_1.difference(set_2) : Retorna um novo set com os\n'
                  'elementos do Set_1 que não estão no Set_2.')
            print('-' * 80)
        else:
            print('opção inválida')    
    elif escolha == '8':
        # symmetric_difference(set2) ou ^: Retorna um novo set com elementos que 
        # estão em um dos sets, mas não em ambos.
        confirma = input('Confirma diferença_simétrica Set_1 e Set_2, "S" ou "N": ').lower().strip()
        if confirma == 'n':
            continue
        elif confirma == 's':
            set_diferenca_simetrica = set_1.symmetric_difference(set_2)
            print(F'set_1: {set_1}')
            print(F'set_2: {set_2}')
            print('Set_symmetric_difference: ', set_diferenca_simetrica)
            print('OBS: set_diferenca_simetrica = set_1.symmetric_difference(set_2): Retorna um\n'
                  'novo set com elementos que estão em um dos sets, mas não em ambos.')
            print('-' * 80)
        else:
            print('opção inválida')    
    elif escolha == '9':
        # issubset(set2): Verifica se o set é um subconjunto de outro set.
        confirma = input('Confirma Subconjunto Set_1 e Set_2, "S" ou "N": ').lower().strip()
        if confirma == 'n':
            continue
        elif confirma == 's':
            set_subconjunto = set_1.issubset(set_2)
            print(F'set_1: {set_1}')
            print(F'set_2: {set_2}')
            print('Set_Subconjunto: ', set_subconjunto)
            print('OBS: set_subconjunto = set_1.issubset(set_2) : issubset(set2) Verifica\n' 
                'se o set_1 é um subconjunto de outro set_2.')    
            print('-' * 80)
        else:
            print('opção inválida')