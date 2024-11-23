################################################################################
import os
os.system('cls')


print('-' * 70)
print('*** Metodo: " ".join() ***')
produtos = ['apple tv', 'mac', 'iphone x', 'iPad']
print(f'Lista A: {produtos}')
print('Tipo: ', type(produtos))
print('-' * 70)

print('-' * 70)
print('Metodo: print("\ n".join(produtos))')
print("\n".join(produtos))
print('Tipo: ', type(produtos))
print('-' * 70)

print('-' * 70)
produtos = ', '.join(produtos)
print(f"Metodo: produtos = ', '.join(produtos): {produtos}")
print('Tipo : ',type(produtos))
print('-' * 70)

produtos = produtos.split(', ')
print(f"Metodo: produtos = produtos.split(', '): {produtos}")
print('Tipo : ',type(produtos))
print('-' * 70)




################################################################################

