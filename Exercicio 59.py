#Exercício 59):

#Melhore o DESAFIO anterior, perguntando para o usuário se ele quer mostrar mais alguns termos. 
#O programa encerrará quando ele disser que quer mostrar 0 termos.

#Resolução do exercício 59):

print('Gerador de PA')
print('=-='*10)

a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Agora digite a razão: '))
total = 0
m = 10
while m != 0:
    total = total + m
    n = 0
    an = a
    while n < total:
        n = n + 1
        an = a + (n - 1) * r
        print(an, end = ' -> ')
    print('PAUSA\n')
    m = int(input('Deseja mostrar mais quantos termos?  '))
print('Encerrando programa!')
print('Você mostrou um total de {} termos'.format(total))