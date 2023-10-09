#Exercício 45):

#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

#Resolução do exercício 3):

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
       soma = soma + c
       cont = cont + 1
print('a soma de todos os {} multiplos de 3 que se encontram no intervalo solicitado é {}.'.format(cont, soma))

