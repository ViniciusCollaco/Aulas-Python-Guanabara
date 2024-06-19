def aumentar(valor = 0, porcentagem = 0):
    resulAum = valor + (valor * porcentagem / 100)
    return resulAum
    
def diminuir(valor = 0, porcentagem = 0):
    resulDim = valor - (valor * porcentagem / 100)
    return resulDim
    
def dobro(valor = 0):
    resulDobr = valor * 2
    return resulDobr
    
def metade(valor = 0):
    resultMeta = valor / 2
    return resultMeta

def formatacao(valor = 0, cifrao = 'R$ '):
    return f'{cifrao}{valor:>.2f}'.replace('.', ',')