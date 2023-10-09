#Exercício 43):

#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

#Resolução do exercício 43):

from time import sleep

for c in range(10, 0-1, -1):
    print(c) 
    sleep(1)
print('BOMM! BOOM! POOW! Felis Ano novo!')
