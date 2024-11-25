# 1. if e else
# Exemplo:
idade = 18
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
# Explicação:
# O comando ifsignifica "se", e é usado para verificar uma condição. No exemplo, o programa verifica se a idade é maior ou igual a 18. Na verdade, ele imprime "Maior de idade". Caso contrário (com o else), ele imprime "Menor de idade".
# Por que usar? Esse tipo de verificação é fundamental para tomar decisões em um programa, como verificar permissões ou validar dados.

# 2. isinstance()
# Exemplo:
dado = 42
if isinstance(dado, int):
    print("É um número inteiro.")
else:
    print("Não é um número inteiro.")
Explicação:
# A função isinstance()verifica se um objeto é de um tipo específico. No exemplo, estamos verificando se dadoé do tipo int(número inteiro). Isso evita que o programa tente fazer algo errado com um dado do tipo errado.
# Por que usar? É útil para garantir que o programa funcione com os tipos de dados corretos, evitando erros inesperados.

# 3. len()
# Exemplo:
senha = "123456"
if len(senha) >= 6:
    print("Senha válida.")
else:
    print("Senha muito curta.")
# Explicação:
# A função len()retorna o tamanho de uma sequência, como o número de caracteres de uma string ou o número de elementos de uma lista. No exemplo, estamos verificando se a senha tem pelo menos 6 caracteres.
# Por que usar? Ajuda a validar o tamanho dos dados, como verificar se uma senha ou um nome atende a critérios mínimos.

# 4. in
# Exemplo:
email = "usuario@dominio.com"
if "@" in email:
    print("Email válido.")
else:
    print("Email inválido.")
# Explicação:
# A palavra-chave inverifica se algo (um caractere ou palavra) está presente em uma sequência (como uma string ou lista). No exemplo, verificamos se o símbolo @está presente no email.
# Por que usar? Facilita validações simples, como verificar se certos elementos essenciais estão presentes.

# 5. try e except
# Exemplo:
entrada = "123a"
try:
    numero = int(entrada)
    print("É um número válido.")
except ValueError:
    print("Entrada inválida, não é um número.")
# Explicação:
# O bloco trytenta executar um código que pode causar um erro. Se houver um erro (neste caso, tente converter um texto com letras para número), o programa usa o bloco exceptpara tratar o erro sem parar de funcionar.
# Por que usar? Previna que o programa “quebre” ao lidar com entradas inesperadas.

# 6. all()
# Exemplo:
valores = [10, 20, 30]
if all(v > 5 for v in valores):
    print("Todos os valores são maiores que 5.")
else:
    print("Nem todos os valores são maiores que 5.")
# Explicação:
# A função all()retorna True(verdadeiro) se todos os itens de uma condição são verdadeiros. No exemplo, verificamos se todos os números em uma lista são maiores que 5.
# Por que usar? Simplifica verificações para listas ou grupos de condições.

# 7. any()
# Exemplo:
valores = [0, -1, 5]
if any(v > 0 for v in valores):
    print("Há valores positivos.")
else:
    print("Não há valores positivos.")
# Explicação:
# A função any()retorna Truese pelo menos uma condição para verdadeira. No exemplo, estamos verificando se existe pelo menos um número positivo na lista.
# Por que usar? Útil para verificar se "alguma coisa" atende a uma condição específica.

# 8. .isdigit()
# Exemplo:
dado = "1234"
if dado.isdigit():
    print("É um número válido.")
else:
    print("Não é um número.")
# Explicação:
# O método .isdigit()verifica se todos os caracteres de uma string são números. No exemplo, validamos se o texto contém apenas números.
# Por que usar? É ideal para garantir que uma entrada de texto seja composta apenas por dígitos.

# 9. .isalpha()
# Exemplo:
nome = "Joao"
if nome.isalpha():
    print("É um nome válido.")
else:
    print("O nome contém caracteres inválidos.")
# Explicação:
# O método .isalpha()verifica se uma string contém apenas letras. No exemplo, garantimos que um nome não tenha números ou símbolos.
# Por que usar? Útil para validar nomes ou palavras que não devem conter números ou caracteres especiais.

# 10. .isalnum()
# Exemplo:
usuario = "Joao123"
if usuario.isalnum():
    print("Nome de usuário válido.")
