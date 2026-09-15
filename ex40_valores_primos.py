valor1 = int(input("Insira o 1° valor: "))
valor2 = int(input("Insira o 2° valor: "))

if(valor1 > valor2):
    valor1, valor2 = valor2, valor1

for atual in range (valor1, valor2 + 1):
    primo = True
    if(atual < 2):
        primo = False

    for num in range (2, atual):
        if(atual % num == 0):
            primo = False
            break
    if(primo == True):
        print(f"{atual} é primo")