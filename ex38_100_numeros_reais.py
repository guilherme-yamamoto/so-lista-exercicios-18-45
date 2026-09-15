print("Insira 100 valores inteiros reais:")
i = 0
maior = 0
menor = float("inf")

while(i < 20):
    i += 1
    inserir_valor = input(f"{i}° valor: ")
    while(inserir_valor == "" or int(inserir_valor) < 0):
        print("Erro, tente novamente.")
        inserir_valor = input(f"{i}° valor: ")
    inserir_valor = int(inserir_valor)
    
    if(inserir_valor > maior):
        maior = inserir_valor
    elif(inserir_valor < menor):
        menor = inserir_valor
print(f"O maior valor é: {maior}.\nO menor valor é: {menor}.")