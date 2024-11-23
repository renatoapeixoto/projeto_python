import os
os.system('cls')

# As listas estão Relacionadas
produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque =  [ 100,       150,      100,     120,        70,         180,      80]

print(produtos)
print (estoque)

produto = input('Insira o nome do produto: ').lower()
if produto in produtos: # VALIDAÇÃO - Verifica se o produto esta na lista
    i = produtos.index(produto)
    qtde_estoque = estoque[i]
    print('Temos {} unidades de {} no estoque.'.format(qtde_estoque, produto))
else:
    print('Produto não está na lista')

