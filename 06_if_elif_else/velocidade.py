# C) A empresa "SafeDrive" está desenvolvendo um sistema de monitoramento de 
# velocidade para ajudar a promover a segurança nas estradas. Eles precisam de 
# um programa que permita aos usuários inserir a velocidade de um carro e, 
# em seguida, exibir na tela uma mensagem adequada com base na velocidade 
# fornecida. O objetivo principal é alertar os motoristas caso ultrapassem o 
# limite de velocidade de 60 km/h, incentivando-os a dirigir dentro dos limites 
# legais e, assim, reduzir o risco de acidentes.

#imports
import os
import winsound  # Parâmetros: frequência (em Hertz), duração (em milissegundos)

# limpa
os.system('cls')

# Entradas e declarações
velocidade = int(input('Digite a velocidade Km/h: '))
resultado = ''

# Processamento
if velocidade <= 60 :
    resultado = 'Você está dentro do intervalo de velocidade ideal, não\
 ultrapasse a velocidade de 60 km/h.'
else :
    resultado = 'Atenção !!! Acima da velocidade permitida.'
    winsound.Beep(1000, 900)  # Som de 1000 Hz por 500 ms

# Saida
print(resultado)