# Format - Aula de Consulta

# Como usar o format para criar formatações personalizadas em prints e textos.

'''
:<		Alinha o texto à esquerda (se tiver espaço na tela para isso)
:>		Alinha o texto à direita (se tiver espaço na tela para isso)
:^		Alinha o texto ao centro (se tiver espaço na tela para isso)
:+		Coloca o sinal sempre na frente do número (independente se é positivo ou negativo)
:,		Coloca a vírgula como separador de milhar
:_		Coloca o _ como separador de milhar
:e		Formato Científico
:f		Número com quantidade fixa de casas decimais
:x		Formato HEX minúscula (para cores)
:X		Formato HEX maiúscula (para cores)
:%		Formato Percentual
'''

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Exemplo de Alinhamento
email = 'lira@gmail.com'
print(f'Meu e-mail não é {email:<30}, show?') # cria 30 espaço e alinha a esquerda

# Exemplo de Edição de Sinal
custo = 500
faturamento = 270
lucro = faturamento - custo
print(f'Faturamento foi {faturamento:+} e lucro foi {lucro:+}')

# Exemplo de Separador de Milhar
custo = 500
faturamento = 270
lucro = faturamento - custo
print(f'Faturamento foi {faturamento:,} e lucro foi {lucro:,}')

# Formato com casas Decimais fixas
custo = 500
faturamento = 270
lucro = faturamento - custo
print(f'Faturamento foi {faturamento:.2f} e lucro foi {lucro:2f}')

#Formato Percentual
custo = 500
faturamento = 1300
lucro = faturamento - custo
margem = lucro / faturamento
print(f'Margem de lucro foi de {margem:.2%}')


'''
Existem módulos/bibliotecas que vão facilitar isso, caso a gente queira, mas 
vamos ver como usar módulos mais a frente do curso. Por enquanto, se você 
precisar, pode fazer substituições em string.
'''

# Formato Moeda -> Combinação de Formatos
custo = 5000
faturamento = 27000
lucro = faturamento - custo
print(f'Faturamento foi R${faturamento:,.2f} e lucro foi R${lucro:,.2f}')

#transformando no formato brasileiro
lucro_texto = f'R${lucro:_.2f}'
print(lucro_texto.replace('.', ',').replace('_', '.'))

# Função round() para arredondar números, caso seja necessário
imposto = 0.15758
preco = 100
valor_imposto = round(preco * imposto, 1)
print(f'Imposto sobre o preço é de {valor_imposto}')