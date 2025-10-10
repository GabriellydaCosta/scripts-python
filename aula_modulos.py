
'''
Aula sobre importação de bibliotecas.

import nome da biblioteca -  você importa a biblioteca toda
from nome da biblioteca import - você importa apenas aquele comando específico da biblioteca
'''

'''
Biblioteca math:
import math

Funções dispníveis:
ceil - arredonda pra mais
floor - arredonda pra menos
trunck - elimina da vírgula pra frente
pow - potência
sqrt - raiz quadrada
factorial - fatores

se eu escrever: from math import sqrt, só fica disponível o sqrt de função.

'''


'''
#Importando a biblioteca completa:

import math
numero = int(input("Digite um valor: "))
raiz = math.sqrt(numero)
print("A raiz quadrada de {} é {}. Arredondando pra cima é {}, e arredondando pra baixo é {}".format(numero, raiz, math.ceil(raiz), math.floor(raiz)))
'''

'''
#Importando apenas a função e não o módulo todo

from math import sqrt
from math import floor
from math import ceil
numero = int(input("Digite um valor: "))
raiz = sqrt(numero)
print("A raiz quadrada de {} é {}. Arredondando pra cima é {}, e arredondando pra baixo é {}".format(numero, raiz, ceil(raiz), floor(raiz)))
'''

'''
Random: biblioteca para gerar números aleatórios.
random.random() o computador gera um número aleatório decimal de 0 a 1 toda vez que acionado.
random.randint(1, 10) gera um número inteiro aleatório de 1 a 10
'''

'''
import random
numero_aleatorio = random.random()
print(numero_aleatorio)
'''

'''
import random
numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)
'''

'''
import emoji
print(emoji.emojize("Olá, mundo :kissing_cat:"))
'''

'''
Exercícios:
16) Programa que leia um número real e mostre na tela a parte inteira
17) Programa que leia o cateto oposto e adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
18) Faça um programa que leia um ângulo e mostre na tela o seu seno, cosseno e tangente
19) O professor quer sortear o nome de um dos seus quatro alunos para apagar o quadro. Leia o nome deles e mostre um escolhido aleatório.
20) sortear a ordem em que 4 alunos vão apresentar um trabalho
21) Faça um programa que abra e reproduza o áudio de um arquivo mp3


'''