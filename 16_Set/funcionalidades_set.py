import os


os.system('cls')
print('=' * 80)
print('APLICAÇÃO EM REMOÇÃO DE DADOS DUPLICADOS COM ESTRUTURA DE DADOS set{}')
print('-' * 80)
# Lista com elementos duplicados
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
print("Lista original...............:", lista_com_duplicatas)
# Usando set removendo duplicatas
set_sem_duplicatas = set(lista_com_duplicatas)
print("Set removendo duplicatas.....:", set_sem_duplicatas)
# Revomendo com set e tranformando em lista novamente.
lista_sem_duplicatas = list(set(lista_com_duplicatas))
print("Lista sem duplicatas.........:", lista_sem_duplicatas)
print('=' * 80)
print()

################################################################################
print('=' * 80)
print ('APLICAÇÃO NAS OPERAÇÕES EM CONJUNTOS DA ESTRUTURA DE DADOS set{}')
print('-' * 80)
# Definição de dois conjuntos
conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}
conjunto_C = {1, 2}
conjunto_D = {9, 10}
print(f'Conjunto A..................: {conjunto_A}')
print(f'Conjunto B..................: {conjunto_B}')
print(f'Conjunto C..................: {conjunto_C}')
print(f'Conjunto D..................: {conjunto_D}')
# União (elementos presentes em A ou B, pode ser de 2 formas.)
uniao = conjunto_A | conjunto_B
uniao = conjunto_A.union(conjunto_B)
print(f'União (A | B)...............: {uniao}')
# Interseção (elementos comuns entre A e B, pode ser de 2 formas.)
intersecao = conjunto_A & conjunto_B
intersecao = conjunto_A.intersection(conjunto_B)
print(f'Interseção (A & B)..........: {intersecao}')
# Diferença (elementos presentes em A, mas não em B, pode ser de 2 formas.)
diferenca_A_B = conjunto_A - conjunto_B
diferenca_A_B = conjunto_A.difference(conjunto_B)
print(f'Diferença (A - B)...........: {diferenca_A_B}')
# Diferença (elementos presentes em B, mas não em A, pode ser de 2 formas.)
diferenca_B_A = conjunto_B - conjunto_A
diferenca_B_A = conjunto_B.difference(conjunto_A)
print(f'Diferença (B - A)...........: {diferenca_B_A}')
# Diferença Simétrica (elementos presentes em A ou B, mas não em ambos, pode ser de 2 formas.)
diferenca_simetrica = conjunto_A ^ conjunto_B
diferenca_simetrica = conjunto_A.symmetric_difference(conjunto_B)
print(f'Diferença Simétrica (A ^ B).: {diferenca_simetrica}')
# Verificação de subconjuntos - Está contido.
esta_contido = conjunto_C.issubset(conjunto_A)
print(f'Conjunto_C é subconjunto(está contido) do Conjunto_A? {esta_contido}')
# Verificação de subconjuntos - Contém.
contem = conjunto_A.issuperset(conjunto_C)
print(f'Conjunto_A é superconjunto(contém) do conjunto_C? {contem}')
# Verificação de disjunção (Verifique se dois conjuntos se não há elementos em comum)
disjuncao = conjunto_A.isdisjoint(conjunto_D)
print(f'A e D são disjuntos? {disjuncao}')
print('=' * 80)
print()

