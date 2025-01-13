# Comandos `key` e `values` em Dicionários (Python)

## O que é um dicionário?
Um dicionário em Python é como uma caixa de armazenamento de informações, onde você tem:

- **Chaves (keys):** são como etiquetas ou rótulos para identificar cada informação.
- **Valores (values):** são os dados que você quer guardar.

### Exemplo
Imagine um dicionário chamado `aluno`:

```python
aluno = {
    "nome": "Ana",
    "idade": 15,
    "nota": 9.5
}
```

- Aqui, `"nome"`, `"idade"` e `"nota"` são as **chaves (keys)**.
- `"Ana"`, `15` e `9.5` são os **valores (values)**.

## Para que servem os comandos `keys()` e `values()`?

### `keys()`
Este comando pega só as chaves do dicionário.

### `values()`
Este comando pega só os valores do dicionário.

### Exemplo prático com o dicionário `aluno`:

#### Pegando as chaves (keys):
```python
chaves = aluno.keys()
print(chaves)
```
**Saída:**
```
dict_keys(['nome', 'idade', 'nota'])
```
Isso mostra as "etiquetas" ou "rótulos" que identificam os valores.

#### Pegando os valores (values):
```python
valores = aluno.values()
print(valores)
```
**Saída:**
```
dict_values(['Ana', 15, 9.5])
```
Isso mostra as informações armazenadas.

## Para que serve na prática?
- Você pode usar **`keys()`** se quiser saber os nomes dos rótulos que o dicionário tem.
- Pode usar **`values()`** para ver todas as informações sem se preocupar com as chaves.

### Exemplo de uso:
Imprimir cada chave com o seu valor:

```python
for chave in aluno.keys():
    print(f"A chave é: {chave}")
```

Imprimir os valores:
```python
for valor in aluno.values():
    print(f"O valor é: {valor}")
```

## Conclusão
- **`keys()`** e **`values()`** são ferramentas que ajudam você a acessar partes específicas do dicionário.
- Eles facilitam muito quando você quer separar o que são as "etiquetas" do que são os "dados".

Se precisar de mais exemplos ou explicações, é só avisar! 😊
