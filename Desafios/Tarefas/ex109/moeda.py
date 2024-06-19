def aumentar(valor = 0, porcentagem = 0, validador = False):
    resulAum = valor + (valor * porcentagem / 100)
    return resulAum if validador is False else formatacao(resulAum)
    
def diminuir(valor = 0, porcentagem = 0, validador = False):
    resulDim = valor - (valor * porcentagem / 100)
    return resulDim if validador is False else formatacao(resulDim)
    
def dobro(valor = 0, validador = False):
    resulDobr = valor * 2
    return resulDobr if validador is False else formatacao(resulDobr)
    
def metade(valor = 0, validador = False):
    resultMeta = valor / 2
    return resultMeta if validador is False else formatacao(resultMeta)

def formatacao(valor = 0, cifrao = 'R$ '):
    return f'{cifrao}{valor:>.2f}'.replace('.', ',')

