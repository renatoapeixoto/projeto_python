# Faça um programa que verifique se o usuário e senha estão inseridos em um banco
# de dados (fake). O usuário só terá acesso se digitar os dados corretos e, assim,
# sair do laço.
import os


os.system('cls')

usuario = 'peixoto.sd@gmail.com'
senha = '010878'

while True:
    n_usuario = input('Digie seu email : ')
    n_senha = input('Digie sua senha: ')
    if senha == n_senha and n_usuario == usuario:
        break
    else:
        print('Digie novamente, dados incorretos.')