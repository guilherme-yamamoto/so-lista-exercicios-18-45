dado1 = 0
dado2 = 7

for i in range (0, 7, 1):
    dado1 += 1
    dado2 -= 1
    if dado1 > 6:
        break

    if(dado1 + dado2 == 7):
        print(f"{dado1} + {dado2} = 7")