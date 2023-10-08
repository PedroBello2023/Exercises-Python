#Exercício 39):

#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

#Resolução do exercício 39):

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    
    if r1 == r2 == r3:
        a = 'EQUILÁTERO'
    elif r1 != r2 != r3:
        a = 'ESCALENO!'
    else:
        a = 'ISÓCELES!'
    print('Você PODE FORMAR um triângulo com essas medidas! Seu triângulo é {}.'.format(a))
else:
    print('Ops!, um triângulo não pode ser formado com essas medidas!')