else:
    print("Nome de usuário contém caracteres inválidos.")
# Explicação:
# O método .isalnum()verifica se uma string contém apenas letras e números, sem espaços ou símbolos. Por exemplo, validamos nomes de usuários que só podem ter letras e números.
# Por que usar? É útil para sistemas onde nomes de usuários não podem conter caracteres especiais.

# 11. strip()
# Exemplo:
nome = "  Maria  "
if nome.strip() != "":
    print("Nome válido:", nome.strip())
else:
    print("Nome vazio.")
# Explicação:
# O método .strip()remove espaços extras no início e no fim de uma string. Isso é importante para evitar problemas com entradas de dados que tenham espaços desnecessários.
# Por que usar? Garanta que os dados estejam limpos antes de usar.

# 12. Validação por expressão regular ( re)
# Exemplo:
import re
email = "usuario@dominio.com"
padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(padrao, email):
    print("Email válido.")
else:
    print("Email inválido.")
# Explicação:
# As expressões regulares são como "regras de busca" para validar formatos específicos, como e-mails, senhas ou telefones. No exemplo, verificamos se o e-mail não está no formato correto.
# Por que usar? Perfeito para validar formatos complexos de dados.

# 13. Comparação entre valores
# Exemplo:
senha1 = "123456"
senha2 = "123456"
if senha1 == senha2:
    print("Senhas correspondem.")
else:
    print("Senhas não correspondem.")
# Explicação:
# Aqui estamos comparando duas variáveis ​​para ver se têm o mesmo valor. Isso é útil, por exemplo, para confirmar se a senha foi digitada corretamente.
# Por que usar? Ajuda a verificar a igualdade de dados.

# 14.enumerate()
# Exemplo:
numeros = [10, 0, 20]
for i, num in enumerate(numeros):
    if num == 0:
        print(f"Valor inválido na posição {i}.")
# Explicação:
# O enumerate()permite acessar o índice e o valor ao mesmo tempo ao iterar por uma lista. Isso ajuda a localizar onde está um dado específico na lista.
# Por que usar? É prático para depuração e validação.

# 15. Validação de intervalo comrange()
# Exemplo:
numero = 15
if numero in range(10, 20):
    print("Número dentro do intervalo.")
else:
    print("Número fora do intervalo.")
# Explicação:
# O range()cria uma sequência de números e inverifica se um número pertence a ela. No exemplo, validamos se o número estiver entre 10 e 20.
# Por que usar? Ajuda a verificar se os dados numéricos estão dentro dos limites.

# 16. Verifique valores nulos ou vazios
# Exemplo:
dado = None
if dado is None:
    print("O dado está vazio.")
else:
    print("O dado contém algum valor.")
# Explicação:
# A palavra-chave Noneé usada em Python para representar algo sem valor (nulo). A verificação is Nonegarante que você está lidando com valores válidos.
# Por que usar? Útil para evitar erros ao trabalhar com dados que não podem estar definidos.

# 17. Verifique números positivos, negativos ou zero
# Exemplo:
numero = -10
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
# Explicação:
# Aqui você está categorizando números com base no seu valor: positivo, negativo ou zero. Isso é feito com comparações simples.
# Por que usar? Ajuda em cálculos ou regras de negócio que dependem do tipo de número.

# 18. Verifique se uma lista ou dicionário está vazio
# Exemplo:
lista = []
if not lista:
    print("A lista está vazia.")
else:
    print("A lista contém elementos.")
# Explicação:
# Listas e dicionários em Python são considerados "falsos" quando estão vazios. A verificação if notpermite validar rapidamente se eles contêm algo.
# Por que usar? Evite erros ao tentar acessar dados em estruturas vazias.

# 19. Verifique duplicatas em uma lista
# Exemplo:
numeros = [1, 2, 3, 4, 4]
if len(numeros) != len(set(numeros)):
    print("Existem duplicatas na lista.")
else:
    print("Todos os elementos são únicos.")
# Explicação:
# Um setem Python remove duplicatas automaticamente. Comparando o tamanho da lista original com o set, você pode detectar duplicatas.
# Por que usar? Útil para garantir que listas contenham apenas valores únicos.

