#Exercício 86):


#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

#Resolução do exercício 86) (modo1):

lista = []
dados = []
medias = []
cont = 0
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    dados.append(nome)
    dados.append(n1)
    dados.append(n2)
    lista.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    cont += 1
    if continuar == 'N':
        break
print('=-='*20)
print('N°   Nome    Média')
print('-'*20)
for i in range(cont):
    print(f'{i:<}°', end = '')
    print(f'{lista[i][0]:^10}', end = '')
    print(f'{(lista[i][1] + lista[i][2])/2:>5}')
print('-'*20)
while True:
    p = int(input('Mostrar notas de qual aluno (999 interrompe)? '))
    if p == 999:
        break
    else:
        for i in range(cont):
            if p == i:
                print(f'As notas de {lista[p][0]} são {lista[p][1:]}')


#Resolução do exercício 86) (modo 2):

ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'nN':
        break
print('=-='*20)
print(f'{"N°.":<4}{"Nome":<15}{"Média":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<15}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar nota do aluno? (999 interrompe) '))
    if opc == 999:
        print('Finalizando...')
        break
    elif opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][2]}')
print('VOLTE SEMPRE!')