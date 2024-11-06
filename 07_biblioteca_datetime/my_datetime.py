# Importando as bibliotecas necessárias
import os
from datetime import datetime
from datetime import date

# Limpando o terminal
os.system('cls' if os.name == 'nt' else 'clear')

data_hora_formatada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
hora_h = datetime.now().time().hour
hora_m = datetime.now().time().minute
hora_s = datetime.now().time().second

data = datetime.now().date()
data_ano = datetime.now().date().year
data_mes = datetime.now().date().month
data_dia = datetime.now().date().day


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