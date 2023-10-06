#Exercício 5):

#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada:

#Resolução do exercício 5) (modo1):

a = int(input('Digite um valor: '))
d = 2*a
t = 3*a
r = a**(1/2)
print('O dobro do valor digitado é {}. \n O triplo do mesmo é {}. \n A raiz desse valor é {}.'.format(d, t, r))

#Resolução do exercício 5) (modo2):

a = int(input('Digite um valor: '))
print(' O dobro do valor digitado é {}. \n O triplo do mesmo é {}. \n A raiz desse valor é {:.2f}.'.format((2*a), (3*a), (a**(1/2))))

#Resolução do exercício 5) (modo3):

a = int(input('Digite um valor: '))
print(' O dobro do valor digitado é {}. \n O triplo do mesmo é {}. \n A raiz desse valor é {:.2f}.'.format((2*a), (3*a), pow(a, (1/2))))

