#Exercício 19):

#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas;
#O nome com todas as letras minúsculas;
#Quantas letras ao todo sem considerar espaços;
#Quantas letras tem o primeiro nome;

#Resolução do exercício 19) (modo1):

nome = str(input('Digite seu nome aqui: ')).strip()
print('Prazer {}!'.format(nome))
print('Seu nome com letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem um total de {} letras sem espaços.'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome têm {} letras.'.format(nome.find(' ')))

#Resolução do exercício 19) (modo2):

ome = str(input('Digite seu nome aqui: ')).strip()
print('Prazer {}!'.format(nome))
print('Seu nome com letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem um total de {} letras sem espaços.'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome têm {} letras.'.format(len(nome.split()[0])))
