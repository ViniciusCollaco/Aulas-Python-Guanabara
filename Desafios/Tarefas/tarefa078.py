lista = []
maior = 0
menor = 0
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = lista[cont] # primeiro elemento sempre será o maior e o menor da lista
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print('-=-' * 30)                
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for indice, valor in enumerate(lista):
    if valor == maior:
        print(f'{indice}... ', end='') 
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for indice, valor in enumerate(lista):
    if valor == menor:
        print(f'{indice}... ', end='')
print()