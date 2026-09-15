N = int(input("Informe até qual termo será calculado a sequência de Fibonacci: "))
print("OBS: O 1° termo começará no 1 ao invés de 0")
res1 = 1
res2 = 0
res3 = 0

for N in range (0, N):
    res3 = res1 + res2
    print(f"{N}° termo: {res3}")
    res1 = res2
    res2 = res3