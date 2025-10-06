'''Aula sobre operadores aritméticos.
+ = adição
- subtração
* = multiplicação
/ = divisão (aceita decimal)
// = divisão inteira
% = resto da divisão
** = potência
pow(x,y) = potência
x**(1/2) = raiz quadrada
x**(1/3) = raiz cúbica
'''


'''
Operadores:
'oi'+'olá' = oiolá
'oi'*5 = oioioioioi 
=*3 é ===
'''


'''
print('='*20)

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
'''


'''
print('Prazer em te conhecer {:>20}!'.format(nome))
Escreve o nome em 20 espaços mas com o vazio na frente


print('Prazer em te conhecer {:<20}!'.format(nome))
Escreve o nome com 20 espaços mas com o vazio atrás

print('Prazer em te conhecer {:=^20}!'.format(nome))
Escreve o nome em 20 espaços ficando centralizado no meio e o restante com =
'''


'''
Quando o valor vai ser usado só uma vez. 
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))
'''

'''
Quando o valor precisa ser utiizado mais de uma vez
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
print('A soma vale {}'.format(n1+n2))
'''


'''
#a divisão é {:.2f} - mostra a divisão apenas com 2 casas decimais
#end ='' não quebra a linha e o print fica junto
#\n quebra a linha

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, \n o produto é {} \n e a divisão é {:.2f}'.format(s, m, d), end =' >>> ')
print('A divisão inteira é {} e a potência é {}'.format(di, e))
'''

'''
Fazer os seguintes exercícios:
5) programa que leia um número inteiro e mostre seu antecessor e sucessor
6) Leia um número e mostre seu dobro, triplo e raiz quadrada
7) Ler duas notas de um aluno e calcular sua média
8) ler o valor em métros e converter em centímetros e milímetros (fazer interface para esse)
9) ler um número inteiro qualquer e mostrar na tela sua tabuada
10) Ler quanto dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar
11) ler largura e altura de uma parede em metros e calcular area e quantidade de tinta para pintar. 1l pinta 2m² (fazer interface para esse)
12) ler preço do produto e mostrar o novo preço com 5% de desconto
13) ler salário do funcionário e mostrar novo salário com 15% de aumento
14) Conversão de graus de celsius para fahrenhit
15) leia quantidade de Km percorridos por um carro alugado e a quantidade de dias que foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''


