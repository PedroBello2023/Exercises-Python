#Exercício 76):

#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

#Resolução do exercício 76):


lista = []
while True:
    num  = int(input('Digite aqui um número: '))
    if num not in lista:
        lista.append(num)
        print('Adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar!')
    continuar = str(input('Deseja continuar [S/N]? ')).upper()
    if continuar == 'S':
        lista.sort()
    else:
        break
print('=-='*15)
lista.sort()
print(f'Você digitou os valores {lista}.') 