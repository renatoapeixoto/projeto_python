# C) A empresa "SafeDrive" está desenvolvendo um sistema de monitoramento de 
# velocidade para ajudar a promover a segurança nas estradas. Eles precisam de 
# um programa que permita aos usuários inserir a velocidade de um carro e, 
# em seguida, exibir na tela uma mensagem adequada com base na velocidade 
# fornecida. O objetivo principal é alertar os motoristas caso ultrapassem o 
# limite de velocidade de 60 km/h, incentivando-os a dirigir dentro dos limites 
# legais e, assim, reduzir o risco de acidentes.

import os


# limpa
os.system('cls')

# Entradas
velocidade = int(input('Digite a velocidade Km/h: '))

# Processamento
if velocidade <= 60 :
    print('Continue assim, você está na velocidade ideal,' end=()
          não ultrapasse a velocidade de 60 km/h.')