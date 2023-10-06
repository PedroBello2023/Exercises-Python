#Exercício 3):

#Faça um prgrama que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

#Resolução exercício 3):

i = input('Digite qualquer coisa aqui: ')


print('O tipo primitivo de {} é {}.'.format(i, type(i)))
print('E numérico?', i.isnumeric())
print('E alphabético?', i.isalpha())
print('E alphanumérico?', i.isalnum())
print('Só tem espaços?', i.isspace())
print('Está em maiúsculas?', i.isupper())
print('está em minúsculas?', i.islower())
print('Está capitalizada?', i.istitle())


