#Exercício 51):

#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

#Resolução do exercício 51):


from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}° nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
print('Tivemos {} pessoas maiores de idade!'.format(totalmaior))
print('Tivemos {} pessoas menores de idade'.format(totalmenor))