#Exercício 72):

#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

#C) Quais foram os números pares.

#Resolução do exercício 72):






tupla = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite o terceiro: ')), int(input('Digite o quarto: ')))

print(f'Você digitou os seguintes valores {tupla}')
print(f'O número nove apareceu {tupla.count(9)} vezes;')
if 3 in tupla:
    print(f'O primeiro valor três foi digitado na posição {tupla.index(3) + 1};')
else:
    print('o valor 3 não foi digitado..')
print('Os valores pares digitados foram', end = ' ')
for n in  tupla:
    if n % 2 == 0:
        print(n, end = '; ')
