#Exercício 32)

#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
#se elas podem ou não formar um triângulo.

#Resolução do exercício 32):

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Você pode formar um triângulo com essas medidas!')
else:
    print('Ops!, um triângulo não pode ser formado com essas medidas!')
