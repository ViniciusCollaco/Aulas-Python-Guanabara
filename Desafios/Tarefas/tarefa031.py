viagem = int(input('Quantos Km são sua viagem ?'))
if viagem <= 200:
    resultado = viagem * 0.50
else:
    resultado = viagem * 0.45
print('Sua viagem de Km {} custara R${:.2f}'.format(viagem, resultado))