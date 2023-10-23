#Exercício 102):

#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# - Quantidade de notas;
# - A maior nota;
# - A menor nota;
# - A média da turma;
# - A situação (opcional);

#Resolução do exercício 102):


def notas(*n, sit = False):
    '''
    Funcaoo para avaliar notas e situacoes de varios alunos;
    parametro n: Uma ou mais notas dos alunos;
    parametro sit: Valor opcional indicando se deve ou nao adicionar no dicionario a situacao;
    return: Dicinario;
    '''
    maior = menor = 0
    dados = {}
    dados['notas'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n)/len(n)
    if sit:
        if dados['media'] >= 7:
            dados['situação'] = 'BOA'
        elif dados['media'] >= 5:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'
    return dados
    

resp = notas(2.5, 4.6, 7.8, 6, sit=True)
print(resp)
help(notas)
