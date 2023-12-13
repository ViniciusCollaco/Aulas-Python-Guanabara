from datetime import date
adulto = 0
crianca = 0
atual = date.today().year
for cont in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu: '.format(cont)))
    idade = atual - ano
    if idade >= 21:
        adulto += 1
    else:
        crianca += 1
print('Ao todo tivemos {} pessoas maiores de idade \nE tembém tivemos {} pessoas menores de idade'.format(adulto, crianca))