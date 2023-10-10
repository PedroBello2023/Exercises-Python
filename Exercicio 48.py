#Exercício 48):

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

#Resolução do exercício 48) (modo1):


print('=-='*9)
print('10 PRIMEIROS TERMOS DA PA')
print('=-='*9)

a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))


soma = 0
for c in range(0, 10):
    soma = a + r*c
    print('{}'.format(soma))
    
#resolução do exercício 48) (modo2):

print('=-='*9)
print('10 PRIMEIROS TERMOS DA PA')
print('=-='*9)

a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
an = a + (10) * r

for c in range(a, an, r):
    print(c)
