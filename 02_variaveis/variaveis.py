# importando a biblioteca de sistema
# primeiro instar o colorama no terminal com o comando abaixo :
# pip install colorama

import os
from colorama import Fore, Back, Style, init

# Limpando o terminal
os.system('cls')

print('-'*70)  # firula
print('Estudo de variáveis')
print('-'*70)  # firula

# As variáveis são declaradas por inferência
nome = 'John Doe'
nascimento = 1970
altura = 1.80
peso = 75.5
doador = True
complexo = 3j  # Python trabalha diretamente com números complexos
PI = 3.14  # isso é uma CONSTANTE, seu valor não deve ser alterado
print('')

# Inicializa o colorama
init(autoreset=True)
print(Style.DIM + Fore.BLACK + Back.WHITE +
      'Nome: ' + nome + ', tipo: ' + str(type(nome)))

print(Fore.GREEN + 'Nascimento: '), type(nascimento)
print(Back.YELLOW + 'Altura: ', type(altura))
print(Fore.BLUE + Back.WHITE + 'Peso: ', type(peso))
print(Style.DIM + 'Doador: ', type(doador))
print(Style.BRIGHT + 'Complexo: ', type(complexo))
print(Style.BRIGHT + 'PI: ', type(PI))

# Explicação:
# Fore: Define a cor do texto (frente). Ex: Fore.RED para vermelho.
# Back: Define a cor de fundo. Ex: Back.YELLOW para amarelo.
# Style: Define o estilo, como brilho (negrito, reduzido). Ex: Style.BRIGHT.
# init(autoreset=True): Isso garante que as cores sejam automaticamente resetadas após cada impressão, para que você não precise redefinir manualmente o estilo para a cor padrão. Sem essa opção, as cores podem persistir em todo o texto seguinte até que você as mude ou redefina.
# Tabela de cores principais:
# Fore Colors (cor da frente)

# Fore.RED
# Fore.GREEN
# Fore.BLUE
# Fore.YELLOW
# Fore.MAGENTA
# Fore.CYAN
# Fore.WHITE
# Fore.BLACK
# Back Colors (cor de fundo)

# Back.RED
# Back.GREEN
# Back.BLUE
# Back.YELLOW
# Back.MAGENTA
# Back.CYAN
# Back.WHITE
# Back.BLACK
# Style

# Style.DIM (brilho reduzido)
# Style.NORMAL (estilo normal)
# Style.BRIGHT (negrito)

# Saída utilizando o método type() para verificar o tipo da variável
# print('\033[0m \033[31mTipos declarados:\033[0m')
# print('\033[0m A var \033[32m nome \033[0m é do tipo: ', type(nome))
# print('\033[0m A var \033[32m nascimento \033[0m é do tipo: ', type(nascimento))
# print('\033[0m A var \033[32m altura \033[0m é do tipo: ', type(altura))
# print('\033[0m A var \033[32m peso \033[0m é do tipo: ', type(peso))
# print('\033[0m A var \033[32m doador \033[0m é do tipo: ', type(doador))
# print('\033[0m A var \033[32m complexo \033[0m é do tipo: ', type(complexo))
# print('\033[0m A var \033[32m PI \033[0m é do tipo: ', type(PI))
