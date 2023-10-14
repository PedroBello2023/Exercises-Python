#Exercício 67):


#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.


#Resolução do exercício 67):

print('='*18)
print('  LOJAS DO PEDRO')
print('='*18)

preço = 0
p = 0
soma = 0
menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome produto: '))
    preço = float(input('Preço do Produto R$: '))
    cont = cont + 1
    soma = soma + preço
    if preço >= 1000:
        p = p + 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O total gasto nas compras é de R$ {soma:.2f};')
print(f'Um total de {p} produtos da sua lista de compras custa acima de R$ 1000,00;')
print(f'O produto mais barato da sua lista custa R${menor} e foi o {barato};')
