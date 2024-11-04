# imports
# biblioteca para interagir com o sistema operacional
# biblioteca para pegara data e hora do sistema

import os
import datetime

# limpar a tela 
os.system("cls")

# firula
print('-' * 70)
print('ENTRADA DE DADOS E, PYTHON')
print('=' * 70)

# Entrada sem casting
nome = input  ("Entre com o nome.....: ")
peso = float(input  ("Entre com o peso.....: "))
altura = float(input("Entre com o altura...: "))

# Entrada com casting
ano_nascimento = int(input("Ano de Nascimento....: "))
cep = int(input("Entre com seu Cep....: "))
bairro = str(input("Entre com o bairro...: "))
rua = str(input("Nome da Rua..........: "))
numero = int(input("Entre com o numero...: "))

# processamento: pegando o ano corrente
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento

# firula
print()
print('-' * 70)
print('SAIDA DE DADOS E, PYTHON')
print('=' * 70)

# saida de dados
print('Nome..................: ', nome)
print('Data de nascimento....: ', ano_nascimento)
print('Peso..................: ', peso)
print('Altura................: ', altura)

# Saída interpolada
print()
print(f'{nome}, você tem {idade} anos!')
print(f'CEP...................: {cep}')
print(f'Bairro................: {bairro}')
print(f'Rua...................: {rua}')
print(f'Número................: {numero}')
print('-' * 70)

