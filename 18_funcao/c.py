# Crie uma função que verifica se uma aluno(a) está cadastrado ou não em um dicionário. 
# Se estiver cadastrado, imprima o nome desse aluno e o resto dos seus dados. 
# O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.
import os
import platform


# Limpa a tela (no Windows)
if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')

cadastro = []
def cadastrar_aluno(nome=None, matricula=None, data_nascimento=None):
    while True:
        # Entrada de dados se os parâmetros não forem fornecidos, posso fazer um cadastro interativo o direto.
        if nome is None: #  Verifica se dois objetos apontam para o mesmo local na memória (ou seja, se são o mesmo objeto).
            nome = input('Digite o nome do aluno............: ')
        if matricula is None:
            matricula = input('Digite a matrícula do aluno.......: ')
        if data_nascimento is None:
            data_nascimento = input('Digite a data de nascimento do aluno...: ')
        
        # Cadastro dos dados
        aux = {'Nome': nome, 'Matricula': matricula, 'Data_nascimento': data_nascimento}
        cadastro.append(aux)
        print(f"Aluno {nome} cadastrado com sucesso!")
        
        # Deseja continuar?
        opcao = input('Deseja continuar cadastrando (S/N)? ').lower().strip()
        if opcao == 'n':
            break
        
        # Resetar os valores para novo cadastro
        nome, matricula, data_nascimento = None, None, None
    return cadastro    

def consultar_aluno(cadastro):
    print('\nConsulta de alunos')
    consultar = input('Digite o nome do aluno: ')
    
    for aluno in cadastro:
        if consultar.lower() == aluno['Nome'].lower():  # Comparação insensível a maiúsculas
            print(f"Aluno encontrado: {aluno}")
            return
    print('Aluno não cadastrado.')

def imprimir_aluno(cadastro):
    if not cadastro: # se o cadastro não tiver elementos 
        print("Nenhum aluno cadastrado.")
        return
    
    print("\nLista de Alunos Cadastrados:")
    for aluno in cadastro:
        nome = aluno['Nome']
        matricula = aluno['Matricula']
        data_nascimento = aluno['Data_nascimento']
        print(f'Aluno: {nome}, Matrícula: {matricula}, Data de Nascimento: {data_nascimento}')

# Executando o programa
resultado = cadastrar_aluno()  # Cadastro interativo
# cadastrar_aluno(nome='Renato', data_nascimento='01/08/1978', matricula='2510203')  # Cadastro direto

imprimir_aluno(resultado)
consultar_aluno(resultado)

