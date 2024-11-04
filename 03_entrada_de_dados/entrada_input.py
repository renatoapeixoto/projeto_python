# limpar tela 
import os
os.system('cls')

from colorama import Fore, Back, Style, init
init(autoreset=True)

print(Fore.MAGENTA +'-' * 70)
print(Fore.YELLOW + 'ENTRADA DE DADOS')
print(Fore.MAGENTA + '=' * 70)

nome = input(Fore.BLUE +'Entre com o Nome....: ')
nascimento = (input(Fore.BLUE + 'Data de Nascimento..: '))
peso = float(input(Fore.BLUE + 'Entre com o Peso....: '))
Altura = float(input(Fore.BLUE + 'Entre com a Altura..: '))


print(Fore.MAGENTA + '-' * 70)
print(Fore.YELLOW + 'SAIDA DE DADOS')
print(Fore.MAGENTA + '=' * 70)

print(Fore.BLUE + "Nome................: ", Fore.BLUE + nome)
print(Fore.BLUE + "Data de Nascimento..: ", Fore.BLUE + nascimento)
print(Fore.BLUE + "Peso................: ", Fore.BLUE + str(peso))
print(Fore.BLUE + "Altura..............: ", Fore.BLUE + str(Altura))

