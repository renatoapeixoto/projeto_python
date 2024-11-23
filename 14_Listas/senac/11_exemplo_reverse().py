import os

# Limpa a tela do terminal/console
os.system('cls')

# Solicita ao usuário para inserir números separados por espaço
entrada = input("Digite números separados por espaço: ")

# Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

# Converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

# Exibe a lista fornecida para referência
print("Lista fornecida:", numeros)

# Solicita ao usuário para decidir se deseja inverter a lista
escolha = input("Deseja inverter a ordem da lista? (s/n): ").strip().lower()

# Verifica a escolha do usuário e inverte a lista se a resposta for 's'
if escolha == 's':
    numeros.reverse() # o método reverse() é chamado para inverter a ordem dos elementos na lista.
    print("Lista invertida:", numeros)
else:
    print("A lista não foi invertida.")
