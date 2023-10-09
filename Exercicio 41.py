#Exercício 41):

#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros

#Resolução do exercício 41):

print('='*10, 'LOJA DO PEDRÃO', '='*10)
preço = float(input('Preço das compras:R$ '))
print('FORMA DE PAGAMENTO')
print('[1] à vista dinheiro/cheque')
print('[2] à vista no cartão')
print('[3] em até 2x no cartão')
print('[4] 3x ou mais no cartão')
opção = int(input('Qual a opção? '))
if opção == 1:
    print('Sua compra não será parcelada... Portando você receberá um desconto de 10% no valor da compra!')
    print('O valor a ser pago é de {}'.format(preço - preço*(10/100)))
elif opção == 2:
    print('Sua compra será a vista no cartão...Portanto ganhará um desconto de 5% no valor da compra!')
    print('O valor a ser pago, com desconto, é {}.'.format(preço - preço*(5/100)))
elif opção == 3:
    print('Você irá pagar de até 2x de R${} no cartão, logo pagará o valor formal!'.format(preço/2))
    print('O valor a ser pago é de {}'.format(preço))
else:
    parcelas = int(input('De quantas vezes? '))
    print('Você irá parcelar o valor em {}x de R${}.'.format(parcelas, (preço + preço*(20/100))/parcelas))
    print('O valor total a ser pago com juros é de R${}.'.format((preço + preço*(20/100))))