#Exercício 9):

#Crie um programa que leia o quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar:
#OBS: Considere 1US$ = R$3,27
#Com precisão de duas casas decimais.

#Resolução do exercício 9):

print('Separe o valor por "pontos" ao invés de "vírgulas"!')

i = float(input('Digite aqui, em R$, o valor que você possui em sua carteira: '))

d = i/3.27

print('Você tem um total de US${:.2f} em sua carteira!'.format(d))
