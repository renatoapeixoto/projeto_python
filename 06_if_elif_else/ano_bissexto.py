# F) A empresa "LeapYearCheck" está desenvolvendo um software de verificação de
# anos bissextos para auxiliar usuários na identificação desses anos de forma 
# rápida e precisa. Eles precisam de um programa que permita aos usuários inserir
# um ano e, em seguida, determine se esse ano é bissexto ou não, de acordo com as
# regras estabelecidas pelo calendário gregoriano. Além disso, é necessário
# realizar a validação de entrada de dados para garantir que o ano inserido 
# pelo usuário seja um valor válido, ou seja, um número inteiro positivo.

# imports
import os

# limpa tela
os.system('cls')

# Entradas e declarações
ano = int(input('Digite um ano: '))
resultado = ''

#Função ano bissexto
# def eh_bissexto(ano):
#     return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
# print(eh_bissexto(2020))  # Saída: True
# print(eh_bissexto(1900))  # Saída: False

# Processamento 01
# if ano < 1582 :
#     print('Não está dentro do período do calendário gregoriano')
# elif (ano % 100) == 0 and (ano % 400) == 0 :
#     resultado = 'ano bissexto'
# elif (ano % 100) == 0 :
#     resultado = 'ano comum'
# elif (ano % 4) == 0 :
#     resultado = 'ano bissexto'
# else:
#     resultado = 'ano comum'

# Processamento 02
# if ano > 1581 :
#      if ano % 4 == 0 :
#          if (ano % 100)  == 0 :
#              if (ano % 400) == 0  :    
#                  resultado = "Ano bissexto"
#              else :
#                  resultado = "Ano comum"
#          else:
#              resultado = "Ano bissexto"
#      else :
#           resultado = "Ano comum"
# else :
#     resultado = "Não está dentro do período do calendário gregoriano"

# Processamento 03
if ano < 1582:
 resultado = "Não dentro do período do calendário gregoriano"
else:
   if (ano % 4) != 0:
     resultado = "ano comum"
   elif (ano % 100) != 0:
     resultado = "Ano bissexto"
   elif (ano % 400) != 0:
     resultado = "ano comum"
   else:
     resultado = "Ano bissexto"

# Saida
print(resultado)
print()