# 20. Verifique se um número é par ou ímpar
# Exemplo:
numero = 5
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
# Explicação:
# Use o operador de resto ( %) para verificar se o número é divisível por 2. Se o resto for 0, é par; caso contrário, é ímpar.
# Por que usar? Muito útil para algoritmos que precisam lidar com números de formas diferentes, dependendo de serem pares ou impares.

# 21. Verifique se um texto está em autoridades ou subsidiárias
# Exemplo:
texto = "HELLO"
if texto.isupper():
    print("O texto está em maiúsculas.")
elif texto.islower():
    print("O texto está em minúsculas.")
else:
    print("O texto está misturado.")
# Explicação:
# Os métodos .isupper()e .islower()verificam se um texto está todo em letras secretas ou minúsculas, respectivamente.
# Por que usar? Útil para validar textos que precisam seguir regras de formatação.

# 22. Verifique se um dado é válido
# Exemplo:
from datetime import datetime
data = "2024-11-31"
try:
    datetime.strptime(data, "%Y-%m-%d")
    print("A data é válida.")
except ValueError:
    print("A data é inválida.")
# Explicação:
# A função datetime.strptime()tenta converter um texto em um objeto de dados. Se falhar, sabemos que os dados são inválidos.
# Por que usar? Necessário para lidar com entradas de dados em formatos específicos.

# 23. Validar CPF ou CNPJ
# Exemplo:
def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    return True
cpf = "123.456.789-09"
if validar_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")
# Explicação:
# Aqui filtramos apenas os números de um CPF e verificamos se ele tem 11 dígitos. Este é um exemplo básico; para uma validação completa, seria necessário usar as regras específicas do CPF.
# Por que usar? Muito útil em sistemas brasileiros que precisam lidar com CPFs ou CNPJs.

# 24. Verifique se uma string começa ou termina com algo específico
# Exemplo:
arquivo = "documento.txt"
if arquivo.endswith(".txt"):
    print("É um arquivo de texto.")
else:
    print("Não é um arquivo de texto.")
# Explicação:
# Os métodos .startswith()e .endswith()verificam se uma string começa ou termina com determinados caracteres.
# Por que usar? Útil para validar extensões de arquivos ou padrões de texto.

# 25. Verifique se uma sequência está ordenada
# Exemplo:
sequencia = [1, 2, 3, 4, 5]
if sequencia == sorted(sequencia):
    print("A sequência está ordenada.")
else:
    print("A sequência não está ordenada.")
# Explicação:
# Comparamos a lista original com a versão ordenada dela, usando a função sorted().
# Por que usar? Ajuda a garantir que os dados estejam organizados.

# 26. Verifique se uma senha é forte
# Exemplo:
import re
senha = "Abc@1234"
if (len(senha) >= 8 and
    re.search(r"[A-Z]", senha) and
    re.search(r"[a-z]", senha) and
    re.search(r"[0-9]", senha) and
    re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha)):
    print("Senha forte.")
else:
    print("Senha fraca.")
# Explicação:
# Usamos expressões regulares para garantir que a senha tenha no mínimo 8 caracteres, uma letra secreta, uma minúscula, um número e um caractere especial.
# Por que usar? Essencial para sistemas que precisam proteger contas de usuários.

# 27. Verifique se um número é primo
# Exemplo:
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
numero = 17
if eh_primo(numero):
    print("O número é primo.")
else:
    print("O número não é primo.")
# Explicação:
# Um número primo é divisível apenas por 1 e por ele mesmo. O algoritmo verifica divisores até a raiz quadrada do número para ser eficiente.
# Por que usar? Muito utilizado em matemática e segurança digital (criptografia).

# 28. Verifique se um número está dentro de um intervalo (usando limites)
# Exemplo:
numero = 15
if 10 <= numero <= 20:
    print("O número está no intervalo.")
else:
    print("O número está fora do intervalo.")
# Explicação:
# Usamos operadores lógicos para verificar se um número está dentro de um intervalo específico.
# Por que usar? Muito útil para validações numéricas, como idades ou faixas de valores.

# 29. Verifique se uma lista contém apenas números
# Exemplo:
lista = [1, 2, 3, "a"]
if all(isinstance(i, (int, float)) for i in lista):
    print("A lista contém apenas números.")
else:
    print("A lista contém valores não numéricos.")
# Explicação:
# O comando all()percorre a lista e verifica se cada elemento é do tipo intou float.
# Por que usar? Ideal para garantir que os dados em uma lista sejam numéricos antes da realização dos cálculos.

