#Exercício 8):

#Faça um programa que leia um número inteiro qualquer e mostre sua tabuada.

#Resolução do exercício 8) (modo1):

a = int(input('Digite um número para ver a sua tabuada: '))

b1 = 2*a
b2 = 3*a
b3 = 4*a
b4 = 5*a
b5 = 6*a
b6 = 7*a
b7 = 8*a
b8 = 9*a
b9 = 10*a

print('A tabuada do número {} é:'.format(a))
print( "-"*10)
print(' 1x{:2}={}\n'.format(a, a),'2x{:2}={}\n'.format(a, b1),'3x{:2}={}\n'.format(a, b2),'4x{:2}={}\n'.format(a, b3),'5x{:2}={}\n'.format(a, b4),
'6x{:2}={}\n'.format(a, b5),'7x{:2}={}\n'.format(a, b6),'8x{:2}={}\n'.format(a, b7),'9x{:2}={}\n'.format(a, b8), '10x{}={}'.format(a, b9))
print( "-"*10)

#Resolução do exercício 8) (modo2):

a = int(input('Digite um número para ver a sua tabuada: '))

print('-'*10)
print('{}x{:2}={}'.format(1, a, 1*a))
print('{}x{:2}={}'.format(2, a, 2*a))
print('{}x{:2}={}'.format(3, a, 3*a))
print('{}x{:2}={}'.format(4, a, 4*a))
print('{}x{:2}={}'.format(5, a, 5*a))
print('{}x{:2}={}'.format(6, a, 6*a))
print('{}x{:2}={}'.format(7, a, 7*a))
print('{}x{:2}={}'.format(8, a, 8*a))
print('{}x{:2}={}'.format(9, a, 9*a))
print('{}x{}={}'.format(10, a, 10*a))
print('-'*10)
