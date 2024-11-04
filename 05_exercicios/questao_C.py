#--------------------------------------------------------------------------------
#Elabore um programa que receba quatro notas de 
#um aluno e calcule a média dessas notas.
#--------------------------------------------------------------------------------

# imports
import os

#limpar a tela
os.system('cls')

# Entrada
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4ª nota: '))

# Processamento
soma = nota1 + nota2 + nota3 + nota4
media = soma / 4  # Média correta

# Saída
print()
print('--- MEDIA ---')
print(f'Nota 1: {nota1} | Nota 2: {nota2} | Nota 3: {nota3} | Nota 4: {nota4} | A sua media é.: {media}')
print('-'*79)


