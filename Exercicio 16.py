#Exercício 16):

#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

#Resolução do exercício 16) (modo1):

import math
a = float(input('Digite o valor do ângulo aqui: '))
sen = math.sin(math.radians(a))
coss = math.cos(math.radians(a))
tan = sen/coss

print('O sen{} é {:.2f}'.format(a, sen))
print('O coss{} é {:.2f}'.format(a, coss))
print('A tan{} é {:.2f}'.format(a, tan))

#Resolução do exercício 16) (modo2):

a = float(input('Digite o valor do ângulo aqui: '))
sen = math.sin(math.radians(a))
coss = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print('O sen{} é {:.2f}'.format(a, sen))
print('O coss{} é {:.2f}'.format(a, coss))
print('A tan{} é {:.2f}'.format(a, tan))