# 30. Verifique se o texto contém apenas caracteres válidos
# Exemplo:
texto = "Hello123!"
caracteres_validos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
if all(char in caracteres_validos for char in texto):
    print("O texto contém apenas caracteres válidos.")
else:
    print("O texto contém caracteres inválidos.")
# Explicação:
# Aqui verificamos se cada caractere do texto pertence a um conjunto de caracteres válidos.
# Por que usar? Útil para impedir a inserção de caracteres inesperados ou potencialmente perigosos, como símbolos especiais.

# 31. Verifique se um número é divisível por outro
# Exemplo:
numero = 10
divisor = 5
if numero % divisor == 0:
    print(f"{numero} é divisível por {divisor}.")
else:
    print(f"{numero} não é divisível por {divisor}.")
# Explicação:
# Usamos o operador %para verificar se o resto da divisão é zero.
# Por que usar? Frequentemente necessário em matemática ou lógica de negócios.

# 32. Validar uma string com tamanho exato
# Exemplo:
codigo = "1234"
if len(codigo) == 4:
    print("O código tem o tamanho correto.")
else:
    print("O código não tem o tamanho correto.")
# Explicação:
# Usamos len()para verificar se uma string tem o comprimento esperado.
# Por que usar? Ideal para códigos, IDs ou entradas que precisam ter um tamanho fixo.

# 33. Verifique se um elemento existe em uma lista
# Exemplo:
lista = ["banana", "maçã", "laranja"]
fruta = "maçã"
if fruta in lista:
    print("A fruta está na lista.")
else:
    print("A fruta não está na lista.")
# Explicação:
# Usamos o operador inpara verificar se um elemento está presente em uma lista.
# Por que usar? Útil para verificar dados existentes em coleções.

# 34. Validar se uma lista tem elementos repetidos
# Exemplo:
lista = [1, 2, 3, 4, 4]
if len(lista) != len(set(lista)):
    print("A lista tem elementos repetidos.")
else:
    print("Todos os elementos são únicos.")
# Explicação:
# Convertendo a lista em um set, eliminamos duplicatas. Comparar os tamanhos ajuda a detectar repetições.
# Por que usar? Importante para validar listas onde apenas valores são esperados.

# 35. Verifique se um número não está no formato decimal
# Exemplo:
numero = "12.34"
try:
    float(numero)
    print("O número está no formato decimal.")
except ValueError:
    print("O número não está no formato decimal.")
# Explicação:
# Usamos a função float()para tentar converter o texto em um número decimal.
# Por que usar? Necessário para validar dados numéricos fornecidos pelo usuário.

# 36. Validar se uma string é um nome próprio (primeira letra guardada)
# Exemplo:
nome = "João"
if nome.istitle():
    print("O nome está no formato correto.")
else:
    print("O nome não está no formato correto.")
# Explicação:
# O método .istitle()verifica se cada palavra da string começa com letra confidencial.
# Por que usar? Muito usado para validar nomes ou títulos.

# 37. Validar o formato de um número de telefone
# Exemplo:
import re
telefone = "(11) 91234-5678"
padrao = r'^\(\d{2}\) \d{5}-\d{4}$'
if re.match(padrao, telefone):
    print("Número de telefone válido.")
else:
    print("Número de telefone inválido.")
# Explicação:
# Usamos expressões regulares para garantir que o telefone siga o padrão esperado.
# Por que usar? Essencial para sistemas que lidam com números de telefone.

# 38. Validar se uma string contém apenas caracteres Unicode válidos
# Exemplo:
texto = "Olá, mundo!"
try:
    texto.encode("utf-8")
    print("O texto contém caracteres válidos.")
except UnicodeEncodeError:
    print("O texto contém caracteres inválidos.")
# Explicação:
# Tentamos codificar uma string como UTF-8 para garantir que ela seja válida.
# Por que usar? Necessário lidar com dados que precisam ser compatíveis com diferentes sistemas.

# 39. Validar se uma lista contém todos os elementos de outra
# Exemplo:
lista1 = [1, 2, 3]
lista2 = [1, 2]
if all(elem in lista1 for elem in lista2):
    print("Todos os elementos de lista2 estão em lista1.")
