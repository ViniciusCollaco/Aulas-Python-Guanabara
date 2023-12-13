lar = float(input('Qual a largura: '))
alt = float(input('Qual a altura: '))
are = (lar * alt) / 2
print('Voce tem uma parede de {:.2f} x {:.2f}, no total de {:.2f} m².\nVoce vai precisar de {:.2f} litros de tinta para pintar'.format(lar, alt, (lar * alt), are))
