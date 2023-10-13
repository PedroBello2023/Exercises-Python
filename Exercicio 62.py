#Exercício 62):

#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
#mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

#Resolução do exercício 62):

a = 'S'
m = 0
cont = 0
maior = 0
menor = 0
while a != 'N':
    n = int(input('Digite um número: '))
    cont += 1
    m = (m + n)/cont
    if cont == 1:
         maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    a = str(input('Quer continuar? [S/N]: ')).upper()
print('A média de todos os valores digitados foi {:.2f}'.format(m))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
    