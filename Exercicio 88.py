#Exercício 88):

#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

#Resolução do exercício 88):

from random import randint
from time import sleep
ranking = []
dado = {'jogador 1': randint(1, 6), 'jogador 2': randint(1 ,6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
print('Valores sorteados:')
for i, v  in dado.items():
    print(f'O jogador {i} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(dado.items(), key = lambda x: x[1], reverse = True)
print('=-='*15)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
for i in range(len(ranking)):
    print(f' -{i + 1}° lugar: {ranking[i][0]} com {ranking[i][1]}.')
    sleep(1)
print('=-='*15)
print(f'{"FIM DO PROGRAMA!":^30}')