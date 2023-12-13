from random import randint
acumulador = 1
computador = randint(0, 10) #faz sorteio de numero
print('Estou pensando em um numero entre 0 a 10. Adivinhe')
res = int(input('Qual numero pensei ? '))
while res != computador:
    acumulador += 1
    if computador > res: 
        print('\nO valor é maior, tente de novo')
    else:
        print('\nO valor é menor, tente de novo')
    res = int(input('\nQual seu palpite ? '))
print('\nAcertou com {} tentativas. Parabéns !'.format(acumulador))