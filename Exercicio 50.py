#Exercício 50):

#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
       
# Resolução do exercício 50):

frase = str(input('Digite aqui uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''


for c in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[c]
if inverso == junto:
    print('A frase que você digitou é {} e sua inversa é {}.'.format(junto, inverso))
    print('A frase é um palindromo!')
else:
    print('A frase que você digitou é {} e sua inversa é {}.'.format(junto, inverso))
    print('A frase não é um palindromo!')

# Resolução do exercício 50) (modo 2):

frase = str(input('Digite aqui uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('A frase que você digitou é {} e sua inversa é {}.'.format(junto, inverso))
if inverso == junto:
    print('A frase é um palindromo!')
else:
    print('A frase não é um palindromo!')