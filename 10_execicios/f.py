import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

# O computador "pensa" em um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Titulo
print('-' * 80)
print("Bem-vindo ao jogo de adivinhação!")
print("O computador pensou em um número entre 1 e 10. Tente adivinhar!")
print('-' * 80)

# Solicita um palpite do usuário
palpite = int(input("Digite seu palpite: "))

# Verifica se o palpite está correto, abaixo ou acima
if palpite != numero_secreto:
    print(f'Errouuuuuuuuuuuuuuu !!!!!!!!! O numero secreto é : {numero_secreto}')
else:
    print(f'Parabéns! Você ganhou o jogo, O numero secreto é : {numero_secreto}')
print('-' * 80)      
 
    
