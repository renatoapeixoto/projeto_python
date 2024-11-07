import os


os.system('cls')

print('VERIFICANDO PAR OU ÍMPAR')
print('-'*70)

# Entrada de dados
numero = int(input('Entre com um número inteiro: '))

if numero % 2 == 0:
  resposta = f'O número {numero} é par!'
else:
    resposta = f'O número {numero} é ímpar!'

print(resposta)
print('Fim do programa!\n')
