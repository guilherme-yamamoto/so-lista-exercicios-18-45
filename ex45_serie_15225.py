numerador = 2
denominador = 2
valor_final = 1

for i in range (0, 14, 1):
    valor_anterior = valor_final
    if(i % 2 == 0):
        valor_final -= (numerador/denominador**2)
        print(f"{valor_anterior:.4f} - {numerador}/{denominador**2} = {valor_final:.4f}")
    elif(i % 2 != 0):
        valor_final += (numerador/denominador**2)
        print(f"{valor_anterior:.4f} + {numerador}/{denominador**2} = {valor_final:.4f}")
    numerador += 1
    denominador += 1