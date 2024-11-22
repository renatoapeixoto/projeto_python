import os

# Limpa a tela do terminal/console
os.system('cls')

# Exibição de cabeçalho formatado
print('-' * 70)
print('SAÍDA COM FOR... ENUMERATE()')
print('-' * 70)

# Inicializa a variável para armazenar a soma
soma = 0

# Criando uma lista com números de 1 a 10
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Percorrendo a lista com o enumerate()
# O enumerate adiciona automaticamente índices a cada elemento da lista
for indice, numero in enumerate(lista_numeros, start=1):  # start=1 inicia os índices a partir de 1
    soma += numero  # Acumula o valor de cada número na variável soma
    print(f'Índice: {indice} = Número: {numero}')  # Exibe o índice e o valor correspondente

# Exibição de resultados finais
print('-' * 70)
print(f'A soma de todos os números é: {soma}')
print('Fim do programa!')
print('-' * 70)

'''
Explicação do Código:
Limpeza do console:
os.system('cls'): Limpa a tela do terminal (funciona apenas em sistemas Windows).

Criação da lista:
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: Define uma lista de números inteiros de 1 a 10.

Uso do enumerate():
A função enumerate() é usada para iterar pela lista, fornecendo, em cada iteração, um par (índice, valor).
O argumento start=1 faz com que os índices comecem em 1 (por padrão, começam em 0).
Acumulação e exibição:

soma += numero: Soma o valor atual (numero) à variável soma.
print(f'Índice: {indice} = Número: {numero}'): Exibe o índice e o número correspondente.
'''