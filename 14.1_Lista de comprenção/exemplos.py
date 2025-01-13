'''
## Sintaxe da Compreensão de Lista
A sintaxe geral da compreensão de lista é:

```python
nova_lista = [expressão for elemento in iterável]
```

- **`expressão`**: O que você quer fazer com cada elemento (transformação ou cálculo).
- **`elemento`**: Cada item do iterável.
- **`iterável`**: Um objeto que pode ser percorrido, como uma lista, string ou intervalo.

OBS: Não pode faltar: expressão , elemento, iterável. 
Podemos fazer transformação e filtragem em iteráveis.

Estrutura:
Expressão , transformação :  elemento loop iteravel :  condição, filtragem (if)
Expressão , transformação :  condição, filtragem (if else): elemento loop iteravel :

'''

import os
os.system('cls')

# cria uma lista ao quadrado de 1 a 5. Transformação.
lista = []
lista = [i ** 2 for i in range(1,6)]
print(lista)

# Criar uma lista com os números de 1 a 5 multiplicados por 2. Transformação.
lista.clear()
lista = [x * 2 for x in range (1,6)]
print(lista)

# Criar uma lista com apenas os números pares de 1 a 10. Filtragem com if.
lista.clear()
lista = [x for x in range (1,11) if x % 2 == 0]
print(lista)

# Dobrar apenas os números ímpares de 1 a 10. Transformação e filtragem.
lista.clear()
lista = [x * 2 for x in range (1,11) if x % 2 == 1 and x >=4]
print(lista)

# Criar uma lista que substitui números ímpares por 0 e mantém os números pares. Filtragem com if e else.
# quando se usa condiçao if else, após a expressão vem a condição.
lista.clear()
lista = [x if x % 2 == 0 else 0 for x in range (1,11)]
print(lista)

lista.clear()
lista = [x if x % 2 == 0 else 0 for x in range (1,11)]
print(lista)

# Compreensão de Lista com Múltiplos Loops
# Você pode usar mais de um loop dentro da compreensão de lista para gerar combinações de elementos.

cores = [1,2]
tamanhos = [1,2,3]
combinacao = [cor + tamanho for cor in cores for tamanho in tamanhos]
print(combinacao)

cores = [1,2]
tamanhos = [1,2,3]
combinacao = [(cor,tamanho) for cor in cores for tamanho in tamanhos]
print(combinacao)

# Compreensão de Dicionários:
cores = ["vermelho", "azul"]
tamanhos = ["P", "M"]
combinacao = {cor : tamanho for cor in cores for tamanho in tamanhos}
print(combinacao) # {'vermelho': 'M', 'azul': 'M'}
# só pode ter uma chave, está soprepondo os valores

# . A função zip
# A função zip combina os elementos de duas listas (ou outros iteráveis) emparelhando os elementos correspondentes.
letras = ["a", "b", "c"]
numeros = [1, 2, 3]
dicionario = {letra: numero for letra, numero in zip(letras, numeros)}
print(dicionario)  # Saída: {'a': 1, 'b': 2, 'c': 3}

#  compreensão de conjunto
numeros = [1, 2, 2, 3, 4, 4]
conjunto = {x ** 2 for x in numeros}
print(conjunto)  # Saída: {16, 1, 4, 9} - retira os numeros repetidos

resultado = [x ** 2 for x in range(10) if x % 2 == 0 and x > 4]
print(resultado)

## Exemplos do Mundo Real
### 1. **Filtrar Números Positivos**:
dados = [-5, 3, -1, 2]
positivos = [x for x in dados if x > 0]
print(positivos)  # Saída: [3, 2]
