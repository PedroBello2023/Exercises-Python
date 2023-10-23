#Exercício 100):

#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

#Resolução do exercício 100):

def ficha(nome = '<desconhecido>', gol = 0): 
            print(f'O jogador {nome} fez {gol} gols no campeonato;')
            print('='*40)

        
print('='*40)
nom = str(input('Qual o nome do jogador? '))
gl = str(input('Quantos gols ele marcou? '))
if gl.isnumeric():
    gl = int(gl)
else:
    gl = 0
if nom.strip() == '' or nom.isnumeric():
    ficha(gol = gl)
else:
    ficha(nom, gl)

