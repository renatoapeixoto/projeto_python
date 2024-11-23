import os
os.system('cls')

print('-' * 70)
print('Escolha uma opção ou digite "sair":')
print('-' * 70)

print('Digite "1" adicionar um item na lista')
print('Digite "2" alterara um item na lista')
print('Digite "3" consultar um item na lista')
print('Digite "4" remover um item na lista')
print('-' * 70)
cadastro = ['camisa', 'short', 'boné']
print(f'Lista: {cadastro}')

while True:
    print('-' * 70)
    opcao = input('Escolha uma opção: ').lower().strip()
    if opcao == 'sair':
        break
    else:
        if opcao == '1':
            item = input('Digite o item para adicionar: ').lower().strip()
            tamanho = len(cadastro)
            cadastro.append(item)
            if tamanho < len(cadastro):
                print('sdicionado com sucesso')
            else:
                print('erro não esperado')        
            print('-' * 70)
        elif opcao == '2':
            alterar_item = input('Digite o item que deseja alterar: ').lower().strip()
            tamanho = len(cadastro) 
            if alterar_item in cadastro:
                i = cadastro.index(alterar_item)
                novo_item = input('Digite a aleração: ').lower().strip()
                cadastro[i] = novo_item
                print('-' * 70)
            else:
                print('Item não cadastrado')
        elif opcao == '3':
            item = input('Digite o item para consultar: ').lower().strip()
            if item in cadastro:
                i = cadastro.index(item)
                print(f'O item {item} encontra-se na posição {i} no cadastro')
                print('-' * 70)
            else:
                print('Item não cadastrado')
                print('-' * 70)
        elif opcao == '4':
            item = input('Digite o item para remover: ').lower().strip()
            tamanho = len(cadastro)
            if item in cadastro:
                cadastro.remove(item)
                if tamanho > len(cadastro):
                    print('removido com sucesso')
                else:
                    print('erro não esperado')        
                print('-' * 70)
            else:
                print('item não cadastrado') 

    print(cadastro)
print('-' * 70)
