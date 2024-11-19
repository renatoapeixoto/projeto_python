''' 3. Exercício de Nível Difícil : Números Perfeitos
Um número perfeito é aquele cuja soma dos divisores, excluindo o próprio número,
é igual ao próprio número. Por exemplo, o número 6 é perfeito, pois seus 
divisores (1, 2 e 3) somam 6. Escreva um programa que encontre e exiba todos 
os números perfeitos entre 1 e um valor fornecido pelo usuário. '''

import os 


os.system('cls' if os.name == 'nt' else 'clear')

tamanho = int(input('Digite o final do intervalo: '))
for i in range (2,tamanho+1):
    div = 0
    for j in range (1,i):
        if i % j == 0:
            div = div + j 
    if div == i:
        print(div, end='|')



exit()
###############################################################################
###############################################################################
# TESTAR SOMENTE UM NUMERO PERFEITO
# numeros_perfeito = []
# soma_divisores = 0
# num = int(input("Digite um número: "))
    
# for divisor in range(1, num): # soma dos divisores
#     if num % divisor == 0:
#         soma_divisores += divisor
    
# if soma_divisores == num :
#     numeros_perfeito.append(num) 
#     print(f'Numero perfeio: {numeros_perfeito}')
# else :
#     print('O numero não é perfeito')   
###############################################################################
###############################################################################
# TESTAR UM INTERVALO DE NUMERO PERFEITO
numeros_perfeito = []

limite = int(input("Digite um número: "))

for numeros in range (2,limite + 1 ) :    
    soma_divisores = 0
    for divisor in range(1, numeros): # soma dos divisores
        if numeros % divisor == 0:
            soma_divisores += divisor
    if soma_divisores == numeros :
        numeros_perfeito.append(numeros) 

tamanho = len(numeros_perfeito)
if tamanho > 0 :
    print(f'Numero perfeio: {numeros_perfeito}')
else :
    print('Não há número perfeito')   
###############################################################################
###############################################################################
