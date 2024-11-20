# 1. Exercício de Nível Médio : Verifique se um número é um número especial
# Escreva um programa que receba um número inteiro do usuário e verifique se ele
#  é um "número especial". Um número é considerado especial se for maior que 1, 
# divisível por 3, mas não por 2 e 5. Se for especial, imprima "Número Especial!". 
# Caso contrário, imprima "Número não especial".

import os
os.system("cls")

numero = int(input("Digite um número inteiro: "))

if numero > 1 and numero % 3 == 0 and numero % 2 != 0 and numero % 5 != 0:
    print("Número Especial!")
else:
    print("Número não especial")
