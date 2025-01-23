# Crie uma função que cadastre o nome de um aluno(a), a matrícula e a data de nascimento. 
# Depois imprima os resultados cadastrados utilizando uma estrutura de repetição for.


def cadastrar_aluno(nome=None, matricula=None, data_nascimento=None):
    cadastro = []
    while True:
        # Entrada de dados
        nome = input('Digite o nome do aluno............: ')
        matricula = input('Digite a matrícula do aluno.......: ')
        data_nascimento = input('Digite a data de nascimento do aluno...: ')
        
        # Cadastro dos dados
        aux = {'Nome': nome, 'Matricula': matricula, 'Data_nascimento': data_nascimento}
        cadastro.append(aux)
        
        # Deseja Continuar
        opcao = input('Deseja continuar (S/N)? ').lower().strip()
        if opcao == 'n':
            break
    return cadastro    

def imprimir_aluno(cadastro):
    print("\nLista de Alunos Cadastrados:")
    for aluno in cadastro:
        nome = aluno['Nome']
        matricula = aluno['Matricula']
        data_nascimento = aluno['Data_nascimento']
        print(f'Aluno: {nome}, Matrícula: {matricula}, Data de Nascimento: {data_nascimento}')

# Executando o programa
resultado = cadastrar_aluno()
imprimir_aluno(resultado)
