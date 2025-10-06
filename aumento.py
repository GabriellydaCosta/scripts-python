#13) ler salário do funcionário e mostrar novo salário com 15% de aumento

salario = float(input("Digite o valor do seu salário: "))
aumento = salario + (salario*(15/100))
print("O salário sem aumento é R${}. Com aumento de 15% fica R${}".format(salario, aumento))