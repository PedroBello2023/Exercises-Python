#Exercício 30):

#Faça um programa que leia 3 números e mostre qual o maior e o menor entre eles;

#Resolução do exercício 30):

a = float(input("Digite o primeiro número: "))
b = float(input('Digite o segundo: '))
c = float(input('Agora o terceiro: '))

if a < b and a < c:
    menor = a
else:
    maior = c
if b < c and b < a:
    menor = b
else:
    maior = a
if c < a and c < b:
    menor = c
else: 
    maior = b
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))