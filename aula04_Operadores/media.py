# imports
import os

os.system('cls')

print('-'*70)
print('Operadores Aritméticos: Ordem de Precedência')
print('-'*70)

# Entrada
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4ª nota: '))

# Processamento
media = nota1 + nota2 + nota3 + nota4 / 4  # Média incorreta para demonstrar erro
media_correta = (nota1 + nota2 + nota3 + nota4) / 4  # Média correta

# Saída
print()
print('---- Notas --------------')
print(f'Nota 1: {nota1} | Nota 2: {nota2} Nota 3: {nota3} Nota 4: {nota4}')
print('-'*70)
print(f'Média errada: {media}')
print(f'Média correta: {media_correta}')
print('-'*70)
print()
