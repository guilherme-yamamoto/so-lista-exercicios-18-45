nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terça nota: "))
nota4 = float(input("Insira a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4 

if(media >= 6):
    print(f"Sua média é {media}. Você foi APROVADO.")
elif(media < 6 and media >= 3):
    print(f"Sua média é {media}. Você está de RECUPERAÇÃO.")
else:
    print(f"Sua média é {media}. Você se f*deu, está RETIDO")