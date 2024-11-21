#imports
import os
os.system('cls')

print('-'*80)
n = int(input('Digite 1º numero: '))
fatorial = 1
for i in range (2 , n+1) : 
    fatorial *= i
    print(fatorial)