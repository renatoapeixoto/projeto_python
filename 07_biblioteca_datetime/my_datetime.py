# Importando as bibliotecas necessárias
import os


import datetime 


# Limpando o terminal
os.system('cls' if os.name == 'nt' else 'clear')

print(f"Data atual no sistema: {datetime.date.today()}")

data_hora_formatada = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print('Data formatada: ', data_hora_formatada)

hora_h = datetime.datetime.now().time().hour
print('Hora: ', hora_h)

hora_m = datetime.datetime.now().time().minute
print('Minuto: ', hora_m)

hora_s = datetime.datetime.now().time().second
print('Segundo: ', hora_s)

data = datetime.datetime.now().date()
print('Data: ', data)

data_ano = datetime.datetime.now().date().year
print('Ano: ', data_ano)

data_mes = datetime.datetime.now().date().month
print('Mês: ', data_mes)

data_dia = datetime.datetime.now().date().day
print('Dia: ', data_dia)

# Obtendo a data e hora atuais
data_atual = datetime.datetime.now()
print('Data atual: ', data_atual)

# Formatando a data e a data/hora
data_formatada = data_atual.strftime("%d/%m/%Y")
data_hora_formatada = data_atual.strftime("%d/%m/%Y %H:%M")



# Exibindo a data e a data/hora formatadas
print(f'Data formatada: {data_formatada}')
print(f'Data e hora formatadas: {data_hora_formatada}')

# Definindo o ano de nascimento e calculando a idade
ano_nascimento = 1970
idade = datetime.date.today().year - ano_nascimento

# Imprimindo a data atual, ano de nascimento e idade
print('-' * 70)
print(f'Data atual no sistema: {datetime.date.today()}')
print(f'Ano de nascimento.........: {ano_nascimento}')
print(f'Ano atual.................: {datetime.date.today().year}')
print(f'Sua idade é...............: {idade} anos')
print('-' * 70)
