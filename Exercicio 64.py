#Exercício 64):

#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
#O programa será interrompido quando o número solicitado for negativo.

#Resolução do exercício 64):
print('=-='*12)
T = 'TABUÀDA'
print(f'{T:^38}')
print('=-='*12)
cont = 0
p = 0

while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    print('-' * 12)
    for cont in range(1, 11):
        p = cont *n 
        print(f'{n} x {cont:>2} = {p}')
    print('-' * 12)
print('Você digitou um número negativo! ENCERRANDO O PROGRAMA...')
    


