#Exercício 106):

#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

#Adapte o código do desafio #104, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

#Modifique as funções que foram criadas no desafio 104 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 105.

#Resolução do exercício 106):

import moeda
p = float(input('Digite o preço:R$ '))
print(f'A metade de {p} é {moeda.metade(p, format = True)}.')
print(f'O dobro de {p} é {moeda.dobro(p, format = True)}.')
print(f'O preço com 10% de aumento é {moeda.aumentar(p, 10, format = True)}.')
print(f'Reduzindo em 13% o preço, ele será {moeda.diminuir(p, 13, format = True)}')