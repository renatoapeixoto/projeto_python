# Desenvolva um programa que crie um dicionário contendo 5 ferramentas, onde o 
# nome de cada ferramenta será a chave e seu respectivo valor será uma descrição 
# ou especificação técnica dessa ferramenta (como tipo de uso, material, etc.). 
# O programa deve permitir que o usuário altere o valor de qualquer ferramenta 
# já inserida. Após a criação e possível modificação do dicionário, o programa 
# deve imprimir não apenas os valores de cada ferramenta, mas também a quantidade
# total de elementos presentes no dicionário. Em seguida, o programa deve listar 
# todas as ferramentas armazenadas, juntamente com suas descrições, ordenadas 
# alfabeticamente por nome, e, por fim, fornecer um relatório mostrando a 
# quantidade de ferramentas que têm mais de uma palavra no nome.


import os
os.system('cls')


# Criação do dicionário contendo 5 ferramentas
ferramentas = {
    "martelo": {
        "descrição": "Ferramenta usada para pregar e quebrar objetos",
        "material": "Aço e madeira",
        "utilidade": "Pregar pregos e quebrar materiais"
    },
    "chave de Fenda": {
        "descrição": "Ferramenta para apertar ou soltar parafusos",
        "material": "Aço e plástico",
        "utilidade": "Ajustar parafusos"
    },
    "alicate de pressao": {
        "descrição": "Ferramenta para segurar, cortar e dobrar",
        "material": "Aço carbono",
        "utilidade": "Segurar e cortar fios"
    },
    "serrote": {
        "descrição": "Ferramenta de corte com dentes afiados",
        "material": "Aço temperado",
        "utilidade": "Cortar madeira"
    },
    "furadeira": {
        "descrição": "Ferramenta elétrica para fazer furos",
        "material": "Aço e plástico",
        "utilidade": "Perfuração de superfícies"
    }
}

def menu():
    print ('MENU PRINCIPAL')
    print ('Opção 1 -  Exibir Ferramentas')
    print ('Opção 2 -  Incluir Ferramentas')
    print ('Opção 3 -  Altera Ferramentas')
    print ('Opção 4 -  Relatorio')
    print ('Opção 5 -  ❌ Sair')

# Usando .items() para ver as chaves principais e os subdicionários
def exibir_ferramenta():
    for ferramenta, detalhes in sorted(ferramentas.items()):
        print('-'*80)
        print(f"🔧 Ferramenta: {ferramenta}")
        for chave, valor in detalhes.items():
            print(f"{chave}: {valor}")
    print('-'*80)
    quantidade = len(ferramentas)
    print(f'O dicionário possui {quantidade} ferramentas.')
    print()

def alterar_ferramenta():
    print(f'Ferramentas Disponíveis:  {" - ".join(ferramentas.keys())}')
    ferramenta = input('Digite a ferramenta que deseha alterar: ')
    for chave, valor in ferramentas[ferramenta].items():
        print(f"    {chave}: {valor}")
    print()   
    if ferramenta in ferramentas:
        caracteristica = input('Digite qual característica que deseha alterar: ')
        if caracteristica in ferramentas[ferramenta]:
            nova_caracteristica = input('Digite a nova descrição: ')
            ferramentas[ferramenta][caracteristica] = nova_caracteristica
            print(f'{ferramenta} : {ferramentas[ferramenta]}')
            print()
        else:
            print('caracteristica não encontrada')
    else:
        print('ferramenta não encontrada')

def inclusao_ferramenta():
    ferramenta = input('Digite a Ferramenta: ')
    if not ferramenta in ferramentas:
        descricao = input('Digite a descrição: ')
        material = input('Digite o material: ')
        utilidade = input('Digite a utilidade: ')
        ferramentas.update({ferramenta:{'descricao':descricao,'material':material,'utilidade':utilidade}})
    else:
        print('ferramenta já cadastrada')
    print()

#def relatorio():
    

while True:
    menu()
    escolha = input('Digite sua escolha: ')
    if escolha == '1':
        exibir_ferramenta()
    elif escolha == '2':
        inclusao_ferramenta()
    elif escolha == '3':
        alterar_ferramenta()
    elif escolha == '4':
        #relatorio()
        for ferramenta in ferramentas:
            if len(ferramenta.split()) > 1: # separa as palavras da chave, se tiver mais de 1 palavra. 
                print(f'{ferramenta}') 
        print()    
    elif escolha == '5':
        exit()

# # Função para exibir as ferramentas e seus detalhes
# def exibir_ferramentas():
#     print("\nFerramentas armazenadas:")
#     for nome, detalhes in ferramentas.items():
#         print(f"\n🔧 {nome}:")
#         for chave, valor in detalhes.items():
#             print(f"  {chave}: {valor}")

# # Função para modificar uma ferramenta
# def alterar_ferramenta():
#     nome = input("\nDigite o nome da ferramenta que deseja alterar: ")
#     if nome in ferramentas:
#         print("\nEscolha o que deseja alterar:")
#         print("1 - Descrição")
#         print("2 - Material")
#         print("3 - Utilidade")
#         escolha = input("Digite o número da sua escolha: ")

#         if escolha == "1":
#             nova_descricao = input("Digite a nova descrição: ")
#             ferramentas[nome]["Descrição"] = nova_descricao
#         elif escolha == "2":
#             novo_material = input("Digite o novo material: ")
#             ferramentas[nome]["Material"] = novo_material
#         elif escolha == "3":
#             nova_utilidade = input("Digite a nova utilidade: ")
#             ferramentas[nome]["Utilidade"] = nova_utilidade
#         else:
#             print("Escolha inválida.")
#         print(f"\n🔄 Ferramenta '{nome}' atualizada com sucesso!")
#     else:
#         print("❌ Ferramenta não encontrada.")

# # Exibir as ferramentas inicialmente
# exibir_ferramentas()

# # Modificar uma ferramenta
# alterar_ferramenta()

# # Exibir as ferramentas após a modificação
# exibir_ferramentas()
