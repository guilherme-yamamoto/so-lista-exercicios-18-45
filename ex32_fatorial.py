valor = int(input("Insira o número inteiro: "))
resultado: int = 1
i = valor

for valor in range (valor, 1, -1):
    resultado *= valor

print(f"\n{i}! = {resultado}")