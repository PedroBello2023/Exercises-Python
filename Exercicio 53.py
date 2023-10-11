#Exercício 53):

#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


#Resolução do exercício 53):

somaidade = 0
homemmaior = 0
mulhernova = 0
nomevelho = ''

for dados in range(1,5):
    print('--------{}°PESSOA--------'.format(dados))
    nome = str(input('Nome: '.format(dados))).strip()
    idade = int(input('Idade: '.format(dados)))
    sexo = str(input('Sexo [M/F]: '.format(dados))).strip()
    somaidade = somaidade + idade
    if sexo == 'm' or sexo == 'M':
        if dados == 1:
            homemmaior = idade
            nomevelho = nome
        if idade > homemmaior:
            homemmaior = idade
    if sexo == 'f' or sexo == 'F':
        if idade < 20:
            mulhernova = mulhernova + 1 
media = (somaidade/4)

print('A media da idade do grupo é {}.'.format(media))
print('A idade do Homem mais velho é {} e ele se chama {}.'.format(homemmaior, nomevelho))
print('Existem {} mulheres com menos de 20 anos.'.format(mulhernova))

