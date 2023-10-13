#Exercício 65):

#faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

#Resolução do exercício 65) (modo1):

print('='*25)
print('VAMOS JOGAR PAR OU IMPAR')
print('='*25)

from random import choice

cont = 0
while True:
    num = int(input('Digite um número: '))
    jogador = str(input('PAR OU ÍMPAR? ')).upper()
    computador = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    computador = choice(computador)
    cont = cont + 1
    if (num + computador) % 2 == 0:
        if jogador == 'PAR':
            print(f'Você jogou {num} e o computador {computador} e deu {num + computador} portanto PAR!.')
            print('Parabéns, você venceu!')
        else:
            print(f'Você jogou {num} e o computador {computador} e deu {num + computador} portanto PAR!.')
            print('Computador ganhou!')
            break
    else:
        if jogador == 'IMPAR':
            print(f'Você jogou {num} e o computador {computador} e deu {num + computador} portanto IMPAR.')
            print('Parabéns você ganhou!')
        else:
            print(f'Você jogou {num} e o computador {computador} e deu {num + computador} portanto IMPAR.')
            print('O computador ganhou!')
            break
    print('='*25)
print(f'GAME OVER! Você jogou {cont} vezes.')


#Resolução do exercício 65) (modo2):

from random import randint
v = 0
while True:
    jogador = int(input('Digita um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
   
    while tipo not in 'PI':
        tipo = str(input('Você quer par ou impar? ')).strip().upper()[0]
    print(f'Você digitou {jogador} e o computador digitou {computador} resultando em {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            v = v + 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            v = v + 1
        else:   
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você ganhou {v} vezes.')
