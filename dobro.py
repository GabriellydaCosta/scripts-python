#6) Leia um número e mostre seu dobro, triplo e raiz quadrada

numero = int(input("Digite um número: "))
dobro = numero *2
triplo = numero *3
raiz = numero ** (1/2)

print("O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}".format(numero, dobro, triplo, raiz))