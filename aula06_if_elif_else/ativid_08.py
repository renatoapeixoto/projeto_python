
#imports
import os


#limpa a tela
os.system('cls')

# Título
print('Equação do segundo grau ax² + bx + c = 0')  

# Entradas e Declarações
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
delta = 0.0
x1 = 0.0
x2 = 0.0
raiz = 0.0

# Processamento
delta = b**2 - 4 * a * c
raiz = (delta ** (1/2))
if delta > 0:
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
if delta == 0:
    x1 = -b / (2 * a)

# Saida 
if delta > 0 :
    print(f'A raiz x1 é: {x1}')    
    print(f'A raiz x2 é: {x2}')    
elif delta == 0 :
    print(f'A raiz x1 é: {x1}')    
else :
    print('A equação não possui raízes reais')
print()

