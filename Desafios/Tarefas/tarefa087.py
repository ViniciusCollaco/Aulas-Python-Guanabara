matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = somaColuna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
        if matriz[linha][2]:
            somaColuna += matriz[linha][2]
print('-=-'*35)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]:^5}', end='')
    print()
print('-=-'*35)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da 3° coluna é {somaColuna}')
print(f'O mair valor da 2° linha é {max(matriz[1])}')