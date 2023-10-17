#Exercício 79):

#Crie um programa que vai ler vários números e colocar em uma lista. 
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
#Ao final, mostre o conteúdo das três listas geradas.

#Resolução do exercício 79):


lista = []
listapar = []
listaimpar= []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print(f'Os valores pares digitados forram {listapar};')
print(f'Os valores ímpares digitados foram {listaimpar};')
    