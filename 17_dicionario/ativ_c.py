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
    "Martelo": {
        "Descrição": "Ferramenta usada para pregar e quebrar objetos",
        "Material": "Aço e madeira",
        "Utilidade": "Pregar pregos e quebrar materiais"
    },
    "Chave de Fenda": {
        "Descrição": "Ferramenta para apertar ou soltar parafusos",
        "Material": "Aço e plástico",
        "Utilidade": "Ajustar parafusos"
    },
    "Alicate": {
        "Descrição": "Ferramenta para segurar, cortar e dobrar",
        "Material": "Aço carbono",
        "Utilidade": "Segurar e cortar fios"
    },
    "Serrote": {
        "Descrição": "Ferramenta de corte com dentes afiados",
        "Material": "Aço temperado",
        "Utilidade": "Cortar madeira"
    },
    "Furadeira": {
        "Descrição": "Ferramenta elétrica para fazer furos",
        "Material": "Aço e plástico",
        "Utilidade": "Perfuração de superfícies"
    }
}

# Usando .items() para ver as chaves principais e os subdicionários
for ferramenta, detalhes in ferramentas.items():
    print(f"Ferramenta: {ferramenta}")
    for chave, valor in detalhes.items():
        print(f"{chave}:{valor}")
    print()
exit()






# Função para exibir as ferramentas e seus detalhes
def exibir_ferramentas():
    print("\nFerramentas armazenadas:")
    for nome, detalhes in ferramentas.items():
        print(f"\n🔧 {nome}:")
        for chave, valor in detalhes.items():
            print(f"  {chave}: {valor}")

# Função para modificar uma ferramenta
def alterar_ferramenta():
    nome = input("\nDigite o nome da ferramenta que deseja alterar: ")
    if nome in ferramentas:
        print("\nEscolha o que deseja alterar:")
        print("1 - Descrição")
        print("2 - Material")
        print("3 - Utilidade")
        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            nova_descricao = input("Digite a nova descrição: ")
            ferramentas[nome]["Descrição"] = nova_descricao
        elif escolha == "2":
            novo_material = input("Digite o novo material: ")
            ferramentas[nome]["Material"] = novo_material
        elif escolha == "3":
            nova_utilidade = input("Digite a nova utilidade: ")
            ferramentas[nome]["Utilidade"] = nova_utilidade
        else:
            print("Escolha inválida.")
        print(f"\n🔄 Ferramenta '{nome}' atualizada com sucesso!")
    else:
        print("❌ Ferramenta não encontrada.")

# Exibir as ferramentas inicialmente
exibir_ferramentas()

# Modificar uma ferramenta
alterar_ferramenta()

# Exibir as ferramentas após a modificação
exibir_ferramentas()
