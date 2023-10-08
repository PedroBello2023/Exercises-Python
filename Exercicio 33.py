#Exercício 33):

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#Resolução do exercício 33):

valor = float(input('Digite aqui o valor da casa:R$ '))
salario = float(input('Digite aqui seu salário:R$ '))
anos = int(input('Digite em quantos anos pretende pagar: '))
parcelas = int(anos * 12)
pagamento = valor/parcelas
print('Para pagar uma casa no valor R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valor, anos, pagamento))

if pagamento <= (30/100)*salario:
    print('Empréstimo AUTORIZADO!')
else:
    print('Emprestimo NEGADO!')