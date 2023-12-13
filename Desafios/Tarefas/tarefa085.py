lista = [[], []]
valor = 0
for p in range(1, 8):
    valor = int(input(f'Qual o {p}° valor ? '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('=-'*35)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares são {lista[0]}')
print(f'Os valores impares são {lista[1]}')