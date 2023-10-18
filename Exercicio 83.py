#Exercício 83):

#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
#No final, mostre a matriz na tela, com a formatação correta.

#Resolução do exercício 83) (modo1):

linhaA = []
linhaB = []
linhaC = []
matriz = []
for c in range (0, 3):
    linhaA.append(int(input(f'Digite valores para [0, {c}]: ')))
    matriz.append(linhaA[:])
    linhaA.clear()
for c in range(0, 3):
    linhaB.append(int(input(f'Digite valores para [1, {c}]: ')))
    matriz.append(linhaB[:])
    linhaB.clear()
for c in range(0, 3):
    linhaC.append(int(input(f'Digite valores para [2, {c}]: ')))
    matriz.append(linhaC[:])
    linhaC.clear()
print('=-='*10)
print(matriz[0], matriz[1], matriz[2])
print(matriz[3], matriz[4], matriz[5])
print(matriz[6], matriz[7], matriz[8])
print('=-='*10)

#Resolução do exercício 83) (modo2):

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = ' ')
    print('\n')
