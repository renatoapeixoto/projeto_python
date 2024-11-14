# Crie um programa que pede que o usuário digite um nome ou uma frase, verifique 
# se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse 
# resultado.
import os


os.system('cls')

frase = input('Digite um nome ou uma frase :').replace(' ', '').lower()

n_frase = frase[ : :-1]
print(frase)
print(n_frase)

if frase == n_frase:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
