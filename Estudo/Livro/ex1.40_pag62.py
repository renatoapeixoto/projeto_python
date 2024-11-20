# Uma pesquisa sobre algumas características físicas da população de uma 
# determinada região coletou os seguintes dados, referentes a cada habitante, 
# para serem analisados:

# sexo (masculino, feminino);
# cor dos olhos (azuis, verdes, castanhos);
# cor dos cabelos (louros, castanhos, pretos);
# idade em anos.

# Para cada habitante, foi digitada uma linha com esses dados e a última linha, 
# que não corresponde a ninguém, conterá o valor de idade igual a -1.

# Fazer um algoritmo que determina e escreve:
# a) a maior idade dos habitantes;
# b) uma porcentagem de indivíduos do sexo feminino cuja idade esteja 
# entre 18 e 35 anos inclusive e que tenham olhos verdes e cabelos louros.
# c) Quantidade de Habitantes

#imports
from os import system
system('cls')

# Declaração
maior_idade = 0
total_feminina = 0.0
habitantes = 0
porc_Fem = 0.00
while True:
    print('-' * 80)
    idade = int(input('Digite a idade: '))
    if idade == -1 :
        break
    else:
        sexo = input('Digite o sexo, (M) ou (F): ')
        olhos = input('Digite cor dos olhos, (azuis, verdes, castanhos): ')
        cabelos = input('Digite a cor dos cabelos, (louros, castanhos, pretos): ')
        if idade > maior_idade :
            maior_idade = idade
        if (sexo == 'F') and (idade >= 18 and idade <= 35) and (olhos == 'verdes') and (cabelos == 'louros'):
            total_feminina = total_feminina + 1
        habitantes = habitantes + 1
    if idade > 0 :
        porc_Fem = (total_feminina / habitantes) * 100
print(f'A maior idade é: {maior_idade}')
print(f'Porcentagem de Habitantes Feminino com idade entre 18 e 35, olhos verdes'
      f' e cabelos louros são: {porc_Fem}')
print(f'Quantidade de Habitantes: {habitantes}')
print('-' * 80)