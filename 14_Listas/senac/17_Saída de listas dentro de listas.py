import os

# Limpa a tela do terminal/console
os.system('cls')

print('-' * 70)
print('VARRENDO LISTAS DENTRO DE LISTAS')
print('-' * 70)

# Simulação de um tabuleiro de jogo da velha (3x3)
jogo_velha = [
    ['X', 'O', 'X'],  # Linha 0
    ['X', 'X', 'O'],  # Linha 1
    ['O', 'O', 'O']   # Linha 2
]

# Exibe o tabuleiro de forma bruta
print(jogo_velha)
print()

# Acessando manualmente valores específicos
print(f"Na linha 1 coluna 1, existe um: {jogo_velha[1][1]}")
print(f"Na linha 0 coluna 2, existe um: {jogo_velha[0][2]}")
print()

# Varrendo todas as linhas e colunas com loops aninhados
for linha in range(0, len(jogo_velha)):  # Itera pelas linhas
    for coluna in range(0, len(jogo_velha[linha])):  # Itera pelas colunas
        print(jogo_velha[linha][coluna], end=' ')  # Exibe os valores
    print()  # Quebra de linha após cada linha do tabuleiro
