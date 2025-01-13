import os
os.system('cls')

print(
'** INCLUSÃO NO DICIONÁRIO ** \n'
'dict.fromkeys()\n'
'atribuição direta\n'
'dicionario.update()\n'
'dicionario.setdefault()\n'
"dicionario = {**novos_itens, ** {'amarelo':'#00FG00'}}\n"
'novo_dicionario = dicionario | novos_itens\n''dicionario |= novos_itens'
)
print('-'*80)
print()

###############################################################################
# Permite criar um dicionario onde todas as chaves têm o mesmo valor inicial
chave = ['a', 'b', 'c']
valor = 0
dicionario = {} # cria dicionario vazio 
dicionario = dict.fromkeys(['a','b','c'], 0) # cria um dicionario com as chaves possuindo um valor padrão. 
dicioanrio = dict.fromkeys(chave, valor) # cria um dicionario com as chaves possuindo um valor padrão.

print('-'*80)
print("dict.fromkeys(['a','b','c'], 0) # cria um dicionario com as chaves possuindo um valor padrão.")
print(dicionario)
print()
###############################################################################
print('-'*80)
print('# 1. Usando a Sintaxe de Atribuição')
print('# A forma mais direta e comum: adicione ou atualize um elemento em um dicionário.')
print('dicionario["cor"] = "azul"')

dicionario = {}
dicionario["cor"] = "azul"

print(dicionario)
print('-'*80)
print()
# Saída: {'cor': 'azul'}
###############################################################################
print('-'*80)
print('# 2. Usando o Método update()')
print('# Permite adicionar pares de chave de valor ou atualizar chaves existentes.\n'
      '# se chave existir o valor será sobrescrito')
dicionario.clear()
dicionario['azul'] = '00000'
print(dicionario)

dicionario.update({"azul": "#0000FF"})
dicionario.update(amarelo="#FFFF00", roxo="#800080") # Também funciona com argumentos nomeados
dicionario02 = {"vermelho": "#FF0000"}
dicionario.update(dicionario02)

print(dicionario)
print('-'*80)
print()
###############################################################################
print('-'*80)
print('# 3. Usando setdefault()')
print('# Adiciona um valor para a chave somente se ela não existir no dicionário.')
print('Define um valor padrão para uma chave usando setdefault(). Se a chave') 
print('já existir no dicionário, retorna o valor existente; caso contrário, ')
print('adiciona a chave com o valor padrão fornecido.')
dicionario.clear()
dicionario['vermelho'] = "#123456"
print(dicionario)

dicionario.setdefault("vermelho", "#000CC")  # Não altera, não faz nada, pois 'vermelho' já existe
dicionario.setdefault("azul","#0000FF")  # Adiciona a chave 'azul' com um valor padrao, caso a chave não esteja no dicionario

print(dicionario)
print('-'*80)
print()
###############################################################################
print('-'*80)
print('# 4. Usando Compreensão de Dicionário')
print('# Permite combinar ou adicionar novos itens em um contexto mais avançado.')
print("# dicionario = {**dicionario, **novos_itens, **{'amarelo':'#00FG00'}")
dicionario.clear()
dicionario = {"vermelho": "#FF0000"}
print('dicionario:', dicionario)

novos_itens = {"azul": "#0000FF", "verde": "#00FF00"}
dicionario = {**dicionario, **novos_itens, **{'amarelo':'#00FG00'}} # recebe novos valores
# Saida : {'vermelho': '#FF0000', 'azul': '#0000FF', 'verde': '#00FF00', 'amarelo': '#00FG00'}
print('dicionario:', dicionario)
print('-'*80)
print()
# Saída: {'vermelho': '#FF0000', 'azul': '#0000FF', 'verde': '#00FF00'}
###############################################################################
print('-'*80)
print('# 5. Usando o Operador |(Python 3.9+)')
print('# Forma elegante e moderna para combinar dicionários')
print('# novo_dicionario = dicionario | novos_itens')
print('# dicionario |= novos_itens')
dicionario = {"vermelho": "#FF0000"}
print(dicionario)
novos_itens = {"azul": "#0000FF", "verde": "#00FF00"}
print(novos_itens)
# Cria um novo dicionário
novo_dicionario = dicionario | novos_itens
print(novo_dicionario)
# Saída: {'vermelho': '#FF0000', 'azul': '#0000FF', 'verde': '#00FF00'}
# Atualiza o dicionário existente
dicionario |= novos_itens
print(dicionario)
# Saída: {'vermelho': '#FF0000', 'azul': '#0000FF', 'verde': '#00FF00'}
print('-'*80)
print()
###############################################################################
