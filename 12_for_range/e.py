import os

os.system('cls')

print('-' * 50)
print('ESTRUTURA DE CONTROLE VALIDAÇÃO E CASTING')
print('-' * 50)

soma = 0

for c in range(0, 5):
    numero = input('Digite um número [0-5]: ')

    # Validação
    if not numero.isnumeric():
        print(f"{numero} Entrada inválida!")
        print()
    else:
        # Casting da variável, ou seja, vai virar um inteiro
        numero = int(numero)

        # Validando o intervalo pedido
        if 0 <= numero <= 5:
            print(f'O número {numero} está dentro do intervalo [0-5]!')
            print()
        else:
            print(f"{numero} Entrada inválida!")
            print()

print('-' * 70)
print()
