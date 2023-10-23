#Exercício 112) (projeto final!)

#Projeto: Vamos criar um menu em Python, usando modularização.

from lib.function import *
from time import sleep
from lib.arquivo import *

arq = "cursoemvideo.txt"

if arquivoExiste(arq):
    print(f'Arquivo {arq} encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)

while True:
    res = menu(['Ver Pessoas Caastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if res == 1:
        lerArquivo(arq)
    elif res == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input('Nome: '))
        idade = input('Idade: ')
        cadastrar(arq, nome, idade)
    elif res == 3:
        print(cabecalho('Saindo do Sistema! Até Logo...'))
        break
    else:
        print('\033[031m[ERROR!] Digite uma opção válida!\033[m')
        sleep(2)