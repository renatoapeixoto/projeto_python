# biblioteca para limpa a tela 
import os
os.system('cls')

# biblioteca para colorir as letras
from colorama import Fore, Back, Style, init
init(autoreset=True)

#inicio do codigo
print(Back.CYAN + Style.BRIGHT + '                     OPERADORES ARITMÉTICOS                           ')
print()

# Entrada de Dados
print(Back.CYAN + Style.BRIGHT + 'SOMA')
print('-'*70)
parcela_1 = float(input('Entre com a 1ª parcela...: '))
parcela_2 = float(input('Entre com a 2ª parcela...: '))
print('-'*70)
print()


print(Back.CYAN + Style.BRIGHT + 'SUBTRAÇÃO')
print('-'*70)
minuendo = float(input('Entre com o minuendo.....: '))
subtraendo = float(input('Entre com a subtraendo...: '))
print('-'*70)
print()


print(Back.CYAN + Style.BRIGHT + 'PRODUTO')
print('-'*70)
multiplicando = float(input('Entre com o multiplicando.: '))
multiplicador = float(input('Entre com o multiplicador.: '))
print('-'*70)
print()


print(Back.CYAN + Style.BRIGHT + 'DIVISÃO')
print('-'*70)
dividendo = float(input('Entre com o dividendo.....: '))
divisor = float(input('Entre com o divisor.......: '))
print('-'*70)

# Processamento
soma = parcela_1 + parcela_2
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor

# Saída
print()

print(Back.RED + Style.BRIGHT +'RESULTADOS')
print('='*70)
print(f'A soma de {parcela_1} + {parcela_2} é...........: {soma}')
print(f'A subtração de {minuendo} - {subtraendo} é......: {diferenca}')
print(f'A multiplicação de {multiplicando} x {multiplicador} é..: {produto}')
print(f'A divisão de {dividendo} ÷ {divisor} é........: {quociente}')
print('='*70)
print()
print()