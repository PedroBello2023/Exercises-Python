def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print('\033[031mERRO! Digite apenas números!\033[m')
        else:
            valido = True
            return float(entrada.replace(',', '.')) 
            
    