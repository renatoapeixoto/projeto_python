# Programa para criar e gerenciar um dicionário de núcleos sem funções

from collections import Counter

dicionario = {}
print("Bem-vindo ao programa de gestão de núcleos!")

# Entrada inicial de 5 núcleos
print("\nInsira os 5 núcleos iniciais e seus valores:")
for i in range(5):
    chave = input(f"Digite o nome do núcleo {i + 1}: ").strip()
    valor = input(f"Digite o valor associado ao núcleo '{chave}': ").strip()
    dicionario[chave] = valor

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar um novo núcleo")
    print("2. Modificar o valor de um núcleo existente")
    print("3. Exibir o dicionário ordenado e gerar relatório")
    print("4. Sair")

    escolha = input("Digite o número da sua escolha: ").strip()

    if escolha == "1":
        nova_chave = input("Digite o nome do novo núcleo: ").strip()
        if nova_chave in dicionario:
            print(f"O núcleo '{nova_chave}' já existe no dicionário.")
        else:
            novo_valor = input(f"Digite o valor associado ao núcleo '{nova_chave}': ").strip()
            dicionario[nova_chave] = novo_valor
            print(f"Núcleo '{nova_chave}' adicionado com sucesso!")

    elif escolha == "2":
        chave_existente = input("Digite o nome do núcleo que deseja modificar: ").strip()
        if chave_existente in dicionario:
            novo_valor = input(f"Digite o novo valor para o núcleo '{chave_existente}': ").strip()
            dicionario[chave_existente] = novo_valor
            print(f"Valor do núcleo '{chave_existente}' atualizado com sucesso!")
        else:
            print(f"O núcleo '{chave_existente}' não foi encontrado no dicionário.")

    elif escolha == "3":
        # Exibe o dicionário ordenado pelas chaves
        print("\nDicionário de núcleos ordenado alfabeticamente:")
        for chave in sorted(dicionario):
            print(f"{chave}: {dicionario[chave]}")
        
        '''
        # Gera o relatório
        # Gerar o relatório de núcleos por inicial
        iniciais_contagem = {}

        # Contar as iniciais manualmente
        for chave in dicionario.keys():
            inicial = chave[0].upper()  # Pega a inicial e a transforma em maiúscula
            if inicial in iniciais_contagem:
                iniciais_contagem[inicial] += 1  # Incrementa a contagem se já existir
            else:
                iniciais_contagem[inicial] = 1  # Cria a inicial no dicionário
       '''
       
        iniciais = [nucleo[0].upper() for nucleo in dicionario.keys()]
        contagem = Counter(iniciais)
        letras_ordenadas = sorted(contagem.keys())
       
       
       
        print("\nRelatório de núcleos por inicial:")
        for letra in letras_ordenadas:
            print(f"Letra '{letra}': {contagem[letra]} núcleos")

    elif escolha == "4":
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
