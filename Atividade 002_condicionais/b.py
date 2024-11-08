import os


os.system('cls')

print('MAIOR, MENOR OU NÚMEROS IGUAIS')
print('-'*70)

# Entrada
numero1 = int(input('Entre com o 1º número inteiro: '))
numero2 = int(input('Entre com o 2º número inteiro: '))
numero3 = int(input('Entre com o 3º número inteiro: '))

# números iguais
if numero1 == numero2 == numero3:
    print(f'Os números são iguais!')
    print('-'*70)
else:

    # Maior número
    if (numero1 > numero2) and (numero1 > numero3):
        maior = f'O número {numero1} é o MAIOR!'
    elif (numero2 > numero3) and (numero2 > numero1):
        maior = f'O número {numero2} é o MAIOR!'
    else:
        maior = f'O número {numero3} é o MAIOR!' 

    # Menor número
    if (numero1 < numero2) and (numero1 < numero3):
        menor = f'O número {numero1} é o MENOR!'
    elif (numero2 < numero3) and (numero2 < numero1):
        menor = f'O número {numero2} é o MENOR!'
    else:
        menor = f'O número {numero3} é o MENOR!' 

    print('-'*70)
    print(maior)
    print(menor)
    print('-'*70)




