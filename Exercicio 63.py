#Exercício 63):

#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

#Resolução do Exercício 63):

soma = cont = 0
while True: 
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print(f'Você digitou {cont} números e a soma deles foi {soma}.')


