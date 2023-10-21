#Exercício 95):

#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
#Seu programa tem que realizar três contagens através da função criada:                                                                                                               
# a) De 1 até 10, de 1 em 1;                         
# b) De 10 até 0, de 2 em 2;
# c) Uma contagem personalizada;

#Resolução do exercício 95):

from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        print( '-=-' * 10)
        print(f'Contagem de {inicio} a {fim} de {passo} em {passo}:')
        sleep(2)
        cont = 0
        while cont <= fim:
            print(cont, end = ' ', flush = 'False')
            sleep(0.5)
            cont += passo
        print('Fim!')
    else:
        print( '-=-' * 10)
        print(f'Contagem de {inicio} a {fim} de {passo} em {passo}:')
        sleep(2)
        cont = inicio
        while cont >= fim:
            print(cont, end = ' ', flush = 'False' )
            sleep(0.5)
            cont -= passo
        print('Fim!')

contador(1, 10, 1)
contador(10, 0, 2)
print('-=-'*10)
print('Agora é sua vez, escolha como quer fazer sua contagem:')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo a Passo: '))
contador(inicio, fim, passo)
