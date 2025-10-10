#15) leia quantidade de Km percorridos por um carro alugado e a quantidade de dias que foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorrido = float(input("Digite a quantidade de Km percorridos com o carro: "))
dias_alugado = int(input("Digite a quantidade de dias que o carro foi alugado: "))
valor_final = (60*dias_alugado) + (0.15*km_percorrido)
print("O preço a pagar é R${:.2f}".format(valor_final))