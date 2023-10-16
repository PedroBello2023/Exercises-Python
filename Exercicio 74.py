#Exercício 74):

#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

#Resolução do exercício 74):

tupla = ('caramelo',  'cuscuz', 'trombete', 'cascalho', 'alface' )
for p in tupla:  
    print(f'\nA palavra {p} tem as vogais:', end = ' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
