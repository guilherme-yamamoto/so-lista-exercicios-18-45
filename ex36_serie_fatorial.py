iterador_serie = int(input("Insira o denominador final da série: "))
res_serie = 1
res_fatorial = 1

for contador in range (1, iterador_serie + 1, 1):
    res_fatorial = 1
    for fatorial in range (contador, 0, -1):
        res_fatorial *= fatorial
    res_serie += (1/res_fatorial)
    print(res_serie)