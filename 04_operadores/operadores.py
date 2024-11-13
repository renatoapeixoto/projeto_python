# imports 
import os
from colorama import Fore, Back, Style, init

os.system('cls') # limpa a tela
init(autoreset=True) # auto resetar a biblioteca colorama

#inicio do codigo
titulo = 'OPERADORES ARITMÉTICOS'
print(Back.CYAN + Style.BRIGHT + '{:^70}'.format(titulo)) # alinhamento format
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

print(Back.CYAN + Style.BRIGHT + 'RAIZ QUADRADA')
print('-'*70)
raiz01 = float(input('Entre com um numero.......: '))
print('-'*70)
print()

print(Back.CYAN + Style.BRIGHT + 'RAIZ CÚBICA')
print('-'*70)
raiz02 = float(input('Entre com um numero.......: '))
print('-'*70)
print()

# Processamento
soma = parcela_1 + parcela_2
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor
raiz_quadrada = raiz01 ** (1/2)
raiz_cubica = raiz02 ** (1/3)

# Saída
print()

print(Back.RED + Style.BRIGHT +'RESULTADOS')
print('='*70)
print(f'A soma de {parcela_1} + {parcela_2} é...........: {soma:}')
print(f'A subtração de {minuendo} - {subtraendo} é......: {diferenca}')
print(f'A multiplicação de {multiplicando} x {multiplicador} é..: {produto}')
print(f'A divisão de {dividendo} ÷ {divisor} é........: {quociente}')
print(f'A Raiz quadrada é...............: {raiz_quadrada}')
print(f'A Raiz cúbica é.................: {raiz_cubica}')
print('='*70)
print()
print()