# Lista principal contendo listas com nome, peso e altura
pessoas = [
    ["John", 40, 1.8],
    ["Alice", 55, 1.6],
    ["Bob", 75, 1.75]
]

# Imprime os dados de cada pessoa
print("Lista de pessoas:")
for pessoa in pessoas:
    print(f"Nome: {pessoa[0]}, Peso: {pessoa[1]} kg, Altura: {pessoa[2]} m")
