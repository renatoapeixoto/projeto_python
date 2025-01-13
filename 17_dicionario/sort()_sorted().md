### A principal diferença entre os métodos sort()e sorted()em Python está relacionada ao tipo de uso , mutabilidade e retorno . Vamos detalhar cada um:

## 1. sort()
Método de listas : Funciona apenas em listas .
Alterar a lista original : Modifica diretamente a lista na qual é chamado ( in-place ).
Retorno : Não retorna nada ( None). Basta reorganizar a lista original.
Exemplo de uso
## Usando sort() para ordenar a lista
``` python
numeros = [5, 2, 9, 1]
numeros.sort()
print(numeros)  # Saída: [1, 2, 5, 9]
```
- Características:
Ideal quando você deseja alterar sua própria lista.
Não pode ser usado em tipos imutáveis, como tuplas ou strings.

- Parâmetros
key: Função para personalizar a ordenação.
reverse: Booleano. Se True, ordena em ordem decrescente.

## Ordenar em ordem decrescente
 ``` python
numeros = [5, 2, 9, 1]
numeros.sort(reverse=True)
print(numeros)  # Saída: [9, 5, 2, 1]
```
### 2. sorted()
Função global : Funciona com qualquer iterável (listas, tuplas, strings, dicionários, etc.).
Não altera o original : Cria e retorna uma nova estrutura ordenada, mantendo o original iterável intacto.

### Sintaxe da Função sorted()
``` python
sorted(iterable, *, key=None, reverse=False)
```
## **Parâmetros**
### **`iterable(obrigatório)`**:

O que pode ser ordenado com sorted()?
O objeto a ser ordenado pode ser qualquer iterável em Python, como:
  * Listas
  * Tuplas
  * Strings (sequências de caracteres)
  * Dicionários (somente as chaves são consideradas por padrão)
  * Qualquer objeto que implemente uma interface iterável (ex.: conjuntos, geradores).

**Listas:**
    Exemplo: [5, 2, 8, 1]
    Ordenação: sorted([5, 2, 8, 1]) -> [1, 2, 5, 8].

**Tuplas:**
    Exemplo: (5, 2, 8, 1)
    Ordenação: sorted((5, 2, 8, 1)) -> [1, 2, 5, 8].

**Strings (sequência de caracteres):**
Strings são iteráveis, e cada caractere será tratado como um elemento.
    Exemplo: "python"
    Ordenação: sorted("python") -> ['h', 'n', 'o', 'p', 't', 'y'].

**Dicionários:**
Ordenação padrão: apenas as chaves do dicionário são consideradas.
    Exemplo: {"b": 2, "a": 1, "c": 3}
    Ordenação: sorted({"b": 2, "a": 1, "c": 3}) -> ['a', 'b', 'c'].

**Conjuntos:**
    Exemplo: Conjuntos (set):
    Ordenação: sorted({5, 2, 8, 1}) -> [1, 2, 5, 8].
    
**Geradores:**
    Ordenação: sorted(x for x in range(5, 0, -1)) -> [1, 2, 3, 4, 5].

### **`key(opcional):`**
Uma função que define as classificações de ordenação.
Essa função é aplicada a cada elemento antes de ser comparada.
Exemplo: key=lenordena com base no comprimento de elementos.

### **`reverse(opcional)`**:
Um valor booleano que, quando definido como True, inverte a ordem da ordenação (ordem decrescente).
O valor padrão é False(ordem crescente).

## **Exemplos Práticos**

### **Ordenar uma lista de números**
### Sem usar `key`:
```python
numeros = [10, 5, 3, 8]
ordenado = sorted(numeros)
print(ordenado)  # Saída: [3, 5, 8, 10]
```

**Ordenação com reverse=True**
**`Ordenando em ordem decrescente:`**
``` python
numeros = [5, 2, 9, 1]
resultado = sorted(numeros, reverse=True)
print(resultado)  # Saída: [9, 5, 2, 1]
```
## O Argumento `key` na Função `sorted()` em Python
O argumento **`key`** da função **`sorted()`** em Python é usado para personalizar a lógica de ordenação. Ele aceita uma **função** que especifica um critério de ordenação. Essa função é aplicada a cada elemento da sequência (lista, tupla, dicionário, etc.) antes de realizar a comparação.

