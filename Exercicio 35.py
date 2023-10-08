#Exercício 35):

#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

#– O primeiro valor é maior

#– O segundo valor é maior

#– Não existe valor maior, os dois são iguais

#Resolução do exercício 35):

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('{} é maior que {}.'.format(num1, num2))
elif num1 < num2:
    print('{} é menor que {}.'.format(num1, num2))
else:
    print('Não existe valor maior! Os números são iguais!')