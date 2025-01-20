import os

os.system('cls')

# Definindo a função
def dados_paciente(nome='Coly', nascimento=2005, peso=46, altura=1.68):
    print(f'Bem-vindo(a) ao sistema Senac, {nome}!')
    print(f'O ano de nascimento da {nome} é {nascimento}.')
    print(f'O peso da {nome} é {peso}Kg.')
    print(f'A altura da {nome} é {altura}m.')
    print('-'*70)

# Início - Para lembrar
def posicional_nomeado(nascimento, nome='Coly'):  # Ok! Funciona!!!
    print(f'Bem-vindo(a) ao sistema Senac, {nome}!')
    print(f'O ano de nascimento da {nome} é {nascimento}.')
    print('-'*70)


# No programa abaixo tem um erro, voce pode colocar os parametros da sequinte forma:
# valor posicional e nomeado -> correto
# valor posicional  -> correto 
# valor nomeado e posicional -> errado
# valor nomeado -> correto   

# def nomeado_posicional(nome='Coly', nascimento):  # Not Ok! Não Funciona!!! -  O valor nomeado veio primeiro que o posicional
#     print(f'Bem-vindo(a) ao sistema Senac, {nome}!')
#     print(f'O ano de nascimento da {nome} é {nascimento}.')
#     print('-'*70)

# Fim - Para lembrar

# Invocando a função
dados_paciente()
posicional_nomeado(1978)

dados_paciente(nome='Isis', nascimento=1985, peso=46, altura=1.56)
dados_paciente(nascimento=2008, nome='Ágata', peso=46, altura=1.58)
dados_paciente(altura=1.66, peso=46, nome='Bia', nascimento=2008)
