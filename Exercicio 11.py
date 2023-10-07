#Exercício 11):

#Faça um algoritmo que leia o salãrio de um funcionário e mostre seu novo salário com 15% de aumento:

#Resolução do exercício 11):

print('Use "pontos" ao invés de "vírgulas"!')
a = float(input('Digite aqui o seu salário atual: R$ '))
b = int(input('Digite aqui o reajuste: '))
i = a + (b/100)*a

print('O seu salário com um reajuste de {}% é R$ {:.2f}'.format(b, i))