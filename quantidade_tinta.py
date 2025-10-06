'''11) ler largura e altura de uma parede em metros e calcular area e quantidade de tinta para pintar. 1l pinta 15m²  de acordo
com o site https://www.suvinil.com.br/blog/um-litro-de-tinta-pinta-quantos-metros-quadrados (fazer interface para esse)'''

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
qtd_tinta = area / 15
print("A área total da parede é {:.1f}m², e a quantidade de tinta em litros necessária para pintar a parede é {:.1f}L".format(area, qtd_tinta))