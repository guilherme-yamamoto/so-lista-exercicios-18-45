valor = int(input("Insira um valor inteiro: "))

if(valor % 2 == 0 and valor % 3 == 0):
    print(f"O valor inserido '{valor}' é divisível por 2 e por 3.")
elif(valor % 2 != 0 and valor % 3 == 0):
    print(f"O valor inserido '{valor}' é divisível por 3 mas não é divisível por 2, resultando em {(valor / 2):.2f}")
elif(valor % 3 != 0 and valor % 2 == 0):
    print(f"O valor inserido '{valor}' é divisível por 2 mas não é divisível por 3, resultando em {(valor / 3):.2f}")
else:
    print(f"O valor inserido '{valor}' não é divisível por 2 e nem por 3, resultando em {(valor / 2):.2f} e {(valor / 3):.2f} respectivamente.")