### **Como o `key` funciona?**
1. **Transformação dos elementos**:
   - A função passada em `key` transforma cada elemento da sequência antes da comparação.
   - Essa transformação define como os elementos serão comparados.

2. **Retorno do `key`**:
   - A função fornecida deve retornar um valor que será usado como critério para a ordenação.

## **Exemplos Práticos**
**Com key, ordenando pelo valor negativo:**
``` python
numeros = [10, 5, 3, 8]
ordenado = sorted(numeros, key=lambda x: -x)
print(ordenado)  # Saída: [10, 8, 5, 3]
```
Explicação:
   - A função lambda x: -x transforma cada número em seu valor negativo.
   - O maior número negativo (-10) é tratado como o menor valor, invertendo a ordem.   


1. Ordenar por comprimento de cordas
Ordenando uma lista de palavras por comprimento:
``` python
palavras = ["banana", "uva", "maçã", "abacaxi"]
resultado = sorted(palavras, key=len)
print(resultado)  # Saída: ['uva', 'maçã', 'banana', 'abacaxi']
```
2. Ordenar uma lista de tuplas pelo segundo elemento
Ordenando uma lista de tuplas com base no segundo valor:
``` python
tuplas = [(1, 3), (4, 1), (2, 2)]
resultado = sorted(tuplas, key=lambda x: x[1])
print(resultado)  # Saída: [(4, 1), (2, 2), (1, 3)]
```
3. Ordenar dicionário pelas chaves
``` python
dicionario = {"c": 3, "a": 1, "b": 2}
resultado = sorted(dicionario)
print(resultado)  # Saída: ['a', 'b', 'c']
```
4. Ordenar dicionário pelos valores
Usando uma função lambdapara acessar os valores:
``` python
dicionario = {"c": 3, "a": 1, "b": 2}
resultado = sorted(dicionario, key=lambda chave: dicionario[chave])
print(resultado)  # Saída: ['a', 'b', 'c']
```
5. Ordenar por ordem inversa com valores absolutos
Ordenando números pelo valor absoluto, em ordem decrescente:
``` python
numeros = [-3, 1, -5, 4]
resultado = sorted(numeros, key=abs, reverse=True)
print(resultado)  # Saída: [-5, 4, -3, 1]
```
6. Ordenar strings ignorando letras secretas
Ordenando palavras de forma sem distinção entre maiúsculas e minúsculas:
``` python
palavras = ["Banana", "uva", "Maçã", "abacaxi"]
resultado = sorted(palavras, key=str.lower)
print(resultado)  # Saída: ['abacaxi', 'Banana', 'Maçã', 'uva']
```
7. Ordenar por múltiplos critérios
Ordenando pessoas pela idade e, em caso de empate, pelo nome:
``` python
pessoas = [("João", 25), ("Ana", 30), ("Carlos", 25)]
resultado = sorted(pessoas, key=lambda x: (x[1], x[0]))
print(resultado)  # Saída: [('Carlos', 25), ('João', 25), ('Ana', 30)]
```
8. Ordenar uma lista de dicionários
Ordenando uma lista de dicionários com base em um campo específico:
``` python
pessoas = [{"nome": "João", "idade": 25}, {"nome": "Ana", "idade": 30}, {"nome": "Carlos", "idade": 20}]
resultado = sorted(pessoas, key=lambda x: x["idade"])
print(resultado)
# Saída: [{'nome': 'Carlos', 'idade': 20}, {'nome': 'João', 'idade': 25}, {'nome': 'Ana', 'idade': 30}]
```
9. Ordenar números com base no resto da divisão por 3
``` python
numeros = [10, 15, 20, 25]
resultado = sorted(numeros, key=lambda x: x % 3)
print(resultado)  # Saída: [15, 10, 25, 20]
```
10. Ordenar por palavras em uma frase
Ordenando uma frase com base no comprimento das palavras:
``` python
frase = "Python é uma linguagem incrível"
resultado = sorted(frase.split(), key=len)
print(resultado)  # Saída: ['é', 'uma', 'Python', 'incrível', 'linguagem']
```
11. Ordenando as tuplas com base na soma dos valores de cada uma:
Ordenando as tuplas com base na soma dos valores de cada uma:
``` python
tuplas = [(1, 2), (3, 1), (0, 4)]
resultado = sorted(tuplas, key=lambda x: sum(x))
print(resultado)  # Saída: [(1, 2), (3, 1), (0, 4)]
```
12. Ordenar cordas pelo último caractere
``` python
palavras = ["banana", "uva", "maçã", "abacaxi"]
resultado = sorted(palavras, key=lambda x: x[-1])
print(resultado)  # Saída: ['banana', 'uva', 'maçã', 'abacaxi']
```
13. Ordenar uma lista de números pela quantidade de dígitos
``` python
numeros = [1, 100, 25, 1000, 3]
resultado = sorted(numeros, key=lambda x: len(str(x)))
print(resultado)  # Saída: [1, 3, 25, 100, 1000]
```
14. Ordenar dados em formato de string
Ordenando uma lista de dados sem formato DD/MM/AAAA:
``` python
datas = ["12/05/2022", "01/01/2023", "15/03/2021"]
resultado = sorted(datas, key=lambda x: list(map(int, x.split("/")))[::-1])
print(resultado)  # Saída: ['15/03/2021', '12/05/2022', '01/01/2023']
```
15. Ordenar um dicionário de listas pelo tamanho das listas
``` python
dicionario = {"a": [1, 2, 3], "b": [4], "c": [5, 6]}
resultado = sorted(dicionario, key=lambda x: len(dicionario[x]))
print(resultado)  # Saída: ['b', 'c', 'a']
```
16. Ordenar strings pelo número de vogais
``` python
palavras = ["banana", "uva", "maçã", "abacaxi"]
resultado = sorted(palavras, key=lambda x: sum(1 for c in x if c in "aeiou"))
print(resultado)  # Saída: ['uva', 'maçã', 'banana', 'abacaxi']
```
17. Ordenar uma lista de números pela proximidade de um valor
``` python
# Ordenando números pela proximidade do valor 10:
numeros = [1, 7, 15, 20]
resultado = sorted(numeros, key=lambda x: abs(x - 10))
print(resultado)  # Saída: [7, 15, 1, 20]
```
18. Ordenar uma lista de strings pelo número de caracteres únicos
``` python
palavras = ["python", "banana", "uva", "abracadabra"]
resultado = sorted(palavras, key=lambda x: len(set(x)))
print(resultado)  # Saída: ['uva', 'python', 'banana', 'abracadabra']
```
19. Ordenar uma lista de listas pelo maior valor de cada sublista
``` python
listas = [[1, 2, 3], [10, 5], [8, 9, 0]]
resultado = sorted(listas, key=lambda x: max(x))
print(resultado)  # Saída: [[1, 2, 3], [8, 9, 0], [10, 5]]
```
20. Ordenar strings por número de letras repetidas
``` python
palavras = ["banana", "uva", "maçã", "abacaxi"]
resultado = sorted(palavras, key=lambda x: sum(x.count(c) > 1 for c in set(x)))
print(resultado)  # Saída: ['uva', 'maçã', 'abacaxi', 'banana']
```

