n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
res = 0

if(n1 > n2):
    n1, n2 = n2, n1

for n1 in range (n1 + 1, n2, 1):
    if(n1 % 2 != 0):
        res += n1
        print(n1, end=" ")
print(f"= {res}")