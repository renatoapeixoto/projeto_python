import os

os.system('cls')  # Limpa a tela (no Windows)

meu_dicionario = {}

while True:
    print('-' * 70)
    print("Menu de opções:")
    print("1. Adicionar um par chave-valor")
    print("2. Definir valor padrão para uma chave usando setdefault()")
    print("3. Atualizar o dicionário usando update()")
    print("4. Mostrar dicionário atual")
    print("5. Sair")
    print('-' * 70)

    opcao = input("Escolha uma opção (1-5): ")

    if opcao == '1':
        # Adicionar um par chave-valor ao dicionário
        chave = input("Digite a chave: ")
        valor = input("Digite o valor: ")
        meu_dicionario[chave] = valor
        print(f"Par {{chave: {chave}, valor: {valor}}} adicionado.")
    elif opcao == '2':
        # Definir valor padrão para uma chave usando setdefault()
        chave = input("Digite a chave para definir um valor padrão: ")
        valor_padrao = input("Digite o valor padrão: ")
        valor_existente = meu_dicionario.setdefault(chave, valor_padrao)
        print(f"Valor para a chave '{chave}': {valor_existente}")

    elif opcao == '3':
        # Atualizar o dicionário usando update()
        # novos pares chave-valor no formato: chave1:valor1,chave2:valor2
        novos_pares = input("Digite os novos pares chave-valor "
                            "no formato chave1:valor1,chave2:valor2: ")
        novos_pares_lista = novos_pares.split(',')
        novos_dados = {}
        for par in novos_pares_lista:
            chave, valor = par.split(':') # unpack
            novos_dados[chave] = valor
        meu_dicionario.update(novos_dados)
        print("Dicionário atualizado:", meu_dicionario)

    elif opcao == '4':
        # Mostrar o dicionário atual
        if meu_dicionario:
            print("Dicionário atual:", meu_dicionario)
        else:
            print("O dicionário está vazio.")

    elif opcao == '5':
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
