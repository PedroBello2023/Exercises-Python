#Exercício 57):

#Faça um programa que leia um número qualquer e mostre o seu fatorial. 

#Resolução do exercício 57) (modo1):


from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))

#Resolução do exercício 57) (modo2):


n = int(input('Digite um número: '))
c = n
f = 1
print('Calculando ... {}! = '.format(c), end = '')
while c > 0:
    print(c, end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f = f*c
    c = c - 1
print(f)