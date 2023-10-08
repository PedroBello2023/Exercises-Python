#Exercício 34):

#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

#Resolução do exercício 34):

n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] Converter para binário;\n[2] Converter para octal;\n[3] Converter para hexadecimal;''')
opção = int(input('Digite sua opção: '))
if opção == 1:
    print('{} convertido para binário é {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} convertido para octal é {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida!')
