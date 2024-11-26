import os

os.system('cls')

# Solicita ao usuário para inserir números separados por espaço
entrada = input("Crie uma lista de números, digite números separados por espaço: ")

# Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()
print(numeros_str)
print(type(numeros_str[1]))
print(f'tamanho: {len(numeros_str)}')

# Converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))
print(numeros)
print(type(numeros[1]))
print(f'tamanho: {len(numeros)}')

# Solicita ao usuário para inserir o número que deseja contar na lista
numero_para_contar = int(input("Digite o número que deseja contar quantas vezes aparece dentro da lista: "))

# Conta o número de vezes que o número fornecido aparece na lista
contagem = numeros.count(numero_para_contar)

if contagem > 0:
    print(f"O número {numero_para_contar} aparece {contagem} vezes na lista.")
else:
    print(f"O número {numero_para_contar} não aparece na lista.")

# Exibe a lista fornecida para referência
print(f"Lista fornecida: {numeros}")
