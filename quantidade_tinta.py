#11) ler largura e altura de uma parede em metros e calcular area e quantidade de tinta para pintar. 1l pinta 2m² (fazer interface para esse)

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
qtd_tinta = area / 2
print("A área total da parede é {:.1f}m², e a quantidade de tinta em litros necessária para pintar a parede é {:.1f}L".format(area, qtd_tinta))