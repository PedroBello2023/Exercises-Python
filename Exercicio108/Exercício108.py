#Exercício 108):

#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

#Adapte o código do desafio #104, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

#Modifique as funções que foram criadas no desafio 104 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 105.

#Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

#Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 104, 105, 106 e 107 para o primeiro pacote e mantenha tudo funcionando.

#Resolução do exercício 108):

from utilidadesCeV.moeda import moeda
p = float(input('Digite o preço:R$ '))
moeda.resumo(p, 30, 15)