import os
os.system('cls' if os.name == 'nt' else 'clear')


# Sinal de Mais (+) -> Serve para concatenar strings
usuario = 'peixoto.sd'
servidor = 'gmail.com'
print(usuario + '@' + servidor)

# str() -> transforma o valor em string
faturamento = 1000
print('O faturamento da loja foi de ' + str(faturamento))

# in e not -> Servem para fazer verificações em string
servidor = 'gmail.com'
print(servidor in 'lira@gmail.com')
print(servidor not in 'lira@gmail.com')

# len() -> Calcula o tamanho do texto (quantidade de caracteres)
cpf = '15389731821'
print('O cpf tem ' + str(len(cpf)) + ' digitos.')

# capitalize() -> Coloca a 1ª letra Maiúscula
texto = 'renato'
print(texto.capitalize())

''' casefold() -> Transforma todas as letras em minúsculas (existe lower() mas o 
casefold é melhor normalmente. '''
texto = 'RENATO'
print(texto.casefold())
print(texto.lower())

# count()-> Quantidade de vezes que um valor aparece na string
texto = 'peixoto.sd@gmail.com'
print(texto.count('.'))
print(texto.count('a'))

''' endswith() -> Verifica se o texto termina com um valor específico e 
dá como resposta True ou False '''
texto = 'peixoto.sd@gmail.com'
print(texto.endswith('gmail.com'))
print(texto.endswith('.com'))

''' find() -> Procura um texto dentro de outro texto e dá como resposta a posição 
do texto encontrado. '''
texto = 'peixoto.sd@gmail.com'
print(texto.find('@'))

# format() -> Formata uma string de acordo com os valores passados. 
faturamento = 1000
print('O faturamento da loja foi de {} reais'.format(faturamento))

''' isalnum() -> Verifica se um texto é todo feito com caracteres alfanuméricos 
(letras e números) -> letras com acento ou ç são considerados letras para essa
 função. '''
texto = 'João123'
print(texto.isalnum()) # True
if texto.isalnum() :
    print(f'{texto} - É letra e numero.')
else :
    print(f'{texto} - não é letra e numero')
# Obs: se o texto fosse 'Jo~ao' ou então 'Joao#' o resultado seria False

# isalpha() -> Verifica se um texto é todo feito de letras.
texto = 'João'
print(texto.isalpha())
if texto.isalpha() :
    print(f'{texto} - É somente letra.')
else :
    print(f'{texto} - não é somente letra')
''' Obs: nesse caso se o texto fosse 'Joao123' o resultado seria False, 
porque 123 não são letras. '''

# isnumeric()-> Verifica se um texto é todo feito por números.
texto = '123'
print(texto.isnumeric())
if texto.isnumeric() :
    print(f'{texto} - É numero.')
else :
    print(f'{texto} - não é numero')

# replace() -> Substitui um texto por um outro texto em uma string.
texto = '1000.00'
print(texto.replace('.', ','))
''' Obs: o replace precisa de 2 argumentos para funcionar. O 1º é o texto que 
você quer trocar. O 2º é o texto que você quer colocar no lugar daquele 
texto que você está tirando. '''

# split() -> Separa uma string de acordo com um delimitador em vários textos diferentes.
texto = 'lira@gmail.com'
texto2 = 'Renato Amaro Peixoto'
lista = texto2.split() 
print(texto.split('@'))
print(texto2.split())
print(lista)
print(lista[0], lista[1], lista[2])

# splitlines() -> separa um texto em vários textos de acordo com os "enters" do texto
texto = '''Olá, bom dia
Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje.
Faturamento = R$2.500,00'''
print(texto.splitlines())

# startswith() -> Verifica se a string começa com determinado texto
texto = 'BEB123453'
print(texto.startswith('BEB')) # True

''' strip() -> Retira caracteres indesejados dos textos. Por padrão, retira 
espaços "extras" no início e no final. '''
texto = '    BEB123453 '
print(texto.strip()) # 'BEB123453'

# title() -> Coloca a 1ª letra de cada palavra em maiúscula
texto = 'renato amaro peixoto'
print(texto.title())    # 'Renato Amaro Peixoto'

# upper() -> Coloca o texto todo em letra maiúscula
texto = 'beb12343'
print(texto.upper())

