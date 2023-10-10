#Exercício 47):

#Desenvolva um programa que leia seis números inteiros e
#mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

#Resolução do exercício 47):

soma = 0
cont = 0
for c in range(1, 7):
    c = int(input('Digite o {}° número: '.format(c)))
    if c % 2 == 0:
        soma = soma + c
        cont = cont + 1
print('Você informou {} números PARES e a soma deles é {}.'.format(cont, soma))