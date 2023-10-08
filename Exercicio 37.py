
#Exercício 37):

#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

#Resolução do exercício 5):

n1 = float(input('Digite aqui a sua primeira nota: '))
n2 = float(input('Digite aqui a sua segunda nota: '))

media = (n1 + n2)/2
print('Sua média final é {:.2f}'.format(media))

if media < 5:
    print('REPROVADO!')
elif 5 <= media < 7:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')