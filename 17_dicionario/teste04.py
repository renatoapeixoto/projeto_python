# Função que retorna o valor da chave "Filme"
def obter_filme(item):
    return item["Filme"]

# Lista de dicionários representando os filmes
lista_consulta = [
    {"Filme": "avatar", "Genero": "ação", "Duracao": "120 minutos", "Classificacao": "livre"},
    {"Filme": "matrix", "Genero": "ficção científica", "Duracao": "150 minutos", "Classificacao": "16 anos"},
    {"Filme": "interestelar", "Genero": "ficção científica", "Duracao": "169 minutos", "Classificacao": "livre"}
]

# Ordena a lista com base no título do filme (chave "Filme")
lista_consulta = sorted(lista_consulta, key=obter_filme)

# Imprime os itens ordenados
for item in lista_consulta:
    print(f'• Filme: {item["Filme"].title()} - Gênero: {item["Genero"].title()} - Duração: {item["Duracao"]} - Classificação: {item["Classificacao"].title()}')
