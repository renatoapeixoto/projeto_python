# Importando as bibliotecas necessárias
import os
from datetime import datetime, date

# Limpando o terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Obtendo a data e hora atuais
data_atual = datetime.now()

# Formatando a data e a data/hora
data_formatada = data_atual.strftime("%d/%m/%Y")
data_hora_formatada = data_atual.strftime("%d/%m/%Y %H:%M")

# Exibindo a data e a data/hora formatadas
print(f'Data formatada: {data_formatada}')
print(f'Data e hora formatadas: {data_hora_formatada}')

# Definindo o ano de nascimento e calculando a idade
ano_nascimento = 1970
idade = date.today().year - ano_nascimento

# Imprimindo a data atual, ano de nascimento e idade
print('-' * 70)
print(f'Data atual no sistema: {date.today()}')
print(f'Ano de nascimento.........: {ano_nascimento}')
print(f'Ano atual.................: {date.today().year}')
print(f'Sua idade é...............: {idade} anos')
print('-' * 70)