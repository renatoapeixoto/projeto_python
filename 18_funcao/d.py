# Crie uma função que receba uma temperatura em fahrenheit e retorne o valor em graus célsius.
import os
import platform


# Limpa a tela (no Windows)
if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')


def fahrenheit_para_celsius(fahrenheit):
    # Docstring (Comentários de Documentação)
    """
    Converte a temperatura de Fahrenheit para Celsius.

    Parâmetros:
        fahrenheit (float): Temperatura em Fahrenheit.

    Retorna:
        float: Temperatura equivalente em Celsius.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Exemplo de uso
temperatura_fahrenheit = float(input('Digite o grau em Fahrenheit para transformar em celsius: '))
temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit}°F é equivalente a {temperatura_celsius:.2f}°C.")



