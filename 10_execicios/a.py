'''Faça um programa que receba um valor e mostre sua raiz quadrada. 
Para raízes que não são exatas, arredonde para cima ou para baixo. 
Faça a validação para números negativos, avisando ao usuário que o resultado 
será um número complexo.'''

import os 
import math
import cmath # numeros complexos


# Limpando o terminal
os.system('cls' if os.name == 'nt' else 'clear') # windonws cls, outros clear.

# Entrada
valor = float(input("Digite um valor para calcular a raiz quadrada: "))


if valor < 0:
        # Calcula a raiz quadrada como número complexo
        raiz = cmath.sqrt(valor)
        print(f"A raiz quadrada de {valor} é {raiz} (número complexo)")
else:
    # Calcula a raiz quadrada como número real
    raiz = math.sqrt(valor)
        
    # Verifica se a raiz é exata
    if raiz.is_integer():
        print(f"A raiz quadrada exata de {valor} é {raiz}")
    else:
         # Pergunta ao usuário se deseja arredondar para cima ou para baixo
        opcao = input(f"A raiz {raiz:.2f} não é exata. Deseja arredondar para cima" 
        "ou para baixo ou para o número mais próximo ? (Digite 'C' ou 'B' ou 'P'): ")
   
        if opcao == "C":
            raiz_arredondada = math.ceil(raiz)
            print(f"A raiz quadrada de {valor} é {raiz:.2f} arredondada para cima é {raiz_arredondada}")
        elif opcao == "B":
            raiz_arredondada = math.floor(raiz)
            print(f"A raiz quadrada de {valor} é {raiz:.2f} arredondada para baixo é {raiz_arredondada}")
        elif opcao == "P":
            raiz_arredondada = round(raiz)
            print(f"A raiz quadrada de {valor} é {raiz:.2f} arredondada para o mais próximo é {raiz_arredondada}")
        else:
            print("Opção inválida. Tente novamente com 'cima' ou 'baixo'.")

