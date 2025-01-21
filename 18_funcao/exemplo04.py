import os

os.system('cls')  # Limpa a tela (Windows)

# Definindo a função para calcular a velocidade média
def calcular_vm_media(espaco, tempo, espaço_km_metros, tempo_hora_minuto):
    # Convertendo a distância para quilômetros
    # se a unidade for metros (1 km = 1000 m)
    if espaço_km_metros == 'metros':
        espaco = espaco / 1000

    # Convertendo o tempo para horas
    # se a unidade for minutos (1 hora = 60 minutos)
    if tempo_hora_minuto == 'minutos':
        tempo = tempo / 60

    vm_media = espaco / tempo
    return vm_media

# Entrada de dados do usuário
espaco = float(input("Digite a distância percorrida: "))
espaço_km_metros = input("A distância é em Km ou metros? ").lower()
tempo = float(input("Digite o tempo gasto: "))
tempo_hora_minuto = input("O tempo é em horas ou minutos? ").lower()

# Invocando a função
vm = calcular_vm_media(espaco, tempo, espaço_km_metros, tempo_hora_minuto)

# Exibir o resultado
print(f"A velocidade média é {vm:.2f} {espaço_km_metros}/{tempo_hora_minuto}.")