################################################################################
import time
print('=' * 80)
print('BUSCA EFICIENTE COM A ESTRUTURA set{}')
print('-' * 80)
# Gerando um grande conjunto de números
grande_lista = list(range(1, 10**6))  # Lista com 1 milhão de elementos
grande_conjunto = set(grande_lista)   # Transformando a lista em um conjunto
print('Criamos um lista com 1.000.000 números e vamos procurar o número 999999')
# Elemento a ser buscado
elemento = 999999
# Busca na lista
print('-' * 43)
print('BUSCA NA LISTA')
inicio_lista = time.time()
print(f'Inicio da busca....: {inicio_lista}') # marca o tempo atual
resultado_lista = elemento in grande_lista # verifica de o numero está dentro da lista
fim_lista = time.time() # marca o tempo atual
print(f'Fim da busca.......: {fim_lista}')
tempo_lista = fim_lista - inicio_lista
print(f'Tempo da busca.....: {tempo_lista}')
print('-' * 43)
# Busca no conjunto, set{}
print('BUSCA NA ESTRUTURA set{}')
inicio_conjunto = time.time()
print(f'Inicio da busca....: {inicio_conjunto}')
resultado_conjunto = elemento in grande_conjunto
fim_conjunto = time.time()
print(f'Fim da busca.......: {fim_conjunto}')
tempo_conjunto = fim_conjunto - inicio_conjunto
print(f'Tempo da busca.....: {tempo_conjunto}')
print('-' * 43)
# Resultados
print(f"Busca na lista...: encontrado = {resultado_lista}, tempo = {tempo_lista:.6f} segundos")
print(f"Busca no conjunto: encontrado = {resultado_conjunto}, tempo = {tempo_conjunto:.6f} segundos")
# Comparação
if tempo_conjunto < tempo_lista:
    fator = tempo_lista / tempo_conjunto
    print(f'A busca no conjunto foi mais rápida {fator:.2f} vezes do que a lista')
else:
    fator = tempo_conjunto / tempo_lista
    print(f'A busca na lista foi mais rápida {fator} vezes (o que é incomum para'
           ' grandes coleções).')
print('=' * 80)
print()

################################################################################
print('=' * 80)
print('APLICAÇÃO EM REDES SOCIAIS COM A ESTRUTURA DE DADOS set{}')
print('-' * 80)
# Dados dos seguidores de dois usuários
seguidores_usuario_A = {"Alice", "Bob", "Charlie", "David"}
seguidores_usuario_B = {"Charlie", "David", "Edward", "Fiona"}
# Exibindo os dados iniciais
print("Seguidores do usuário A...................:", seguidores_usuario_A)
print("Seguidores do usuário B...................:", seguidores_usuario_B)
# Amigos em comum (interseção)
amigos_comuns = seguidores_usuario_A & seguidores_usuario_B
print("Amigos em comum (A ∩ B)...................:", amigos_comuns)
# Seguidores exclusivos de A (diferença)
seguidores_exclusivos_A = seguidores_usuario_A - seguidores_usuario_B
print("Seguidores exclusivos do usuário A (A - B):", seguidores_exclusivos_A)
# Seguidores exclusivos de B (diferença)
seguidores_exclusivos_B = seguidores_usuario_B - seguidores_usuario_A
print("Seguidores exclusivos do usuário B (B - A):", seguidores_exclusivos_B)
# Seguidores não compartilhados (diferença simétrica)
seguidores_nao_compartilhados = seguidores_usuario_A ^ seguidores_usuario_B
print("Seguidores não compartilhados (A ^ B).....:", seguidores_nao_compartilhados)
# Todos os seguidores únicos (união)
todos_seguidores = seguidores_usuario_A | seguidores_usuario_B
print("Todos os seguidores únicos (A ∪ B)........:", todos_seguidores)
print()



print('=' * 80)
# Listas de dados
dados_totais = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
usuarios_bloqueados = {"Charlie", "David"}  # Conjunto de exclusão
usuarios_prioritarios = {"Alice", "Eve"}   # Conjunto de inclusão prioritária

# Transformando os dados totais em um conjunto
dados_set = set(dados_totais)

# Filtrando dados - removendo usuários bloqueados
dados_filtrados = dados_set - usuarios_bloqueados
print("Dados após exclusão dos bloqueados:", dados_filtrados)

# Adicionando usuários prioritários (mesmo que não estivessem nos dados totais)
dados_com_prioritarios = dados_filtrados | usuarios_prioritarios
print("Dados com inclusão prioritária:", dados_com_prioritarios)

# Verificando se há usuários duplicados
print("Conjunto final (sem duplicados, automaticamente):", dados_com_prioritarios)

# Filtrando com base em uma condição adicional (por exemplo, nomes com mais de 4 caracteres)
dados_condicionais = {usuario for usuario in dados_com_prioritarios if len(usuario) > 4}
print("Dados filtrados por nomes com mais de 4 caracteres:", dados_condicionais)
