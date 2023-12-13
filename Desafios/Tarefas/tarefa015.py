dias = int(input('Quantos dias alugados ?'))
km = float(input('Quantos KM rodados ?'))
print('O total a pagar é de R$ {:.2f}'.format((dias * 60) + (km * 0.15)))