#Exercício 103):

c = ['\033[m', '\033[0;30;41m', '\033[0;30;43m' ]
def ajuda(com):
    help(com)

def titulo(msg, cor = 0):
    tam = len(msg)
    print(c[cor], end = '')
    print('~'*tam)
    print(msg)
    print('~'*tam)
    print(c[0], end = '')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Comando ou Biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)