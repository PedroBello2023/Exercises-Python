#Exercício 60):

#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
#Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

#Resolução do exercício 60):


print('-'*30)
print('    Sequencia de Fibonacci')
print('-'*30)
n = int(input('Digite o número de termos que\nvocê quer ver na sequência: '))
a1 = 0
a2 = 1
print('{} => {} =>'.format(a1,a2), end = ' ') 
cont = 3
while cont <= n:
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    cont = cont + 1
    print('{} =>'.format(a3), end = ' ')
print('FIM!')