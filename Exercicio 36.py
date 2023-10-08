#Exercício 36):

#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
#se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#resolução do exercício 36):

from datetime import date 

nasc = int(input('Digite aqui seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos de idade!'.format(nasc, idade))
if idade < 18:
    print('Você ainda vai se alistar no serviço militar! Faltam {} anos para você se alistar.'.format(18 - idade))
elif idade == 18:
    print('E a hora exata de se alistar!')
else:
    print('Ja passou do tempo do alistamento! Se passaram {} anos da data certa para o seu alistamento.'.format(idade - 18))
