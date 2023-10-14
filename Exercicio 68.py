#Exercício 68):

#Crie um programa que simule o funcionamento de um caixa eletrônico. 
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
    
#Resolução do exercício 68):

print('='*38)
print('{:^30}'.format('BANCO DO PH'))
print('='*38)
valor = int(input('Quanto gostaria de sacar? R$ '))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total = total - ced
        totalced = totalced + 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
        
