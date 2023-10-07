#Exercício 12):

#Faça um programa que converta uma temperatura digitada em C° e converta para F:

#Resolução do exercício 12):

print('Use pontos ao invés de vírgulas: ')
a = float(input("Digite a temperatura aqui: "))
b = a*(9/5) + 32

print('Sua temperatura de {}° equivalem a {}F!'.format(a, b))