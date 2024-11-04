#Utilizando o programa anterior como base, faça:

#Crie quatro novas variáveis, cada uma com um tipo de dado diferente e coerente.
#Realize o casting dessas variáveis para novos tipos.
#Utilize f-strings para exibir os valores e os tipos das variáveis, incluindo as que foram alteradas pelo casting.

import os
os.system('cls')

nome = str(input("Digie o Nome: "))
idade =  int(input("Digite a Idade: "))
peso =  float(input("Digite a Peso: "))

print()


print(f"Seu nome é {nome}")
print(f"Sua idade é {idade} anos")
print(f"Seu peso é {peso} kilos")