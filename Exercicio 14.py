#Exercício 14):

#Crie um programa que leia um número real qualquer pelo teclado e mostre a sua porção inteira:


import math

a = float(input('Digite um número: '))
print('O número {} tem a parte inteira igual a {}'.format(a, math.trunc(a)))

#Resolução do exercício 14) (modo2):

from math import trunc 

a = float(input('Digite um número: '))
print('O número {} tem a parte inteira igual a {}'. format(a, math.trunc(a)))

#Resolução do exercício 14) (modo3):

a = float(input('Digite um número: '))
print('O número {} tem a parte inteira igual a {}'.format(a, int(a)))
