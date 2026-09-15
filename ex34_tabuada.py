N_fixo = int(input("insira um número: "))
tabuada = int(input("Informe até que número vai ser calculada a tabuada: "))

for N_movel in range (0, tabuada + 1, 1):
    print(f"{N_fixo} x {N_movel} = {N_fixo * N_movel}")