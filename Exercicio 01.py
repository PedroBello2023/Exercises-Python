#Exercício 1):

#Faça um programa que leia o nome de uma pessoa e dê uma mensagem de boas vindas.

#Resolução do exercício 1) (modo 1):


nome = input("Qual é o seu nome? ")
print("Prazer em conhecelo(a)",nome,"seja muito bem vindo(a)!" )

#Resolução do exercício 1) (modo 2):

nome = input("Qual é o seu nome? ")
print("Prazer em conhecelo(a) {}".format(nome), "seja muito bem vindo(a)!")
