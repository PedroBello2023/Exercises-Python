#Exercício 13):

#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro curta R$ 60,00 por dia e R$0,15 por km rodado.

#Resolução do exercício 13):

a = int(input('km rodados: '))
b = float(input('Quantidade de dias alugado: '))
i = 60*b + 0.15*a
print('O valor a ser pago pelo aluguel do carro é R${:.2f}'.format(i))