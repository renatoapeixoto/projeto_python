import os


os.system('cls')

print('ANO BISSEXTO')
print('-'*70)

ano = int(input('Entre com o ano: '))

if ano <= 0:
    print('Ano inválido!')
else:
    if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
        print(f'O ano {ano} é bissexto!')
    else:
        print(f'O ano {ano} não é bissexto!') 

print('-'*70)