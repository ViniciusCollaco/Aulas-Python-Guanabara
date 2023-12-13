lista = []
par = []
impar = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
for indice, valor in enumerate(lista):
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares {impar}')
    