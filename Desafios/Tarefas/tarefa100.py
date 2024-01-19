from random import randint
from time import sleep
def sorteia(numeros):
    for indice in range(0, 5):
        sorteador = randint(1, 10)
        numeros.append(sorteador)
        print(f'{sorteador} ', end='', flush=True)
        sleep(0.3)
    print('TERMINOU!')
    
def somaPar(numeros):
    acumulador = 0
    for valor in numeros:
        if valor % 2 == 0:
            acumulador += valor
    print(f'Somando os valores pares {numeros}, temos {acumulador}.')

numeros = []
sorteia(numeros)
somaPar(numeros)