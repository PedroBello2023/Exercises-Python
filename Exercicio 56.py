#Exercício 56):

#Crie um programa que leia dois valores e mostre um menu na tela:

#[ 1 ] somar

#[ 2 ] multiplicar

#[ 3 ] maior

#[ 4 ] novos números

#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.

a = int(input('Digite um valor: '))
b = int(input('Digite um segundo valor: '))
print('-=-'*14)

sair = False
while not sair:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    print('-=-'*14)
    opção = int(input('Escolha uma opção das listadas acima: '))
    if opção <= 5:
        if opção == 5: 
            sair = True
            print('Saindo do programa...Tchau Tchau!')
        else:
            if opção == 1:
                print('A soma entre {} e {} é {}.'.format(a, b, a + b))
                print('-=-'*14)
            elif opção == 2:
                print('O produto entre {} e {} é {}.'.format(a, b, a * b))
                print('-=-'*14)
            else:
                if a > b and opção == 3:
                    print('O maior entre os valores digitados é {}.'.format(a))
                    print('-=-'*14)
                else:
                    print('O maior entre os valores digitados é {}.'.format(b))
                    print('-=-'*14)
                if opção == 4:
                    a = int(input('Digite um novo valor: '))
                    b = int(input('Digite um segundo valor: '))
    else:
        print('\033[031mOPS! Não temos essa opção. Verifique as opções e tente novamente!\033[0m')
        print('-=-'*14)