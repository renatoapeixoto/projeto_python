################################################################################
import os
os.system('cls')

# metodo .extend()
print('-' * 70)
print('*** Metodo extend() ***')
produtos = ['tv', 'mac', 'iphone x', 'iPad']
novos_produtos = ['tv', 'windows phone' 'ipad']
print(f'Lista A: {produtos}')
print(f'Lista B: {novos_produtos}')
produtos.extend(novos_produtos)
print(f'Metodo: .extend(): {produtos}')
print()

produtos = [10,20,30,40]
novos_produtos = [40,50,60]
print(f'Lista A: {produtos}')
print(f'Lista B: {novos_produtos}')
produtos.extend(novos_produtos)
print(f'Metodo: .extend(): {produtos}')
print('-' * 70)
# item repetido ele adiciona outro 
################################################################################

################################################################################
# Concatenar listas
print('-' * 70)
print('*** Concatenar listas ***')
produtos = ['apple tv', 'mac', 'iphone x', 'iPad']
novos_produtos = ['chromecast', 'windows phone']
print(f'Lista A: {produtos}')
print(f'Lista B: {novos_produtos}')
concatenar_listas = produtos + novos_produtos
print(f'Concatenar: {concatenar_listas}')
print('-' * 70)
################################################################################

################################################################################
# Diferença usando o metodo append(), adiciona uma lista dentro de outra lista.
print('-' * 70)
print('*** Diferença usando o metodo append, cria uma lista dentro de outra ***')
produtos = ['apple tv', 'mac', 'iphone x', 'iPad']
novos_produtos = ['chromecast', 'windows phone']
print(f'Lista A: {produtos}')
print(f'Lista B: {novos_produtos}')
produtos.append(novos_produtos)
print(f'Metodo: .append(): {produtos}')
print('-' * 70)
################################################################################

################################################################################
# Ordenação
print('-' * 70)
print('*** Ordenação, metodo .sort() ***')
produtos = ['apple tv', 'mac', 'iphone x', 'IPad']
novos_produtos = [30,10,4,25,55,101]
print('CUIDADO! a ordenação considera letra maiuscula primeiro \n\
que a minuscula, considerando a ordem na tabela ascii\n')
print(f'Lista A: {produtos}')
print(f'Lista B: {novos_produtos}')
produtos.sort()
novos_produtos.sort()
print(f'Metodo: .sort(): {produtos}')
print(f'Metodo: .sort(): {novos_produtos}')
print('-' * 70)

print('-' * 70)
print('*** Ordenação, metodo .sort(reverse=True) ***')
produtos = ['apple tv', 'mac', 'iphone x', 'iPad']
novos_produtos = [30,10,4,25,55,101]
print(f'Lista A: {produtos}')
print(f'Lista B: {novos_produtos}')
print('Ordenação Decrescente')
produtos.sort(reverse=True)
novos_produtos.sort(reverse=True)
print(f'Metodo: .sort(reverse=True): {produtos}')
print(f'Metodo: .sort(reverse=True): {novos_produtos}')
print('-' * 70)
################################################################################

