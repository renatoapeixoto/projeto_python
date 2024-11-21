import os
os.system('cls')

for i in range (1,6):
    for j in range (1,i+1):
        print(f'{j}',end='')
    for l in range (i-1,0,-1):
        print(f'{l}',end='')
    print()

# triangulo = []
# for i in range (1,6):
#     num = []
#     for j in range (1,i+1):
#         num.append(j)
#     for l in range (i-1,0,-1):
#         num.append(l)
#     triangulo.append(num)        
#     print(f'{triangulo[i-1]}')