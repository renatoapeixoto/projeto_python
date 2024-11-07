import os


os.system('cls')

print('AUMENTO SALARIAL')
print('-'*70)

salaria_atual = float(input('Ente com o salarial atual do funcionário: R$'))

# Verificando salário igual a 0
if (salaria_atual <= 0.0):
    print('Salário inválido!')
    print('-'*70)
else:

    if salaria_atual > 1500:
        novo_salario = salaria_atual + (salaria_atual * 0.05)
    elif salaria_atual < 1000:
        novo_salario = salaria_atual + (salaria_atual * 0.1)
    else:
        novo_salario = salaria_atual
        print('Funcionário não receberá aumento!')
    

print(f'Seu salário atualizado é: R${novo_salario}')
print('-'*70)
