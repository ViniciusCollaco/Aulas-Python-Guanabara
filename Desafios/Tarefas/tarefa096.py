def area(largura, comprimento):
    quadrado = largura * comprimento
    print(f'A area de um terreno {largura} x {comprimento} é de {quadrado}m².')

print('Controle de terrenos')
print('-'*30)
largura = float(input('LARGURA (m): '))
comprimneto = float(input('COMPRIMENTO (m): '))
area(largura, comprimneto)
