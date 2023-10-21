#Exercício 94):

# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 

#Resolução do exercício 94): 

def escreva(texto):
    print('-' * (len(texto)+4))
    print(f'  {texto}')
    print('-' * (len(texto) + 4))
    
texto = str(input('Escreva aqui um texto qualquer: '))
escreva(texto)