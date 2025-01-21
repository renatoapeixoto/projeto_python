import os
import platform

# Limpa a tela (no Windows)
if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')


# Definindo uma função para calcular a velocidade média
def calcular_velocidade_media(distancia, tempo):
    # Fórmula da velocidade média: Vm = ΔS/Δt
    velocidade_media = distancia / tempo
    return velocidade_media

# Entrada de dados do usuário
distancia = float(input("Digite a distância percorrida (em km): "))
tempo = float(input("Digite o tempo gasto (em horas): "))

# Calcular a velocidade média usando a função criada
velocidade = calcular_velocidade_media(distancia, tempo)

# Exibir o resultado formatado com 2 casas decimais
print(f"A velocidade média é {velocidade:.2f} km/h.")
