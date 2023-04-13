from random import randint
computador = randint(0, 5) #faz sorteio de numero
print('Estou pensando em um numero entre 0 a 5. Adivinhe')
res = int(input('\nQual numero pensei ? ')) #jogador tenta adivinhar
if res == computador: 
    print('Parabens, Voce acertou!!!')
else:
    print('Voce errou!!! Eu pensei no {}'.format(computador))