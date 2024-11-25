import os
os.system('cls')

lista01 = ['camisa', 'short', 'boné']
lista02 = ['computador', 'geladeira', 'sofá']

# função montar_Tela
def montar_tela (list01, list02):
    os.system('cls')
    print('-' * 80)
    print('MENU PRINCIPAL: "ESTRUTURA DE LISTAS"')
    print('-' * 80)
    print('Escolha a opção que deseja executar nas Listas:')
    print('-' * 80)
    print('Digite "1" adicionar')
    print('Digite "2" alterar')
    print('Digite "3" consultar')
    print('Digite "4" remover')
    print('Digite "5" mover')
    print('-' * 80)
    # imprimir listas
    print(f'Lista01: {list01}')
    print(f'Lista02: {list02}')

# Função escolher lista
def escolher_lista (op):
    if op == '1':
        return lista01
    elif op == '2':
        return lista02

# Escolher opções    
escolha= ['1', '2', '3', '4', '5', '6', '7']
montar_tela(lista01, lista02)
while True:  # Escolha opção
    print('-' * 80)
    opcao = input('Digite o numero das "opções", ou "menu", ou "sair" para encerrar o programa: ').lower().strip()
    if opcao == 'sair':
        exit()
    elif opcao == 'menu':
        montar_tela(lista01, lista02)
    elif not opcao:
        print('opção inválida !!!')
        continue
    elif not opcao in escolha: 
        print('opção inválida !!!')
    else:
        if opcao == '1':  # Adicionar item na lista
            while True: # loop opção 1 
                print('-' * 80)
                item = input('Digite um item para "adicionar" na lista, ou "sair", ou "voltar" para opção: ').lower().strip()
                if item == 'sair':
                    exit()
                # validação do item
                elif not item:
                    print('opção inválida !!!')
                    continue
                elif item == 'voltar':
                    break
                # Escolher a lista para adicionar o item        
                while True:
                    print('-' * 80)
                    op = input('Deseja adicionar na Lista01 ou na Lista02 ?\n' 
                            'Digite "1", ou "2", ou "voltar", ou "sair": ').lower().strip()
                    # vslidsção
                    if op == 'sair':
                        exit()
                    elif op == 'voltar':
                        print('-' * 80)
                        break
                    elif op == '1' or op == '2':
                        # guardar valor da lista original em uma variavel
                        lista_escolhida = escolher_lista(op)
                        aux_lista = lista_escolhida.copy()
                        # adicionando na lista escolhida
                        lista_escolhida.append(item)
                        # validação se foi adicionado na lista
                        tamanho = len(lista_escolhida)
                        if tamanho > len(aux_lista):
                            print('Adicionado com sucesso !!!!')
                            print('-' * 80)
                            print(f'Lista01: {lista01}')
                            print(f'Lista02: {lista02}')
                            break
                        else:
                            print('Erro não esperado !!!!')
                            exit()        
                        print('-' * 80)
                    else:
                        print('Opção inválida !!!')
        
        elif opcao == '2':
            while True: # loop opção 1 
                print('-' * 80)
                op = input('Digite "1" p/ alterar Lista01, ou "2" p/ alterar Lista02, ou "voltar": ')
                if op == 'sair':
                        exit()
                # validação do item
                elif not op:
                    print('opção inválida !!!')
                    continue
                elif op == 'voltar':
                    break
                elif op != '1' and op != '2':
                    print('Opção inválida')
                else:
                    lista_escolhida = escolher_lista(op)
                    print(lista_escolhida)
                    while True:
                        alterar_item = input('Digite o item da lista para alterar, ou "voltar": ').lower().strip()
                        if not alterar_item:
                            print('opção inválida !!!')
                            continue                       
                        elif alterar_item == 'voltar':
                            break
                        elif not alterar_item in lista_escolhida:
                            print('item não encontrado, tente novamente !')
                            continue
                        else:
                            i = lista_escolhida.index(alterar_item)
                            aux_lista = lista_escolhida[1]
                            novo_item = input('Digite a aleração: ').lower().strip()
                            lista_escolhida[i] = novo_item
                            if lista_escolhida[i] != aux_lista:
                                print('Adicionado com sucesso !!!!')
                                print('-' * 80)
                                print(f'Lista01: {lista01}')
                                print(f'Lista02: {lista02}')
                                break
        elif opcao == '3':
            while True: # loop opção 1 
                print('-' * 80)
                op = input('Digite "1" p/ consultar Lista01, ou "2" p/ consultar Lista02, ou "voltar", ou "sair": ')
                if op == 'sair':
                        exit()
                # validação do item
                elif not op:
                    print('opção inválida !!!')
                    continue
                elif op == 'voltar':
                    break
                elif op != '1' and op != '2':
                    print('Opção inválida')
                else:
                    lista_escolhida = escolher_lista(op)
                    print(lista_escolhida)
                    while True:
                        item = input('Digite o item da lista para consultar sua posição, ou "voltar" : ').lower().strip()
                        if item == 'voltar':
                            break
                        elif not item:
                            continue
                        elif item in lista_escolhida:
                            i = lista_escolhida.index(item)
                            print(f'O item {item} encontra-se na posição {i} da lista{op}: {lista_escolhida}')
                            break
                        else:
                            print('Item não encontrado !!!')
                            continue
#         elif opcao == '4':
#             item = input('Digite o item para remover: ').lower().strip()
#             tamanho = len(lista)
#             if item in lista:
#                 lista.remove(item)
#                 if tamanho > len(lista):
#                     print('Removido com sucesso !!!!')
#                 else:
#                     print('Erro não esperado !!!!')        
#                 print('-' * 80)
#             else:
#                 print('Item não cadastrado !!!!') 
#         elif opcao == '5':
#             item = input('Digite o item para mover: ').lower().strip()
#             i = lista.index(item)
#             tamanho = len(lista)
#             if item in lista:
#                 aux = lista.pop(i)
#                 lista02.append(aux)
#                 if tamanho > len(lista):
#                     print('-' * 80)
#                     print('Movido com sucesso !!!!')
#                     print('-' * 80)
#                 else:
#                     print('Erro não esperado !!!!')        
#                 print('-' * 80)
#             else:
#                 print('Item não cadastrado !!!!') 
#         elif opcao == "":
#             os.system('cls')
#             #print()
#             print('-' * 80)
#             print('MENU PRINCIPAL: "ESTRUTURA DE LISTAS"')
#             print('-' * 80)
#             print('Escolha uma opção, ou digite "Sair", ou Aperte Enter para voltar:')
#             print('-' * 80)
#             print('Digite "1" adicionar')
#             print('Digite "2" alterar')
#             print('Digite "3" consultar')
#             print('Digite "4" remover')
#             print('Digite "5" mover')
#             print('-' * 80)
#     print(f'Lista01: {lista}')
#     print(f'Lista02: {lista02}')
#     # print('-' * 80)
    
# print('-' * 80)

