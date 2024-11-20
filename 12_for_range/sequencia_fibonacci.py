import os
os.system('cls')

A = int(input("Digite o limite inferior: "))
B = int(input("Digite o limite superior: "))
fib = [0, 1]
while fib[-1] <= B:
    fib.append(fib[-1] + fib[-2])
print(fib)
for item in fib:
    if A <= item <= B:
        print(item)
    

# fibonacci = [0, 1]
# while fibonacci[-1] <= B:
#     fibonacci.append(fibonacci[-1] + fibonacci[-2])

# print("Números de Fibonacci no intervalo: [", A, ",", B, "]:")
# for num in fibonacci:
#     if A <= num <= B:
#         print(num, end=" ")
