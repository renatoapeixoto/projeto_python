import os
import platform


if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')


def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).

    Parâmetros:
        peso (float): Peso da pessoa em quilogramas (kg).
        altura (float): Altura da pessoa em metros (m).

    Retorna:
        float: O valor do IMC arredondado para 2 casas decimais.
    """
    imc = peso / (altura ** 2)
    
    if imc > 30 :
        classificacao = 'Obesidade'
    elif imc > 25:
        classificacao = 'Sobrepeso'
    elif imc > 18.5:
        classificacao = 'Normal'
    else:
        classificacao = 'Abaixo dio peso'

    return imc , classificacao  # Retorna o IMC arredondado para 2 casas decimais



# Exemplo de uso
peso = float(input('Dgite o seu peso em kg: '))  # Peso em kg
altura = float(input('Digite sua altura: ')) # Altura em metros


imc, classificacao = calcular_imc(peso, altura)

print(f"O IMC para peso {peso:.2f}kg e altura {altura:.2f}m é {imc:.2f} classificado como {classificacao}.")
