def aumentar(preço, taxa, format = False):
    res = (preço * (taxa/100)) + preço
    if format == False:
        return res
    else:
        return moeda(res)  

def diminuir(preço, taxa, format = False):
    res = (preço * (taxa/100) + preço)
    if format == False:
        return res
    else:
        return moeda(res)

def dobro(preço, format = False):
    res = preço * 2
    if format == False:
        return res
    else:
        return moeda(res)

def metade(preço, format = False):
    res = preço * (0.5)
    if format == False:
        return res
    else:
        return moeda(res)

def moeda(preço = 0, cifra = 'R$'):
    return f'{cifra} {preço:.2f}'.replace('.', ',')

def resumo(p = 0, a = 0, d = 0 ):
    print('-'*30)
    print(f'{"RESUMO":^25}')
    print('-'*30)
    print(f'Preço Analisado:   {moeda(p):<20}')
    print(f'Dobro do Preço:    {moeda((2 * p)):<20}')
    print(f'Metade do Preço:   {moeda((p / 2)):<20}')
    print(f'{a:<3}% de Aumento:   {moeda(((p * (a/100)) + p)):<20}')
    print(f'{d:<3}% de redução:   {moeda(((p * (d/100)) + p)):<20}')
    print('-'*30)