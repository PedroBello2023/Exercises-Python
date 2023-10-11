#Exercício 55):

# Melhore o jogo do EXERCÍCIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

#Resolução do problema 55) (modo1):


from random import randint
from time import sleep

computador = randint(0, 5)


print('-=-'*18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-'*18)
jogador = int(input('Em que número eu pensei? '))
while jogador != computador:
    print('carregando...')
    sleep(3)
    jogador = int(input('Tente novamente: '))
print('carregando...')
sleep(3)
print('O computador escolheu {}'.format(computador))

#Resolução do exercício 55) (modo2):

from random import randint
print('Sou o seu coputador, acabei de pensar em um número entre 0 e 10.')
print('Consegue advinhar?')
computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    palpites = palpites + 1
    jogador = int(input('Qual é o seu palpite? '))
    if computador == jogador:
        acertou = True
    elif computador > jogador:
        print('Mais... tente novamente!')
    elif computador < jogador:
        print('Menos... continue tentado!')
print('Você acertou!')
print('Você tentou {} vezes!'.format(palpites))