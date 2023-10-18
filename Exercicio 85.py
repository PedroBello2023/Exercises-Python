#Exercício 85):

#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

#Resolução do exercício 85):

import random 
from time import sleep


print('='*30)
print('      JOGOS MEGA SENA      ')
print('='*30)
lista = []

for l in range(1, 61):
    lista.append(l)

jog = []
jogos = []


j = int(input('Quantos jogos você quer que sejam gerados? '))
for i in range(j):
    for L in range(1, 7):
        jog.append(random.choice(lista))
        jog.sort()
    jogos.append(jog[:])
    jog.clear()
    print(f'jogo {i + 1}: {jogos[i]}')
    sleep(0.75)
    
    
#Resolução do exercício 85) (modo2):

from random import randint

print('='*30)
print('      JOGOS MEGA SENA      ')
print('='*30)


lista = []
jog = []
jogos = int(input('Quantos jogos você quer que eu gere? '))
tot = 1
while tot <= jogos:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jog.append(lista[:])
    lista.clear()
    tot += 1
print('='*3, 'GERANDO OS NÚMEROS...', '='*4)
sleep(1)
for i, l in enumerate(jog):
    print(f'Jogo {i + 1}: {l}')
    sleep(0.75)
    
        