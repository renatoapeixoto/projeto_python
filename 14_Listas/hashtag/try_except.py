import os
os.system('cls')

try:
    # Lista
    produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
    print(produtos)
    # remover da lista - metodo .pop() 
    produto = input('Remover um produto na lista: ').lower()
    produtos.remove(produto)
    
    print(f'O produto {produto} foi revomido da lista.')
    print(produtos)
    print()
except:
    print('Produto não está na lista')