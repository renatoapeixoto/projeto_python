import os
os.system('cls')

'''Em que situações são usadas?
Os programadores usam dicionários frequentemente em situações como:
Armazenar dados estruturados: Por exemplo, armazenar dados de usuários de uma aplicação:
'''
usuarios = {
    "usuario1": {"nome": "Carlos", "idade": 30},
    "usuario2": {"nome": "Mariana", "idade": 25}
}
print(usuarios["usuario1"]["nome"])  # Saída: Carlos
print(usuarios["usuario1"]["idade"])  # Saída: Carlos
print(usuarios["usuario2"]["nome"])  # Saída: Carlos
print(usuarios["usuario2"]["idade"])  # Saída: Carlos

# Contar frequências (contador): Contar a frequência de elementos em uma lista:
palavras = ["maçã", "banana", "maçã", "laranja", "banana", "banana"]
contador = {}
for palavra in palavras:
    contador[palavra] = contador.get(palavra, 0) + 1
print(contador)  # Saída: {'maçã': 2, 'banana': 3, 'laranja': 1}

# Agrupar dados relacionados: Por exemplo, dados em uma API retornam frequentemente no formato JSON, que é muito parecido com dicionários em Python:
dados = {
    "cidade": "São Paulo",
    "clima": {"temperatura": 28, "umidade": 75},
    "previsao": ["sol", "chuva", "nublado"]
}
print(dados[1])
print(dados["clima"]["temperatura"])  # Saída: 28

# Armazenar resultados de cálculos: Memorizar cálculos para evitar repetições:
cache = {}
def fatorial(n):
    if n in cache:
        return cache[n]
    if n == 0:
        return 1
    resultado = n * fatorial(n - 1)
    cache[n] = resultado
    return resultado
print(fatorial(5))  # Saída: 120
