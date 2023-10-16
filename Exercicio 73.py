#Exercicio 73):

#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

#Resolução do exercício 73):

print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)
tupla = ('Macarrão', 6.70, 
'Feijão', 7.20, 'Arroz', 5.50, 'ovo', 12.50, 'Picanha', 120.00)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end = '')
    else:
        print(f'R${tupla[pos]:>7.2f}')
print('-'*40)
