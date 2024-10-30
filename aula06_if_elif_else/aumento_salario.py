# D) A empresa "SalaryBoost" está implementando um sistema automatizado para
# calcular os aumentos salariais de seus funcionários com base em critérios
# específicos. Eles precisam de um programa que receba como entrada o salário
# atual de um funcionário e, em seguida, calcule o novo salário com base em
# determinadas condições. Essas condições incluem um aumento de 5% caso o salário
# atual seja superior a R$1500,00, e um aumento de 10% caso o salário atual seja
# inferior a R$1000,00. Além disso, o programa deve garantir que o salário
# informado não seja igual a zero ou negativo, pois isso não seria válido.

# imports
import os


# limpa a tela
os.system('cls')

# Entradas e declarações
salario = float(input('Digite o salário do funcionario: '))
novo_salario = 0.0
aumento = ''

# Processamento
while True :
    if salario <= 0.0 :
        print('Salario inválido, valor <= zero, Digite novamente: ')
        print()
        salario = float(input('Digite o salário do funcionario: '))
    else :
        if salario > 1500 :
            novo_salario = salario * 1.05
            aumento = '5%'
            break       
        else :
            novo_salario = salario * 1.10
            aumento = '10%'
            break

# Saida
print(f'O salário de R$ {salario}, aumentou {aumento}, passando para'
      f' R$ {novo_salario}')
print('')