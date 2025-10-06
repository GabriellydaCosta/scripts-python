#12) ler preço do produto e mostrar o novo preço com 5% de desconto

preco = float(input("Digite o preço do produto: "))
desconto = preco - (preco*(5/100))
print("O valor original do produto é R${}, mas com 5% de desconto sai por R${}".format(preco, desconto))