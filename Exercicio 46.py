#Exercício 46):

#Refaça o EXERCÍCIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

#Resolução do exercício 4):

from time import sleep
n = int(input('Digite um número para imprimir sua tabuada: '))
print('A tabuada do número escolhido será ...')
sleep(1)
print('Calculando ... ')
sleep(2)

for c in range(0, 11):
    print('{:2} x {} = {}'.format(c, n, (c * n)))
