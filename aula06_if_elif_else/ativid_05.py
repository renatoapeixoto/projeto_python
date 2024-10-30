# E) A empresa "TravelCalc" está desenvolvendo um sistema de cálculo de preços de 
# passagens de ônibus com base na distância da viagem. Eles precisam de um 
# programa que solicite ao usuário a distância a desejada e, em seguida, calcule 
# o preço da passagem de acordo com as políticas da empresa. Segundo essas 
# políticas, viagens de até 200 km têm um custo de R$0,70 por km rodado, enquanto
# viagens acima dessa distância passam a custar R$0,40 por km rodado.

# imports
import os

# limpa tela
os.system('cls')

# Entradas e declarações
preco_passagem = 0.0 
distancia = float(input('Digite a distancia da viagem em Km : '))

# Processamento
if distancia < 200 :
    preco_passagem = distancia * 0.70
else :
    preco_passagem = distancia * 0.40

# Saida
print(f'O valor da passagem é R$: {preco_passagem}')
print()