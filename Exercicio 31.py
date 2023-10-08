#Enunciado do problema 31):

#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

#Resolução do exercício 31) (modo1):

salario = float(input('Qual o valor do seu salário: '))
aumento10 = salario*(10/100)
aumento15 = salario*(15/100)
if salario <= 1250:
    print('O seu salário com aumento é de {}'.format(salario + aumento10))
else:
    print('O 256seu salário com aumento é de {}'.format(salario + aumento15))

#Resolução do exercício 31) (modo2):

salario = float(input('Qual o valor do seu salário: '))

if salario <= 1250:
    novo = salario + salario*10/100
else:
    novo = salario + salario*15/100
    
print('Seu salário que era {} agora é {}'.format(salario, novo))