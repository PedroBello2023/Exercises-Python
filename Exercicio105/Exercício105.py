#Exercício 105):

#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

#Adapte o código do desafio #104, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

#Resolução do exercício 105):

import moeda
p = float(input('Digite o preço:R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.')
print(f'O preço com 10% de aumento é {moeda.moeda(moeda.aumentar(p, 10))}.')