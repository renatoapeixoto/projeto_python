# Método `.items()` em Python

O método **`.items()`** é usado em **dicionários** em Python para retornar um **objeto de visualização** que contém pares **(chave, valor)** do dicionário. Ele é muito útil quando você quer percorrer o dicionário e acessar **tanto a chave quanto o valor ao mesmo tempo**.

---

## 📌 Sintaxe
```python
dicionario.items()
```

---

## 📚 Como funciona?
O método **`.items()`** retorna um objeto que é uma **visualização de pares (chave, valor)**. Você pode convertê-lo para uma lista, se necessário, ou percorrê-lo diretamente em um loop.

---

## ✅ Exemplo 1: Usando `.items()` para iterar em um dicionário
```python
dicionario = {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'}

# Percorrendo o dicionário com .items()
for chave, valor in dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')
```

💡 **Saída**:
```
Chave: nome, Valor: Alice
Chave: idade, Valor: 25
Chave: cidade, Valor: São Paulo
```

---

## ✅ Exemplo 2: Convertendo `.items()` em uma lista
```python
dicionario = {'a': 1, 'b': 2, 'c': 3}

# Convertendo para lista de tuplas
lista_de_pares = list(dicionario.items())
print(lista_de_pares)
```

💡 **Saída**:
```
[('a', 1), ('b', 2), ('c', 3)]
```

---

## ✅ Exemplo 3: Verificando se um par (chave, valor) está no dicionário
```python
dicionario = {'x': 10, 'y': 20, 'z': 30}

# Verificando se ('x', 10) está no dicionário
if ('x', 10) in dicionario.items():
    print("Par encontrado!")
else:
    print("Par não encontrado.")
```

💡 **Saída**:
```
Par encontrado!
```

---

## 🧠 Comparação com outros métodos

| Método       | Retorna                     | Exemplo                       |
|--------------|-----------------------------|--------------------------------|
| `.keys()`    | As chaves do dicionário      | `['nome', 'idade', 'cidade']`  |
| `.values()`  | Os valores do dicionário     | `['Alice', 25, 'São Paulo']`   |
| `.items()`   | Pares (chave, valor)         | `[('nome', 'Alice'), ('idade', 25), ('cidade', 'São Paulo')]` |

---

## 🔧 Exemplo prático com dicionário complexo
Vamos usar o dicionário abaixo como exemplo:
```python
ferramentas = {
    "Martelo": {
        "Descrição": "Ferramenta usada para pregar e quebrar objetos",
        "Material": "Aço e madeira",
        "Utilidade": "Pregar pregos e quebrar materiais"
    }
}
```

### ✅ Exemplo 1: Percorrendo as chaves e os subdicionários usando `.items()`
```python
# Usando .items() para ver as chaves principais e os subdicionários
for ferramenta, detalhes in ferramentas.items():
    print(f"Ferramenta: {ferramenta}")
    print(f"Detalhes: {detalhes}")
```

💡 **Saída**:
```
Ferramenta: Martelo
Detalhes: {'Descrição': 'Ferramenta usada para pregar e quebrar objetos', 'Material': 'Aço e madeira', 'Utilidade': 'Pregar pregos e quebrar materiais'}
```

---

### ✅ Exemplo 2: Percorrendo as chaves internas do subdicionário
```python
# Percorrendo as chaves internas
for ferramenta, detalhes in ferramentas.items():
    print(f"Ferramenta: {ferramenta}")
    for chave, valor in detalhes.items():
        print(f"{chave}: {valor}")
```

💡 **Saída**:
```
Ferramenta: Martelo
Descrição: Ferramenta usada para pregar e quebrar objetos
Material: Aço e madeira
Utilidade: Pregar pregos e quebrar materiais
```

---

### ✅ Exemplo 3: Transformando o dicionário em uma lista de tuplas
```python
# Convertendo para lista de tuplas
ferramentas_lista = list(ferramentas.items())
print(ferramentas_lista)
```

💡 **Saída**:
```
[('Martelo', {'Descrição': 'Ferramenta usada para pregar e quebrar objetos', 'Material': 'Aço e madeira', 'Utilidade': 'Pregar pregos e quebrar materiais'})]
```

---

## 🚀 Dica final
Sempre que você precisar acessar **chaves e valores** simultaneamente em um dicionário, o uso de **`.items()`** é a abordagem mais eficiente. Explore as possibilidades para simplificar o seu código!
