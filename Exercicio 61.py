#Exercício 61):

#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

#Resolução do exercício 68) (modo1)):

n = 0
cont = 0
cont2 = 0
soma = 0
soma2 = 0
while n != 999:
    n = int(input('Digite um número [digite 999 para parar]: '))
    cont = cont + 1
    soma = soma + n
    soma2 = soma - 999
    cont2 = cont - 1
    
print('Condição de parada... Encerrando o programa!')
print('Você digitou {} números e a soma deles é {}'.format(cont2, soma2))

#Resolução do exercício 61) (modo2):

n = cont = soma = 0
n = int(input('Digite um número [digite 999 para parar]: '))
while n != 999:
    soma += n 
    cont += 1
    n = int(input('Digite um número [digite 999 para parar]: '))
print('Condição de parada... Encerrando o programa!')
print('Você digitou {} números e a soma deles é {}'.format(cont, soma))