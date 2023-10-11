#Exercício 54):

#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

#Resolução do exercício 54):

n = 0
n = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
if n != 'F' and n != 'M':
    while n != 'F' and n != 'M':
        n = str(input(('Dados inválidos. Por favor, informe seu sexo [F/N]: '))).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(n))