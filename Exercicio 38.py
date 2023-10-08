#Exercício 38):

#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM

#– Até 14 anos: INFANTIL

#– Até 19 anos: JÚNIOR

#– Até 25 anos: SÊNIOR

#– Acima de 25 anos: MASTER

#Resolução do exercício 38):

from datetime import date
nasc = int(input('Digite aqui o seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print('Sua idade é {} anos.'.format(idade))
if idade <= 9:
    print('sua categoria é MIRIM!')
elif 9 < idade <= 14:
    print('Sua categoria é INFANTIL!')
elif 14 < idade <= 19:
    print('Sua categoria ŕ JUNIOR!')
elif 19 < idade <= 25:
    print('Sua categoria é SÊNIOR!')
else:
    print('Sua categoria é MASTER!')
