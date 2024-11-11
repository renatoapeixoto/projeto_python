A = int(input("Digite o limite inferior: "))
B = int(input("Digite o limite superior: "))

fibonacci = [0, 1]
while fibonacci[-1] <= B:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print("Números de Fibonacci no intervalo [", A, ",", B, "]:")
for num in fibonacci:
    if A <= num <= B:
        print(num, end=" ")
