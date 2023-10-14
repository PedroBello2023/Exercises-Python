#Exercício 69):

#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

#Resolução do exercício 69):

num = ('zero', 'um', 'dois', 'três', 'quatro',
'cinco', 'seis', 'sete', 'oito',
'nove', 'dez', 'onze', 'doze', 'treze',
'quatorze', 'quinze', 'dezesseis', 'dezesete',
'dezoito', 'dezenove', 'vinte')
    
numero = int(input('Digite um número de 0 a 20: '))
while True:
    if numero < 0 or numero > 20:
        numero = int(input('Tente novamente. Digite um número de 0 a 20: '))
    else:
        break
print(f'O número que você digitou é {numero} e por extenso se escreve {num[numero]}.')

#Resolução do exercício 72) (modo2):
num = ('zero', 'um', 'dois', 'três', 'quatro',
'cinco', 'seis', 'sete', 'oito',
'nove', 'dez', 'onze', 'doze', 'treze',
'quatorze', 'quinze', 'dezesseis', 'dezesete',
'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente!', end = ' ')
print(f'O número que você digitou é o {num[numero]}.')
