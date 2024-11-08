import math
import os


os.system('cls' if os.name == 'nt' else 'clear')

print('-------------------------------------------------------------------------')
# Sinal de Mais (+) -> Serve para concatenar strings
usuario = 'peixoto.sd'
servidor = 'gmail.com'
print(usuario + '@' + servidor)
# saida -> peixoto.sd@gmail.com
print('-------------------------------------------------------------------------')

# str() -> transforma o valor em string
faturamento = 1000
print('O faturamento da loja foi de ' + str(faturamento))
#saida -> peixoto.sd@gmail.com
print('-------------------------------------------------------------------------')

# in e not -> Servem para fazer verificações em string
servidor = 'gmail.com'
print(servidor in 'lira@gmail.com')
print(servidor not in 'lira@gmail.com')
# True
# False
print('-------------------------------------------------------------------------')

# len() -> Calcula o tamanho do texto (quantidade de caracteres)
cpf = '15389731821'
print('O cpf tem ' + str(len(cpf)) + ' digitos.')
print('-------------------------------------------------------------------------')

# capitalize() -> Coloca a 1ª letra Maiúscula
texto = 'renato amaro peixoto'
print(texto.capitalize())
# Renato amaro peixoto
print('-------------------------------------------------------------------------')

''' casefold() -> Transforma todas as letras em minúsculas (existe lower() mas o 
casefold é melhor normalmente. '''
texto = 'RENATO'
print(texto.casefold())
print(texto.lower())
# renato
# renato
print('-------------------------------------------------------------------------')

# count()-> Quantidade de vezes que um valor aparece na string
texto = 'peixoto.sd@gmail.com'
print(texto.count('.'))
print(texto.count('a'))
# 2
# 1
print('-------------------------------------------------------------------------')

''' find() -> Procura um texto dentro de outro texto e dá como resposta a posição 
do texto encontrado. A procura é da esquerda para direita '''
texto = 'peixoto.sd@gmail.com'
print(texto.find('@'))
# 10
print('-------------------------------------------------------------------------')

# rfind() -> Procura da esquerda para direita, mostra a posiçõa.
texto = 'peixoto.sd@gmail.com'
print(texto.rfind('o'))
# 18
print('-------------------------------------------------------------------------')

# format() -> Formata uma string de acordo com os valores passados. 
faturamento = 1000
print('O faturamento da loja foi de {} reais'.format(faturamento))
# O faturamento da loja foi de 1000 reais
print('-------------------------------------------------------------------------')

''' isalnum() -> Verifica se um texto é todo feito com caracteres alfanuméricos 
(letras e números) -> letras com acento ou ç são considerados letras para essa
 função. '''
texto = 'João123'
print(texto.isalnum()) # True
if texto.isalnum() :
    print(f'{texto} - É letra e numero.')
else :
    print(f'{texto} - não é letra e numero')
# True
# João123 - É letra e numero.
# Obs: se o texto fosse 'Jo~ao' ou então 'Joao#' o resultado seria False
print('-------------------------------------------------------------------------')

# isalpha() -> Verifica se um texto é todo feito de letras.
texto = 'João'
print(texto.isalpha())
if texto.isalpha() :
    print(f'{texto} - É somente letra.')
else :
    print(f'{texto} - não é somente letra')
# True
# João - É somente letra.
''' Obs: nesse caso se o texto fosse 'Joao123' o resultado seria False, 
porque 123 não são letras. '''
print('-------------------------------------------------------------------------')

# isnumeric()-> Verifica se um texto é todo feito por números.
texto = '123'
print(texto.isnumeric())
if texto.isnumeric() :
    print(f'{texto} - É numero.')
else :
    print(f'{texto} - não é numero')
# True
# 123 - É numero.
print('-------------------------------------------------------------------------')

# 
# Calcula a raiz quadrada como número real
valor = 16
raiz = math.sqrt(valor)
# Verifica se a raiz é exata
if  raiz.is_integer() :
    print(f"A raiz quadrada é exata, Valor: {valor} é {raiz}")
else :
    print(f"A raiz quadrada não é exata, valor: {valor} é {raiz}")
# A raiz quadrada exata de 16 é 4.0
print('-------------------------------------------------------------------------')


# replace() -> Substitui um texto por um outro texto em uma string.
texto = '1000.00'
print(texto.replace('.', ','))
# 1000,00
''' Obs: o replace precisa de 2 argumentos para funcionar. O 1º é o texto que 
você quer trocar. O 2º é o texto que você quer colocar no lugar daquele 
texto que você está tirando. '''
print('-------------------------------------------------------------------------')

# split() -> Separa uma string de acordo com um delimitador em vários textos diferentes.
texto = 'lira@gmail.com'
texto2 = 'Renato Amaro Peixoto'
lista = texto2.split() 
print(texto.split('@'))
print(texto2.split())
print(lista)
print(lista[0], lista[1], lista[2])
# ['lira', 'gmail.com']
# ['Renato', 'Amaro', 'Peixoto']
# ['Renato', 'Amaro', 'Peixoto']
# Renato Amaro Peixoto
print('-------------------------------------------------------------------------')

# Separando palavras da string em uma lista
frase1 = "Olá, Mundo!"
lista = frase1.split(",")  # Divide a string em uma lista usando a vírgula como separador
print(f"Frase original: '{frase1}'")
print(f"Frase dividida em lista: {lista}")
# Frase original: 'Olá, Mundo!'
# Frase dividida em lista: ['Olá', ' Mundo!']
print('-------------------------------------------------------------------------')

# splitlines() -> separa um texto em vários textos de acordo com os "enters" do texto
texto = '''Olá, bom dia
Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje.
Faturamento = R$2.500,00'''
print(texto.splitlines())
'''['Olá, bom dia', 'Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje.',
 'Faturamento = R$2.500,00']'''
print('-------------------------------------------------------------------------')


# startswith() -> Verifica se a string começa com determinado texto
texto = 'BEB123453'
print(texto.startswith('BEB')) # True
# True
print('-------------------------------------------------------------------------')

''' endswith() -> Verifica se o texto termina com um valor específico e 
dá como resposta True ou False '''
texto = 'peixoto.sd@gmail.com'
print(texto.endswith('gmail.com'))
print(texto.endswith('.com'))
# True
# True
print('-------------------------------------------------------------------------')

''' strip() -> Retira caracteres indesejados dos textos. Por padrão, retira 
espaços "extras" no início e no final. '''
texto = '    BEB123453 '
print(texto.strip()) 
# BEB123453
print('-------------------------------------------------------------------------')

# title() -> Coloca a 1ª letra de cada palavra em maiúscula
texto = 'renato amaro peixoto'
print(texto.title())    
# Renato Amaro Peixoto
print('-------------------------------------------------------------------------')

# upper() -> Coloca o texto todo em letra maiúscula
texto = 'beb12343'
print(texto.upper())
# BEB123453
print('-------------------------------------------------------------------------')

# Unindo uma lista de palavras em uma string com separador
lista = ['Olá', 'mundo']
print(len(lista)) # 2
juncao = "_".join(lista)  # Junta a lista em uma string com "_" como separador
print(len(juncao)) # 9
juncao1 = ' '.join(lista)
print(len(juncao1)) # 9
print(f"Lista original: {lista}")
print(f"Lista unida em string: {juncao}")
print(f"Lista unida em string: {juncao1}")
print('-' * 70)
# 2
# 9
# 9
# Lista original: ['Olá', 'mundo']
# Lista unida em string: Olá_mundo
# Lista unida em string: Olá mundo