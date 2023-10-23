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