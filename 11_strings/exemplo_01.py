import os

os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 70)
print('Fatiamento de Strings')
print('-' * 70)

frase = 'String em Python!'

# Exibindo a string original
print(f"String original: {frase}")
print('-' * 70)

# Fatiamento: acessando partes específicas da string
# Primeiros cinco caracteres
primeiros_cinco = frase[:5]
print(f"Primeiros cinco caracteres: {primeiros_cinco}")
print('-' * 70)

# Últimos dez caracteres
ultimos_dez = frase[-10:]
print(f"Últimos dez caracteres: {ultimos_dez}")
print('-' * 70)

# Do quarto ao décimo caractere
quarto_ao_decimo = frase[3:10]
print(f"Do quarto ao décimo caractere: {quarto_ao_decimo}")
print('-' * 70)

# A cada dois caracteres
a_cada_dois = frase[::2]
print(f"A cada dois caracteres: {a_cada_dois}")
print('-' * 70)

# Invertendo a string
invertida = frase[::-1]
print(f"String invertida: {invertida}")
print('-' * 70)
