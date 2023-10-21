#Exercício 99):

# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

#Resoluçaõ do exercício 99):

def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial do número n:
    :para n: O numero a ser calculado o fatorial;
    :para show: (opcional) se você quer que mostre o calculo do fatorial ou nao;
    :rturn: Retorna o valor do fatorial de n;
    """
    f=1
    for c in range(n, 0, -1):
        if show == True:
            print(f'{c}', end = ' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f
            

print(fatorial(5, False))

help(fatorial)
