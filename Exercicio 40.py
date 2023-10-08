#Exercício 40):

#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida

#Resolução do exercício 40):

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))
ICM = peso /(altura**2)
print('Seu ICM é {:.1f}.'.format(ICM))
if ICM < 18.5:
    print('ABAIXO DO PESO!')
elif 18.5 <= ICM < 25: 
    print('PESO IDEAL!')
elif 25 <= ICM < 30:
    print('SOBREPESO!')
else:
    print('OBESIDADE MOŔBIDA!')