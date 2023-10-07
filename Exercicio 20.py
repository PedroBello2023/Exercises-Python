#Exercício 20):

#Faça um programa que leia um número de 0 até 999 e mostre na tela cada um dos dígitos separados:

#Resolução do exercício 20):

v = int(input('Digite, aqui, um valor de 0 a 9999: '))
u = int(v/1%10)
d = int(v/10%10)
c = int(v/100%10)
m = int(v/1000%10)
print('Analisando o número {}.'.format(v))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
