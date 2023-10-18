#Exercício 81):

#Faça um programa que leia nome e peso de várias pessoas,                                      
#guardando tudo em uma lista. No final, mostre:                                                                                                   
    
#A) Quantas pessoas foram cadastradas.                                                                                                              
#B) Uma listagem com as pessoas mais pesadas.                                                                                                   
#C) Uma listagem com as pessoas mais leves.

#resolução do exercício 81):

temp = []
lista = []
maior = menor = 0
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(float(input('Digite seu peso [KG]: ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('='*30)
print(f'Ao todo você cadastrou {len(lista)} pessoas;')
print(f'O peso maior foi de {maior} referente a', end = ' ')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end = '')
print(f'\nO menor peso foi de {menor} referente a', end = ' ')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end = '')
        
