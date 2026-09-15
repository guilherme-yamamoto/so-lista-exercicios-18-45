a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o primeiro valor: "))

while(a == b):
    print("\nOs dois valores são iguais, insira valores diferentes!\n")
    a = int(input("Insira o primeiro valor: "))
    b = int(input("Insira o primeiro valor: "))

if(a > b):
    print(f"Os valores em ordem crescente são: {b}, {a}.")
elif(b > a):
    print(f"Os valores em ordem crescente são: {a}, {b}.")