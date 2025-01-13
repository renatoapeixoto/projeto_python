# b) Crie um programa que permita ao usuário construir um dicionário contendo 5
# núcleos como chaves e seus respectivos valores, que podem ser específicos ou
# códigos de cor. O programa deve oferecer a possibilidade de adicionar novos 
# núcleos ou modificar o valor de uma cor já existente, caso o usuário deseje.
# Após a criação do dicionário, o programa deve exibir o dicionário de núcleos 
# ordenados alfabeticamente pelas chaves (cores) e, em seguida, gerar um 
# relatório que mostre a quantidade de núcleos que começam com cada letra do 
# alfabeto. O relatório deve ser apresentado de forma ordenada, exibindo quantos
# núcleos existem para cada inicial.

import os # para limpar a tela 
import msvcrt # gerar um pausa até que seja apertado uma tecla
import matplotlib.pyplot as plt # mostrar a cores, biblioteca usada para grafico

os.system('cls')

def mostrar_cor (valores):
    # Criar uma area de desenho com tamanho ajustado
    plt.subplots(figsize=(4, 2))  # Largura: 6, Altura: 3
    # Normalizar os valores para [0, 1]
    cor_rgb = (valores[0] / 255, valores[1] / 255, valores[2] / 255)
    # Mostrar a cor
    plt.imshow([[cor_rgb]])
    # adiciona um titulo
    plt.title(f"Cor: RGB({valores[0]}, {valores[1]}, {valores[2]}), fecha a janela p/ sair.")
    # remove os eixos do grafico
    plt.axis("off")
    # mostra o grafico
    plt.show()

def menu():
    print(
        'Digite uma opção:\n'
        '1 - criar cores\n'
        '2 - alterar cores\n'
        '3 - Relatório\n'
        '4 - mostrar cores na tela\n'

        'S - sair')
    
cores = {
    "vermelho": (255,0,0),
    "verde": (0,255,0),
    "azul": (0,0,255),
        }

print('DICIONÁRIO DE CORES "RGB" - vermelho, verde e azul')
print('-'*80)
print('Cores Básicas:')
for chave in cores:
    print(f'{chave} : {cores[chave]}')
print('Misture as cores para formar novas cores. ')

condicao = True
while condicao == True:
    
    print('-'*80)
    menu()
    print('-'*80)
    
    opcao = input("Digite o número da sua escolha: ").strip().lower()
    if opcao == '1' :
        try:
            chave = input('Digite o nome da cor que deseja criar: ')
            if chave == '':
                print('Você precisa digitar um valor, tente novamente, aperte uma tecla para continuar...')
                msvcrt.getch() # gera uma pausa até que seja apertado uma tecla
                continue
            print('Informe a proporção de vermelho, verde e azul para a nova cor.')
            vermelho = int(input(f'Digite a proporção de vermelho, um número de (0-255). '))
            verde = int(input(f'Digite a proporçõa de verde, um número de (0-255). '))
            azul = int(input(f'Digite a proporção de azul, um número de (0-255). '))
            
            if 0 <= vermelho <= 255 and 0 <= verde <= 255 and 0 <= azul <= 255:
                valores = (vermelho,verde,azul) 
                cores.update({chave:valores}) # atualiza um dicionario, se a chave existir, sobrepõe
                mostrar_cor(valores)
                print('Incluído com sucesso, aperte uma tecla para continuar...')
                msvcrt.getch()
            else:
                print('Verifique os valores e tente novamente, aperte uma tecla para continuar...')
                msvcrt.getch()
        except:
            print('Erro, Verifique os valores, tente novamente, aperte uma tecla para continuar...')
            msvcrt.getch()

    elif opcao == '2' :
        try:
            for chave, valor in sorted(cores.items()):
                print(f'{chave}:{valor}')
            print('-'*80)
            chave = input('Digite a cor que deseja alterar: ')
            if chave == '':
                print('Você precisa digitar um valor, tente novamente, aperte uma tecla para continuar...')
                msvcrt.getch() # gera uma pausa até que seja apertado uma tecla
                continue
            vermelho = int(input(f'Digite quantidade de vermelho, um número de (0-255). '))
            verde = int(input(f'Digite quantidade de verde, um número de (0-255). '))
            azul = int(input(f'Digite quantidade de azul, um número de (0-255). '))
            
            if 0 <= vermelho <= 255 and 0 <= verde <= 255 and 0 <= azul <= 255:
                valores = (vermelho,verde,azul) 
                cores.update({chave:valores}) # atualiza um dicionario, se a chave existir, sobrepõe
                mostrar_cor(valores)
                print('Alterado com sucesso, aperte uma tecla para continuar...')
                msvcrt.getch()
            else:
                print('Verifique os valores e tente novamente, aperte uma tecla para continuar...')
                msvcrt.getch()
                continue
        except:
            print('Erro, Verifique os valores, tente novamente, aperte uma tecla para continuar...')
            msvcrt.getch()
            continue        

    elif opcao == '3':
        print('\nRelatório Cores Cadastradas:')
        for chave, valor in sorted(cores.items()):
            print(f'{chave}:{valor}')
        
        iniciais_contagem = {}
        for chave in sorted(cores.keys()):
            inicial = chave[0].upper()
            if not inicial in iniciais_contagem.keys():
                iniciais_contagem[inicial] = 1
            else:
                iniciais_contagem[inicial] += 1
        print('\nQuantas vezes aparece as iniciais das cores:')
        for chave, valor in sorted(iniciais_contagem.items()):
            print(f'{chave}:{valor}')
        print('\nAperte uma tecla para continuar...')
        msvcrt.getch()
    elif opcao == '4':
        for chave, valor in sorted(cores.items()):
            print(f'{chave}:{valor}')
        escolha = input('Digite o nome da cor para mostra na tela: ').strip()
        if escolha in cores:
            mostrar_cor(cores[escolha])
        else:
            print('Cor não encontrada, tente novamente')
    
    elif opcao == 's':
        print()
        condicao = False
    
    else:
        print('Escolha não encontrada, tente novamente, aperte uma tecla para continuar...')
        msvcrt.getch()
        