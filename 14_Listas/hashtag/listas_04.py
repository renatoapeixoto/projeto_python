import os
os.system('cls')

lista01 = ['camisa', 'short', 'boné']
lista02 = ['computador', 'geladeira', 'sofá']

# função montar_Tela
def montar_tela (list01, list02):
    print('-' * 70)
    print('MENU PRINCIPAL: "ESTRUTURA DE LISTAS"')
    print('-' * 70)
    print('Escolha uma opção, ou digite "Sair"')
    print('-' * 70)
    print('Digite "1" adicionar')
    print('Digite "2" alterar')
    print('Digite "3" consultar')
    print('Digite "4" remover')
    print('Digite "5" mover')
    print('-' * 70)
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
montar_tela(lista01, lista02)
while True:  # Escolha opção
    print('-' * 70)
    opcao = input('Escolha uma "Opção", ou "Sair" para encerrar o programa: ').lower().strip()
    if opcao == 'sair':
        exit()
    else:
        if opcao == '1':  # Adicionar item na lista
            
            while True: # loop opção 1 
                
                item = input('Digite um item para "adicionar", ou "voltar" para opções: ').lower().strip()
                if item == 'voltar':
                    break
                # validação do item
                while True:
                    if not item:
                        item = input('Digite um item para "adicionar", ou "voltar" para opções: ').lower().strip()
                    else:
                        break
                if item == 'voltar':
                    break
                            
                # Escolher a lista para adicionar o item        
                print('-' * 70)
                while True:
                    op = input('Deseja adicionar esse item na Lista01 ou na Lista02 ?\n' 
                            'Se preferir, volte novamente para opções.\n'
                            'Digite "1", "2", ou "voltar": ').lower().strip()
                    # vslidsção
                    while True:
                        if op == '1' or op == '2':
                            # guardar valor da lista original em uma variavel
                            lista_escolhida = escolher_lista(op)
                            aux_lista = lista_escolhida.copy()
                            # adicionando na lista escolhida
                            lista_escolhida.append(item)
                            # validação se foi adicionado na lista
                            tamanho = len(lista_escolhida)
                            if tamanho > len(aux_lista):
                                print('Adicionado com sucesso !!!!')
                                print(f'Lista01: {lista01}')
                                print(f'Lista02: {lista02}')
                                print('-' * 70)
                                break
                            else:
                                print('Erro não esperado !!!!')
                                exit()        
                            print('-' * 70)
                        elif op == 'voltar':
                            print('-' * 70)
                            break
                        else:
                            print('Opção inválida')
                    if op == 'voltar':
                        break
                    if op == '1' or op == '2':
                        break
            
            
        
   

        
        
#         elif opcao == '2':
#             op = input('Escolha a lista, Digite "1" p/ Lista01, ou "2" para Lista02: ')
#             if op == '1' and op == '2':
#                 lista_escolhida = escolher_lista(op)
#             else:
#                 print('Opção inválida')
#                 opcao = ""
            
#             alterar_item = input('Digite o item que deseja alterar: ').lower().strip()
#             if alterar_item in lista_escolhida:
#                 pass
#             else:
#                 print('Item não está na lista')
#                 opcao = ""
            
#             tamanho = len(escolher_lista(op))
#             lista_escolhida = escolher_lista(op)
           
#             if op == '1' and op == '2':
                             

#                 if alterar_item in lista_escolhida:
#                     i = lista.index(alterar_item)
#                     novo_item = input('Digite a aleração: ').lower().strip()
#                     lista[i] = novo_item
#                     print('-' * 70)
#                 else:
#                     print('Item não cadastrado !!!!')




#             else:
#                 print('Opção inválida')
            
            
            
           
#         elif opcao == '3':
#             item = input('Digite o item para consultar: ').lower().strip()
#             if item in lista:
#                 i = lista.index(item)
#                 print(f'O item {item} encontra-se na posição {i} na lista01')
#                 print('-' * 70)
#             else:
#                 print('Item não cadastrado !!!!')
#                 print('-' * 70)
#         elif opcao == '4':
#             item = input('Digite o item para remover: ').lower().strip()
#             tamanho = len(lista)
#             if item in lista:
#                 lista.remove(item)
#                 if tamanho > len(lista):
#                     print('Removido com sucesso !!!!')
#                 else:
#                     print('Erro não esperado !!!!')        
#                 print('-' * 70)
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
#                     print('-' * 70)
#                     print('Movido com sucesso !!!!')
#                     print('-' * 70)
#                 else:
#                     print('Erro não esperado !!!!')        
#                 print('-' * 70)
#             else:
#                 print('Item não cadastrado !!!!') 
#         elif opcao == "":
#             os.system('cls')
#             #print()
#             print('-' * 70)
#             print('MENU PRINCIPAL: "ESTRUTURA DE LISTAS"')
#             print('-' * 70)
#             print('Escolha uma opção, ou digite "Sair", ou Aperte Enter para voltar:')
#             print('-' * 70)
#             print('Digite "1" adicionar')
#             print('Digite "2" alterar')
#             print('Digite "3" consultar')
#             print('Digite "4" remover')
#             print('Digite "5" mover')
#             print('-' * 70)
#     print(f'Lista01: {lista}')
#     print(f'Lista02: {lista02}')
#     # print('-' * 70)
    
# print('-' * 70)

