print("Insira os valores A, B e C em ordem, já o valor D pode ser fora de ordem.")
a = float(input("Insira o valor A: "))
b = float(input("Insira o valor B: "))
c = float(input("Insira o valor C: "))
d = float(input("Insira o valor D: "))

while(a > b or b > c):
    print("\nUm dos três valores estão fora de ordem! Vamos refazer:")
    a = float(input("Insira o valor A: "))
    b = float(input("Insira o valor B: "))
    c = float(input("Insira o valor C: "))
    d = float(input("Insira o valor D: "))

if(d >= c):
    print(f"Os valores em ordem são: {a}, {b}, {c}, {d}")
elif(d >= b and d < c):
    print(f"Os valores em ordem são: {a}, {b}, {d}, {c}")
elif(d >= a and d < b):
    print(f"Os valores em ordem são: {a}, {d}, {b}, {c}")
else:
    print(f"Os valores em ordem são: {d}, {a}, {b}, {c}")