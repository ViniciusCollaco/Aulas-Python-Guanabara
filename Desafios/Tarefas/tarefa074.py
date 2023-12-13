from random import randint
numeros = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('Os valores sorteados foram: ', end='')
for cont in numeros:
    print(f'{cont} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
