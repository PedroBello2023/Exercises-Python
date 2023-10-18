#Exercício 84):

#Aprimore o desafio anterior, mostrando no final:                                                   
    
#A) A soma de todos os valores pares digitados.                                                                                                  
#B) A soma dos valores da terceira coluna.                                                                                                                
#C) O maior valor da segunda linha.

#Resolução do exercício 84):

soma = 0
cont = 0
maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            cont += matriz[l][c]
        if c == 2:
            soma += matriz[l][c]
        if l == 1 and c == 0:
            maior = matriz[l][c]
        else:
            if l == 1 and c == 2 and matriz[l][c] > maior:
                maior = matriz[l][c]
            if l == 1 and c == 2 and matriz[l][c] > maior:
                maior = matriz[l][c] 
print('=-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = ' ')
    print('\n')
print('=-='*20)
print(f'A soma de todos os valores pares é {cont};')
print(f'A soma dos valores da terceira coluna é {soma};')
print(f'O maior valor da segunda linha é {maior}')
print('=-='*20)