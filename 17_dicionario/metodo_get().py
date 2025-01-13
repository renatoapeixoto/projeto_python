import os
os.system('cls')

dicionario = dict.fromkeys(['a','b','c'],10)
print(dicionario)

# É utilizado para acessar um valor associado a uma chave.
# Procura uma chave e retorna o valor, caso não ache retorna um valor padrão, se o valor padrao 
# não for especificado retorna none.
busca = dicionario.get('a', 0)
print(busca)

busca = dicionario.get('g', 'não encontrado')
print(busca)

busca = dicionario.get('g')
print(busca)
