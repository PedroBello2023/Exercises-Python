#Ecercício 77):

#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
#No final, mostre a lista ordenada na tela.

#Resolução do exercício 77):

lista = []
maior = 0
menor = 0
for c in range(0,5):
    n = int(input(f'Digite o {c + 1}° valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('=-'*25)
print(f'Os valores digitados em ordem foi {lista}.')
print('=-'*25)
