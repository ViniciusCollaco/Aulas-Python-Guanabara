velocidade = int(input('Qual a velocidade do veiculo ?'))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Voce esta acima do limite de velocidade, pague R${:.2f}'.format(multa))
else:    
 print('Tenha uma otima viagem')