#Exercício 90):

#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. 
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

#Resolução do Exercício 90):

dicionario = {}
gols = []
soma = 0
dicionario['nome'] = str(input('Nome do Jogador: '))
tot = int(input('Número de partidas jogadas: '))
for i in range(tot):
    gols.append(int(input(f'Quantos gols ele fez na partida {i+1}?:' )))
dicionario['Gol por Partida'] = gols[:]
for i in gols:
    soma += i
dicionario['Total de Gols'] = soma
print('=-='*30)
print(dicionario)
print('=-='*30)
for k, v in dicionario.items():
    print(f' - O campo {k} tem o valor {v}.')
print('=-='*30)
print(f' - O jogador {dicionario["nome"]} jogou {tot} partidas.')
for i, v in enumerate(dicionario["Gol por Partida"]):
    print(f' => na partida {i +1} fez {v} gols.')
print(f' - Foi um total de {dicionario["Total de Gols"]} gols em todas as partidas.')
print('=-='*30)
