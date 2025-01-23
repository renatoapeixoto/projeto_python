# Cópia rasa x Cópia profunda

### O que é uma cópia profunda?

**`Imagine o seguinte:`**
Você tem uma caixa cheia de objetos e decide fazer uma cópia dela. No caso de uma cópia rasa, você pega uma nova caixa , mas não copia os objetos de verdade para a nova caixa. Em vez disso, você coloca etiquetas que apontam para os mesmos objetos que estão na caixa original.

Isso significa que:

A caixa nova é diferente da original.
Mas os objetos dentro das duas caixas ainda são os mesmos. Se você mexer nos objetos, as mudanças aparecerão nas duas caixas porque ambos estão "apontando" para os mesmos itens.
Agora em Python com um dicionário:
Um dicionário pode salvar "coisas" como números, textos ou até listas. Quando você usa o método .copy(), ele cria uma nova "caixa" (dicionário) , mas, se tiver algo mais complexo dentro (como listas ou outros dicionários), a cópia só coloca "etiquetas" apontando para os mesmos dados.

* Imutaveis - string , numeros e tuplas
* mutaveis - listas e dicionarios

```python
original = {
    "nome": "João",
    "idade": 15,
    "hobbies": ["futebol", "videogame"]
}
copia = original.copy()  # Faz uma cópia rasa do dicionário
```

O que acontece agora:

O dicionário copia é uma nova caixa .
Mas a lista de hobbies ( ["futebol", "videogame"]) não foi copiada de verdade . O copia e o original estão compartilhando essa lista.

O que acontece ao modificar algo compartilhado?

Se você alterar um valor dentro da lista (que é compartilhado), uma mudança aparecerá em ambos os dicionários :

```python
copia["hobbies"].append("natação")  # Adiciona um hobby na lista
print("Original:", original)
print("Cópia:", copia)
# Original: {'nome': 'João', 'idade': 15, 'hobbies': ['futebol', 'videogame', 'natação']}
# Cópia: {'nome': 'João', 'idade': 15, 'hobbies': ['futebol', 'videogame', 'natação']}
```

Lembre-se de alterar a lista na cópia afetiva ou original , porque os dois estão usando a mesma lista na memória .

Em resumo:
Cópia rasa cria uma nova estrutura externa (o dicionário), mas os objetos dentro dela (como listas ou outros dicionários) não são duplicados .
Os objetos internos são apenas referências compartilhadas , ou seja, apontam para o mesmo lugar na memória.
Alterar esses objetos internos relacionados tanto ao original quanto à cópia.

| **Característica**                              | **Cópia Rasa**              | **Cópia Profunda**             |
| ------------------------------------------------------ | ---------------------------------- | ------------------------------------- |
| Copia objetos simples?                                 | Sim                                | Sim                                   |
| Copiar objetos compostos (listas, dicionários, etc.)? | Não, aponta para o mesmo lugar    | Sim, cria uma nova cópia na memória |
| As alterações afetam o outro?                        | Sim, se forem estruturas compostas | Não, são independentes              |