Retorno : Retorna o resultado ordenado como uma nova lista .
Exemplo de uso

# Usando sorted() para criar uma nova lista ordenada
``` python
numeros = [5, 2, 9, 1]
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)  # Saída: [1, 2, 5, 9]
print(numeros)  # Lista original permanece a mesma: [5, 2, 9, 1]
```
- Características:
Mais flexível, pois pode ser usado em strings, tuplas e outros iteráveis.
Mantenha o objeto original intacto.

- Parâmetros
key: Função para personalizar a ordenação.
reverse: Booleano. Se True, ordena em ordem decrescente.

# Ordenar uma string
``` python
texto = "python"
texto_ordenado = sorted(texto)
print(texto_ordenado)  # Saída: ['h', 'n', 'o', 'p', 't', 'y']
```

Diferenças Resumidas
|Atribuição	        |sort()	            |sorted()
|-------------------|-------------------|-------------
|Tipo de Operação	|Método de listas	|Função global
|Tipo de entrada	|Apenas listas	    |Qualquer iterável
|Modifica Original	|Sim (no local)	    |Não (cria uma nova lista)
|Retorno	        |None	            |Nova lista
---

## Quando usar sort() e quando usar sorted()?
### Usar sort() quando:
Você precisa ordenar uma lista e quer que a própria lista original seja modificada.
Não precisa de uma nova cópia.

