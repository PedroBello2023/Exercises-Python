#Exercício 66):

#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.

#Resolução do exercício 66):

tot18 = 0
masc = 0
fem = 0

while True:
    idade = int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Qual seu sexo [M/F]? ')).upper().strip()[0]
    if idade >= 18:
        tot18 = tot18 + 1
    if sexo == 'M':
        masc = masc + 1
    if sexo == 'F' and idade < 20:
        fem = fem + 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar [S/N]? ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18};')
print(f'O total de homens cadastrados nesta pesquisa: {masc};')
print(f'O total de mulheres com menos de 20 anos: {fem}')