else:
    print("Nem todos os elementos de lista2 estão em lista1.")
# Explicação:
# Usamos o all()para garantir que cada elemento de uma lista esteja presente em outro.
# Por que usar? Útil em comparações de conjuntos de dados.

# 40. Verifique se dois dicionários têm as mesmas chaves
# Exemplo:
dict1 = {"nome": "João", "idade": 25}
dict2 = {"nome": "Maria", "idade": 30}
if dict1.keys() == dict2.keys():
    print("Os dicionários têm as mesmas chaves.")
else:
    print("Os dicionários têm chaves diferentes.")

41. Validar se um texto é um palíndromo
Exemplo:
Pitão

Copiar código
texto = "arara"
if texto == texto[::-1]:
    print("O texto é um palíndromo.")
else:
    print("O texto não é um palíndromo.")
Explicação:
Um palíndromo é uma palavra ou frase que é igual quando lida de trás para frente. Aqui, comparamos o texto original com ele mesmo invertido usando o fatiamento [::-1].

Por que usar? Pode ser útil em exercícios de lógica ou jogos de palavras.
42. Validar se uma senha contém espaços
Exemplo:
Pitão

Copiar código
senha = "senha123"
if " " in senha:
    print("A senha não deve conter espaços.")
else:
    print("A senha é válida.")
Explicação:
Usamos o operador inpara verificar a presença de espaços na senha.

Por que usar? Evite problemas em senhas que não devem ter espaços por questões de segurança.
43. Validar se uma string é um número romano
Exemplo:
Pitão

Copiar código
import re

numero_romano = "XIV"
padrao = r'^(?=[MDCLXVI])M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
if re.match(padrao, numero_romano):
    print("É um número romano válido.")
else:
    print("Não é um número romano válido.")
Explicação:
Usamos uma expressão regular para verificar se uma string segue o formato de números romanos.

Por que usar? Útil para sistemas que lidam com representações antigas de números.
44. Validar se uma lista está em ordem decrescente
Exemplo:
Pitão

Copiar código
numeros = [5, 4, 3, 2, 1]
if numeros == sorted(numeros, reverse=True):
    print("A lista está em ordem decrescente.")
else:
    print("A lista não está em ordem decrescente.")
Explicação:
Usamos sorted()o parâmetro reverse=Truepara verificar se a lista está ordenada de forma decrescente.

Por que usar? Útil em cenários onde a ordem dos dados é importante.
45. Validar se uma string é uma URL
Exemplo:
Pitão

Copiar código
import re

url = "https://www.google.com"
padrao = r'^(http|https)://[a-zA-Z0-9\-\.]+\.[a-z]{2,3}(/.*)?$'
if re.match(padrao, url):
    print("A URL é válida.")
else:
    print("A URL não é válida.")
Explicação:
Usamos uma expressão regular para validar URLs que começam com httpou https.

Por que usar? Necessário para sistemas que lidam com links ou endereços web.
46. ​​Validar se dois arquivos têm o mesmo conteúdo
Exemplo:
Pitão

Copiar código
with open("arquivo1.txt", "r") as file1, open("arquivo2.txt", "r") as file2:
    if file1.read() == file2.read():
        print("Os arquivos têm o mesmo conteúdo.")
    else:
        print("Os arquivos têm conteúdos diferentes.")
Explicação:
Abrimos os dois arquivos e comparamos seus conteúdos diretamente.

Por que usar? Útil para verificar integridade ou duplicação de dados.
47. Validar se uma imagem não está no formato correto
Exemplo:
Pitão

Copiar código
from PIL import Image

try:
    img = Image.open("imagem.jpg")
    img.verify()
    print("A imagem é válida.")
except (IOError, SyntaxError):
    print("A imagem não é válida.")
Explicação:
Usamos uma biblioteca PIL(ou Pillow) para abrir e verificar o formato da imagem.

Por que usar? Ideal para sistemas que lidam com upload de imagens.
48. Validar se um número é um quadrado perfeito
Exemplo:
Pitão

Copiar código
import math

numero = 16
if math.isqrt(numero) ** 2 == numero:
    print("É um quadrado perfeito.")
else:
    print("Não é um quadrado perfeito.")
Explicação:
Um quadrado perfeito é um número inteiro que é o quadrado de outro número inteiro. Usamos math.isqrt()para verificar isso.

