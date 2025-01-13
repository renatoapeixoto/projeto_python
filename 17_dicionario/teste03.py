# # Exercício 5
# Uma empresa está analisando os resultados de vendas do 1º semestre de 2022 e 2023
# Qual foi o % de crescimento de cada mês de 2023 em relação a 2022?
# Depois de calcular isso, calcule o valor total de crescimento de 2023 em relação a 2022
vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    percentual = valor_23 / valor_22 - 1
    print(f"Em {mes}, a variação percentual foi de: {percentual:.1%}")

total_22 = sum(vendas_22.values())
total_23 = sum(vendas_23.values())
crescimento = total_23 / total_22 - 1
print(f"Crescimento Real: {crescimento:.1%}")

# Exercício 6 - Desafio
# No final da reunião de apresentação dos números, seu chefe perguntou:
# E se nos meses de 2023 que a gente vendeu menos do que 2022 a gente tivesse pelo menos empatado com 2022 (ou seja, se nos meses de 2023 em que as vendas foram menores do que o mesmo mês em 2022, o valor de vendas tivesse sido igual a 2022)
# Qual teria sido o nosso crescimento de 2023 frente a 2022?


# existem várias formas de fazer, aqui resolvemos editar o dicionario de vendas_23 quando o valor dele era menor do que vendas_22, para depois de editado recalcularmos o crescimento
for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    percentual = valor_23 / valor_22 - 1
    if percentual < 0:
        vendas_23[mes] = valor_22
    print(f"Em {mes}, a variação percentual foi de: {percentual:.1%}")

total_22 = sum(vendas_22.values())
total_23 = sum(vendas_23.values())
crescimento = total_23 / total_22 - 1
print(f"Crescimento simulado: {crescimento:.1%}")