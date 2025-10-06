#10) Ler quanto dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar
#consideirando o dolar a $5,31

real = float(input("Digite o valor em real: "))
dolar = real / 5.31
print("R${:.2f} equivalem a US${:.2f} considerando a cotação de US$5,31 por dólar".format(real, dolar))
