# Como descobrir o índice de um item de uma lista?
import os
os.system('cls')

produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 100, 120, 70, 180, 80]

print(f'Produtos: {produtos}')
print(f'Estoque: {estoque}')

produto = input('Digite o nome do produto: ').lower().strip()

if produto in produtos:
    indice = produtos.index(produto)
    print(f'O produto {produtos[indice]} tem no estoque: {estoque[indice]} unidades')
else:
    print('produto não está na lista')
