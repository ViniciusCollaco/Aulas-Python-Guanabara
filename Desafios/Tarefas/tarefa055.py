maior = 0
menor = 0
for contagem in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(contagem)))
    if contagem == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\nO maior peso foi de {:.2f}Kg'.format(maior))
print('O menor peso lido foi de {:.2f}Kg'.format(menor))