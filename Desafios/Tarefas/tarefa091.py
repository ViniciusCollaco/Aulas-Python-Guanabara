from random import randint
from time import sleep
cont = 0
jogadas = {'jogador1':randint(1, 6), 'jogador2':randint(1, 6), 'jogador3':randint(1, 6), 'jogador4':randint(1, 6)}
print('Valores sorteadas: ')
for chave, valor in jogadas.items():
    print(f'{chave} tirou {valor} no dado.')
    sleep(1)
print('-=-'*30)
for indice in sorted(jogadas, key = jogadas.get, reverse=True):
    cont += 1
    print(f'{cont}° lugar: {indice} com {jogadas[indice]}')
    sleep(1)