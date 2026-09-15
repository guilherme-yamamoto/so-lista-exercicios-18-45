casa = int(input())
quantia = 0

for i in range (1, casa + 1, 1):
    if(quantia < 1):
        quantia += 1
        print(f"Casa {i}: {quantia} grãos")
        i += 1
    quantia *= 2
    print(f"Casa {i}: {quantia} grãos")