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

def resumo(valor = 0, porcentagemAum = 10, porcentagemRedu = 5):
    print('-'*35)
    print('RESUMO DO VALOR'.center(30))
    print('-'*35)
    print(f'Preço analisado: \t{formatacao(valor)}')
    print(f'O dobro do preço: \t{dobro(valor, True)}')
    print(f'A metade do preço: \t{metade(valor, True)}')
    print(f'{porcentagemAum}% de aumento: \t{aumentar(valor, porcentagemAum, True)}')
    print(f'{porcentagemRedu}% de redução: \t{diminuir(valor, porcentagemRedu, True)}')
    print('-'*35)