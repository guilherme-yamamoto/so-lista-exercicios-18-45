import math

A = float(input("Insira o coeficiente A: "))
B = float(input("Insira o coeficiente B: "))
C = float(input("Insira o coeficiente C: "))
delta = B**2 - 4 * A * C
x1 = (-B + math.sqrt(delta)) / (2 * A)
x2 = (-B - math.sqrt(delta)) / (2 * A)

if(delta > 0):
    print(f"Existem 2 raízes reais pois delta é maior que zero. Delta vale {delta}, x1 vale {x1:.1f} e x2 vale {x2:.1f}.")
elif(delta == 0):
    print(f"Existe apenas uma raiz real, pois delta é igual a zero. Delta vale {delta}, x vale {x1:.1f}.")
else:
    print(f"Não existe raiz, pois delta é negativo e vale {delta}")