lista = []
maior = 0
menor = 0
for cont in range(0, 5):
    lista.append(int(input(f'Digite o valor paraposição {cont}: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print(f'Os valores digitados são {lista}')
print(f'O maior numero digitado foi {maior} nas posições ', end='')
for indice, valor in enumerate(lista):
    if valor == maior:
        print(f'{indice}... ', end='')
print()
print(f'O menor numero digitado foi {menor} nas posições ', end='')
for incide, valor in enumerate(lista):
    if valor == menor:
        print(f'{incide}... ', end='')
print()