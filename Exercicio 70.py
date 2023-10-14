#Exercício 70):


#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time da Cuiabá.

#Resolução do exercício 70):

times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo' 'Bragantino',
'Fluminense', 'Athletico-PR', 'Fortaleza', 'Atlético-MG', 'Cuiabá', 'Cruzeiro', 'Internacional',
'São Paulo', 'Corinthians', 'Bahia', 'Goiás', 'Santos', 'Vasco', 'América-MG', 'Coritiba')


print('='*35)
print(f'Lista dos times do brasileirão:{times}')
print('='*35)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('='*35)
print(f'Os ultimos 4 colocados são: {times[-4:]}')
print('='*35)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('='*35)
print(f'O Cuiabá está na {times.index("Cuiabá")}° posição da lista.')
print('='*35)
