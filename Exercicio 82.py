#Exercício 82):

#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
#No final, mostre os valores pares e ímpares em ordem crescente.

#Resolução do exercício 82) (modo1):

pares = []
impares = []
lista = []
pos = 0
for i in range(0, 7):
    n = int(input(f'Digite o {i + 1}° valor: '))
    lista.append(n)
    if lista[pos] % 2 == 0:
        pares.append(lista[pos])
        pos += 1
    else:
        impares.append(lista[pos])
        pos += 1

pares.sort()
impares.sort()
print('=-='*20)
print(f'Os valores pares em ordem crescente foram: {pares};')
print(f'Os valores ímpares na ordem crescente foram: {impares};' )
print('=-='*20)

#Resolução do exercício 82) (modo2):

núm = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input(f'Digite o {c + 1}° valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
 
núm[0].sort()
núm[1].sort()
print('=-='*20)
print(f'Os valores pares digitados foram {núm[0]};')
print(f'Os valores ímpares digitados foram {núm[1]};')
print('=-='*20)
        
