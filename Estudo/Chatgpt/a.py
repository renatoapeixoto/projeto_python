import os
os.system('cls')

A = int(input("Digite o limite inferior: "))
B = int(input("Digite o limite superior: "))

# soma = 0
# for i in range (A, B):
#     soma = i + (i+1)
# print(soma)
# exit()
soma = 0
fib = [0, 1]
while fib[-1] <= B:
    fib.append(fib[-1] + fib[-2])
print(fib)





exit()








fibonacci = [0, 1]
while fibonacci[-1] <= B:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print("Números de Fibonacci no intervalo: [", A, ",", B, "]:")
for num in fibonacci:
    if A <= num <= B:
        print(num, end=" ")
