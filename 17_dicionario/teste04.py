# Função para cadastrar filmes
def cadastrar_filmes():
    filmes = []
    
    for i in range(5):
        print(f"\nCadastro do {i + 1}º filme:")
        titulo = input("Título: ").strip()
        genero = input("Gênero: ").strip()
        duracao = float(input("Duração (em horas): "))
        classificacao = input("Classificação indicativa: ").strip()
        
        filme = {
            "Título": titulo,
            "Gênero": genero,
            "Duração": duracao,
            "Classificação": classificacao
        }
        filmes.append(filme)
    
    return filmes

# Função para alterar informações de um filme
def alterar_filme(filmes):
    titulo_alterar = input("\nDigite o título do filme que deseja alterar: ").strip()
    for filme in filmes:
        if filme["Título"].lower() == titulo_alterar.lower():
            print("\nFilme encontrado. Digite as novas informações:")
            filme["Título"] = input("Novo título: ").strip()
            filme["Gênero"] = input("Novo gênero: ").strip()
            filme["Duração"] = float(input("Nova duração (em horas): "))
            filme["Classificação"] = input("Nova classificação indicativa: ").strip()
            print("\nFilme alterado com sucesso!")
            return
    print("\nFilme não encontrado.")

# Função para listar filmes ordenados por título
def listar_filmes(filmes):
    filmes_ordenados = sorted(filmes, key=lambda x: x["Título"])
    print("\nLista de filmes cadastrados (ordenados por título):")
    for filme in filmes_ordenados:
        print(f"\nTítulo: {filme['Título']}")
        print(f"Gênero: {filme['Gênero']}")
        print(f"Duração: {filme['Duração']} horas")
        print(f"Classificação: {filme['Classificação']}")

# Função para gerar relatório
def gerar_relatorio(filmes):
    duracao_maior_2h = sum(1 for filme in filmes if filme["Duração"] > 2)
    classificacao_livre = sum(1 for filme in filmes if filme["Classificação"].lower() == "livre")
    
    print("\nRelatório:")
    print(f"Filmes com duração superior a 2 horas: {duracao_maior_2h}")
    print(f"Filmes com classificação indicativa 'Livre': {classificacao_livre}")

# Programa principal
def main():
    filmes = cadastrar_filmes()
    
    while True:
        print("\nOpções:")
        print("1. Alterar informações de um filme")
        print("2. Listar filmes cadastrados")
        print("3. Gerar relatório")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            alterar_filme(filmes)
        elif opcao == "2":
            listar_filmes(filmes)
        elif opcao == "3":
            gerar_relatorio(filmes)
        elif opcao == "4":
            print("\nSaindo do programa...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

# Executa o programa principal
main()