Por que usar? Importante em problemas matemáticos ou lógicos.
49. Validar se uma string está no formato JSON
Exemplo:
Pitão

Copiar código
import json

dados = '{"nome": "João", "idade": 30}'
try:
    json.loads(dados)
    print("O formato JSON é válido.")
except json.JSONDecodeError:
    print("O formato JSON é inválido.")
Explicação:
Usamos json.loads()para tentar decodificar uma string como JSON. Se falhar, ela não está no formato correto.

Por que usar? Essencial para sistemas que lidam com APIs ou dados estruturados.
50. Validar se um número é parte de uma sequência de Fibonacci
Exemplo:
Pitão

Copiar código
def eh_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

numero = 21
if eh_fibonacci(numero):
    print("O número faz parte da sequência de Fibonacci.")
else:
    print("O número não faz parte da sequência de Fibonacci.")
Explicação:
A sequência de Fibonacci é uma série em que cada número é a soma dos dois anteriores. O algoritmo verifica se o número pertence a essa sequência.

Por que usar? Útil em problemas matemáticos ou desafios de programação.
51. Validar se uma string não está no formato de horário (HH :MM )
Exemplo:
Pitão

Copiar código
import re

horario = "23:45"
padrao = r'^([01]\d|2[0-3]):([0-5]\d)$'
if re.match(padrao, horario):
    print("O horário é válido.")
else:
    print("O horário é inválido.")
Explicação:
Usamos uma expressão regular para verificar se o horário está no formato de 24 horas (HH :MM ).

Por que usar? Necessário para validações de entradas de horários.

52. Validar se uma string é um endereço IP válido
Exemplo:
Pitão

Copiar código
import ipaddress

ip = "192.168.1.1"
try:
    ipaddress.ip_address(ip)
    print("O endereço IP é válido.")
except ValueError:
    print("O endereço IP é inválido.")
Explicação:
A biblioteca ipaddressverifica se o formato do endereço IP é válido (IPv4 ou IPv6).

Por que usar? Essencial em sistemas de rede ou aplicativos que lidam com endereços IP.
53. Validar se um número é múltiplo de outro
Exemplo:
Pitão

Copiar código
numero = 12
divisor = 4
if numero % divisor == 0:
    print(f"{numero} é múltiplo de {divisor}.")
else:
    print(f"{numero} não é múltiplo de {divisor}.")
Explicação:
Usamos o operador %para verificar se o resto da divisão é zero, ou que indica que o número é múltiplo.

Por que usar? Útil em cálculos matemáticos e lógica de jogos ou regras.
54. Validar se uma string contém apenas caracteres ASCII
Exemplo:
Pitão

Copiar código
texto = "Olá, mundo!"
if all(ord(char) < 128 for char in texto):
    print("O texto contém apenas caracteres ASCII.")
else:
    print("O texto contém caracteres fora do padrão ASCII.")
Explicação:
Os caracteres ASCII têm valores entre 0 e 127 na tabela Unicode. Verificamos isso usando a função ord().

Por que usar? Importante para sistemas que são restritos a formatos antigos ou restritos.
55. Validar se um arquivo existe
Exemplo:
Pitão

Copiar código
import os

arquivo = "meu_arquivo.txt"
if os.path.exists(arquivo):
    print("O arquivo existe.")
else:
    print("O arquivo não existe.")
Explicação:
Usamos a função os.path.exists()para verificar se o arquivo está presente no sistema de arquivos.

Por que usar? Necessário antes de tentar abrir ou manipular arquivos para evitar erros.
56. Validar se uma string contém caracteres repetidos
Exemplo:
Pitão

Copiar código
texto = "banana"
if len(set(texto)) != len(texto):
    print("A string contém caracteres repetidos.")
else:
    print("A string não contém caracteres repetidos.")
Explicação:
Transformamos uma string em um set, que elimina duplicatas. Se o tamanho setfor diferente do tamanho original da string, há caracteres repetidos.

Por que usar? Útil para validar nomes ou palavras que devem ser únicas.
57. Validar se uma matriz é quadrada
Exemplo:
Pitão

Copiar código
matriz = [[1, 2], [3, 4]]
if all(len(linha) == len(matriz) for linha in matriz):
    print("A matriz é quadrada.")
else:
    print("A matriz não é quadrada.")
