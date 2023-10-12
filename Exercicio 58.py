#Exercício 58):

#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

#Resolução do exercício 58):

print('Gerador de PA')
print('=-='*10)

n = 0
a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Agora digite a razão: '))
an = a
while n < 10:
    n = n + 1
    an = a + (n - 1)*r
    print(an, end = ' -> ')
print('FIM!')
