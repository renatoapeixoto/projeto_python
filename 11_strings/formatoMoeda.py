import os
os.system('cls')

# Transformando no formato brasileiro
lucro = float(input('Digite um valor R$: '))  # Exemplo de valor
print(lucro)
print(type(lucro))
print()

lucro_texto = f'R${lucro:,.2f}'
print(lucro_texto)
print(type(lucro_texto))
print()


lucro_texto = '{:,.2f}'.format(lucro)
print(lucro_texto)
print(type(lucro_texto))
print()

lucro_texto = lucro_texto.replace(',','_')
print(lucro_texto)
print(type(lucro_texto))
print()

lucro_texto = lucro_texto.replace('.',',')
print(lucro_texto)
print(type(lucro_texto))
print()

lucro_texto = lucro_texto.replace('_','.')
print(lucro_texto)
print(type(lucro_texto))
print()

lucro_texto = f'R${lucro:_.2f}'.replace('.', ',').replace('_', '.')
print(lucro_texto)
print()
