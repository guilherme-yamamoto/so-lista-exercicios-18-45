preco = float(input("Digite o preço atual do seu produto: "))
venda = int(input("Digite a média de vendas mensais do seu produto: "))

if(venda < 500 and preco < 30):
    print(f"O preço do produto deve aumentar em 10%, indo de R${preco:.2f} para R${(preco + preco * 0.10):.2f}")
elif(venda >= 500 and venda < 1000 and preco >= 30 and preco < 80):
    print(f"O preço do produto deve aumentar em 15%, indo de R${preco:.2f} para R${(preco + preco * 0.15):.2f}")
elif(venda >= 1000 and preco >= 80):
    print(f"O preço do produto deve diminuir em 5%, indo de R${preco:.2f} para R${(preco - preco * 0.05):.2f}")
else:
    print(f"O preço continuará igual, valendo R${preco:.2f}")
