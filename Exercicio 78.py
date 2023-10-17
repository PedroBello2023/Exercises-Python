#Exercício 78):


#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: 
#A) Quantos números foram digitados.                     
#B) A lista de valores, ordenada de forma decrescente. 
#C) Se o valor 5 foi digitado e está ou não na lista.

#Resolução do exercício 78):

lista = []

while True:
    n = int(input('Digite um valor: '))
    c = str(input('Quer continuar [s/n]? ')).upper()[0]
    if c == 'S':
        lista.append(n)
    elif c == 'N':
        lista.append(n)
        break
if 5 in lista:
    print('='*30)
    print('O valor 5 está na lista;')
else:
    print('='*30)
    print('O valor 5 não foi encontrado na sua lista;')
print(f'Você digitou {len(lista)} valores;')
lista.sort(reverse = True)
print(f'Sua lista em ordem decrescente é {lista}')
print('='*30)