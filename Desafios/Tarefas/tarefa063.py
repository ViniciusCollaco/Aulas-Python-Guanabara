print('-=-' * 30)
print('Sequncia de Fibonacci')
print('-=-' * 30)
termo = int(input('Quantos termos voce quer mostrar: '))
contador = 3
t1 = 0
t2 = 1
print('-=-' * 30)
if termo >= 2:
    print('{} - {}'. format(t1, t2), end='')
    while contador <= termo:
        t3 = t1 + t2
        print(' - {}'.format(t3), end='')
        t1 = t2
        t2 = t3
        contador += 1
    print(' - ACABOU!!!')
elif termo == 1:
    print('1 - ACABOU!!!')
else:
    print('0 - ACABOU!!!')