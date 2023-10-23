def aumentar(preço, taxa):
    return (preço * (taxa/100)) + preço

def diminuir(preço, taxa):
    return (preço * (taxa/100) + preço)

def dobro(preço):
    return preço * 2

def metade(preço):
    return preço * (0.5)