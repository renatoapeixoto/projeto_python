import math

math.ceil(x)
Retorna o arredondamento para cima.

math.floor(x)
Retorna o arredondamento para baixo.

math.pow(x, y)
Retorna x elevado à potência y..

math.sqrt(x)
Retorna a raiz quadrada de x.

math.cos(x)
Retorna o cosseno de x radianos.

math.sin(x)
Retorna o seno de x radianos.

math.tan(x)
Retorna o tangente de x radianos.

math.hypot(c_oposto, c_adjacente)
Retorna o valor da hipotenusa

--------------------------------------------------------------------------------
### A biblioteca random

A biblioteca random em Python é uma biblioteca padrão que fornece funções para 
gerar números aleatórios e realizar operações relacionadas à aleatoriedade. 
Essa biblioteca é útil em uma variedade de aplicações, como simulações, jogos,
 criptografia, entre outros, onde a aleatoriedade desempenha um papel importante.

# Importando o módulo random para gerar números aleatórios
import random

# Gerando um número aleatório entre 0 e 1
numero_aleatorio = random.random()

# Exibindo o número aleatório gerado
print(numero_aleatorio)  # Saída: um número aleatório entre 0 e 1


A função mais comum da biblioteca random é a função random(), que gera um número 
decimal aleatório entre 0 e 1 (inclusive 0, mas exclusivo de 1). Isso significa 
que o número gerado pode estar em qualquer lugar dentro do intervalo semiaberto
 [0, 1).

 A biblioteca random

Além da função random(), a biblioteca random oferece outras funções para gerar 
números aleatórios com diferentes distribuições e propriedades. 
Alguns exemplos incluem:

randint(a, b): 
Retorna um número inteiro aleatório entre a e b (inclusive ambos os limites).

uniform(a, b): 
Retorna um número decimal aleatório entre a e b (inclusive ambos os limites), 
com uma distribuição uniforme.

randrange(start, stop, step): 
Retorna um elemento aleatório de uma sequência gerada pela função range(), 
começando em start, terminando antes de stop, e avançando de acordo com step.

choice(seq): 
Retorna um elemento aleatório de uma sequência (como uma lista, tupla ou string).

shuffle(seq): 
Embaralha os elementos de uma sequência.

sample(population, k): 
Retorna uma amostra de k elementos únicos de uma população (sem substituição).

