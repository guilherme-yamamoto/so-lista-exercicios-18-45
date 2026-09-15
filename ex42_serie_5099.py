numerador = 1
denominador = 1
valor_final = 0

for i in range (0, 50, 1):
    valor_final += (numerador/denominador)
    print(f"+ {numerador} / {denominador} = {valor_final:.3f}")
    numerador += 1
    denominador += 2