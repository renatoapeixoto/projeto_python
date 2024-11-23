# Listas em Python

# Estrutura:
# lista = [valor, valor, valor, valor, ...]
# lista[i] -> é o valor de índice i da lista. <br>
# Obs: Lembre que no python o índice começa em 0, então o primeiro item de uma lista é o item lista[0]
# Para substituir um valor de uma lista você pode fazer:<br>
# lista[i] = novo_valor

import os
os.system('cls')

# Listas de Produtos de uma Loja:
produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']

# Lista de Unidades Vendidas de cada Produto da Loja"""
vendas = [1000, 1500, 350, 270, 900]
print(f'{produtos}\n{vendas}')

# as listas são mutáveis
vendas[3] = 300
print(vendas)

# As strings são imutáveis
texto = 'lira@gmail.com'
texto.replace('a' , 'o') # não muda o valor 
print(texto)

# Tenho que atrubuir a mudança para uma variavel para pode mudar o valor
texto = 'lira@gmail.com'
texto = texto.replace('a' , 'o') # não muda o valor 
print(texto)
