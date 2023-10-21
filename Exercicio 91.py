#Exercíio 91):

#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
#No final, mostre: 
#A) Quantas pessoas foram cadastradas 
#B) A média de idade 
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

#Resoluçaõ domexercício 91):

dados = {}
galera =[]
mulheres = []
idademaior = []
soma = media = 0

#Leitura dos dados;
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))
    while True:
        dados['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['Sexo'] == 'F':
            mulheres.append(dados['Nome'])
        if dados['Sexo'] in 'MF':
            break
        print('ERRO! Por favor escolha entre M ou F...')
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    galera.append(dados.copy())
    while True:
        continuar = str(input('Quer que continue? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Escolha entre S ou N...')
    if continuar == 'N':
        break
#Análise dos dados;
print('=-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas;')
media = soma/len(galera)
print(f'B) A media de idade é de {media:5.2f} anos;')
print(f'C) As mulheres cadastradas nesta pesquisa são {mulheres};')
print('=-='*30)
for p in galera:
    if p['Idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v};', end = ' ')
        print()
print('\n>>>>> Programa Encerrado <<<<<')



        
    





            
    





    
 