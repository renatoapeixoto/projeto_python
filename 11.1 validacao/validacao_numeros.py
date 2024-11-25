# 1. Validação Simples: Checar se é um Número
# Se você recebe um dado (por exemplo, entrada do usuário) e quer verificar se 
# ele é um número, pode usar str.isdigit() ou tentar converter para um 
# tipo numérico com int() ou float().

# Exemplo 1: Usando isdigit() para números inteiros
entrada = input("Digite um número: ")
if entrada.isdigit():
    print(f"{entrada} é um número válido!")
else:
    print(f"{entrada} não é um número válido.")
# Limitação: isdigit() não funciona para números negativos ou com casas decimais.

# Exemplo 2: Usando Conversão com try e except
# Essa abordagem funciona para inteiros e números decimais (positivos ou negativos).
entrada = input("Digite um número: ")
try:
    numero = float(entrada)  # Pode ser int() ou float(), dependendo do caso
    print(f"{numero} é um número válido!")
except ValueError:
    print(f"{entrada} não é um número válido.")

# 2. Validação de Tipo Específico
# Se você quer verificar propriedades específicas do número, como se é inteiro,
# positivo, negativo, ou está dentro de um intervalo, veja os exemplos abaixo.

# Exemplo 1: Verificar se é Inteiro
entrada = input("Digite um número inteiro: ")
try:
    numero = int(entrada)
    print(f"{numero} é um número inteiro válido!")
except ValueError:
    print(f"{entrada} não é um número inteiro válido.")

# Exemplo 2: Verificar se é um Número Positivo
entrada = input("Digite um número positivo: ")
try:
    numero = float(entrada)
    if numero > 0:
        print(f"{numero} é um número positivo válido!")
    else:
        print(f"{numero} não é um número positivo.")
except ValueError:
    print(f"{entrada} não é um número válido.")

# Exemplo 3: Verificar se está Dentro de um Intervalo
entrada = input("Digite um número entre 1 e 100: ")
try:
    numero = float(entrada)
    if 1 <= numero <= 100:
        print(f"{numero} está dentro do intervalo!")
    else:
        print(f"{numero} está fora do intervalo.")
except ValueError:
    print(f"{entrada} não é um número válido.")

# 3. Validação de Formato
# Se você quer validar números com um formato específico 
# (como números com 2 casas decimais), pode usar expressões regulares (regex).
# Exemplo: Números Decimais com 2 Casas
import re
entrada = input("Digite um número decimal com até 2 casas: ")
# Expressão regular para números com até 2 casas decimais
padrao = r"^-?\d+(\.\d{1,2})?$"  # Aceita negativos e até 2 casas decimais
if re.match(padrao, entrada):
    print(f"{entrada} é um número válido!")
else:
    print(f"{entrada} não é um número válido.")

# 4. Validação com Funções Personalizadas
# Você pode encapsular a lógica de validação em funções para reutilizar.
# Exemplo: Função para Validar Inteiros
def validar_inteiro(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
# Teste
entrada = input("Digite um número inteiro: ")
if validar_inteiro(entrada):
    print(f"{entrada} é um número inteiro válido!")
else:
    print(f"{entrada} não é um número inteiro.")

# 5. Aplicações Práticas
# a) Entrada de Usuário em Loop até ser Válida
while True:
    entrada = input("Digite um número válido: ")
    try:
        numero = float(entrada)
        print(f"Você digitou o número: {numero}")
        break
    except ValueError:
        print("Entrada inválida. Tente novamente.")

# b) Validação em Dados Lidos de Arquivo
dados = ["10", "15.5", "abc", "-20"]
for item in dados:
    try:
        numero = float(item)
        print(f"{numero} é um número válido!")
    except ValueError:
        print(f"{item} não é um número válido.")