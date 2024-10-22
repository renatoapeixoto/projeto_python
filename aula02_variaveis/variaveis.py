# importando a biblioteca de sistema
import os

# Limpando o terminal
os.system('cls')

print('-'*70)  # firula
print('Estudo de variáveis')
print('='*70)  # firula

# As variáveis são declaradas por inferência
nome = 'John Doe'
nascimento = 1970
altura = 1.80
peso = 75.5
doador = True
complexo = 3j  # Python trabalha diretamente com números complexos
PI = 3.14  # isso é uma CONSTANTE, seu valor não deve ser alterado

# Saída utilizando o método type() para verificar o tipo da variável
print('\033[0m \033[31mTipos declarados:\033[0m')
print('\033[0m A var \033[32m nome \033[0m é do tipo: ', type(nome))
print('\033[0m A var \033[32m nascimento \033[0m é do tipo: ', type(nascimento))
print('\033[0m A var \033[32m altura \033[0m é do tipo: ', type(altura))
print('\033[0m A var \033[32m peso \033[0m é do tipo: ', type(peso))
print('\033[0m A var \033[32m doador \033[0m é do tipo: ', type(doador))
print('\033[0m A var \033[32m complexo \033[0m é do tipo: ', type(complexo))
print('\033[0m A var \033[32m PI \033[0m é do tipo: ', type(PI))

print('-'*70)
print('')

# primeiro instar no terminal o comando abaixo 
# pip install colorama

from colorama import Fore, Back, Style, init

# Inicializa o colorama
init(autoreset=True)

print(Fore.RED + 'Este texto está em vermelho', type(nome))
print(Fore.GREEN + 'Este texto está em verde'), type(nascimento)
print(Back.YELLOW + 'Este texto tem um fundo amarelo', type(altura))
print(Fore.BLUE + Back.WHITE + 'Texto azul com fundo branco', type(peso))
print(Style.DIM + 'Este texto está com brilho reduzido', type(doador))
print(Style.BRIGHT + 'Este texto está em negrito', type(complexo))
print(Style.BRIGHT + 'Este texto está em negrito', type(PI))

