import tkinter as tk

#8) ler o valor em metros e converter em centímetros e milímetros (fazer interface para esse)
metro = float(input("Digite o valor em metros: "))
cm = metro * 100
mm = metro * 1000
print("{} metros são {} cm e {} mm".format(metro, cm, mm))