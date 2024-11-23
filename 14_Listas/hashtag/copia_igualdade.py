'''Quando você usa lista2 = lista1, ambas as variáveis ​​apontam para a mesma 
lista na memória. Isso significa que, ao modificar lista1, as alterações 
também aparecem em lista2, pois elas estão relacionadas ao mesmo local de 
memória.
Como Resolver (Fazendo uma Cópia Independente):
Se você deseja que lista2seja independente lista1, você deve fazer uma cópia 
da lista, e não apenas atribuí-la.'''

# Criando a lista inicial
print('-' * 70)
lista1 = ['apple tv', 'mac', 'iphone x', 'iPad', 'apple watch', 'mac book', 'airpods']

# Fazendo uma atribuição direta de lista1 para lista2
lista2 = lista1

# Alterando o item na posição [2] da lista1
lista1[2] = 'iphone12'

# Imprimindo as duas listas para verificar a igualdade
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print('-' * 70)


## RESOLVENDO O PROBLEMA , FAZENDO COPIA INDEPENDENTE:
# Criando a lista inicial
print('-' * 70)
lista1 = ['apple tv', 'mac', 'iphone x', 'iPad', 'apple watch', 'mac book', 'airpods']

# Fazendo uma cópia da lista1 para lista2
lista2 = lista1.copy()

# Alterando o item na posição [2] da lista1
lista1[2] = 'iphone12'

# Imprimindo as duas listas para verificar a independência
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print('-' * 70)
