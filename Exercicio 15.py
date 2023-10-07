#Exercício 15):

#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo
#calcule e mostre o comprimento da hipotenusa.

#Resolução do exercício 15) (modo 1):

a = float(input('Digite o comprimento do cateto oposto: '))
b = float(input('agora digite o comprimento do cateto adjacente: '))

c = int(((a**2) + (b**2))**(1/2))

print('O valor da hipotenusa é {:.2f}'.format(c))

#Resolução do exercício 15) (modo 2):

import math

a = float(input('Digite o comprimento do cateto oposto: '))
b = float(input('agora digite o comprimento do cateto adjacente: '))
h = math.hypot(a, b)
print('O valor da hipotenusa é {}'.format(h))

#Resolução do exercício 15) (modo3):

a = float(input('Digite o comprimento do cateto oposto: '))
b = float(input('agora digite o comprimento do cateto adjacente: '))
print('O valor da hipotenusa é {}'.format(math.hypot(a, b)))