### Usar sorted() quando:
Você está lidando com outros iteráveis, como tuplas, strings ou dicionários.
Precisa preservar a estrutura original e obter uma nova lista ordenada .

### Como sorted() funciona em dicionários?
Por padrão , a sorted() ordem das chaves do dicionário em ordem crescente.
Ele aceita argumentos questionáveis, como:

**`key:`** Para definir a lógica de ordenação personalizada.
**`reverse:`** Para inverter a ordem da ordenação (de crescente para decrescente).

**Exemplos Práticos**
1. Ordenar apenas as chaves (padrão)
Por padrão, o sorted() retorna uma lista com as chaves do dicionário, ordenadas alfabeticamente (para strings) ou em ordem crescente (para números).

### 1. Ordenar as chaves
``` python
meu_dicionario = {"b": 2, "a": 5, "c": 1}
chaves_ordenadas = sorted(meu_dicionario)
print(chaves_ordenadas)  # Saída: ['a', 'b', 'c']
```
### 2. Ordenar pelos valores
Se você deseja ordenar o dicionário com base nos valores , use o argumento keye a função lambdapara acessar os valores:
``` python
Copiar código
meu_dicionario = {"b": 2, "a": 5, "c": 1}
# Ordenar pelas chaves com base nos valores
ordenado_por_valores = sorted(meu_dicionario, key=lambda chave: meu_dicionario[chave])
print(ordenado_por_valores)  # Saída: ['c', 'b', 'a']
# Nesse caso:
# 'c'vem primeiro porque o valor associado é 1, que é o menor.
# 'b'vem em seguida, pois o valor é 2.
# 'a'é o último, com o valor 5.
```

### 3. Ordenar em ordem decrescente
Use o parâmetro reverse=True para inverter a ordem:
``` python
meu_dicionario = {"b": 2, "a": 5, "c": 1}
# Ordenar pelos valores em ordem decrescente
ordenado_decrescente = sorted(meu_dicionario, key=lambda chave: meu_dicionario[chave], reverse=True)
print(ordenado_decrescente)  # Saída: ['a', 'b', 'c']
``` 

### 4. **`Crie um dicionário ordenado`**
Se você quiser que o resultado seja um **dicionário ordenado (em vez de uma lista)**, você pode reconstruí-lo:
``` python
meu_dicionario = {"b": 2, "a": 5, "c": 1}
# Ordenar pelos valores e reconstruir um dicionário
dicionario_ordenado = {chave: meu_dicionario[chave] for chave in sorted(meu_dicionario, key=lambda chave: meu_dicionario[chave])}
print(dicionario_ordenado)  # Saída: {'c': 1, 'b': 2, 'a': 5}
```

### 5. Ordenar por pares (chave-valor)
- Use o método items()para ordenar os pares chave-valor diretamente.
``` python
meu_dicionario = {"b": 2, "a": 5, "c": 1}
# Ordenar pelos valores diretamente
pares_ordenados = sorted(meu_dicionario.items(), key=lambda item: item[1])
print(pares_ordenados)  # Saída: [('c', 1), ('b', 2), ('a', 5)]
```
- Se você precisar de um dicionário ordenado:
```python
dicionario_ordenado = dict(pares_ordenados)
print(dicionario_ordenado)  # Saída: {'c': 1, 'b': 2, 'a': 5}
```
Resumo
O método sorted()permite ordenar dicionários de diferentes formas:
* Ordenar chaves (padrão):
* sorted(meu_dicionario)
* Ordenar pelos valores:
* sorted(meu_dicionario, key=lambda chave: meu_dicionario[chave])
* Ordem decrescente:
* Adicionar reverse=True.







