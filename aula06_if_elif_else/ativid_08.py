# H) A empresa "RootCalc" está desenvolvendo um software de cálculo de raízes de 
# equações quadráticas para auxiliar engenheiros e cientistas em suas análises e 
# projetos. Eles precisam de um programa que calcule as raízes da equação 
# quadrática 𝑥²−6𝑥+5 sem depender de funções ou métodos predefinidos, utilizando 
# apenas os conceitos e operações básicas aprendidos até o momento. Essas raízes
# são conhecidas como 𝑥’ = 5 e 𝑥’’ = 1, e o programa deve ser capaz de calcular 
# essas raízes de forma precisa, seguindo os princípios matemáticos fundamentais.

#imports
import os


#limpa a tela
os.system('cls')

# Título
print("-"*70)
print('Equação do segundo grau a.x² + b.x + c = 0')  
print("-"*70)

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

