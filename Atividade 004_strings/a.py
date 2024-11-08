import os


os.system('cls')

print('-'*70)
print('PROGRAMA: NOME COMPLETO')
print('='*70)

primeiro_nome = str(input('Digite seu primeiro nome: '))
segundo_nome = str(input('Digite seu segundo nome: '))
sobrenome = str(input('Digite seu sobrenome: '))

nome_completo = primeiro_nome + ' ' + segundo_nome + ' ' + sobrenome

print('-'*70)
print(f'Nome completo: {nome_completo}')
print('='*70)