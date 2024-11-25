# 1. Usando o fatiamento ( [::-1])
# O método mais simples e rápido:
lista = [1, 2, 3, 4, 5]
lista_revertida = lista[::-1]
print(lista_revertida)  # Saída: [5, 4, 3, 2, 1]
# Explicação:
# O fatiamento com [::-1]cria uma nova lista com os elementos na ordem inversa.

# 2. Usando o método.reverse()
# Este método altera a lista original:
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)  # Saída: [5, 4, 3, 2, 1]
# Explicação:
# O método .reverse()reverte os elementos da lista para nenhum lugar, ou seja, modifica a lista original. Ele não retorna uma nova lista.

# 3. Usando a funçãoreversed()
# Retorna um iterador que pode ser convertido em uma lista:
lista = [1, 2, 3, 4, 5]
lista_revertida = list(reversed(lista))
print(lista_revertida)  # Saída: [5, 4, 3, 2, 1]
# Explicação:
# A função reversed()cria um iterador que percorre os elementos da lista de trás para frente. Para transformá-lo novamente em uma lista, use list().

# 4. Usando um loop
# Caso prefira reverter manualmente:
lista = [1, 2, 3, 4, 5]
lista_revertida = []
for elemento in lista:
    lista_revertida.insert(0, elemento)
print(lista_revertida)  # Saída: [5, 4, 3, 2, 1]
# Explicação:
# Inserimos cada elemento no início de uma nova lista, construindo-a na ordem reversa.

# 5. Usando Compreensão de Lista
# Uma maneira elegante com Python:
lista = [1, 2, 3, 4, 5]
lista_revertida = [lista[i] for i in range(len(lista) - 1, -1, -1)]
print(lista_revertida)  # Saída: [5, 4, 3, 2, 1]
# Explicação:
# Usamos um loop dentro da compreensão da lista para acessar os elementos da lista de trás para frente.

''''
Comparação dos Métodos
Método	                Altera a lista original?	Cria Nova Lista?	Velocidade
[::-1]	                Não	                            Sim	            Rápido
.reverse()	            Sim	                            Não	            Muito rápido
reversed()	            Não	                            Sim	            Rápido
Manual de Loops	        Não	                            Sim	            Mais lento
Compreensão de Lista	Não	                            Sim	            Rápido

Escolha o Método
Se você precisar apenas de uma cópia invertida da lista sem alterar o original: Use [::-1]ou reversed().
Se você quiser reverter a lista em nenhum lugar: Use .reverse().
'''