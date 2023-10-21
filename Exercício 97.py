#Exercício 97):

# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

#Resolução do exercício 97):

from random import randint
from time import sleep
numeros = []
par = []
def sorteia(lista):
    print('='*60)
    print('Sorteando os valores: ', end = ' ')
    for i in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}', end = ' ', flush = 'False')
        sleep(0.5)
    print('PRONTO!')
    print()
def somapar():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos valores pares da lista {numeros} é {soma}.')
    print('='*60)
sorteia(numeros)
somapar()


