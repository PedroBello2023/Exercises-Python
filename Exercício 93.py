#Exercício 93):

#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

#Resolução do exercício 93):

def area(larg, comp):
    area = larg*comp
    print('-'*30)
    print(f'{"CONTROLE DE TERRENOS":^30}')
    print('-'*30)
    print(f'A area do terreno com as dimensões {larg } x {comp} é {area:.2f} m²;')
    

larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))

area(larg, comp)
