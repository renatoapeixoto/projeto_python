import os


os.system('cls')

velocidade = int(input('Entre com a velocidade do veículo: '))

print(f'O veículo está a {velocidade}km/h ')

if velocidade > 60:
    resposta = 'Você ultrapassou o limite de velocidade!'
else:
    resposta = 'Você está dentro do limite de velocidade!'

print(resposta)
print('-'*70)