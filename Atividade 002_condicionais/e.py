import os


os.system('cls')

distancia = float(input('Qual a distância da viagem? '))

print(f'Distância da viagem {distancia}km')

if distancia <= 200:
    print('O custo dessa viagem será de R$0,70 por Km rodado!')
    valor_passagem = distancia * 0.7
elif distancia > 200:
    print('O custo dessa viagem será de R$0,40 por Km rodado!')
    valor_passagem = distancia * 0.4
else:
    print('Valor inválido!')

print(f'Valor à pagar: R${valor_passagem}')
print('-'*70)