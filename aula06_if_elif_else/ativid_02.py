# B) A empresa "DataMax" está desenvolvendo um novo software de análise 
# estatística e precisa de uma funcionalidade que permita aos usuários inserir 
# três números e, em seguida, exibir na tela qual é o maior número, qual é o 
# menor número ou se os números são todos iguais. Essa funcionalidade é crucial 
# para os analistas de dados da "DataMax" que trabalham com conjuntos de dados 
# diversos e precisam rapidamente identificar as características básicas desses 
# conjuntos,como a presença de outliers ou a uniformidade dos números.

import os


# limpa a tela
os.system('cls')

# Entrada
valor1 = float(input('Digite o 1º um numero: '))
valor2 = float(input('Digite o 2º um numero: '))
valor3 = float(input('Digite o 3º um numero: '))
maior = 0
menor = 0
igual = 0

# valor igual
if valor1 == valor2 and valor2 == valor3 :
    igual = valor1
    print(f'Os números tres números são iguais.')
else:
    # maior numero
    if valor1 > valor2 and valor1 > valor3 :
        maior = valor1
    elif valor2 > valor3 :
        maior = valor2
    else:
        maior = valor3

    # menor numero
    if valor1 < valor2 and valor1 < valor3 :
        menor = valor1
    elif valor2 < valor3 :
        menor = valor2
    else:
        menor = valor3

    #imprimir maior e menor
    print(f'O maior número é : {maior}')
    print(f'O menor número é : {menor}')