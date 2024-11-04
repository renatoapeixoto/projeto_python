# imports - pular 2 linhas de espaço depois dos imports
import os
os.system("cls")


# declaraçoes
a = 10
b = 5
c = "jose"
d = 'jose'

# titulo
print('-'*80)
print('Condicionais: OPERADORES RELACIONAIS')
print('-'*80)

# igualdade ==
if c == d:
    print('-'*80)
    print(f'{c} é igual {d}')
    print('-'*80)
else:
    print(f'{c} não é iigual a {d}')

# diferença !=
if a != c:
    print('-'*80)
    print(f'{a} é diferente de {c}')
    print('-'*80)
else:
    print(f'{a} não é diferente de {c}')

# Maior que (>)
if a > b:
    print('-'*80)
    print(f'{a} é maior que {b}')
    print('-'*80)
else:
    print(f'{a} não é maior que {b}')

# Menor que (<)
if b < a:
    print('-'*80)
    print(f'{b} é menor que {a}')
    print('-'*80)
else:
    print(f'{b} não é menor que {a}')

# Maior ou igual a (>=)
if a >= b:
    print('-'*80)
    print(f'{a} é maior ou igual a {b}')
    print('-'*80)
else:
    print(f'{a} não é maior ou igual a {b}')

# Menor ou igual a (<=)
if b <= a:
    print('-'*80)
    print(f'{b} é menor ou igual a {a}')
    print('-'*80)
else:
    print(f'{b} não é menor ou igual a {a}')

print('Fim do programa!')
print('-'*80)
print()
