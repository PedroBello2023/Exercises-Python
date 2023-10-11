#Exercício 52):

#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

#Resolução do exercício 52):

maior = 0
menor = 0
for kg in range(1, 6):
    peso = float(input('Digite aqui o peso da {}° pessoa em kg: '.format(kg)))
    if kg == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))


