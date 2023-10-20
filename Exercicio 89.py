#Exercício 89):

#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

#Resolução do exercício 89):

from datetime import date
ano = date.today().year
cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
nascimento = int(input('Nascimento: '))
cadastro['CTPS'] = int(input('CTPS (0 se não tem): '))
cadastro['Idade'] = ano - nascimento
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de contrato: '))
    cadastro['Salário'] = float(input('Salário:R$ '))
    tempo_serviço = ano - cadastro['Contratação']
    
    if tempo_serviço >= 20 and cadastro['Idade'] < 65:
        cadastro['Aposentadoria'] = (f'{65} anos')
    if tempo_serviço < 20:
        if cadastro['Idade'] + tempo_serviço < 65:
            if cadastro['Idade'] + 20 < 65:
                cadastro['Aposentadoria'] = (f'{65} anos')
            elif cadastro['Idade'] + 20 > 65:
                cadastro['Aposentadoria'] = (f'{cadastro["Idade"] + 20} anos')
for k, v in cadastro.items():
    print(f' - {k} tem o valor {v}.')