Explicação:
Uma matriz quadrada tem o mesmo número de linhas e colunas. Verificamos isso conferindo o comprimento de cada linha.

Por que usar? Necessário em algoritmos matemáticos, como multiplicação de matrizes.
58. Validar se uma string é uma palavra única (sem espaços)
Exemplo:
Pitão

Copiar código
palavra = "Python"
if " " not in palavra:
    print("É uma palavra única.")
else:
    print("Não é uma palavra única.")
Explicação:
Usamos o operador inpara verificar se há espaços na string.

Por que usar? Útil para garantir que nomes de variáveis, identificadores ou palavras não tenham espaços.
59. Validar se dois textos são anagramas
Exemplo:
Pitão

Copiar código
texto1 = "amor"
texto2 = "roma"
if sorted(texto1) == sorted(texto2):
    print("Os textos são anagramas.")
else:
    print("Os textos não são anagramas.")
Explicação:
Um anagrama é formado ao reorganizar as letras de uma palavra. Verificamos isso ordenando ambas as palavras e comparando.

Por que usar? Útil em jogos de palavras ou algoritmos de processamento de texto.
60. Validar se um número é uma potência de outro
Exemplo:
Pitão

Copiar código
numero = 8
base = 2
if (numero > 0 and (numero & (numero - 1)) == 0):
    print(f"{numero} é uma potência de {base}.")
else:
    print(f"{numero} não é uma potência de {base}.")
Explicação:
Usamos uma combinação de bitwise e verificações matemáticas para identificar potências de 2.

Por que usar? Necessário em algoritmos de criptografia e lógica binária.
61. Validar se uma string contém um caractere especial
Exemplo:
Pitão

Copiar código
import re

texto = "senha@123"
if re.search(r'[!@#$%^&*(),.?":{}|<>]', texto):
    print("A string contém caracteres especiais.")
else:
    print("A string não contém caracteres especiais.")
Explicação:
Usamos uma expressão regular para verificar a presença de caracteres especiais.

Por que usar? Importante para validar senhas ou entradas que necessitem de maior segurança.
62. Validar se uma lista é simétrica
Exemplo:
Pitão

Copiar código
lista = [1, 2, 3, 2, 1]
if lista == lista[::-1]:
    print("A lista é simétrica.")
else:
    print("A lista não é simétrica.")
Explicação:
Uma lista é simétrica se for igual a ela mesma invertida.

Por que usar? Comum em algoritmos matemáticos ou lógicos.
63. Validar se um número está na base binária
Exemplo:
Pitão

Copiar código
numero = "10101"
if all(char in '01' for char in numero):
    print("O número está na base binária.")
else:
    print("O número não está na base binária.")
Explicação:
Verificamos se todos os caracteres de um número estão entre 0 e 1.

Por que usar? Necessário em lógica de sistemas e programação em baixo nível.

64. Validar se uma string é uma palavra reservada em Python
Exemplo:
Pitão

Copiar código
import keyword

palavra = "def"
if palavra in keyword.kwlist:
    print(f"'{palavra}' é uma palavra reservada em Python.")
else:
    print(f"'{palavra}' não é uma palavra reservada.")
Explicação:
O módulo keywordcontém uma lista de todas as palavras reservadas do Python. Verificamos se a string está nessa lista.

Por que usar? Importante para evitar nomes de variações ou funções que entrem em conflito com palavras reservadas.
65. Validar se uma string contém apenas letras e espaços
Exemplo:
Pitão

Copiar código
texto = "Olá Mundo"
if all(char.isalpha() or char.isspace() for char in texto):
    print("A string contém apenas letras e espaços.")
else:
    print("A string contém caracteres inválidos.")
Explicação:
Verificamos se cada caractere da string é uma letra ( isalpha()) ou um espaço ( isspace()).

Por que usar? Útil para validar nomes, frases ou textos que não possam conter números ou símbolos.
66. Validar se uma matriz é diagonal
Exemplo:
Pitão

Copiar código
matriz = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
if all(matriz[i][j] == 0 for i in range(len(matriz)) for j in range(len(matriz[i])) if i != j):
    print("A matriz é diagonal.")
else:
    print("A matriz não é diagonal.")
Explicação:
Uma matriz diagonal tem todos os elementos fora da diagonal principal igual a zero.

