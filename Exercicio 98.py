#Exercício 98):

#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

#Resolução do exercício 98):

def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        print(f'Você tem {idade} anos: NÃO VOTA.')
    elif 18 <= idade <= 60:
        print(f'Vôce tem {idade} anos: VOTO OBRIGATÓRIO.')
    else:
        if 16 > idade < 18 or idade > 65:
            print(f'Você tem {idade} anos: VOTO OPCIONAL.')
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

