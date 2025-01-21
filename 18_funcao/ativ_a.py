# Crie uma função que receba uma lista de números. Depois retorne duas listas com os
# números pares, os números ímpares, a quantidade de números pares e a quantidade
# de números ímpares.

# função para ver numeros pares e impares. e suas quantidades 
numeros = []
def numeros_pares_impares (numeros):
    pares = []
    impares = []
    qtd_pares = 0
    qtd_impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
            qtd_pares +=1
        else:
            impares.append(impares)
            qtd_impares =+ 1
    return (pares, qtd_pares, impares, qtd_impares)


numero = input("Dgite algm numero: ")




numero_impar = input("Números ímpares: ")
numero_"Quantidade de pares:", qtd_pares)
print("Quantidade de ímpares:", qtd_impares)









def separar_pares_impares(lista_numeros):
    # Inicializando as listas e os contadores
    pares = []
    impares = []
    qtd_pares = 0
    qtd_impares = 0

    # Percorrendo a lista de números
    for numero in lista_numeros:
        if numero % 2 == 0:  # Verifica se o número é par
            pares.append(numero)
            qtd_pares += 1
        else:  # Caso contrário, é ímpar
            impares.append(numero)
            qtd_impares += 1

    # Retorna as listas e as quantidades
    return pares, impares, qtd_pares, qtd_impares

# Exemplo de uso
numeros = [10, 15, 22, 33, 40, 57, 60]
pares, impares, qtd_pares, qtd_impares = separar_pares_impares(numeros)

print("Números pares:", pares)
print("Números ímpares:", impares)
print("Quantidade de pares:", qtd_pares)
print("Quantidade de ímpares:", qtd_impares)
