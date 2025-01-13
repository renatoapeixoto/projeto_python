'''
FUNÇÃO MAP VERSUS FOR

A função map no Python é uma função embutida que permite aplicar outra função a 
todos os itens de um iterável (como listas, tuplas ou conjuntos) e retorna um 
iterador com os resultados.

Sintaxe:
map(função, iterável, ...)

função: É uma função que será aplicada a cada item do iterável.
iterável: É o conjunto de dados (lista, tupla, etc.) ao qual você quer aplicar a função.
O map pode aceitar múltiplos iteráveis, contanto que a função passada suporte o 
número de argumentos equivalentes.
Como funciona:
O mappercorre cada elemento do iterável, aplica a função a ele, e devolve o resultado. Ele retorna um objeto do tipo map, que é um iterador. Para visualizar os resultados, normalmente convertemos esse iterador em uma lista ou outro tipo de coleção.

'''
import os
os.system('cls')

numeros = ['1', '2', '3']
# Converte cada elemento para inteiro
resultado = map(int, numeros)
print(resultado)
print(list(resultado))  # Saída: [1, 2, 3]

resultado2 = list(map(int, numeros))
print(resultado2)

# Exemplo 2: Dobre os valores de uma lista
def dobro(x):
    return x * 2

valores = [1, 2, 3, 4]
resultado = map(dobro, valores)
print(list(resultado))  # Saída: [2, 4, 6, 8]

# Exemplo 3: Usando lambdacommap
# O map é frequentemente combinado com funções anônimas ( lambda) para simplificar o código:
valores = [1, 2, 3, 4]
resultado = map(lambda x: x * 2, valores)
print(list(resultado))  # Saída: [2, 4, 6, 8]

# Exemplo 4: Usando múltiplos iteráveis
# Você pode passar mais de um iterável, e a função deve aceitar o mesmo número de argumentos:
numeros1 = [1, 2, 3]
numeros2 = [4, 5, 6]
# Soma os elementos correspondentes
resultado = map(lambda x, y: x + y, numeros1, numeros2)
print(list(resultado))  # Saída: [5, 7, 9]

'''
Benefícios do map:
Eficiência : O mapnão cria imediatamente uma nova lista, mas retorna um iterador, ou que economiza memória em listas grandes.
Legibilidade : Deixa o código mais limpo e expressivo, especialmente ao lidar com transformações de dados.
Versatilidade : Funciona com qualquer iterável e qualquer função.
Diferenças entre mape for loop:
A mesma transformação pode ser feita com um for, mas o map é mais direto e funcional:
'''
# Usando for:
valores = [1, 2, 3, 4]
resultado = []
for x in valores:
    resultado.append(x * 2)
print(resultado)  # Saída: [2, 4, 6, 8]

# Usando map:
valores = [1, 2, 3, 4]
resultado = map(lambda x: x * 2, valores)
print(list(resultado))  # Saída: [2, 4, 6, 8]

''' 
Limitações:
Imutabilidade : O map não altera o iterável original, apenas retorna um novo 
iterador com os resultados.
Complexidade em funções : Quando as transformações são muito complexas, usar
 map pode dificultar a leitura do código. Neste caso, for os loops podem ser mais claros.
'''
