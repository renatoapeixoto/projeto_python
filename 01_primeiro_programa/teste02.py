import os
os.system('cls')

tri = [1]
for i in range (1,6):
    for j in range (1,i+1):
        print(f'{j}',end='')
        for r in range(i-1,0,-1):
            print(r)