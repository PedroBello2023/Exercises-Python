#Exercicio 92):

#Aprimore o desafio 90 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

#Desafio 90):
#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. 
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

#Resolução do Exercício 92):

dicionario = {}
gols = []
time = []
soma = 0
while True:
    dicionario.clear()
    dicionario['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input('Número de partidas jogadas: '))
    gols.clear()
    for i in range(tot):
        gols.append(int(input(f'Quantos gols ele fez na partida {i+1}?:' )))
    dicionario['Gol por Partida'] = gols[:]
    for i in gols:
        soma += i
    dicionario['Total de Gols'] = soma
    time.append(dicionario.copy())
    while True:
        continuar = str(input('Deseja continuar?[S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor escolha S ou N...')
    if continuar == 'N':
        break
print('=-='*15)
print(f'{"cod nome":<5}{"gols":>17}{"Total":>17}')
print('-'*45)
for k, v in enumerate(time):
    print(f'{k:<3}', end = '')
    for d in v.values():
        print(f'{str(d):<18}', end = '')
    print()
print('-'*45)
while True:
    jogador = int(input('Você quer ver os dados de qual jogador??(999 para encerrar): '))
    if jogador == 999:
        break
    else:
        if jogador > len(time) or jogador < 0:
            print()
            print('Não localizamos esse jogador, por favor tente novamente...')
            break
        for k, v in enumerate(time):
            if jogador == k:
                print()
                print(f'FAZENDO LEVANTAMENTO DO JOGADOR {v['Nome']}...')
                print()
                for i in range(tot):
                    print(f'Na partida {i + 1} fez {v['Gol por Partida'][i]} gols;')
                    print()
print(' ')               
print('>>>>>>>> Encerrando Programa! <<<<<<<<')



