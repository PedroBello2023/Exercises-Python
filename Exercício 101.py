#Exercício 101):

#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

#Resolução do exercício 101) (modo1):

def leiaint(num):
    while True:
        num = input('Digite um inteiro: ')
        if num.isnumeric():
            return num
            break
        else:
            print('\033[31mERRO! Você digitou um número inválido!\033[m')
            

n = leiaint('Digite um número: ')
print('\033[32mVocê digitou o número {}.\033[m'.format(n))

#Resolução do exercício 101) (modo2):

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input('Digite um inteiro: '))
        if n.isnumeric():
            valor = int(n)
            ok = True
            break
        else:
            print('\033[31mERRO! Você digitou um número inválido!\033[m')
        if ok:
            break
    return valor       

n = leiaint('Digite um número: ')
print('\033[32mVocê digitou o número {}.\033[m'.format(n))

