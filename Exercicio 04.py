#Exercício 4):

#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

#Resolução do exercício 4):

a = int(input('Digite um valor: '))
S = a + 1
A = a - 1
print('O antecessor do número escolhido é {} e o sucessor é {}!'.format(A, S))

#Resolução do exercício 4) (modo2):

a = int(input('Digite um valor: '))

print('O antecessor do número escolhido é {} e o sucessor é {}!'.format((a-1), (a+1))) 

