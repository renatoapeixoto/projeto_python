import os

os.system('cls')

print('-' * 70)
print('ESTRUTURA DE CONTROLE: CONTINUE')
print('=' * 70)

print()

for c in range(1, 11):
    if c == 5:
        # 5 está fora do loop; se remover a linha abaixo, ele não aparecerá na saída
        # Deixei para verificação!
        print(f'O número {c} está fora do loop')
        continue  # Salta e o ciclo continua

    print(f'O número é {c}')

print('-' * 70)
print()
