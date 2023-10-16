#Exercício 71):

#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

#Resolução do exercício 71):

from random import randint
maior = 0
menor = 0
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números gerados foram:', end = ' ')
for n in numeros:
    print(f'{n}', end = ' ')
print(f'\nO maior valor sorteado foi o {max(numeros)}')
print(f'O menor valor sorteado foi o {min(numeros)}')
