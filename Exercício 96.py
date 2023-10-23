#Exercício 96):

#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

#Resolução do exercício 96):

from time import sleep
def maior(* num):
    numeros = []
    print('='*45)
    print('Analisando os valores...')
    sleep(2)
    for i in num:
       print(i, end = ' ', flush = 'False')
       sleep(0.5)
       numeros.append(i)
    print()
    print(f'foram informados {len(numeros)} valores ao todo.')
    sleep(2)
    for i in range(0, len(numeros)):
        if i == 0:
            maior  = numeros[i]
        else:
            if numeros[i] > maior:
                maior = numeros[i]
    print(f'O maior valor dentre os valores informados é {maior}.')
    print('='*45)

maior(8, 2, 45, 4)
maior(1, 3, 6, 78, 756, 34)
maior(3, 6, 5, 98, 756, 453, 1234)