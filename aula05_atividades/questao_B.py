#--------------------------------------------------------------------------------
#Crie um programa que pergunte o ano de nascimento do usuário 
#e calcule sua idade atual.  
#--------------------------------------------------------------------------------

# imports
import os
from datetime import datetime

#limpar a tela
os.system('cls')

# Solicita o ano de nascimento do usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Obtém o ano atual
ano_atual = datetime.now().year

# Calcula a idade
idade = ano_atual - ano_nascimento

# Exibe a idade do usuário
print("-" * 70)
print(f"Sua idade atual é: {idade} anos.")
print("-" * 70)