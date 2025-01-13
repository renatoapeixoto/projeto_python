# retorna uma copy rasa do dicionario
import os
os.system('cls')

# dicionario = chave:valor
dicionario = {'Qtd':'2', 1:[1,2,3], ('item'):(2),'usuario':{'nome':'Renato'},'idade':46 }
dicionario02 = {'a': 1}

''' Imutaveis - string , numeros e tuplas
    mutaveis - listas e dicionarios '''

dicionario_copy = dicionario.copy() # retorna uma copy rasa do dicionario
print('Dicionario_Original:',dicionario)
print('Dicionario_copy....:',dicionario_copy)
print()

dicionario_copy['Qtd'] = '3' # não altera o dicionario original 
dicionario_copy[1][2]= 10 # altera o dicionario original 
dicionario_copy[1].append(4) # inclui um elemento na lista , altera o original.
dicionario_copy['item'] = 4 # tupla não suporta atribuição ou alteração de itens, nesse caso será substituida a tupla pelo numero 4.
dicionario_copy['usuario']['nome'] = 'Nicolle' # chave usuario, valor: chave nome e valor nicolle
dicionario_copy['idade'] = 36 # Não altera o dicionario originanal
dicionario_copy.update(dicionario02) # quando adiciona não altera o original
dicionario_copy.setdefault('k',0) # quando adiciona não altera o original

print('# Imutaveis - string , numeros e tuplas. Mudanças na cópia, não altera os valores no dicionario original')
print('# mutaveis - listas e dicionarios. Mudanças na cópia, altera o dicionário original')
print('# Após algumas alterações no diciconario_copy verificar se alterou o dicionario original')
print(f'Dicionario_Original: {dicionario}')
print('Dicionario_copy....:',dicionario_copy)
#Após a mudança no diciconario_copy não alterou o original')
print()