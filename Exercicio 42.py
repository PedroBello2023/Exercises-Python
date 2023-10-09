#Exercício 42):

#Crie um programa que faça o computador jogar Jokenpô com você.

#Resolução do exercício 42):

import time


print('Suas opções!')
print('''
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')


from random import randint

itens = ('PEDRA', 'PAPEL', 'TESOURA')

computador = randint(0, 2)


jogador = int(input('Qual é a sua jogada: '))
time.sleep(1)
print('\nJO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO\n')


if computador == jogador:
    
    print('=-'*12)
    print('Computador jogou {}.'.format(itens[computador]))
    print('Jogador jogou {}.'.format(itens[jogador]))
    print('=-'*12)
    print('\nEMPATE')
    
else:
    if computador < jogador:
        
        print('=-'*12)
        print('Computador jogou {}.'.format(itens[computador]))
        print('Jogador jogou {}.'.format(itens[jogador]))
        print('=-'*12)
        print('\nCOMPUTADOR VENCEU!')
        
        
    else:
        
        print('=-'*12)
        print('Computador jogou {}.'.format(itens[computador]))
        print('Jogador jogou {}.'.format(itens[jogador]))
        print('=-'*12)
        print('\nJOGADOR VENCEU!')