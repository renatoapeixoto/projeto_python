# a) Faça um programa para criar um dicionário com pelo menos 4 elementos. O 
# programa deve permitir que o usuário insira as chaves e valores. As chaves 
# devem ser únicas, e o programa deve garantir isso. Após inserir todos os 
# elementos, o programa deve exibir o dicionário ordenado pelas chaves.

import os
os.system('cls')

print('-'*80)
print('Incluir pelo menos com 4 elementos no dicionario')
print('-'*80)

dicionario = dict()
dicionario02 = []
contador = 1
while contador <= 4:
    chave = input('Digite "s" para sair, ou digite chave: ').strip()
    if chave == 's' and contador < 4:
        print(f'Pelo menos você tem que digitar {4-contador} elemento no dicionário')
        continue
    elif chave == 's' and contador > 4:
        break
    elif chave == '':
        print('Você não digitou a chave, tente novamente.')
        continue
    elif chave in dicionario:
        print('chave repetida, tente novamente')
        continue
    
    valor = input('Digite Valor: ').strip()
    dicionario[chave] = valor
    contador += 1
    print(f'Dicionario: {dicionario}')

# # Ordenando e imprimindo o dicionário
# for chave in sorted(dicionario):
#     print(f"{chave}: {dicionario[chave]}")


# Ordenando o dicionário e criando um novo
# dicionario_ordenado = {chave:dicionario[chave] for chave in sorted(dicionario)}



for chave in sorted(dicionario):
    aux = {chave:dicionario[chave]}
    dicionario02.append(aux)
    print(dicionario02)


print(f'Dicionario: {dicionario}')
    
# print(f' {}')





