#Exercício 49):

# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Resolução do exercício 49):

n = int(input('Digite um número: '))
soma = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end = ' ')
        soma = soma + 1
    else:
        print('\033[31m', end = ' ')
    print(c, end = ' ')
print('\n\033[mO número {} foi divisível {} vezes!'.format(n, soma))
if soma == 2:
    print('O NÚMERO É PRIMO!')
else:
    print('O NÚMERO NÃO É PRIMO!')