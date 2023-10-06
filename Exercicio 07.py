#Exercício 7):

#Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

#Resolução do exercício 7):

a = float(input("Digite a medida em metros: "))
c = a/100
m = a/1000

print('A medida digitada convertida para centímetros é igual a {}cm e em milímetros é igual a {}ml.'.format(c, m))
