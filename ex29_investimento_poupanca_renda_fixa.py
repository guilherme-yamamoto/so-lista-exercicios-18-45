tipo_investimento = str(input("Digite o tipo de investimento a ser realizado:\nPoupança = Digite '1' | Renda Fixa = Digite '2'\n"))

while(tipo_investimento != "1" and tipo_investimento != "2"):
    print("\nErro, tente novamente.")
    tipo_investimento = str(input("Digite o tipo de investimento:\nPoupança = Digite '1' | Renda Fixa = Digite '2'\n"))

valor_investido = float(input("\nDigite o valor a ser investido: "))

if(tipo_investimento == "1"):
    print(f"Ao investir R${valor_investido:.2f} na poupança (3% mensal), o valor corrigido em 30 dias será de R${(valor_investido + valor_investido * 0.03):.2f}.")
elif(tipo_investimento == "2"):
    print(f"Ao investir R${valor_investido:.2f} na renda fixa (5% mensal), o valor corrigido em 30 dias será de R${(valor_investido + valor_investido * 0.05):.2f}.")