Por que usar? Necessário em cálculos matriciais em álgebra linear.
67. Validar se uma sequência contém apenas números consecutivos
Exemplo:
Pitão

Copiar código
numeros = [3, 4, 5, 6]
if numeros == list(range(min(numeros), max(numeros) + 1)):
    print("Os números são consecutivos.")
else:
    print("Os números não são consecutivos.")
Explicação:
Comparamos a lista com um intervalo gerado pelo menor e maior número da sequência.

Por que usar? Útil para verificar padrões em dados numéricos.
68. Validar se um número é perfeito
Exemplo:
Pitão

Copiar código
numero = 28
if sum(divisor for divisor in range(1, numero) if numero % divisor == 0) == numero:
    print("O número é perfeito.")
else:
    print("O número não é perfeito.")
Explicação:
Um número perfeito é igual à soma de todos os seus divisores (excluindo ele mesmo).

Por que usar? Aplicado em matemática e teoria dos números.
69. Validar se um valor é NaN (Not a Number)
Exemplo:
Pitão

Copiar código
import math

valor = float('nan')
if math.isnan(valor):
    print("O valor é NaN.")
else:
    print("O valor não é NaN.")
Explicação:
O método math.isnan()verifica se o valor é "Not a Number" (resultado de operações inválidas).

Por que usar? Necessário para lidar com dados inválidos ou ausentes em cálculos.
70. Validar se uma lista é um subconjunto de outra
Exemplo:
Pitão

Copiar código
lista1 = [1, 2]
lista2 = [1, 2, 3, 4]
if set(lista1).issubset(lista2):
    print("A lista1 é um subconjunto da lista2.")
else:
    print("A lista1 não é um subconjunto da lista2.")
Explicação:
Usamos o método issubset()para verificar se todos os elementos da primeira lista estão na segunda.

Por que usar? Essencial em algoritmos que comparam conjuntos de dados.
71. Validar se uma string contém palavras proibidas
Exemplo:
Pitão

Copiar código
texto = "Este é um teste."
palavras_proibidas = ["teste", "proibido"]
if any(palavra in texto for palavra in palavras_proibidas):
    print("O texto contém palavras proibidas.")
else:
    print("O texto não contém palavras proibidas.")
Explicação:
Usamos any()para verificar se alguma das palavras proibidas aparece no texto.

Por que usar? Útil para filtrar conteúdos indesejados em sistemas de moderação.
72. Validar se uma lista é palíndroma
Exemplo:
Pitão

Copiar código
lista = [1, 2, 3, 2, 1]
if lista == lista[::-1]:
    print("A lista é palíndroma.")
else:
    print("A lista não é palíndroma.")
Explicação:
Uma lista palíndroma é igual quando lida de frente para trás ou de trás para frente.

Por que usar? Comum em problemas de lógica ou processamento de dados.
73. Validar se um número não está no formato hexadecimal
Exemplo:
Pitão

Copiar código
numero = "1A3F"
if all(char in "0123456789ABCDEF" for char in numero.upper()):
    print("O número está no formato hexadecimal.")
else:
    print("O número não está no formato hexadecimal.")
Explicação:
Verificamos se todos os caracteres pertencem ao conjunto válido de números hexadecimais.

Por que usar? Necessário em sistemas que lidam com endereços de memória ou núcleos.
74. Validar se um dado é um feriado (exemplo básico)
Exemplo:
Pitão

Copiar código
from datetime import datetime

feriados = ["2024-01-01", "2024-12-25"]
data = "2024-01-01"
if data in feriados:
    print("A data é um feriado.")
else:
    print("A data não é um feriado.")
Explicação:
Comparamos os dados fornecidos com uma lista de feriados.

Por que usar? Útil em sistemas de agendamento ou calendários.
75. Validar se uma lista é uma sequência geométrica
Exemplo:
Pitão

Copiar código
lista = [2, 4, 8, 16]
if all(lista[i] / lista[i - 1] == lista[1] / lista[0] for i in range(1, len(lista))):
    print("A lista é uma sequência geométrica.")
else:
    print("A lista não é uma sequência geométrica.")
Explicação:
Uma sequência geométrica tem uma razão comum entre os elementos consecutivos. Verificamos isso iterativamente.

Por que usar? Importante em matemática e modelagem de dados.
