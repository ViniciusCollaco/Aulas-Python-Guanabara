from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.5)
    if inicio < fim:
        contar = inicio
        while contar <= fim:
            print(f'{contar}', end=' ', flush=True)
            sleep(0.5)
            contar += passo
        print('FIM!')
    else:
        contar = inicio
        while contar >= fim:
            print(f'{contar}', end=' ', flush=True)
            sleep(0.5)
            contar -= passo
        print('FIM!')
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
