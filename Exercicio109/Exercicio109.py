#Exercicio 109):

#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

#Resolução do exercício 109):

from utilidadesCeV.moeda import moeda
from utilidadesCeV.dado import dado
p = dado.leiaDinheiro('Digite o preço:R$ ')
moeda.resumo(p, 30, 15)
