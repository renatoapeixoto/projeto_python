# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, 
# solicite ao usuário digitar uma letra. Caso a letra seja o “f" 
# finalize a aplicação. Do contrário, imprima novamente a mesma frase até que 
# o caractere “f" seja digitado.

import os


os.system('cls')

while True:
    print("Estou em looping")
    letra = input('Digite uma letra: ')
    if letra == 'f':
        break