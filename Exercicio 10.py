#Exercício 10):

#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la sabendo que cada litro de tinta pinta uma área de 2m²:

#Resolução do exercício 10):

print('coloque apenas valores, sem a unidade de medida!')
a = float(input('Digite a largura da parede, em metros: '))
b = float(input('Digite a altura da parede, em metros: '))
A = a*b
L = int(A*2)

print('A parede tem uma área de {} m², a quantidade necessária de tinta para pintar esta parede é {}L'.format(A, L))

