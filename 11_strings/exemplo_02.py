import os

# Limpa a tela (compatível com Windows e Unix)
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 70)
print('Funções String')
print('-' * 70)

# Definindo a string
frase1 = "Olá, Mundo!"

# retorna o comprimento (número de caracteres) de uma string.
quantidade_caracteres = len(frase1)
print(f"A frase '{frase1}' contém {quantidade_caracteres} caracteres")
print('-' * 70)

# converte todos os caracteres da string para minúsculas.
minusculas = frase1.lower()
print(f"Frase original: {frase1}")
print(f"Frase em minúsculas: {minusculas}")
print('-' * 70)

# converte todos os caracteres da string para maiúsculas.
maiusculas = frase1.upper()
print(f"Frase original: {frase1}")
print(f"Frase em minúsculas: {maiusculas}")
print('-' * 70)

# converte o primeiro caractere da string para maiúscula e os demais para 
# minúscula.
capitalizada = frase1.capitalize()  # Capitaliza apenas o primeiro caractere
print(f"Frase original: {frase1}")
print(f"Frase capitalizada: {capitalizada}")
print('-' * 70)

# remove os espaços em branco (ou outros caracteres especificados) do início e 
# do final da string.
frase2 = '   Olá, Mundo   '
sem_espacos = frase2.strip()  # Remove espaços em branco no início e no fim
remove_letra_a = frase2.strip('a')
print(f"Frase original: '{frase2}'")
print(f"Frase sem espaços: '{sem_espacos}'")
print(f"Remove letra a: '{remove_letra_a}'")

print('-' * 70)

# Substituindo uma palavra na frase1
substituicao = frase1.replace("Mundo", "Python")  # Substitui "Mundo" por "Python"
print(f"Frase original: {frase1}")
print(f"Frase com substituição: {substituicao}")
print('-' * 70)

# Separando palavras da string em uma lista
lista = frase1.split(",")  # Divide a string em uma lista usando a vírgula como separador
print(f"Frase original: '{frase1}'")
print(f"Frase dividida em lista: {lista}")
print('-' * 70)

# Unindo uma lista de palavras em uma string com separador
lista = ['Olá', 'mundo']
juncao = "_".join(lista)  # Junta a lista em uma string com "_" como separador
juncao1 = ' '.join(lista)
print(f"Lista original: {lista}")
print(f"Lista unida em string: {juncao}")
print(f"Lista unida em string: {juncao1}")
print('-' * 70)
