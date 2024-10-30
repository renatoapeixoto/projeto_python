# G) Você está desenvolvendo um programa para determinar se três segmentos podem
# formar um triângulo. Para isso, o programa precisa receber as medidas dos três
# segmentos e compará-las entre si. A resposta resultante dessa comparação deve 
# indicar se os segmentos fornecidos podem formar um triângulo ou não.

#imports
import os


#limpa a tela
os.system('cls')

# Título
print('Verificar se os segmentos formam um triangulo')  

# Entradas e Declarações
a = float(input('Digite o segmento < a > do triângulo: '))
b = float(input('Digite o segmento < b > do triângulo: '))
c = float(input('Digite o segmento < c > do triângulo: '))

# Processamento
if (a+b)>c and (a+c)>b and (b+c)>a :
    resultado = 'É um triangulo'
else :
    resultado = 'Não é um triangulo'

# Saidas
print(resultado)
