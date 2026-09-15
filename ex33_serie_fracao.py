N = int(input("Insira um número N: "))
resultado = 1
iterar = 1

print(f"Para a série harmônica: 1 + 1/2 + 1/3 + ... + 1/{N}, o resultado será:")

for N in range (1, N, 1):
    iterar += 1
    resultado += (1/iterar)

print(f"{resultado:.3f}")