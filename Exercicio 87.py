#Exercício 87):

#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
#No final, mostre o conteúdo da estrutura na tela.

#Resolução do exercício 87)(modo1):


dicionario = {}

dicionario['nome'] = str(input('Qual o nome do aluno? '))
dicionario['media'] = float(input(f'Qual a média de {dicionario["nome"]}? '))

print('=-='*15)
print(f'- O nome do aluno é {dicionario["nome"]}')
print(f'- A média de {dicionario["nome"]} é {dicionario["media"]}')
if dicionario['media'] >= 7:
    print(f'- {dicionario["nome"]} está APROVADO!')
elif 5 <= dicionario['media'] < 7:
    print(f'- {dicionario["nome"]} está de RECUPERAÇÃO!')
else:
    print(f'- {dicionario["nome"]} está REPROVADO!')


#Resolução do exercício 87) (modo2):

dicionario = {}

dicionario['Nome'] = str(input('Qual o nome do aluno? '))
dicionario['Media'] = float(input(f'Qual a média de {dicionario["Nome"]}? '))

print('=-='*15)
if dicionario['Media'] >= 7:
    dicionario['situação'] = 'Aprovado'
elif 5 <= dicionario['Media'] < 7:
    dicionario['situação'] = 'Recuperação'
else:
    dicionario['situação'] = 'Reprovado'
    
for k, v in dicionario.items():
    print(f'- {k} é igual a {v}')
    
