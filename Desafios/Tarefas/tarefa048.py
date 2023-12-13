resul = 0
acumul = 0
for conta in range (1, 501, 2):
    if conta % 3 == 0:
        acumul = acumul + 1
        resul = resul + conta
print('A soma dos {} multiplos de 3 são: {}'.format(acumul, resul))