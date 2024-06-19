def aumentar(valor = 0, taxa = 0):
    resulAum = valor + (valor * taxa/100)
    return resulAum
    
def diminuir(valor = 0, taxa = 0):
    resulDim = valor - (valor * taxa/100)
    return resulDim
    
def dobro(valor = 0):
    resulDobr = valor * 2
    return resulDobr
    
def metade(valor = 0):
    resultMeta = valor / 2
    return resultMeta

def formatacao(valor = 0, sifram = 'R$ '):
    return f'{sifram}{valor:>.2f}'.replace('.', ',')