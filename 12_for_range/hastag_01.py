import os

os.system('cls')


produtos = ['coca', 'pepsi', 'guaraná', 'sprite', 'fanta', 'mineirinho']
producao = [15000, 12000, 13000, 5000, 250, 800]

print(produtos)
print(producao)

for i in range(len(produtos)):
    print('Produção do {} é de {}'.format(produtos[i], producao[i]))

print('#' *70)
################################################################################
    
produtos = ['coca', 'pepsi', 'guaraná', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]

print(produtos)
print(producao)

for i in range(5):  # repete 5 vezes porque são 5 produtos
    print('Produção do {} é de {}'.format(produtos[i], producao[i]))

print('#' *70)
################################################################################



